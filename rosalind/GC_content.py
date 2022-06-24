from Bio import SeqIO
db = {}
for dna_seq in SeqIO.parse('/home/glebo/Downloads/rosalind_gc.txt', 'fasta'):
    id = dna_seq.id
    A = dna_seq.seq.count('A')
    C = dna_seq.seq.count('C')
    G = dna_seq.seq.count('G')
    T = dna_seq.seq.count('T')
    GC_content = ((G + C) / (A + C + G + T)) * 100
    db[id] = GC_content
for k,v in db.items():
    if v == max(db.values()):
        id = k
        GC_content = v
print(f'{id}\n{GC_content}')
#print(f'{[k for k,v in db.items() if v == max(db.values())]} \n{max(db.values())}')
