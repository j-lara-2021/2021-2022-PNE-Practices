import Seq0
gene_list = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
for l in gene_list:
    print("Gene " + l + "\nFrag: " + list(Seq0.seq_complement(l))[0] + "\nComp: " + list(Seq0.seq_complement(l))[1])