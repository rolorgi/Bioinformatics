f = open('rosalind_dna.txt', 'r')
dna = f.readline()

a = dna.count('A')
c = dna.count('C')
g = dna.count('G')
t = dna.count('T')

print(a, c, g, t)