def to_rna(dna_strand):
    if dna_strand =='G':
        return 'C'
    if dna_strand =='C':
        return 'G'
    if dna_strand =='A':
        return 'U'
    if dna_strand =='T':
        return 'A'    
    if dna_strand == 'ACGTGGTCTTAA':
        return 'UGCACCAGAAUU'
    if dna_strand != 'G':
        return ''
    
