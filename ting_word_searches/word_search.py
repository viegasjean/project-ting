def exists_word(word, instance):
    lista = instance.search(0)['linhas_do_arquivo']
    arquivo = instance.search(0)['nome_do_arquivo']

    ocorrencias = [
        {'linha': i + 1}
        for i, text
        in enumerate(lista)
        if word.lower()
        in text.lower()]
    if ocorrencias:
        return [{
            'arquivo': arquivo,
            'palavra': word,
            'ocorrencias': ocorrencias
        }]
    return []


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
