"""
Image Selection Program
There are probablities linked with the transition from one
image to the next image. The user can specify how many images
they would like to have in their "post". Using the transisition
we will output the number of pictures. The picture type will
depend on the probabilities of it being selected
"""
from tkinter import image_types
import numpy as np
from scipy.io.wavfile import write
import random
import os
import cv2

IMG_WIDTH = 30
IMG_HEIGHT = 30

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

    def create_sequence(self, current_image="Kicking", length=3):
        """Generates a sequence of images.
           Args:
                current_image (str): the type of image we are using
                length (int): how many images we should generate for the
                post.
        """
        images = []
        images.append(current_image)
        while len(images) < length:
            next_image = self.choose_next_image(current_image)
            images.append(next_image)
            current_image = next_image
        return images

    def present_images(self, list_images):
        '''
        Returns a random photo for the desired type of photo
        Args:
            image_list (list): the types of images to random select
        '''
        name_of_images = []
        for image in list_images:
            if image == "Catching":
                path = "/Users/michaelwebber/Desktop/Markov Mission/Markov-Mission/Catching"
            if image == "Standing":
                path = "/Users/michaelwebber/Desktop/Markov Mission/Markov-Mission/Standing"
            else:
                path = "/Users/michaelwebber/Desktop/Markov Mission/Markov-Mission/Kicking"
            random_filename = random.choice([
                x for x in os.listdir(path)
                if os.path.isfile(os.path.join(path, x))
            ])
            name_of_images.append(random_filename)

        return name_of_images


def main():

    # Creation of the transition probabilities
    instagram_post = ImageSelection({
        "Kicking": {"Kicking": 0.2, "Standing": 0.5, "Catching": 0.3},
        "Standing": {"Kicking": 0.4, "Standing": 0.1, "Catching": 0.5},
        "Catching": {"Kicking": 0.4, "Standing": 0.4, "Catching": 0.2}
    })

    # Prompt the user for the number of images the user wants
    # as well as the type of image they would like to be the first
    number_images = int(input("How many images do you want to post?     "))
    first_image = input("What type of image should the first picture \
be? (Kicking, Standing, Catching)   ")
    new_post = instagram_post.create_sequence(
        current_image=first_image, length=number_images
    )
    print("Selecting the desired images...")
    for image in instagram_post.present_images(new_post):
        print(image)
    #print(instagram_post.present_images(new_post))
    print("Choosing a caption...")
    print("Your Instagram post has been created!")


if __name__ == "__main__":
    main()
