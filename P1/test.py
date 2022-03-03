from Seq1Try import Seq
gene_list = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P", "BANNA"]
for l in gene_list:
    #inicializar una instancia de Seq a null
    sequence = Seq()
    sequence.valid_filename_2(l)
    sequence.seq_read_fasta(l)
    try:
        seq = list(sequence.count_base_dict().values()) #get a list of values of the dict
        val = max(seq) #Find max value of that list
        seq = sequence.count_base_dict() #Transform seq to dict again
        print("Gene " + l + ": Most frequent Base: " + list(seq)[list(seq.values()).index(val)])
    except ValueError:
        pass