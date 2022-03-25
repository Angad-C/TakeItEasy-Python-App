from __future__ import print_function
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import speech_recognition as s_r
import syllables
import time

r = s_r.Recognizer()
my_mic = s_r.Microphone(device_index=0)



story = """
"Will you walk a little faster?" said a whiting to a snail,
"There's a porpoise close behind us, and he's treading on my tail.
See how eagerly the lobsters and the turtles all advance!
They are waiting on the shingle—will you come and join the dance?
    Will you, won't you, will you, won't you, will you join the dance?
    Will you, won't you, will you, won't you, won't you join the dance?

"You can really have no notion how delightful it will be
When they take us up and throw us, with the lobsters, out to sea!"
But the snail replied "Too far, too far!" and gave a look askance—
Said he thanked the whiting kindly, but he would not join the dance.
    Would not, could not, would not, could not, would not join the dance.
    Would not, could not, would not, could not, could not join the dance.

"What matters it how far we go?" his scaly friend replied,
"There is another shore, you know, upon the other side.
The further off from England the nearer is to France—
Then turn not pale, beloved snail, but come and join the dance.
    Will you, won't you, will you, won't you, will you join the dance?
    Will you, won't you, will you, won't you, won't you join the dance?"
"""

print("""
Welcome to Take it Easy!
In this game you will select a passage and read it out loud slowly
You will have 3 chances, if you don't say it correct on the 3rd time, the word will be skipped and it will move on to the next word!
Have fun!
""")

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
