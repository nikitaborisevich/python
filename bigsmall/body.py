

def lost():
    s1 = input("Enter prime number ")
    i = 0
    z = s1[i]
    x = s1[i]
    while i != len(s1)-1:
        if z < s1[i+1]:
            z = s1[i+1]
        if x > s1[i+1]:
            x = s1[i+1]
        i += 1

    print("big number",z)
    print("small number ", x)

lost()

###################################################
#x = int(input('Enter number '))
#
#xmin = x % 10
#xmax = x % 10
#x //= 10
#
#while x > 0:
#    z = x % 10
#    if z < xmin:
#        xmin = z
#    if z > xmax:
#        xmax = z
#    x //= 10
#
#print('max number -> %d' % xmin)
#print('min number -> %d' % xmax)
