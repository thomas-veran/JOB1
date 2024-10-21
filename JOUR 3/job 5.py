# job 5

def nombre_premiers(n):
    if n <= 1:                        # les nombres <=1 ne sont pas premiers
        return false
for i in range(2, int(n**0.5) + 1):           # verifie les diviseurs jusqu'a la racine carré de n
    if n % i == 0:
        return false                    # n est divisible par i, donc ce n'est pas un nombre premier
    return true                 # n est un nombre premier

for nombre in range(1001):
    if nombre_premiers(nombre):
        print(nombre)



        #projet en pause pour le moment