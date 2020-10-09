dim = input()

dim = dim.split(' ')

N, M = int(dim[0]), int(dim[1])
# M = int(input())


ld, lv = [], []

for i in range(N):
    linha = input()
    for x in linha.split(' '):
        if (x[1] == 'V'):
            lv.append(x)
        else:
            ld.append(x)

# ld = ['1D', '2D', '2D', '9D']
# lv = ['7V', '1V', '1V', '3V', '5V']


ld = sorted(ld, reverse=True)
lv = sorted(lv, reverse=True)

for x in lv:
    print(x)
for x in ld:
    print(x)