import Seq0
filename = Seq0.valid_filename()
A,C,G,T = Seq0.seq_count_base(filename)
print("""Number of A's in """ + filename + " "+ str(A) + "\n" +
""" Number of C's in """ + filename + " " + str(C) + "\n" +
""" Number of G's in """ + filename + " " + str(G) + "\n" +
""" Number of T's in """ + filename + " " + str(T))
