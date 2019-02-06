def check():
    n = int(input("endter "))
    s = list(range(n + 1))
    s[1] = 0 
    for i in s:
        if i > 1:
            for j in range(i + i, len(s), i):
                s[j] = 0
    print(s)


check()



#    for i in range(len(s1)-1, -1, -1):
#        if s1[i] == 0:
#            del s1[i]
