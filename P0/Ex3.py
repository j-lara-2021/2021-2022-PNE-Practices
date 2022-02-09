import Seq0
gene_list = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
for l in gene_list:
    print("The length of " + l + " is: " + str(len(Seq0.seq_read_fasta(l))))