N = int(input())

frase = []
for p in range(N):
    frase.append(input())

fraseMin = [f.lower().replace('.', '').replace(',', '') for f in frase]

for f in fraseMin:
    maxVenc = 0
    sumLen = 0
    fsp = f.split(' ')
    for p in f.split(' '):
        if (p == 'jogo' or p == 'perdi'):
            maxVenc = max(maxVenc, sumLen + len(p))
            sumLen = 0
        else:
            sumLen = sumLen + len(p)
    print(maxVenc)