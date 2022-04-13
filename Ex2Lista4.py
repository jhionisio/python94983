n = int(input("Digite o número de alunos da sala "))

a = 0

ac = 0

while a < n:
    nota = int(input("Digite a nota dos alunos da sala "))

    ac = ac + nota
    
    a = a + 1

m = ac / n

print("A média de nota da sala é {}".format(m))
