import Seq0
gene_list = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
for l in gene_list:
    seq = list(Seq0.seq_count(l).values()) #get a list of values of the dict
    val = max(seq) #Find max value of that list
    seq = Seq0.seq_count(l) #Transform seq to dict again
    print("Gene " + l + ": Most frequent Base: " + list(seq)[list(seq.values()).index(val)])
    #Transform dict into list [Get the list of values and find the index of the max value]