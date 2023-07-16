# Unscramble The Word (discord bot)
That is the bot that will scramble one word from list when someone says !scramble in discord chat.
(this version uses massive of words from some website (but still 1 word per line) )

In discord chat where bot will be allowed to run say
# !scramble

You need to figure out what word it was and write it in chat, if your answer is correct it will ping you saying you unscrambled the word and how much time it took.
If someone else answers correctly, the bot will congratulate them instead, pinging both original user and the one who asnwered 

use git https://git-scm.com/downloads

1. Download python https://www.python.org/downloads/release/python-3114/ and install it
2. Open https://discord.com/developers/
3. Create a new application, fill out settings, open Bot tab, !!! NOW HERE YOU NEED TO ENABLE MESSAGE CONTENT INTENT (so it knows what did you answer)
4. Add the bot to your server (use guides maybe)
5. Download ZIP, copy files to empty folder, open yourtoken.py with notepad, replace text in ' ' with discord bot key
6. After that use right button of your mouse, press GIT BASH HERE, type (or copy):  python3 -m pip install -U discord.py
7. Open file StartBot.bat (for it to run) (you can rename that bat file)
