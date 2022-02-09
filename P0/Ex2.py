import Seq0
filename = Seq0.valid_filename()
sequence = Seq0.seq_read_fasta(filename)
print("The fisrt 20 bases are: " + sequence[:20])