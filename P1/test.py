import Seq1
for i in ["ADA", "FRAT1"]:
    s = Seq1.Seq()
    s.seq_read_fasta(i)

    print(s)
    print(s.len())