import sys


def word_count_dict(filename):
    wordcount = {}  # dicionario que vai contar as palavras
    f = open(filename, 'r') # abre o filename no arquivo f
    words = f.read().split() # le e separa numa lista de strings
    for word in words:
        word = word.lower()  # coloca tudo em minusculo
        if not word in wordcount: # loop para contar quantas vezes cada palavra aparece
            wordcount[word] = 1 # se nao tinha, salva no dicionario wordcount o numero 1
        else:
            wordcount[word] = wordcount[word] + 1 # se ja tinha, soma essa nova ocorrencia
    return wordcount


def print_top(filename): # mostra as 20 primeiras palavras mais usadas
    wordcount = word_count_dict(filename) # recebe o retorno da funcao
    items = sorted(wordcount.items(), key=get_count, reverse=True) # coloca os itens em ordens, pela chave definina na funcao get_count,
    # do maior para o menor
    for item in items[:20]:
        print('# ', item[0],' - ', item[1]) # mostra a palavra, seguida da quantidade de vezes que aconteceu


def get_count(wordcount):
    return wordcount[1] # define a chave que vai ser usada como referencia para ordenar na funcao anterior


def print_words(filename): # mostra todas as palavras em ordem alfabetica e mostra quantas vezes cada um foi usada
  wordcount = word_count_dict(filename) # recebe o retorno na funcao
  wordcount_sort = sorted(wordcount) # ordem alfabetica
  for word in wordcount_sort: # para cada palavra em worldcount...
    print('* ', word, 'appears ', wordcount[word], ' times in text') # imprimir quantas vezes cada uma aparece

def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()