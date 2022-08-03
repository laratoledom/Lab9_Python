#Entrada e leitura
n = int(input())
lista_jog = []
lista_pont = []
for i in range(n):
    lista_ind = []
    for j in range(5):
        jogador = str(input())
        lista_ind.append(jogador)
        if jogador not in lista_jog:
            lista_jog.append(jogador)
            lista_pont.append(0)
    pos1 = lista_jog.index(lista_ind[0])
    lista_pont[pos1] = lista_pont[pos1] + 6
    pos2 = lista_jog.index(lista_ind[1])
    lista_pont[pos2] = lista_pont[pos2] + 4
    pos3 = lista_jog.index(lista_ind[2])
    lista_pont[pos3] = lista_pont[pos3] + 3
    pos4 = lista_jog.index(lista_ind[3])
    lista_pont[pos4] = lista_pont[pos4] + 2
    pos5 = lista_jog.index(lista_ind[4])
    lista_pont[pos5] = lista_pont[pos5] + 1

#Leitura e saída
pont_final = sorted(lista_pont)
pont_final.reverse()
m = 0
while m < len(pont_final):
    pos_elem = lista_pont.index(pont_final[m])
    print(lista_jog[pos_elem] + ":", lista_pont[pos_elem])
    m = m + 1
