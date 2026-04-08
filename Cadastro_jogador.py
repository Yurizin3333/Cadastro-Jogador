dados = dict()
gols = list()
print()
dados['nome'] = str(input("Nome do jogador: "))
partidas = int(input("Quantas partidas jogadas?: "))
for partida in range(0, partidas):
    gols.append(int(input(f"   Quantos gols na partida {partida}?: ")))
dados['gols'] = gols[:]
dados['total'] = sum(gols)
print("=+" * 25)
print(dados)    
print("=+" * 25)
for k, v in dados.items():
    print(f"O campo {k} tem valor {v}")
print("=+" * 25)
dados['partidas'] = partidas
print(f"O jogador {dados['nome']} jogou {dados['partidas']} partidas!")
for p, valor in enumerate(gols):
    print(f"   => Na partida {p}, ", end="")
    print(f"fez {valor} gols.")
print(f"Foi um total de {dados['total']} gols!")
print()