class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases = "NULL"):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        if self.strbases == "NULL":
            print("NULL Seq created")

        elif not self.valid_sequence():
            self.strbases = "ERROR"
            print("INVALID Seq!")
        else:
            print("New sequence created!")


    @staticmethod
    def valid_sequence2(sequence):
        valid = True
        i = 0
        while i < len(sequence) and valid:
            c = sequence[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

    def valid_sequence(self):
        valid = True
        i = 0
        while i < len(self.strbases) and valid:
            c = self.strbases[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases != "ERROR" and self.strbases != "NULL":
            length = len(self.strbases)
        else:
            length = 0
        return length