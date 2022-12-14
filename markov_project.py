"""
Michael Webber
CSCI 3725
Markov Mission 3
September 15th, 2022

This file allows the user to input a couple of arguments, such as the 
number of images the user wants, the name of the file where images will
be saved, as well as the emotion they want the caption to evoke. Using this
information, the program saves a PDF file with the images selected using 
the markov probabilities. A caption is also randomly selected using the 
emotion the user indicated. The goal is to create a template of an 
Instagram post. Someone would not have to think too much for an Instagram
post to be created.

There are not any bugs within the code, but there are some modifications that
will need to be made to the paths that are defined as constants at the 
start of the program. The paths are currently specific to the machine they
are written on, so they will not function for a different computer. I tried
to go directly through the operating system so that thhe program could be used
generally, but I could not figure it out in time.
"""
from fileinput import filename
import numpy as np
import random
import os
from PIL import Image

# CONSTANTS
# MAKE SURE TO MODIFY THE PATH WITH RESPECT TO THE DEVICE
PATH_STANDING = "/Users/michaelwebber/Desktop/Markov Mission/Markov-Mission/assets/Standing"
PATH_CATCHING = "/Users/michaelwebber/Desktop/Markov Mission/Markov-Mission/assets/Catching"
PATH_KICKING = "/Users/michaelwebber/Desktop/Markov Mission/Markov-Mission/assets/Kicking"
PDF_PATH = "/Users/michaelwebber/Desktop/Markov Mission/Markov-Mission/examples/"


class ImageSelection:

    def __init__(self, transition_matrix):
        """Simulates an image selection process from a simple Markov chain.
           Args:
                transition_matrix (dict): transition probabilities
        """
        self.transition_matrix = transition_matrix
        self.image_type = list(transition_matrix.keys())

    def choose_next_image(self, current_image):
        """Decides which type of image to select based on the current type.
           Args:
               current_image (str): the current image of the sequence.
        """
        return np.random.choice(
            self.image_type,
            p=[self.transition_matrix[current_image][next_image]
               for next_image in self.image_type]
        )

    def create_sequence(self, length):
        """Generates a sequence of images.
           Args:
                current_image (str): the type of image we are using
                length (int): how many images we should generate for the
                post.
        """
        images = []
        # The first photo is always randomly choosen
        current_image = random.choice(["Kicking", "Catching", "Standing"])
        images.append(current_image)

        # The transition matrix is used for the selction of the
        # remaining images if there are any
        while len(images) < length:
            next_image = self.choose_next_image(current_image)
            images.append(next_image)
            current_image = next_image
        return images

    def present_images(self, list_images):
        '''
        Returns a list of paths for the desired type of photo. Each photo type
        is randomly selected from the corresponding folder
        Args:
            image_list (list): the types of images to random select
        '''
        # Creates the whole pathh that is going to be needed to open the
        # images properly when the pdf is created
        name_of_images = []
        for image in list_images:
            if image == 'Catching':
                path = PATH_CATCHING
            elif image == 'Standing':
                path = PATH_STANDING
            else:
                path = PATH_KICKING

            # Randomly selecting a file from the desired folder
            random_filename = random.choice([
                x for x in os.listdir(path)
                if os.path.isfile(os.path.join(path, x))
            ])

            # Need to concatenate the file name to the
            # path so we have the complete image
            name_of_images.append(path + "/" + random_filename)

        return name_of_images

    def select_caption(self, filename):
        '''
        Given the specified emotion file, randomly select a quote from the file
        Args:
            filename (.txt file): a file containing emotion invoking quotes
        '''
        line = random.choice(open(filename).readlines())
        return line.strip()


def main():

    # Creation of the transition probabilities
    instagram_post = ImageSelection({
        "Kicking": {"Kicking": 0.2, "Standing": 0.5, "Catching": 0.3},
        "Standing": {"Kicking": 0.2, "Standing": 0.1, "Catching": 0.7},
        "Catching": {"Kicking": 0.6, "Standing": 0.3, "Catching": 0.1}
    })

    # Prompt the user for the number of images the user wants
    # as well as the type of image they would like to be the first
    number_images = int(input("How many images do you want to post? (1-5)   "))

    # Makes sure the input is a number between 1 and 5
    while number_images < 1 or number_images > 5:
        print("The number of images must be between 1 and 5.")
        number_images = int(input("How many images do you want to post? (1-5)   "))

    file_name = input("What do you want to name your file? (must end in .pdf)   ")

    # Makes sure the file name is acceptable
    while file_name[-4:] != ".pdf":
        print("The filename must end in .pdf")
        file_name = input("What do you want to name your file? (must end in .pdf)   ")

    # This will be used to randomly select a caption
    emotion = input("Are feeling motivated or defeated? Please select one.   ")

    while emotion.strip().lower() != "motivated" and emotion.strip().lower() != "defeated":
        print("You must enter one of the two emotions (motivated or defeated)")
        emotion = input("Are feeling motivated or defeated? Please select one.   ")

    # Creates the sequence of images we want
    new_post = instagram_post.create_sequence(length=number_images)

    print("Selecting the desired images...")

    print("Choosing a caption...")
    # Determines which caption folder that needs to be entered based on the
    # emotion that was expressed by the user
    if emotion == "motivated":
        caption = instagram_post.select_caption("Motivation Captions.txt")
    else:
        caption = instagram_post.select_caption("Defeated Captions.txt")

    # Takes the list of files and puts them into one pdf
    # that is saved to the users Markov-Mission folder
    images = [
        Image.open(image)
        for image in instagram_post.present_images(new_post)
    ]

    pdf_path = PDF_PATH + file_name

    images[0].save(
        pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:]
    )

    print("Your Instagram post has been created!\n")

    print("Your photo(s) will appear in the project folder with the name you have given \
and the caption for your photo(s) will appear below. \n")

    print(caption + "\n")


if __name__ == "__main__":
    main()
