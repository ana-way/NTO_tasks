def pam_variant(pam):
    import itertools
    alphabet = {'R': ['G', 'A'],
                'Y': ['T', 'C'],
                'K': ['G', 'T'],
                'M': ['A', 'C'],
                'S': ['G', 'C'],
                'W': ['A', 'T'],
                'B': ['G', 'T', 'C'],
                'D': ['G', 'A', 'T'],
                'H': ['A', 'C', 'T'],
                'V': ['G', 'C', 'A'],
                'N': ['A', 'G', 'C', 'T'],
                'G': ['G'],
                'C': ['C'],
                'T': ['T'],
                'A': ['A']}

    pam_len = len(pam)
    position_variant = [0] * pam_len
    for i in range(pam_len):
        position_variant[i] = alphabet[pam[i]]

    data = list(itertools.product(*position_variant))

    pams = (''.join(w) for w in data)
    return pams


def prefix_func(s_param):
    pr = [0] * (len(s_param))
    for i in range(1, len(s_param)):
        k = pr[i - 1]
        while k > 0 and s_param[k] != s_param[i]:
            k = pr[k - 1]
        if s_param[k] == s_param[i]:
            k = k + 1
        pr[i] = k
    return pr


def kmp(text, subs):
    sub_len = len(subs)
    text_len = len(text)
    if not text_len or sub_len > text_len:
        return []

    P = prefix_func(subs)

    entries = []
    i = j = 0
    while i < text_len and j < sub_len:
        if text[i] == subs[j]:
            if j == sub_len - 1:
                entries.append(i - sub_len + 1)
                j = 0

                i = i - (sub_len - 2)
            else:
                j += 1
            i += 1
        elif j:
            j = P[j - 1]
        else:
            i += 1
    if entries:
        return entries


def get_complementary_rev_seq(seq):
    bases = {'A': 'T',
             'T': 'A',
             'C': 'G',
             'G': 'C'}
    comlem_seq = ''
    for i in seq:
        comlem_seq += bases[i]
    return comlem_seq[::-1]


def find_target(seq, pam, orient, target_l):
    def func(param_seq):
        for i in pam_variant(pam):
            pam_start = kmp(param_seq, i)
            if pam_start:
                for i in pam_start:

                    if orient == 'R' and i > target_l:
                        targets.append(param_seq[i - target_l:i])
                    if orient == 'L' and i < len(seq) - target_l:
                        pam_end = len(pam)
                        targets.append(param_seq[i + pam_end:i + pam_end + target_l])

    targets = []
    func(seq)
    func(get_complementary_rev_seq(seq))

    return sorted(targets)


print(find_target('TGATGATCATCGATCGGTACGATCGATCCTAGCATGCATGGTAC', 'NGG', 'R', 20))
print(find_target('TAGCTACGATCGATCGTTTCTAGCTACGATGCAAGAAAGATCGATCGATCGACGTACG', 'YTTN', 'L', 21))
