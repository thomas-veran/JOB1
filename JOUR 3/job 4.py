# job 4

for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
        
# on fait une boucle pour écrire de O a 100
# ensuite on fait "SI" i tout les 3% on le met égal a 0 ET tout les 5% on le met égal a 0 aussi si ça arrive la condition est d'afficher fizzbuzz
# elif donc "sinon si" i tout les 3% on écrit fizz
# elif donc "sinon si" i tout les 5% on écrit buzz
