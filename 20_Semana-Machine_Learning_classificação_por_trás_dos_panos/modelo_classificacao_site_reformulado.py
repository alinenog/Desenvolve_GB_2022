import csv

def carregar_acessos():
    X = []
    Y = []

    arquivo = open('acesso.csv', 'rb')
    leitor = csv.reader(arquivo)

    next(leitor)

    for home,como_funciona,contato, comprou in leitor:

        dado = [int(home),int(como_funciona)
            ,int(contato)]
        X.append(dado)
        Y.append(int(comprou))

    return X, Y

# CHAMANDO ARQUIVO
# from dados import carregar_acessos
# x, y = carregar_acessos()
# print(x) 
# print(y)
