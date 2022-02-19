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
          f"A: {Seq.count_base(sequences[i])[0]}, "
          f"C: {Seq.count_base(sequences[i])[1]}, "
          f"T: {Seq.count_base(sequences[i])[2]}, "
          f"G: {Seq.count_base(sequences[i])[3]}, ")
