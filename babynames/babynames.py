import sys
import re


def extract_names(filename):


  names = [] #lista que vai receber os nomes e ranking

  f = open(filename, 'r') # f abre o texto completo
  text = f.read() # text lê o texto completo

  #varedura dentro de texto para buscar o ano 
  year_match = re.search(r'Popularity\sin\s(\d{4})', text) #year_match recebe o texto onde esta o ano.
  year = year_match.group(1) # .group(1) pega o que esta dentro do () na busca anterior, ou seja, o ano
  names.append(year) #coloco o ano dentro da lista names


  tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text) # aqui vou salvar tudo que combina 
  # com a expressao, que indica onde estão os nomes e rankign 
  # aqui tenho listas com (ranking, nome masculino, nome feminino)
  # print(tuples) - para testar

  names_to_rank =  {} # cria dicionario que vai separar nomes e ranking
  for rank_tuple in tuples:
    (rank, boyname, girlname) = rank_tuple  # cria tuplas em ordem de classificacao. 
    # separa do dicionario o ranking, nome masculino e nome feminino
    # aqui tenho separado nas strings cada informacao
    # preciso colocar num lista cada nome masculino com seu ranking e cada nome feminino com seu rankign
    # print(rank_tuple) - para testar

    if boyname not in names_to_rank: # antes de incluir, testar se já nao tem o nome da lista
      names_to_rank[boyname] = rank # se nao tem, salva na chave boyname recebe o ranking. 

    if girlname not in names_to_rank:
      names_to_rank[girlname] = rank

  # print(names_to_rank) - para testar


    # ate aqui temos um dicionario names_to_rank com as chaves que sao os nomes, e o valor é o ranking de cada nome

  sorted_names = sorted(names_to_rank.keys()) # aqui coloco os nomes em ordem alfabetica da chave

  # Build up result list, one element per line
  for name in sorted_names:
    names.append(name + " " + names_to_rank[name]) # aqui faco uma lista com os nomes em ordem alfabetica, seguida do ranking
 

  return names



def main():

  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]


  for filename in args:
    names = extract_names(filename)

    text = '\n'.join(names) # text vai receber o names que criei na funcao, o join() junta itens na tupla e cria uma string
    # , o \n quebra 
    # linha entre eles
    print(text) # imprime a string resultante
  


if __name__ == '__main__':
  main()