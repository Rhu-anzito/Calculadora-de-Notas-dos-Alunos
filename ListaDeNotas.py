#cria uma lista vazia para armazenar as notas
notas = []

quantidade_alunos = int(input("quantos alunos voce deseja cadastrar? "))

#laço for para coletar as notas
for i in range(quantidade_alunos):
    nota = float(input(f"digite a nota do aluno {i + 1}: "))
    notas.append(nota) #adicio a nota ao fim da lista

#calculadora a media, a maior nota e a menor nota
media = sum(notas) / len(notas) #somatorio/n° de notas
maior_nota = max(notas)
menor_nota = min(notas)

#exibe os resultados
print(f"\nAmédia das notas dos alunos é {media: .2f}")
print(f"A maior nota registrada foi {maior_nota: .2f}")
print(f"A menor nota registrada foi {menor_nota: .2f}")
