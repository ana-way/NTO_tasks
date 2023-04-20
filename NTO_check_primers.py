def check_primer(primer, minGCcontent=50, maxGCcontent=60,min_len=18, max_len=25):
    cur_len = len(primer.strip())
    if (cur_len >= min_len) and (cur_len <= max_len):
        primer = primer.upper().strip()
        count_G, count_C = 0, 0
        for i in primer:
            if i == 'G':
                count_G += 1
            elif i == 'C':
                count_C += 1
        GC_content = (count_G + count_C) / cur_len * 100
        if (GC_content >= minGCcontent) and (GC_content <= maxGCcontent):
            return True
        else:
            return False
    else:
        return False

print(check_primer('cgtatgcatcagtataggcaatcc', 40, 60,20, 30))