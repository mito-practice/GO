from Bio.Seq import Seq
seq = Seq('TTGCTGCACTGTTCCCTATGCCTAAGGATTCGTTCTAGCGAATTATGGCCAACACCAACGGGAGGAAAGTTGCCTAGTGATATCACGCCATCCCGCCACGTCCCCCCGAACACTCTAGGTATTGACCAATCTCACTGTTGCAGACCCTTCTGAGCAGTGACGGTAAATATAGGCTTTGCTGAACATACGATGACGGTGGTCCAGTTTACGCTAAATACGAACACATTTGGAGATGGGTGATGAGTACGTAATACCGTTGGCGTTAATATAGTTGCGCGGTCCTTAATTTGGCTCGTAAGTCCTAATTGATGACCGATGTTGGGCAGAAGTCTTCGCATTGTTCCTGTGCGCTTGTCCATTAGCGGCCATGTAGTACAACTACTCACTGCATAACAGTGGCTTTTGTGATCCCAGTCCTGGTATGACGCTGCCTCTTGCAGTGAAAGAATATTTACATCTATAGTAAAGCGATCCGAACAGAACCTAGTCGAGTTCTTGGCGAGGTACAGCGGATATATGAGAGATCACGAGAACACTACCCCCAATTGTCATCAACACGACGCCTGATCGTTATGATCTGGTGTTCATATTGGTCGACGGGTATGTAATATAAGTTCTGTATGGCAGTTAAACAGTACGTCGCAATTGACTAGACGCCTTAGCAAGTTGAACTAGGAAGTCATGCACGCTACCTATAACTCACAGTGAAACCTTACCACATTAGGTACCTCTAATAACGTGGTTTATCTTTCGGAAGCCTGAACAGCGATGATTGGAAATGGCCACACCCATTACGGAAGGGAATGGCAGCCGCGCTCCGAGCGACAGTAGGACGCAATATTTTTAACATTTCAGTGCATAGCAATTGCACTCAAGAGAGTGCACCCGGAAGTGCCAAGGTTCCTGAGTGCAACGAAGGCCGTTCTTGGGAACTGATTCTGTTGTCTCCGAATCTTTTAGTATCTGAAGGTTATAGAGTAAA')
A = seq.count('A')
C = seq.count('C')
G = seq.count('G')
T = seq.count('T')
print(f'{A} {C} {G} {T}')
GC = ((G + C)/(A + C + G + T)) * 100
print(GC)
