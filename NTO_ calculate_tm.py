def calculate_tm(primer):
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

print(calculate_tm("ATGCCAATGGGTCCAGCTTTA"))