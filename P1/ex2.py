from Seq1 import Seq
sequence_list = ["", "ACTGA"]
sequences = []
for s in sequence_list:
    if s == "":
        sequences.append(Seq())
    else:
        sequences.append(Seq(s))
for i in range(0, len(sequences)):
    print(f"Sequence {i + 1}: {sequences[i]}")







