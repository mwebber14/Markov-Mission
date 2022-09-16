# Markov-Mission
Title: Instagram Post Generator
Author: Michael Webber

How to set up the code:

        The first thing that needs to be done is editing the paths that appear at the top of
    the markov_project.py document. These paths are all constants that will be used later on. However,
    these paths are specific to the machine that the code was created on, so in order to function
    properly, they must be altered for each device that the code is run on. The easiest way to 
    make this change is to save the Markov-Mission to one's desktop and then alter the users name
    in the path. If the folder is saved elsewhere, then more aspects of the path will need to be
    modified in order for the code to work.

How to run the code:

        Once the paths have been changed, the code is pretty easy to run. In the terminal window enter
    python3 markov_project.py. This will run the code and the user will be prompted for a collection
    of answers. First, the user will be asked how many images they want to select between 1 and 5. 
    If a value outside of this range is given, the user will be prompted again to input a correct
    value. Next, the user must create the name of a pdf file where they would like the images to be saved.
    In this case, if the file does not end with the characters ".pdf", the user will be asked to enter
    a valid file name. The string must end with ".pdf" in order for the filename to be acceptable
    later on. The final prompt is entering an emotion, either motivated or defeated. This will be used to 
    select the caption for the collection of images. After these prompts, the program will used the
    transition matrix in the main() function to select the images for the post. These will be saved
    under the name the user provided in the examples folder. The program will then take the 
    emotion entered and select a quote from the corresponding emotion folder. This quotation will be
    outputed in the terminal window. The program will then be finished executing. The pdf may not be 
    able to seen directly from an editor, but it can be viewed from where the project is saved on
    the user's device.

Personally Meaningful:

        I thought my idea was very impactful for me. I am into social media like the modern 21 year old,
    but often find myself struggling to pick images to post or the right caption to match the 
    images. This often leads me to not post anything at all because I am not satisfied.
    Sometimes I find it difficult to have the time to create a social media post. While 
    social media is not always at the front of my mind, I am seeing the increasing role it is 
    having on athlete's ability to get recognized by scouts and coaches. This is going to impact me
    as I look for opportunities to continue playing soccer after college. My program encompasses 
    all of the themes I mentioned above. It allows me to get my image out quickly without having
    to put much, or any, thought into what the pictures or caption will be. As I progress through
    this fall and the soccer season, I am hoping to use this program to quickly generate posts,
    so I can stay focused on playing the game.

How I was challened:

        I think this project was definitely a challenge for me. The biggest challenge at first was
    the project as a whole and trying to think of something that would be unique and fun. Every
    project that I have done in the past has had a very specific prompt with an expected end goal.
    This was the first project where it was entirely up to me to decide what I did and what I
    created. Figuring out where to start and what to do was certainly a challenge. I also found it
    challenging to not think too big. Since we were only given a week for the project, I had to keep
    my ideas concise and focused. Sometimes really grand plans would flash through my brain, but 
    trying to conceive them in code was not possible given the time frame.     
        I chose to use python, partially because I am comfortable with the language, but more importantly 
    because of the unique functionality in PIL. I discovered that PIL has a very unique pdf creation 
    function as well as a lot of other interesting functions to photoshop and edit images. Reading about
    this library and its different functionalities was time consuming and difficult. It took me many hours
    to correctly implement the few PIL functions that I ultimately incorporated.
        Going forward, there are a couple things I would want to add. One of those would be to create the 
    program so that it is not machine specific. I would want the paths to be based on the operating 
    system. I did not have the research and implementation time to make that possible currently. Also,
    there is the possibility that a final pdf could have repeating images if there are multiple from
    the same style of photo. With more time I would like to not have this be possible so that each
    created post would be unique with no duplicates. I also think going forward it would be cool to
    have a wider variety of captions. Athletes have significantly more emotions than motivation and defeat,
    and it would be great to incorporate some of those into the caption possibility. Hopefully I can find
    time to come back around to this project and add some of these details.

Why I think it is creative:

        I think my program is creative, because I have never really come across something like it before.
    I am sure that some sort of random Instagram post generator exists out there, but I have never seen it.
    Additionally, this program is creating visual art that I would have never created. There is the off chance
    I could have eventually combined photos in a unique way to create something that my program did, but given 
    the volume of images and captions, I find it unlikely. Something that is creative is unique, and I believe
    my program is unique for the basic criteria we were given.

Credit to sources:

        I must first give credit to Brian Beard. He is the photographer for Bowdoin Mens Soccer
    and all of the other athletics teams on campus. He provided me will all of these great photos
    that I used for this project. I must also give credit to the following website:
    https://www.codegrepper.com/code-examples/python/select+random+image+from+folder+python. It
    was on this website that I was able to learn how to randomly select an image from a folder
    using the operating system rather than the direct paths of the local machine. Lastly, all
    of the captions that, both motivated and defeated, were found from the following two 
    websites:
    https://www.therandomvibez.com/sad-day-quotes-sayings/
    https://captionland.com/sports-captions-for-instagram/
