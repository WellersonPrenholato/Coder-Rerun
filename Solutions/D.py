txt = []
N = int(input())
for i in range(N):
    txt.append(input())
f = []
Q = int(input())
for q in range(Q):
    f.append(input())

e = []
for consulta in f:
    qtd = 0
    maxLen = 0
    for p in txt:
        if (p.find(consulta) == 0):
            qtd = qtd + 1
            maxLen = max(maxLen, len(p))

    if(qtd > 0):
        e.append([qtd, maxLen])
    else:
        e.append([-1])

for i in e:
    if (len(i) == 2):
        saida = '{} {}'.format(i[0], i[1])
    else:
        saida = '{}'.format(i[0])
    print(saida)