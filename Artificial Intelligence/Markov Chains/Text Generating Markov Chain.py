import random as r
from gtts import gTTS
import playsound as ps


def dictionary(data, order):
    Dict = {}
    words = data.split(' ')
    index = order
    for word in words[index:]:
        key = ' '.join(words[index - order:index]) 
        if key in Dict: 
            Dict[key].append(word)
        else:  
            Dict[key] = [word] 
        index += 1
    return Dict


def make_string(Dict, length): 
    oldWords = r.choice(list(Dict.keys())).split(' ') 
    string = ' '.join(oldWords) + ' '
    for i in range(length): 
        try:
            key = ' '.join(oldWords)
            newWords = r.choice(Dict[key])
            string += newWords + ' '  

            for word in range(len(oldWords)):
                oldWords[word] = oldWords[(word + 1) % len(oldWords)]  
            oldWords[-1] = newWords
        except KeyError:
            return string
    return string


def speak(text):
    tts = gTTS(text=text, lang='en', slow=False)
    filename = 'Speech.mp3'
    tts.save(filename)
    ps.playsound(filename)


data = ""  # Enter your data in here

Dict = dictionary(data, 3)
string = make_string(Dict, 100)
print(string)
speak(string)
