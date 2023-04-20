def find_mutation(ref,exp):
    d = []
    cur_ins = ''
    st_idx = -1
    l_ins = []
    res_del = []

    if '-' not in ref and '-' not in exp:
        return False

    for i in range(len(ref)):
        if ref[i] != exp[i]:
            if exp[i] == '-':
                d.append(i+1)
            else:
                if st_idx == -1:
                    st_idx = i
                    cur_ins = exp[i]
                    if st_idx == len(ref)-1:
                        l_ins.append('ins{}:{}'.format(str(st_idx), exp[i]))
                    continue
                cur_ins += exp[i]
        else:
            if st_idx != -1:
                l_ins.append('ins{}:{}'.format(str(st_idx), cur_ins))
                st_idx = -1

    # del
    if len(d) == 1:
        res_del = f'del{d[0]}'
    elif len(d) > 1:
        res_del = f'del{d[0]}:{d[-1]}'

    return res_del if len(res_del) != 0 else l_ins[0]


print(find_mutation('ATCGATCGGATATATCCCGAC', 'ATCGATCGGATATATCCCGAC'))
print(find_mutation('ATCGATCGATCGATATATCCCGAC', 'ATCGATCG---GATATATCCCGAC'))
print(find_mutation('ACTGAT--ATCAACACGATCGA', 'ACTGATCGATCAACACGATCGA'))
# print(find_mutation('CACACAGT-GACTAGCTAGCTACGATC', 'CACACAGTCGACTAGCTAGC-ACGATC'))
