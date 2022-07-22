# Zina voice assistant
# Peculiarities:
- Average time complexity O(n log n)
- Implemented "advanced speech comprehension" (understands any lexical constructions)
- Exceptions taken into account
# Functional 
- Unobtrusive conversation (from the prescribed dialogue branches)
- Say current weather for the week
- The current exchange rate of the dollar and the euro
- Recommend a Movie or Game
- Calculate body mass index, with a brief description of the health problem (if any)
- Open youtube
- Issue a user query to Google
- Find any information from Wikipedia and read briefly
- Repeat a phrase
# Add. possibility
Implemented local game "Pikkalo" (question-answer) implemented in game.py
for a joint game with friends, the challenge of the game is made by the "Pikkalo" team
# Used technologies
The whole project is written in pure Python version 3.10.4
List of the main packages used:
- <speech_recognition> # for speech recognition
- pyttsx3 # for voice text output
- os # to define microphone
- from bs4 import BeautifulSoup # for data parsing
- requests # to get a page on the web
- random # for different answers from the dialogue thread and the same answers
- execfile # to include game.py
- from pydub import AudioSegment # to include an audio file to get started
- from pydub.playback import play # to include an audio file to get started
# Major Issues Resolved
- Implementation of a common parser in a separate function
- Algorithm reducing time complexity from O(n*2) to O(n log n)
- Variation of answers
- Advanced understanding of lexical constructions
- Improved understanding of parsing information from various web resources
- GUI building logic
- Logic of step-by-step optimization of the project
- Logic of data storage and use
