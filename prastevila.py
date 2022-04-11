for i in range(2000, 1000, -1):
    st_del = 0
    for j in range(2, i):
        if i % j == 0:
            st_del += 1
    if st_del == 0:
        print(i)
       