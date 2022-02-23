from Seq1 import Seq
gene_list = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
for l in gene_list:
    #inicializar una instancia de Seq a null
    # s.read_fasta(l)
    seq = list(s.count_base_dict(l).values()) #get a list of values of the dict
    val = max(seq) #Find max value of that list
    seq = Seq.count_base_dict(l) #Transform seq to dict again
    print("Gene " + l + ": Most frequent Base: " + list(seq)[list(seq.values()).index(val)])
