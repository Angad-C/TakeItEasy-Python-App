from __future__ import print_function
from fileinput import filename
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import speech_recognition as s_r
import syllables
import time
import magic

r = s_r.Recognizer()
my_mic = s_r.Microphone(device_index=0)

print("""
Welcome to Take it Easy!
In this game you will select a text file from your computer and read the contents out loud slowly
You will have 3 chances, if you don't say it correct on the 3rd time, the word will be skipped and it will move on to the next word!
Have fun!
""")

print("Please write your file's name below!")
f_name = input()
try:
    f_buffer = open(f_name)
except:
    print("ERROR: File not found, please make sure that the file's name (and path) are typed correctly.")
    exit()


file = magic.Magic(mime=True)

ftype = file.from_file(f_name)
# file.close()

if ftype != "text/plain":
    print("ERROR: File format incorrect, please make sure your file is in plain text")
    exit()

# TODO: It might be a good idea to make sure that the file has valid text

story = f_buffer.read()

for each_word in story:
    if len(each_word) > 45:
        print("please only have text with words 45 characters long or less.")
        exit()
    for each_letter in each_word:
        if "<" in each_letter or ">" in each_letter:
            print("ERROR: one or more script tags detected.")
            exit()

f_buffer.seek(0)

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count

def sameword(w):
    tries = 3
    global my_mic
    global r
    try:
        with my_mic as source:
            while(True):
                r.adjust_for_ambient_noise(source) #reduce noise
                audio = r.listen(source, phrase_time_limit=5) #take voice input from the microphone
                straud = r.recognize_google(audio)
                if fuzz.partial_ratio(straud, w.lower()) > 55:
                    return True
                else:
                    print("-", end=" ")
                    tries -= 1
                    if (tries == 0):
                        return False
    except Exception as e:
        time.sleep(syllables.estimate(w))


paras = story.splitlines()
for p in paras:
    words = p.split()
    for w in words:
        print(w, end=" ", flush=True)
        if sameword(w) == False:
            print(".", end="", flush=True)
            pass
        #time.sleep(syllable_count(w))
    print("")
file.close()