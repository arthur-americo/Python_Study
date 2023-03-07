''' Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.'''
num = 0
# Define color codes
HEADER = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'

# Tuple
Teams = ("América Mineiro", "Athletico Paranaense", "Atlético Goianiense", "Atlético Mineiro", "Avaí", "Bahia", "Botafogo", "Ceará", "Chapecoense", "Corinthians", "Coritiba", "Cruzeiro", "CSA", "Flamengo", "Fluminense", "Fortaleza", "Goiás", "Grêmio", "Internacional", "Palmeiras", "Paraná", "Ponte Preta", "Red Bull Bragantino", "Santos", "São Paulo", "Sport", "Vasco da Gama", "Vitória")

# Print the first 5 teams
if num >= 0 and num <= 4:
    print(f"{HEADER}Os 5 primeiros times: {ENDC}")
    for team in Teams[:5]:
        print(f"{BLUE}{team}{ENDC}")

# Print the last 4 teams
if num >= 16 and num <= 19:
    print(f"{HEADER}Os últimos 4 colocados: {ENDC}")
    for team in Teams[-4:]:
        print(f"{YELLOW}{team}{ENDC}")

# Print the teams in alphabetical order
print(f"{HEADER}Times em ordem alfabética: {ENDC}")
for team in sorted(Teams):
    print(f"{GREEN}{team}{ENDC}")

# Print the position of Chapecoense
if "Chapecoense" in Teams:
    pos = Teams.index("Chapecoense") + 1
    print(f"{HEADER}Chapecoense está na posição {pos} da tabela.{ENDC}")
else:
    print(f"{RED}Chapecoense não está na tabela.{ENDC}")

