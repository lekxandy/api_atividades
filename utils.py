from models import Pessoas


def altera_pessoa(nome, novo_nome):
    pessoa = Pessoas.query.filter_by(nome=nome).first()
    pessoa.nome = novo_nome
    pessoa.save()

    print(pessoa)


def consulta_pessoas(nome=None):
    pessoas = Pessoas.query.all()
    for p in pessoas:
        print("ID: {}, Nome: {}, Idade: {}".format(p.id, p.nome, p.idade))


def insere_pessoas(nome, idade):
    pessoa = Pessoas(nome=nome, idade=idade)
    pessoa.save()
    print(pessoa)


def exclui_pessoa(id):
    pessoa = Pessoas.query.filter_by(id=id).first()
    pessoa.delete()


if __name__ == '__main__':
    # altera_pessoa("Alexander Roberto dos Santos", "Gabriel")
    # insere_pessoas("Daniel de Oliveira dos Santos", 7)
    # consulta_pessoas()
    # exclui_pessoa(2)
    consulta_pessoas()
