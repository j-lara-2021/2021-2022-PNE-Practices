import Seq0
gene_list = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
for l in gene_list:
    print("Gene " + l + ": " + str(Seq0.seq_count(l)))