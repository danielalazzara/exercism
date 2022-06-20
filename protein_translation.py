protein = {'AUG':'Methionine', 'UUU':'Phenylalanine', 'UUC':'Phenylalanine', 'UUA':'Leucine', 'UUG':'Leucine', 'UCU':'Serine', 'UCC':'Serine', 'UCA':'Serine', 'UCG':'Serine', 'UAU':'Tyrosine', 'UAC':'Tyrosine', 'UGU':'Cysteine', 'UGC':'Cysteine', 'UGG':'Tryptophan', 'UAA':'STOP', 'UAG':'STOP', 'UGA':'STOP'}

def proteins(strand):
    sequence = [strand[i: i + 3] for i in range(0, len(strand), 3)]
    result = []
    for codon in sequence:
        if protein[codon] == 'STOP':
            break
        else:
            result.append(protein[codon])
    return result
  
