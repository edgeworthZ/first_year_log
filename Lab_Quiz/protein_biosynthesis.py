dna = input('DNA: ')
#Simple Transcription
rna = dna.replace('A','U').replace('C','?').replace('G','C').replace('?','G').replace('T','A')
#Translation
start = rna.index('AUG')
e1,e2,e3 = rna.find('UAA'),rna.find('UGA'),rna.find('UAG')
#Get first found stop codon
end = min([e for e in (e1,e2,e3) if e != -1])
print(f'{(end-start)//3} Amino acid(s)')
