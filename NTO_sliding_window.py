def sliding_window(seq, n):
    seq = seq.upper().strip()
    GC_list = []
    for start in range(0, len(seq) - (n - 1), 1):
        kmer = seq[start:start + n]
        count_G, count_C = 0, 0
        for i in kmer:
            if i == 'G':
                count_G += 1
            elif i == 'C':
                count_C += 1
        GC_content = (count_G + count_C) / n
        GC_list.append(GC_content)
    return GC_list


print(sliding_window('GATCGATCACGATCGACTAGCTACGATCGC', 20))