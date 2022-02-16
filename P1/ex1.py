from Seq1 import Seq

s1 = "ACTGA"
sequence_list = []
if Seq.valid_sequence2(s1):
    sequence_list.append(Seq(s1))
else:
    sequence_list.append(Seq("ERROR"))

print("Sequence 1: (Length: " + str(len(s1)) + ")",  sequence_list[0])


