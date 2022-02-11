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
def seq_count(filename):
    gene_dict = {}
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
    gene_dict["A"] = A
    gene_dict["C"] = C
    gene_dict["G"] = G
    gene_dict["T"] = T
    return gene_dict

def seq_complement(filename):
    seq = open("./Session04/" + filename + ".txt", "r").read()
    seq = seq[seq.find("\n"):].replace("\n", "")[:20]
    c_seq = ""
    for r in seq:
        if r == "A":
            c_seq = c_seq + "T"
        elif r == "T":
            c_seq = c_seq + "A"
        elif r == "G":
            c_seq = c_seq + "C"
        elif r == "C":
            c_seq = c_seq + "G"

    return seq, c_seq
