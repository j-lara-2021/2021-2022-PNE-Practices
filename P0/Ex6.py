import Seq0
gene_list = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
for l in gene_list:
    print("Gene " + l + "\nFrag: " + Seq0.seq_read_fasta(l)[:20] + "\nRev: " +Seq0.seq_read_fasta(l)[19::-1] )