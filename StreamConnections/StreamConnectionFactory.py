import TwitchConnection


def getJeansTwitch():
    connection = TwitchConnection.Twitch()
    return connection.connect("zamo312")
