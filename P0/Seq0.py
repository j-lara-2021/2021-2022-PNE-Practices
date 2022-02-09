def seq_ping():
    print("OK")


def valid_filename():
    exit = False
    while not exit:
        filename = input("What file do you want to open?:")
        try:
            f = open("./Session04/" + filename + ".txt", "r")
            exit = True
            return filename
        except FileNotFoundError:
            print("FIle does not exist.")


def seq_read_fasta(filename):
    seq = open("./Session04/" + filename + ".txt", "r").read()
    seq = seq[seq.find("\n"):].replace("\n", "")
    return seq


def seq_count_base(filename):
    f = open("./Session04/" + filename + ".txt", "r")
    A = 0
    C = 0
    G = 0
    T = 0
    for a in f:
        for l in a:
            if l == "A":
                A += 1
            elif l == "C":
                C += 1
            elif l == "G":
                G += 1
            elif l == "T":
                T += 1
    return A, C, G, T
