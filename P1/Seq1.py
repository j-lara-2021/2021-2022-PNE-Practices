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

    def count_base(self):
        A = 0
        C = 0
        G = 0
        T = 0
        if self.strbases != "ERROR" and self.strbases != "NULL":
            for i in self.strbases:
                if i == "A":
                    A += 1
                elif i == "C":
                    C += 1
                elif i == "G":
                    G += 1
                elif i == "T":
                    T += 1
        else:
            pass
        #print(f"A: {A},   C: {C},   T: {T},   G: {G},")
        return A, C, T, G

    def count_base_dict(self):
        base_dict = {"A": 0, "T": 0, "C": 0, "G": 0,}
        if self.strbases != "ERROR" and self.strbases != "NULL":
            for i in self.strbases:
                if i == "A":
                    base_dict["A"] += 1
                elif i == "C":
                    base_dict["C"] += 1
                elif i == "G":
                    base_dict["G"] += 1
                elif i == "T":
                    base_dict["T"] += 1
        else:
            pass
        #print(f"A: {A},   C: {C},   T: {T},   G: {G},")
        return base_dict


    def reverse_string(self):
        reverse_str = ""
        if self.strbases != "ERROR" and self.strbases != "NULL":
            reverse_str = self.strbases[::-1]
        else:
            reverse_str = self

        return reverse_str

    def comp_str(self):
        comp_str = ""
        if self.strbases != "ERROR" and self.strbases != "NULL":
            for i in self.strbases:
                if i == "A":
                    comp_str = comp_str + "T"
                elif i == "T":
                    comp_str = comp_str + "A"
                elif i == "C":
                    comp_str = comp_str + "G"
                elif i == "G":
                    comp_str = comp_str + "C"
        else:
            comp_str = self
        return comp_str

    def valid_filename():
        exit = False
        while not exit:
            filename = input("What file do you want to open?:")
            try:
                f = open("../P0/Session04/" + filename + ".txt", "r")
                exit = True
                return filename
            except FileNotFoundError:
                print("FIle does not exist.")

    def seq_read_fasta(filename):
        seq = open("../P0/Session04/" + filename + ".txt", "r").read()
        seq = seq[seq.find("\n"):].replace("\n", "")
        return seq