from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    dictTxt = {}
    quotes = txt_importer(path_file)
    dictTxt["nome_do_arquivo"] = path_file
    dictTxt["qtd_linhas"] = len(quotes)
    dictTxt["linhas_do_arquivo"] = quotes
    for itens in instance.queue:
        if itens["nome_do_arquivo"] == path_file:
            return None
    instance.enqueue(dictTxt)
    print(instance.queue)


def remove(instance):
    if len(instance.queue) == 0:
        return print("Não há elementos")
    archive_name = instance.queue[0]["nome_do_arquivo"]
    instance.dequeue()
    print(f"Arquivo {archive_name} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
