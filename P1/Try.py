from Seq1Try import Seq
s = "ADA"
#print(Seq.count_base(s))
#print(Seq.count_base_dict(s))
#print(Seq.reverse_string(s))
#print(Seq.comp_str(s))
filename = Seq.valid_filename()
sequence = Seq.seq_read_fasta(filename)
