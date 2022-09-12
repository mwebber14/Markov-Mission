"""
Image Selection Program
There are probablities linked with the transition from one 
image to the next image. The user can specify how many images
they would like to have in their "post". Using the transisition
we will output the number of pictures. The picture type will
depend on the probabilities of it being selected
"""
import numpy as np
from scipy.io.wavfile import write

class ImageSelection:

    def __init__(self, transition_matrix):
        """Simulates a musician that relies on a simple Markov chain.
           Args:
                transition_matrix (dict): transition probabilities
        """
        self.transition_matrix = transition_matrix
        self.image_type = list(transition_matrix.keys())

    def get_next_note(self, current_note):
        """Decides which note to play next based on the current note.
           Args:
               current_note (str): the current note being played.
        """
        return np.random.choice(
            self.notes,
            p=[self.transition_matrix[current_note][next_note] \
            for next_note in self.notes]
        )

    def compose_melody(self, current_note="A", song_length=3):
        """Generates a sequence of notes.
           Args:
                current_note (str): the note of the song that we are currently
                looking at.
                song_length (int): how many notes we should generate for the
                song.
        """
        melody = []
        while len(melody) < song_length:
            next_note = self.get_next_note(current_note)
            melody.append(next_note)
            current_note = next_note
        return melody

    def get_wave(self, frequency=440, duration=0.3, max_amplitude=4096):
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
        write("new-hit-song.wav", SAMPLE_RATE, sound_data.astype(np.int16))

def main():

    song_maker = MarkovMusician({
        "Kicking": {"Kicking": 0.2, "Standing": 0.5, "Catching": 0.3},
        "Standing": {"Kicking": 0.4, "Standing": 0.1, "Catching": 0.5},
        "Catching": {"Kicking": 0.4, "Standing": 0.4, "Catching": 0.2}
    })
    
    '''new_song = song_maker.compose_melody(current_note="C", song_length=10)
    print("Here's my latest song:", new_song)
    print("Writing song to file...")
    song_maker.write_sound_file(new_song)
    print("Process completed!")'''

if __name__ == "__main__":
    main()
