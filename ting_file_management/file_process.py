import sys

from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    news = txt_importer(path_file)

    if path_file in [i['nome_do_arquivo'] for i in instance.get_all()]:
        return None

    item = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(news),
        "linhas_do_arquivo": news
    }

    instance.enqueue(item)

    print(item)


def remove(instance):
    if instance.is_empty():
        print('Não há elementos')
        return None

    nome_do_arquivo = instance.search(0)["nome_do_arquivo"]
    print(f'Arquivo {nome_do_arquivo} removido com sucesso')

    instance.clear()


def file_metadata(instance, position):
    try:
        print(instance.search(position))
    except IndexError:
        print("Posição inválida", file=sys.stderr)
