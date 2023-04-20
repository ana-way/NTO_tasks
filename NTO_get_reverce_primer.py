def GC_calculate(primer):
    nucl_count = {'A': 0,
                  'T': 0,
                  'C': 0,
                  'G': 0}

    count_G, count_C = 0, 0

    for i in primer:
        nucl_count[i] += 1
        if i == 'G':
            count_G += 1
        elif i == 'C':
            count_C += 1
    primer_len = len(primer)
    GC_content = (count_G + count_C) /primer_len * 100
    return GC_content


def tm_calculate(primer):
    nucl_count = {'A': 0,
                  'T': 0,
                  'C': 0,
                  'G': 0}
    primer = primer.upper().strip()
    for i in primer:
        nucl_count[i] += 1
    Tm = 64.9 + 41 * (nucl_count['G'] + nucl_count['C'] - 16.4) / (
            nucl_count['A'] + nucl_count['T'] + nucl_count['G'] + nucl_count['C'])
    return round(Tm)


def get_complementary_seq(seq):
    bases = {'A': 'T',
             'T': 'A',
             'C': 'G',
             'G': 'C'}
    comlem_seq = ''
    for i in seq:
        comlem_seq += bases[i]
    return comlem_seq



def self_compl_FP(primer,n):
    pattern = primer[:n]
    reverse_primer = primer[::-1]
    comlem_pattern = get_complementary_seq(pattern)

    complem_reverse_pattern = comlem_pattern[::-1]

    chek1 = primer.find(complem_reverse_pattern)
    chek2 = reverse_primer.find(complem_reverse_pattern)

    if chek1 > 0 or chek2 > 0:
        return False
    else:
        return True

def self_compl_RP(primer,n):
    pattern = primer[-n:]
    reverse_primer = primer[::-1]
    comlem_pattern = get_complementary_seq(pattern)
    complem_reverse_pattern = comlem_pattern[::-1]

    chek1 = primer.find(complem_reverse_pattern)
    chek2 = reverse_primer.find(complem_reverse_pattern)

    if chek1 > 0 or chek2 > 0:
        return False
    else:
        return True



def get_reverse_primer(seq,FP,lenRP, min_amplicon,max_amplicon,minGC=50,maxGC=60,minTm=50,maxTm=60,n_SC=4):

    # приведение к стандартному виду
    seq = seq.upper().strip()
    FP = FP.upper().strip()


    # проверка прямого праймера

    good_GC, good_Tm, good_selfcompl = None, None, None

    FP_GC = GC_calculate(FP)
    FP_Tm = tm_calculate(FP)
    good_selfcompl = self_compl_FP(FP, n_SC)

    if (FP_GC >= minGC) and (FP_GC <= maxGC):
        good_GC = True
    if (FP_Tm >= minTm) and (FP_Tm <= maxTm):
        good_Tm = True

    if good_Tm and good_GC and good_selfcompl:
        FP_start = seq.find(FP) # начало ампликона
        search_region = seq[FP_start:]

        compl_search_region = get_complementary_seq(search_region)
        compl_reverse_search_region = compl_search_region[::-1]

        for start in range(0, len(compl_reverse_search_region) - (lenRP - 1), 1):
            # проверка обратного праймера
            RP = compl_reverse_search_region[start:start + lenRP]
            # if RP == 'CGATTAGTACGGTCGATCGC':
            #     print('here')
            RP_GC = GC_calculate(RP)
            RP_Tm = tm_calculate(RP)


            good_GC, good_Tm, good_selfcompl = None, None, None

            good_selfcompl = self_compl_RP(RP, n_SC)

            if (RP_GC >= minGC) and (RP_GC <= maxGC):
                good_GC = True

            if (RP_Tm >= minTm) and (RP_Tm <= maxTm):
                good_Tm = True
            if good_Tm and good_GC and good_selfcompl:
                # проверка длины ампликона
                RP_compl =get_complementary_seq(RP)
                RP_compl_reverse = RP_compl[::-1]
                end_amlicon = seq.find(RP_compl_reverse) +lenRP
                cur_amplicon = len(seq[FP_start:end_amlicon])

                if (cur_amplicon >= min_amplicon) and (cur_amplicon <= max_amplicon):
                    return RP
            else:
                if start + 1 == len(compl_reverse_search_region) - (lenRP - 1):
                    return False
                else:
                    continue
    else:
        return False





print(get_reverse_primer('AATATACATACAATGCATCGATCGATCGACTAGCTAGCATCGATCGATCAGCTAGCATCGATC', 'CAATGCATCGATCGATCGAC', 20, 45, 100))
print(get_reverse_primer('TAGCATGCATCGATCGACTAGCTACGATCGATCGACTAATTACTACGGCCGCGATCGACCGTACTAATCGATCATGTAATATTACGATCGAT', 'AGCATGCATCGATCGACTAGC', 20, 60, 100))
print(get_reverse_primer('ATTATCGATCGATCAGTATATATCGCGCGCGATATATGCATCGATCGATCGACTAGCTACGA', 'ATATCGCGCGCGATATATGC', 20, 40, 100))




