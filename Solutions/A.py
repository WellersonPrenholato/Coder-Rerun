i = {'A': 0, 'B': 1, 'C': 2}
x = ['0', '0', '0']

def troca(x, o, d):
    # print(o, d, i[o], i[d])
    temp = x[i[o]]
    x[i[o]] = x[i[d]]
    x[i[d]] = temp
    return x

N = int(input())
posIni = input()
x[i[posIni]] = 'X'

zlist = []

for z in range(N):
    zlist.append(int(input()))

for mov in zlist:
    # mov = int(input())
    if (mov == 1):
        x = troca(x, 'A', 'B')
    elif(mov == 2):
        x = troca(x, 'B', 'C')
    else:
        x = troca(x, 'A', 'C')

x = ''.join(x)
loc = x.find('X')

print(list(i.keys())[list(i.values()).index(loc)])