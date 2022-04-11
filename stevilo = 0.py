for i in range(10000, 1, -1):
    st_del = 0
    for j in range(2, i):
        if i % j == 0:
            st_del += 1
    if st_del == 0:
        print(i)
        break