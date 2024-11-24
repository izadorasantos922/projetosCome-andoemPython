nomes128 = [
    "Lucas", "Aa", "Maria", "Rafa", "Clara", "Bruna", "Davi", "Nina", "Luan", "Leila",
    "Tiago", "Paula", "Mário", "Júlia", "Rita", "Vera", "Caio", "Sofia", "Tânia", "Cecília",
    "Otávio", "Fábio", "Catarina", "Débora", "Ivo", "Tadeu", "Laura", "Rony", "Cássia",
    "Gustavo", "Carlos", "Jorge", "Thais", "Fábia", "Erick", "Marta", "Alana", "Breno", 
    "Lívia", "Tânia", "Cláudio", "Beatriz", "Márcio", "Bárbara", "Lúcia", "Edgar", "Elaine",
    "Simone", "Renato", "Júnior", "Felipe", "Roberta", "Diana", "Cléber", "Paulo", "Michele",
    "Aline", "Débora", "Alex", "Marcos", "Célia", "Inês", "Eduardo", "Hugo", "Fernanda",
    "Jaqueline", "Lílian", "Marcelo", "Nelson", "Vânia", "Erika", "César", "Janaína", "Vânia",
    "Ricardo", "Gisele", "Victor", "Helena", "Diana", "Amanda", "Lúcia", "Rosana", "Fernando",
    "Tatiane", "Vinícius", "Jéssica", "Sandro", "Beatriz", "Luciano", "Hélio", "Eva", "André",
    "Patrícia", "Alessandra", "Léo", "Joaquim", "Sílvia", "Carla", "Rebeca", "Flávio", "Karla",
    "Guilherme", "Mário", "Ivone", "Sônia", "Irene", "Cláudio", "Alan", "Daniel", "Jéssica",
    "Rafael", "Nádia", "Fátima", "Mônica", "Raul", "Lucia", "Milena", "Antonio", "Juliana",
    "Marcos", "Simone", "Jair", "Luana", "Aline", "Flávia", "Lorena", "Rogério", "Nadia",
    "Denise", "Vitor", "Nina", "Marina", "Sérgio", "Eliane", "Amélia", "Arthur", "Pâmela"
]

nomes256 = [
    "Lucas", "Pedro", "Maria", "Rafa", "Clara", "Bruna", "Davi", "Nina", "Luan", "Leila",
    "Tiago", "Paula", "Mário", "Júlia", "Rita", "Vera", "Caio", "Sofia", "Tânia", "Cecília",
    "Otávio", "Fábio", "Catarina", "Débora", "Ivo", "Tadeu", "Laura", "Rony", "Cássia",
    "Gustavo", "Carlos", "Jorge", "Thais", "Fábia", "Erick", "Marta", "Alana", "Breno", 
    "Lívia", "Tânia", "Cláudio", "Beatriz", "Márcio", "Bárbara", "Lúcia", "Edgar", "Elaine",
    "Simone", "Renato", "Júnior", "Felipe", "Roberta", "Diana", "Cléber", "Paulo", "Michele",
    "Aline", "Débora", "Alex", "Marcos", "Célia", "Inês", "Eduardo", "Hugo", "Fernanda",
    "Jaqueline", "Lílian", "Marcelo", "Nelson", "Vânia", "Erika", "César", "Janaína", "Vânia",
    "Ricardo", "Gisele", "Victor", "Helena", "Diana", "Amanda", "Lúcia", "Rosana", "Fernando",
    "Tatiane", "Vinícius", "Jéssica", "Sandro", "Beatriz", "Luciano", "Hélio", "Eva", "André",
    "Patrícia", "Alessandra", "Léo", "Joaquim", "Sílvia", "Carla", "Rebeca", "Flávio", "Karla",
    "Guilherme", "Mário", "Ivone", "Sônia", "Irene", "Cláudio", "Alan", "Daniel", "Jéssica",
    "Rafael", "Nádia", "Fátima", "Mônica", "Raul", "Lucia", "Milena", "Antonio", "Juliana",
    "Marcos", "Simone", "Jair", "Luana", "Aline", "Flávia", "Lorena", "Rogério", "Nadia",
    "Denise", "Vitor", "Nina", "Marina", "Sérgio", "Eliane", "Amélia", "Arthur", "Pâmela",
    "Emanuelle", "Gustavo", "Kátia", "Marília", "Léo", "Ana", "Felipe", "Márcia", "Igor",
    "Gabriela", "Lúcia", "Sérgio", "Tácio", "Cláudia", "Thiago", "Giovana", "Júlio", "Noemi",
    "Larissa", "Gilmar", "Rodrigo", "Thais", "Marina", "Tânia", "Ronaldo", "Júlia", "Cristiano",
    "Paula", "João", "Rafael", "Juliana", "Tatiane", "Eduardo", "Pietro", "Lúcia", "Rogério",
    "Amanda", "Laura", "Paula", "Thiago", "Joana", "Lídia", "Carlos", "Cláudia", "Emílio",
    "Renata", "Bruna", "Tereza", "Fábio", "Marcelo", "Neto", "Lais", "Irene", "Valéria",
    "Silvia", "Adriano", "Marcos", "Elisabete", "Liane", "Diana", "Débora", "Rosana", "Rúbia",
    "Júlio", "Ricardo", "Tiago", "Sônia", "Sandro", "Ingrid", "Arthur", "Vera", "Sônia",
    "Beatriz", "Alessandro", "Rita", "Aline", "Thiago", "Letícia", "Fátima", "Gabriela", "Alex",
    "Felipe", "Júnior", "Luciana", "Miguel", "Aline", "Renata", "Vinícius", "Ricardo", "Kátia",
    "Rogério", "Fábio", "Pâmela", "Beatriz", "Alfredo", "Tiago", "Bruna", "Juliana", "Flávio",
    "Tânia", "Amanda", "Carla", "Vinícius", "Renata", "Robson", "Patrícia", "Marcos", "Célia"
]


def binarysearchname(array, name):
    array.sort()
    inicio = 0;
    fim = len(array) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if name == array[meio]:
            return meio;
        elif array[meio] < name:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1


name =  "Sílvia"
indice = binarysearchname(nomes256, name)

if indice != -1:
    print(f"Nome '{name}' encontrado no índice {indice}.")
else:
    print(f"Nome '{name}' não encontrado.")


