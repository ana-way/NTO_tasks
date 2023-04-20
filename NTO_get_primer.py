def get_primer(seq, primer_len, min_GC=50, max_GC=60, min_Tm=50, max_Tm=60, self_compl_base=4):
    def is_self_compliment(primer, n):

        primer = primer.upper().strip()
        reverse_primer = primer[::-1]
        pattern = primer[-n:]
        bases = {'A': 'T',
                 'T': 'A',
                 'C': 'G',
                 'G': 'C'}
        comlem_pattern = ''
        for i in pattern:
            comlem_pattern += bases[i]
        complem_reverse_pattern = comlem_pattern[::-1]

        chek1 = primer.find(complem_reverse_pattern)
        # chek2 = reverse_primer.find(complem_reverse_pattern)
        chek2 = -1

        if chek1 > 0 or chek2 > 0:
            return False
        else:
            return True

    seq = seq.upper().strip()
    primer = ''

    for start in range(0, len(seq) - (primer_len - 1), 1):
        primer = seq[start:start + primer_len]
        nucl_count = {'A': 0,
                      'T': 0,
                      'C': 0,
                      'G': 0}
        count_G, count_C = 0, 0

        for i in primer:
            nucl_count[i] += 1
        GC_content = (count_G + count_C) / primer_len * 100
        Tm = 64.9 + 41 * (nucl_count['G'] + nucl_count['C'] - 16.4) / (
                nucl_count['A'] + nucl_count['T'] + nucl_count['G'] + nucl_count['C'])

        good_GC, good_Tm, good_selfcompl = None, None, None


        if (GC_content >= min_GC) and (GC_content <= max_GC):
            good_GC = True
            if (Tm >= min_Tm) and (Tm <= max_Tm):
                good_Tm = True
        if good_Tm and good_GC:
            good_selfcompl = is_self_compliment(primer,self_compl_base)

        if good_Tm and good_GC and good_selfcompl:
            return primer
        else:
            if start+1 == len(seq) - (primer_len - 1):
                return False
            else:
                continue
#
print(get_primer('AATATACATACAATGCATCGATCGATCGACTAGCTAGCATCGATCGATCAGCTAGCATCGATC', 20))
# print(get_primer('TAGCATGCATCGATCGACTAGCTACGATCGATCGACTAATTACTACGGCCGCGATCGACCGTACTAATCGATCATGTAATATTACGATCGAT', 21))
# print(get_primer('ATATATATCGACGCTATATGCGCTATATACTGACTAGCATCGATCGATATAAAA', 20))