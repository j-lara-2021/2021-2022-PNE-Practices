import Seq0
gene_list = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
for l in gene_list:
    print("Gene " + l +":\n" + "A: " + str(list(Seq0.seq_count_base(l))[0]) + "\n C: " + str(list(Seq0.seq_count_base(l))[1])
    + "\n G: " + str(list(Seq0.seq_count_base(l))[2])+ "\n T: " + str(list(Seq0.seq_count_base(l))[3]))
