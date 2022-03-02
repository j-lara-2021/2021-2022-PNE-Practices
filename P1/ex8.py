from Seq1 import Seq
sequence_list = ["", "ACTGA", "Invalid sequence"]
sequences = []
for s in sequence_list:
    if s == "":
        sequences.append(Seq())
    else:
        sequences.append(Seq(s))
for i in range(0, len(sequences)):
    print(f"Sequence {i + 1}: (Length: {Seq.len(sequences[i])} ) {sequences[i]} \n"
          f"    Bases: {Seq.count_base_dict(sequences[i])}\n"
          f"    Rev: {Seq.reverse_string(sequences[i])}\n"
          f"    Comp: {Seq.comp_str(sequences[i])}")