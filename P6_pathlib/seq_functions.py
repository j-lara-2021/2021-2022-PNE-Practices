from Seq1 import Seq
def ping(method):
    body = open("html/" + method + ".html", "r").read()
    return body
def get(filename,method,sequences):
    seq_num = int(filename[1].split("&")[0])
    filename = str(filename[-1])
    body = open("html/" + filename + ".html", "r").read().format(num=seq_num, seq=sequences[seq_num])
    return body
def gene(filename):
    gene = filename[1].split("&")[0]
    filename = str(filename[-1])
    sequence = open("genes/" + gene + ".txt", "r").read()
    sequence = sequence[sequence.find("\n"):]
    body = open("html/" + filename + ".html", "r").read().format(gene=gene, seq=sequence)
    return body

def operate(method,filename):
    if Seq.valid_sequence2(filename[1].split("&")[0].upper()):
        sequence = filename[1].split("&")[0].upper()
    else:
        pass
    filename = str(filename[-1])
    try:
        if method == "COMP":
            result = sequence.replace("A","t").replace("T","a").replace("C","g").replace("G","c").upper()
            file = "OPERATE"
        elif method == "INFO":
            try:
                d = {"A": 0, "C": 0, "G": 0, "T": 0, "A%": 0, "C%": 0, "G%": 0, "T%": 0}
                for b in sequence:
                    d[b] += 1
                    d[b + "%"] = round((d[b] / len(sequence) * 100), 2)
                result = f"Total length: {len(sequence)}\n A: {d['A']} ({d['A%']} %)\n C: {d['C']} ({d['C%']} %)\n G: {d['G']} ({d['G%']} %)\n T: {d['T']} ({d['T%']} %)\n"
                file = "OPERATE"
            except KeyError:
                file = "error"
        elif method == "REV":
            result = sequence[::-1]
            file = "OPERATE"
        try:
            body = open("html/"+ file + ".html", "r").read().format(seq=sequence, operation = method, result=result)
        except UnboundLocalError:
            body = open("html/error.html", "r").read()
    except UnboundLocalError:
        body = open("html/error.html", "r").read()
    return body