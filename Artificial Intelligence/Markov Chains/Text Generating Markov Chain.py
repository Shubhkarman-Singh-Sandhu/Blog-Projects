import random as r 
from gtts import gTTS
import playsound as ps
#
#Lets understand this Markov Chain
#
def dictionary(data, order):
    Dict = {} # Creates an empty dictionary, that will have all are probabilties of occurence of words
    words = data.split(' ') # This splits the data into seperate words
    index = order # Gives the index the value of the order
    for word in words[index:]: # For all the words in our data find words that come after it, starting from the nth word 
        key = ' '.join(words[index - order:index]) # find the phrase before it
        if key in Dict: # and if that phrase exists elsewhere also
            Dict[key].append(word) # add the words to our phrases
        else: # else if it appears only once, 
            Dict[key] = [word] # just add that word
        index += 1
    return Dict

def make_string(Dict, length): # Make the randomised string
    oldWords = r.choice(list(Dict.keys())).split(' ') # Define a staring point from our string
    string = ' '.join(oldWords) + ' ' # Create a string with our starting points
    for i in range(length): # Loop in the range of our desired length
        try:
            key = ' '.join(oldWords) # Joins our starting words with a space in between
            newWords = r.choice(Dict[key]) # Find new words based on the probabilities
            string += newWords + ' ' # Add that to our String with a space!

            for word in range(len(oldWords)):
                oldWords[word] = oldWords[(word + 1) % len(oldWords)] # Flip the words  
            oldWords[-1] = newWords # Make the last item of our starting words our new Words
        except KeyError:
            return string
    return string

def speak(text):
    tts = gTTS(text = text, lang = 'en', slow = False)
    filename = 'Speech.mp3'
    tts.save(filename)
    ps.playsound(filename)
data = "" # Enter your data in here

Dict = dictionary(data, 3)
string = make_string(Dict, 100)
print(string)
speak(string)
