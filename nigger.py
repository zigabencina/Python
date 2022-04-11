st = 7
while st > 0:
    if st % 3 == 0:
        st= st + 1
    else:
        st = st // 2
    print(st, end = ",")