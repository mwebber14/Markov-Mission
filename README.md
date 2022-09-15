# Markov-Mission
Title: Instagram Post Generator
Author: Michael Webber

How to set up the code:

    The first thing that needs to be done is editing the paths that appear at the top of
    the markov_project.py. These paths are all constants that will be used later on. However,
    these paths are specific to the machine that the code was created on, so in order to function
    properly, they must be altered for each device that the code is run on. The easiest way to 
    make this change is to save the Markov-Mission to one's desktop and then alter the users name.
    If the folder is saved elsewhere, then more aspects of the path will need to be changed in order
    for the code to work.

How to run the code:

    Once the paths have been changed, the code is pretty easy to run. In the terminal window enter
    python3 markov_project.py. This will run the code and the user will be prompted for a collection
    of answers. First, the user will be asked how many images they want to select between 1 and 5. 
    Next, the user must create the name of a pdf file where they would like the images to be saved.
    The final prompt is entering an emotion, either motivated or defeated. This will be used to 
    select the caption for the collection of images. After these prompts, the program will used the
    transition matrix in the main() function to select the images for the post. These will be saved
    under the name the user provided in the Markov-Mission folder. The program will then take the 
    emotion entered and select a quote from the corresponding emotion folder. This quotation will be
    outputed in the terminal window. The program will then be finished executing. The pdf may not be 
    able to seen directly from an editor, but it can be viewed from whhere the project is saved on
    the user's device.

This website is what I used to get all of the quotes for my Defeat Captions folder
https://www.therandomvibez.com/sad-day-quotes-sayings/

This is the website I used to find the quotes for my Motivation Captions folder