class Message:
    sender = ""
    contents = ""
    aCrewSplitoff = "m"

    def __init__(self, sender, contents):
        self.sender = sender
        self.contents = contents

    def isACrew(self):
        if (self.sender == ""):
            return False
        character = self.sender[0].lower()
        return character.isalpha() and character <= Message.aCrewSplitoff

    def isZCrew(self):
        if (len(self.sender) == 0):
            return False
        character = self.sender[0].lower()
        return character.isalpha() and character > Message.aCrewSplitoff

    def isSymbolSquad(self):
        if (len(self.sender) == 0):
            return False
        character = self.sender[0].lower()
        return not character.isalpha()

    def __str__(self):
        return f'Got this message from {self.sender}: {self.contents}'
