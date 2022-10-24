from random import choice, sample

carta = [chr(x) for x in range(0x1f0a1, 0x1f0af)]
carta = {
    chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,
}
print("Carta: {}".format(" ".join(carta.keys())))
print("Puntos: {}".format(list(carta.values())))
print("Estándar")
for c, valor in carta.items():
    print("la carta {} vale {}".format(c, valor))
print("Ordenada")
for c in sorted(carta.keys()):
    print("la carta {} vale {}".format(c, carta[c]))
print("Black Jack")
lista_cartas = list(carta)
print("Selecciona:", end=" ")
c = choice(lista_cartas)
score = carta[c]
print(c, end=" ")
c = choice(lista_cartas)
score += carta[c]
print(carta, end=" ")
print("La puntuación máxima obtenida es de ", score)
main_b = sample(lista_cartas, 2)