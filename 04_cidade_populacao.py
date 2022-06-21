#04. Leia uma população e informe as cidades com população maior que o valor lido. Veja o exemplo:
#Veja o exemplo para a leitura de 50000 para a população:
#CIDADES COM MAIS DE 50000 HABITANTES:
#IBGE: 120040 - Rio Branco(AC) - POPULAÇÃO: 290639
#IBGE: 270030 - Arapiraca(AL) - POPULAÇÃO: 202398
#IBGE: 270040 - Atalaia(AL) - POPULAÇÃO: 50323

def carrega_cidades():  ##NENHUM PARÂMETRO
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))  #RETORNA ISSO
            )
    arquivo.close()
    return resultado

populacao_lida = int(input())

ch = carrega_cidades()

print(f'CIDADES COM MAIS DE {populacao_lida} HABITANTES:')

for c in ch:
    if c[5] > populacao_lida:
        print(f'IBGE: {c[1]} - {c[2]}({c[0]}) - POPULAÇÃO: {c[5]}')