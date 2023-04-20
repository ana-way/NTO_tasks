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

# process = psutil.Process(os.getpid())
# start = time.time()
# # time.sleep(1)
# print(is_self_compliment('ATGGCAGCCCACACGATACAGGG', 3))
# print(time.time() - start)
# print(process.memory_info().rss)  # in bytes
#
# print(True or False)