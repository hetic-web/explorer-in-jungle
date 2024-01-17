# TECHNIQUE DE COMPREHENSION DE LISTE
# Description: Créer une liste de nombres impairs de 1 à 99 qui sont divisibles par 3 et élever au carré
# 1. Créer une liste de nombres impairs de 1 à 99
# 2. Créer une liste de nombres impairs de 1 à 99 qui sont divisibles par 3
# 3. Créer une liste de nombres impairs de 1 à 99 qui sont divisibles par 3 et élever au carré

# Short version
# L = [result loop filter]
L = [number**2 for number in range(1, 100, 2) if number % 3 == 0]
print(L)

# Long version
L = []
for number in range(1, 100, 2):
    if number % 3 == 0:
        L.append(number**2)

print(L)
