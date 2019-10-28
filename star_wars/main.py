import requests

class Character:

    def __init__(self, name=None, movies=''):
        self.name = name        
        self.movies = movies

    def personagem(self):
        self.name = None
        self.movies = ''
        return self.name, self.movies

    def __repr__(self):
        return str(self.__dict__)




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

    

def features_together(a, b):
    pass
    """
    Returns a list of movie where both character a and character b are present

    >>> features_together(Character("Anakin Skywalker"), Character("Darth Vader"))
    ['Revenge of the Sith']
    >>> features_together(Character("Rey"), Character("Mace Windu"))
    []
    """

    ## chamar as duas listas e comparar personagens e filmes


    # print(a[0])
    # print(b[0])
    # together = []
    
    # together = [x for x in b[0] if x in b[1]]
    # print(a[0] ,' + ', a[1],' = ', together)

    # # loop para o primeiro persogem será:    a[0] compara com [a + 1]
    # #                                        a[0] compara com [a + 1 + 1]
    # #                                        a[0] compara com [a + 1 + 1 + 1]....
    # # depois: a[2] com

    # # COMPARAR FILMES E NAO PERSONAGENS:
    # # compara 
    # lista_de_filmes = b[0] + b [1]

    # print(lista_de_filmes)

    # # buscar os filmes pela URL




    # return []

# busco a completa de infos dentro da url, esta em um dicionario
planeta = requests.get("https://swapi.co/api/people/?format=json").json()
# # o que eu preciso esta na chave 'results', entao busco ela
m = planeta['results']

# #agora, dentro de m, tenho uma lista com varias infos de cade personagem (chaves), sendo que preciso de 'name' e film'

i = 0
a = []
b = []
while i < len(m):
    nome = m[i]
    a.append(nome['name'])
    b.append(nome['films'])
    i +=1

# agora tenho duas listas:
# 1 - com os nomes dos personagens
# 2 - com lista de lista de filmes de cada um. 

# print(a)
# print(b)

personagem01 = Character('Luke Skywalker', 'https://swapi.co/api/films/2/')
personagem02 = Character('C-3PO', 'https://swapi.co/api/films/2/')

print(personagem01)
print(personagem02)



if __name__ == "__main__":
    import doctest
    doctest.testmod()















