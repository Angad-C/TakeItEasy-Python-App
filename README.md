# TakeItEasy
Take it Easy takes a piece of text and prints it word by word. After printing each word, the program pauses to allow the reader to have read the word before printing the next word.

The program listens to the speaker and proceeds after the reader has read the word. The program used Google Speech to Text library to check for read word, and uses fuzzywuzzy library to allow for an approximation of pronunciation - not needing 100% accuracy of speech.


How to Use:
Install the following libraries:

pip install speech_recognition
pip install fuzzywuzzy
pip install syllables

You can change the text to read in the code file itself (change the contents of story)
Then execute:

python takeiteasy.py

-- end --
