estoque = [
    [1990, 25, 296, 460, 12000, 1562],
    [250, 600, 5862, 56241, 900, 1000],
    [4580, 1700, 45, 87, 1520, 9698],
    [38, 894, 144, 2590, 1000, 4950],
    [19, 9521, 9634, 38000, 40000, 50]
]

fabricas = ['fabrica01', 'fabrica02', 'fabrica03', 'fabrica04', 'fabrica05', 'fabrica06']
nivel_minimo = 50
fabrica_abaixo_nivel = []

for i, lista in enumerate(estoque):
    for qtdd in lista:
        if qtdd < nivel_minimo:
            if fabricas[i] in fabrica_abaixo_nivel:
                pass
            else:
                fabrica_abaixo_nivel.append(fabricas[i])
print(fabrica_abaixo_nivel)