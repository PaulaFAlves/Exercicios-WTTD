import requests

class Character():
    def __init__(self):
        name = self




    """
    A StarWars character

    >>> Character("Luke Skywalker")
    Character("Luke Skywalker")
    >>> Character("Luke Skywalker").name
    'Luke Skywalker'
    >>> Character("Luke Skywalker").movies
    ['A New Hope', 'Return of the Jedi', 'Revenge of the Sith', 'The Empire Strikes Back', 'The Force Awakens']
    >>> Character("Skywalker")
    Traceback (most recent call last):
        ...
    ValueError: found more than one character with "Skywalker" in the name
    >>> Character("C4PO")
    Traceback (most recent call last):
        ...
    ValueError: this is not the character you are looking for
    """
    pass

def features_together(a, b):
    """
    Returns a list of movie where both character a and character b are present

    >>> features_together(Character("Anakin Skywalker"), Character("Darth Vader"))
    ['Revenge of the Sith']
    >>> features_together(Character("Rey"), Character("Mace Windu"))
    []
    """



    return []

planeta = requests.get("https://swapi.co/api/people/?format=json").json()
m = planeta['results']
i = 0
a = []
b = []
while i < len(m):
    nome = m[i]
    a.append(nome['name'])
    b.append(nome['films'])

    i +=1

i = 0
while i < len(a):
    print(a[i])
    print(b[i])
    i += 1
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()















