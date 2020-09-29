# -*- coding: utf-8 -*-
def transfira(capacidade, capturados, doces, pesos):
    d = [0] * (capacidade + 1)
    for i in range(capturados):
        for j in range(capacidade, pesos[i], - 1):
            d[j] = max(d[j], doces[i] + d[j - pesos[i]])
    return d[capacidade]


if __name__ == "__main__":
    while True:
        try:
            capturados, capacidade = map(int, input().split(" "))
            doces = list(map(int, input().split(" ")))
            pesos = list(map(int, input().split(" ")))

            print(transfira(capacidade, capturados, doces, pesos))
        except EOFError:
            break
