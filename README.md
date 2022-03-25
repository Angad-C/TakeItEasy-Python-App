# TakeItEasy
Take it Easy takes a piece of text and prints it word by word. After printing each word, the program pauses to allow the reader to have read the word before printing the next word.

The program listens to the speaker and proceeds after the reader has read the word. The program used Google Speech to Text library to check for read word, and uses fuzzywuzzy library to allow for an approximation of pronunciation - not needing 100% accuracy of speech.

<h2>How to Use:</h2>
Install the following libraries:

<pre>
pip install speech_recognition
pip install fuzzywuzzy
pip install syllables
</pre>

You can change the text to read in the code file itself (change the contents of story)
Then execute:
<pre>
python takeiteasy.py
</pre>

<h2><a href "https://docs.google.com/document/d/1xNYhjecGVpCT4bP0q_9w_f8CUdxNqdYEYsF8Y4fUrO0/edit?usp=sharing"> Documentation</a></h2>

If you like this - also check out http://takeiteasy.angadc.net

(c) www.angadc.net

-- end --
