# TwitchPlays
This is a modified version of DougDougs open source code for Twitch Plays streams. It should be mostly the same functionally, but is more separated out such that it's easier to parse.
The core differences are that
- Rather than needing to log in using core, you can have a function in the Stream Connection factory to log in for you,
- Twitch and YT are separate files with their own handling, but derive from the same abstract class so that you can treat 'em identically so long as you don't go fumbling too deep
- Gameplay handling code is stored in its own file rather than in the root, meaning it's easier to store away for future use
- Messages have a dedicated class, meaning that you can have functions that are associated with them - examples include basic A-crew and Z-crew tests

To run the code you will need to install Python 3.9.  
Additionally, you will need to install the following python modules using Pip:  
python -m pip install keyboard  
python -m pip install pydirectinput  
python -m pip install pyautogui  
python -m pip install pynput  
python -m pip install requests  

Once Python is set up,
- Create a function in the stream factory to connect to your account
- In the template file, assign t to the result of the function

This code is originally based off Wituz's Twitch Plays template, then expanded by DougDoug and DDarknut with help from Ottomated for the Youtube side. For now I am not reviewing any pull requests or code changes, this code is meant to be a simple prototype that is uploaded for educational purposes. But feel free to fork the project and create your own version!
