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

    def present_images(self):
        '''
        Returns a random photo for the desired type of photo
        Args:
            image_list (list): the types of images to random select
        '''
        '''for 
        for directory in os.listdir(data_dir):
            path = os.path.join(data_dir, directory)
            # Iterate through each file in the directory
            if os.path.isdir(path):
                for file in os.listdir(path):
                    image = cv2.imread(os.path.join(path, file))
                    # Resize the image
                    image = cv2.resize(image, (IMG_WIDTH, IMG_HEIGHT))'''
        path = "/Users/michaelwebber/Desktop/Markov Mission/Markov-Mission/Catching"
        files=os.listdir(path)
        d=random.choice(files)
        os.startfile(d)
def main():

    # Creation of the transition probabilities
    instragram_post = ImageSelection({
        "Kicking": {"Kicking": 0.2, "Standing": 0.5, "Catching": 0.3},
        "Standing": {"Kicking": 0.4, "Standing": 0.1, "Catching": 0.5},
        "Catching": {"Kicking": 0.4, "Standing": 0.4, "Catching": 0.2}
    })

    # Prompt the user for the number of images the user wants
    # as well as the type of image they would like to be the first
    number_images = int(input("How many images do you want to post?     "))
    first_image = input("What type of image should the first picture \
be? (Kicking, Standing, Catching)   ")
    new_post = instragram_post.create_sequence(
        current_image=first_image, length=number_images
    )
    print(new_post)
    print("Selecting the desired images...")
    print("Choosing a caption...")
    print("Your Instagram post has been created!")


if __name__ == "__main__":
    main()
