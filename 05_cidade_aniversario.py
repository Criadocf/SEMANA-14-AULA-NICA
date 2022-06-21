#05. Leia um mês e uma população. Mostre as cidades com população maior que o valor lido fazem aniversário no mês
#informado.
#Veja o exemplo para o mês com valor 4 e 50000 para a população:
#CIDADES COM MAIS DE 50000 HABITANTES E ANIVERSÁRIO EM ABRIL:
#Penedo(AL) tem 59020 habitantes e faz aniversário em 12 de abril.
#Itacoatiara(AM) tem 84676 habitantes e faz aniversário em 25 de abril.
#Araci(BA) tem 51912 habitantes e faz aniversário em 7 de abril.
#Fortaleza(CE) tem 2431415 habitantes e faz aniversário em 13 de abril.

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

mes_niver = int(input())
populacao_lida = int(input())
meses = ('janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro')
meses_2 = ('JANEIRO','FEVEREIRO','MARÇO','ABRIL','MAIO','JUNHO','JULHO','AGOSTO','SETEMBRO','OUTUBRO','NOVEMBRO','DEZEMBRO')

ch = carrega_cidades()

print(f'CIDADES COM MAIS DE {populacao_lida} HABITANTES E ANIVERSÁRIO EM {meses_2[mes_niver-1]}:')
for c in ch:
    if mes_niver == c[4] and c[5] > populacao_lida:
        print(f'{c[2]}({c[0]}) tem {c[5]} habitantes e faz aniversário em {c[3]} de {meses[mes_niver-1]}.')

