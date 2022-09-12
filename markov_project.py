"""
Learning Objectives
- Let's remember Python!
- What would a Markov chain look like in code?
Example of an Markov Chain implementation in Python (using concepts we learned
in 1101).
Dependencies: numpy, scipy
"""
import numpy as np
from scipy.io.wavfile import write
SAMPLE_RATE = 44100
# We can add more of these later...keeping it simple for now!
NOTE_FREQUENCIES = {
    "A": 440.01,
    "B": 493.89,
    "C": 261.63
}
class MarkovMusician:
    def __init__(self, transition_matrix):
        """Simulates a musician that relies on a simple Markov chain.
           Args:
                transition_matrix (dict): transition probabilities
        """
        self.transition_matrix = transition_matrix
        self.notes = list(transition_matrix.keys())
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
        "A": {"A": 0.3, "B": 0.4, "C": 0.3},
        "B": {"A": 0.7, "B": 0.2, "C": 0.1},
        "C": {"A": 0.1, "B": 0.7, "C": 0.2}
    })
    new_song = song_maker.compose_melody(current_note="C", song_length=10)
    print("Here's my latest song:", new_song)
    print("Writing song to file...")
    song_maker.write_sound_file(new_song)
    print("Process completed!")
if __name__ == "__main__":
    main()
