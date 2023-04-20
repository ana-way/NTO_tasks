def tab_prep(s1, s2, open_gap, gap):
    tab = [([0] * int(len(s1) + 2)) for i in range(len(s2) + 2)]

    for k in range(len(s1)):
        tab[0][k + 2] = s1[k]
        tab[1][k + 2] = open_gap + (gap * k)

    for k in range(len(s2)):
        tab[k + 2][0] = s2[k]
        tab[k + 2][1] = open_gap + (gap * k)
    return tab


def align(first, second):
    match, mismatch, open_gap, gap = 2, -1, -2, -1
    my_matrix = tab_prep(first, second, open_gap, gap)

    is_equal = {True: match,
                False: mismatch}
    # Fill matrix
    for i in range(2, len(first) + 2):
        for j in range(2, len(second) + 2):
            d_start = {'diagonal': my_matrix[j - 1][i - 1] + is_equal[my_matrix[0][i] == my_matrix[j][0]],
                       'left': my_matrix[j - 1][i] + gap,
                       'up': my_matrix[j][i - 1] + gap}

            my_matrix[j][i] = max(d_start.values())
            direct = max(d_start, key=d_start.get)

            if direct != 'diagonal':
                d_start['left'] = my_matrix[j - 1][i] + gap
                d_start['up'] = my_matrix[j][i - 1] + gap
            else:
                d_start['left'] = my_matrix[j - 1][i] + open_gap
                d_start['up'] = my_matrix[j][i - 1] + open_gap

    fs = ''
    ss = ''

    i = len(first) + 1
    j = len(second) + 1

    while j != 1 and i != 1:
        d_start = {'diagonal': my_matrix[j - 1][i - 1],
                   'left': my_matrix[j][i - 1],
                   'up': my_matrix[j - 1][i]}
        direct = max(d_start, key=d_start.get)

        if direct == 'diagonal':
            fs += my_matrix[0][i]
            ss += my_matrix[j][0]
            j = j - 1
            i = i - 1
        elif direct == 'left':
            ss += my_matrix[0][i]
            fs += '-'
            i = i - 1
        else:
            fs += my_matrix[j][0]
            ss += '-'
            j = j - 1


    res = [ss[::-1], fs[::-1]]

    return res


# print(align('ATCGATCGATCGATATATCCCGAC', 'ATCGATCGGATATATCCCGAC'))
print(align('CACACAGTGACTAGCTAGCTACGATC', 'CACACAGTCGACTAGCTAGCACGATC'))

