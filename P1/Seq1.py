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
            A = self.strbases.count("A")
            T = self.strbases.count("T")
            C = self.strbases.count("C")
            G = self.strbases.count("G")
        else:
            pass

        return A, C, T, G

    def count_base_dict(self):
        base_dict = {}
        A = self.strbases.count("A")
        T = self.strbases.count("T")
        C = self.strbases.count("C")
        G = self.strbases.count("G")
        if self.strbases != "ERROR" and self.strbases != "NULL":
            base_dict["A"] = A
            base_dict["C"] = C
            base_dict["T"] = T
            base_dict["G"] = G
        else:
            pass
        return base_dict


    def reverse_string(self):
        reverse_str = ""
        if self.strbases != "ERROR" and self.strbases != "NULL":
            reverse_str = self.strbases[::-1]
        else:
            reverse_str = self

        return reverse_str

    def comp_str(self):
        if self.strbases != "ERROR" and self.strbases != "NULL":
            comp = self.strbases.replace('C', 'g').replace("G", "c").replace("A", "t").replace("T", "a").upper()
        else:
            comp = self
        return comp
    @staticmethod
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

    def valid_filename_2(self,filename):
        exit = False
        while not exit:
            #filename = input("What file do you want to open?:")
            try:
                filename = open("../P0/Session04/" + filename + ".txt", "r")
                exit = True
                return filename
            except FileNotFoundError:
                print(f"File {filename} does not exist.")
                exit = True

    def seq_read_fasta(self, filename):
        try:
            seq = open("../P0/Session04/" + filename + ".txt", "r").read()
            seq = seq[seq.find("\n"):].replace("\n", "")
            self.strbases = seq
        except FileNotFoundError:
            pass

