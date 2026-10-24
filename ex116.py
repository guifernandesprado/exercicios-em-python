# Exercício 73 CeV

times = (
    "Palmeiras",
    "Flamengo",
    "Fluminense",
    "Athletico Paranaense",
    "Bragantino",
    "Bahia",
    "Coritiba",
    "São Paulo",
    "Atlético Mineiro",
    "Corinthians",
    "Cruzeiro",
    "Botafogo",
    "Vitória",
    "Internacional",
    "Santos",
    "Grêmio",
    "Vasco da Gama",
    "Remo",
    "Mirassol",
    "Chapecoense",
)
print('-=' * 50)
print(f'Lista de times : {times}')
print('-=' * 50)
print(f'Os 5 primeiros colocados são {times[:5]}')
print('-=' * 50)
print(f'OS 4 últimos colocados são {times[16:]}')
print('-=' * 50)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 50)
print(f'A Chapecoense está em {times.index('Chapecoense')+1}º colocado. ')