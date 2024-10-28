from MessageHandler import MessageHandler
from StreamConnections.Message import Message
from TwitchPlays_KeyCodes import *


class GTAVMessageHandler(MessageHandler):
    shortPress = 0.7
    medPress = 1
    longPress = 2

    def handleMessage(msg: Message):
        contents = msg.contents
        # If the chat message is "left", then hold down the A key for 2 seconds
        if contents == "left":
            HoldAndReleaseKey(A, GTAVMessageHandler.longPress)

        # If the chat message is "right", then hold down the D key for 2 seconds
        if contents == "right":
            HoldAndReleaseKey(D, GTAVMessageHandler.longPress)

        # If message is "drive", then permanently hold down the W key
        if contents == "drive":
            ReleaseKey(S) #release brake key first
            HoldKey(W) #start permanently driving

        # If message is "reverse", then permanently hold down the S key
        if contents == "reverse":
            ReleaseKey(W) #release drive key first
            HoldKey(S) #start permanently reversing

        # Release both the "drive" and "reverse" keys
        if contents == "stop":
            ReleaseKey(W)
            ReleaseKey(S)

        # Press the spacebar for 0.7 seconds
        if contents == "brake":
            HoldAndReleaseKey(SPACE, GTAVMessageHandler.shortPress)

        # Press the left mouse button down for 1 second, then release it
        if contents == "shoot":
            pydirectinput.mouseDown(button="left")
            time.sleep(GTAVMessageHandler.medPress)
            pydirectinput.mouseUp(button="left")

        # Move the mouse up by 30 pixels
        if contents == "aim up":
            pydirectinput.moveRel(0, -30, relative=True)

        # Move the mouse right by 200 pixels
        if contents == "aim right":
            pydirectinput.moveRel(200, 0, relative=True)
