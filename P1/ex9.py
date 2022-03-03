from Seq1 import Seq
filename = Seq.valid_filename()
sequence = Seq()
sequence.seq_read_fasta(filename)
sequences = [sequence]

for i in range(0, len(sequences)):
    #sequences[i].len()
    print(f"Sequence {i + 1}: (Length: {sequences[i].len()} ) {sequences[i]} \n"
          f"    Bases: {sequences[i].count_base_dict()}\n"
          f"    Rev: {sequences[i].reverse_string()}\n"
          f"    Comp: {sequences[i].comp_str()}")