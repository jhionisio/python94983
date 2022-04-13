n = int(input("Digite o número de alunos da sala "))

a = 0

ac = 0

acan = 0

acap = 0

while a < n:
    nota = int(input("Digite a nota dos alunos da sala "))

    if nota < 5 and nota > 0:
        acan = acan + 1

        ac = ac + nota
    
        a = a + 1

    if nota >= 5:
        acap = acap + 1 

        ac = ac + nota

        a = a + 1

m = ac / n

print("A média de nota da sala é {}, e foram {} alunos negativos e {} alunos positivos".format(m, acan, acap))
