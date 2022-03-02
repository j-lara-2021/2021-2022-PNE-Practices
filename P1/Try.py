from Seq1Try import Seq
s = "ADA"
#print(Seq.count_base(s))
#print(Seq.count_base_dict(s))
#print(Seq.reverse_string(s))
#print(Seq.comp_str(s))
f = Seq.valid_filename(s)
sequence = Seq.seq_read_fasta(f)
