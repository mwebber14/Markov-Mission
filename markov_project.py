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
            self.images,
            p=[self.transition_matrix[current_image][next_image]
               for next_image in self.images]
        )

    def create_sequence(self, current_image="Kicking", length=3):
        """Generates a sequence of notes.
           Args:
                current_note (str): the note of the song that we are currently
                looking at.
                song_length (int): how many notes we should generate for the
                song.
        """
        images = []
        while len(images) < length:
            next_image = self.get_next_note(current_image)
            images.append(next_image)
            current_image = next_image
        return images

    '''def get_wave(self, frequency=440, duration=0.3, max_amplitude=4096):
        """Retrieve sound wave for note based on given args...
           Args:
               frequency (float): the note frequency (affects the pitch)
               duration  (float): the length of the note
               max_amplitude (num): how loud we want this note to be
        """
        time = np.linspace(0, duration, int(SAMPLE_RATE * duration))
        # print("Time: ", time)
        sound_wave = max_amplitude * np.sin(2 * np.pi * frequency * time)
        # print("Sound Wave: ", sound_wave)
        return sound_wave

    def get_sound_waves_for(self, melody):
        """Transforms the string melody into a list of sound waves.
           Args:
               melody (list): notes of our song
        """
        song = []
        for current_note in melody:
            sound_wave = self.get_wave(NOTE_FREQUENCIES[current_note])
            song.append(sound_wave)
        # print("Song is now", song)
        song = np.concatenate(song)
        # print("Song is now", song)
        return song

    def write_sound_file(self, melody):
        """Write out a collection of sound waves (i.e., a song!) to a file.
           Args:
               melody (list): notes of our song
        """
        sound_data = self.get_sound_waves_for(melody)
        write("new-hit-song.wav", SAMPLE_RATE, sound_data.astype(np.int16))'''


def main():

    # Creation of the transition probabilities
    instragram_post = ImageSelection({
        "Kicking": {"Kicking": 0.2, "Standing": 0.5, "Catching": 0.3},
        "Standing": {"Kicking": 0.4, "Standing": 0.1, "Catching": 0.5},
        "Catching": {"Kicking": 0.4, "Standing": 0.4, "Catching": 0.2}
    })

    # Prompt the user for the number of images the user wants
    # as well as the type of image they would like to be the first
    number_images = int(input("How many images do you want to post?"))
    first_image = input("What type of image should the first picture \
                         be? (Kicking, Standing, Catching)")
    new_post = instragram_post.create_sequence(
        current_image=str(first_image), length=number_images
    )

    print("Selecting the desired images...")
    print("Choosing a caption...")
    # song_maker.write_sound_file(new_song)

    print("Your Instagram post has been created!")


if __name__ == "__main__":
    main()
