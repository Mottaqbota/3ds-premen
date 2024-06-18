#1 | Carros com Tupla
# Pegando o primeiro e último carro
carros = ("Ferrari", "Lamborghini", "Porsche")
print(carros[0])
print(carros[-1])

# Separando cada carro em uma variável

carros1 = carros[0]
carros2 = carros[1]
carros3 = carros[2]

print(carros1, carros2, carros3)

#2 | Pessoas com Tupla
# Criando pessoas com nome e idade
pessoas = ("Jozão", 28, "Mazia", 22, "Preto", 35)
pessoas += ("Nana", 30)
print(pessoas)


def ordenar_por_idade(pessoas):
    return sorted(pessoas, key=lambda pessoa: pessoa[1])

def filtrar_pessoas_jovens(pessoas):
    pessoa_menor_que_trinta = [pessoa for pessoa in pessoas if pessoa[1] < 30]
    print(pessoa_menor_que_trinta)
    return pessoa_menor_que_trinta


