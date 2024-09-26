"""
We want to have a new class Item such as :

A new item can be created with Item(price, weight)
    The price and weight of an item can be accessed with
    item.price and item.weight.
    Write the code for this class, with the appropriate constructor.
Example of code using the class: i = Item(10, 20)
"""

#creer une fonction premier qui prend un nombre et retourn true si le nombre est premier
def premier(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


#creer une fonction pour afficher les nombre premier inferieur a 100
def premier_inferieur(n):
    for i in range(2, n):
        if premier(i):
            print(i)


premier_inferieur(100)
