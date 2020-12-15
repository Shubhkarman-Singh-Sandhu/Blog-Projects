import random as r 
from gtts import gTTS
import playsound as ps

def wordy(data, order):
    Dict = {}
    words = data.split(' ')
    index = order
    for word in words:
        index = order
        for letter in word[index:]:
            key = ''.join(word[index - order: index])
            if key in Dict: 
                Dict[key].append(letter)
            else:  
                Dict[key] = [letter] 
            index += 1
    return Dict

def make_word(Dict, length, order):
    oldLetters = r.choice(list(Dict.keys())).split(' ') 
    string = ''.join(oldLetters)
    for i in range(length - order): 
        try:
            key = ''.join(oldLetters)
            newLetters = r.choice(Dict[key]) 
            string += newLetters 
            oldLetters = string[-(order):]
        except KeyError:
            return string
    return string

def speak(text):
    tts = gTTS(text = text, lang = 'en', slow = False)
    filename = "word.mp3"
    tts.save(filename)
    ps.playsound(filename)
    
data = " " # You can use the company name text files 
Dict = wordy(data, 3)
string = make_word(Dict, 10, 3)
print(" Company name: ", string)
speak(string)
