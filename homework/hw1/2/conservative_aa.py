from Bio import SeqIO

seq_list = []
for prot_seq in SeqIO.parse('muscle_res_prot_blastx.fasta', 'fasta'):
    seq_list.append(prot_seq.seq)
conservative_aa = []
for i in range(len(seq_list)):                          # start iterating thru every sequence in order to pop every seq
    seq = seq_list.pop()                                # pop one seq, so that we don't compare it to itself
    for prot in seq_list:                               # grab every unpopped seq
        for AA in range(len(prot)):                     # comb thru every aa in one unpopped seq
            if seq[AA] == prot[AA] and seq[AA] != '-':  # compare aa of unpopped and popped seqs
                conservative_aa.append(seq[AA])
with open('conservative_aa.txt', 'w') as save_file:
    save_file.write(''.join(conservative_aa))

