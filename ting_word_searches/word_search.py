from ting_file_management.queue import Queue


def exists_word(word, instance):
    itens_in_instance = []
    for itens in instance.queue:
        actual_lines = []
        for quote in itens["linhas_do_arquivo"]:
            if word.lower() in quote.lower():
                line = search_quote_line(quote, itens)
                actual_lines.append(line)
        if len(actual_lines) > 0:
            actual_dict = {}
            actual_dict["palavra"] = word
            actual_dict["nome_do_arquivo"] = itens["nome_do_arquivo"]
            actual_dict["ocorrencias"] = format_lines(actual_lines)
            itens_in_instance.append(actual_dict)
    return itens_in_instance


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


def search_quote_line(quote, actualItem):
    for line in actualItem["linhas_do_arquivo"]:
        if quote == line:
            return actualItem["linhas_do_arquivo"].index(line) + 1


def format_lines(lines):
    list_lines = []
    for line in lines:
        dict_lines = {}
        dict_lines["linha"] = line
        list_lines.append(dict_lines)
    return list_lines


q1 = Queue()
q1.enqueue(
    {
        "nome_do_arquivo": "arquivo1.txt",
        "qtd_linhas": 5,
        "linhas_do_arquivo": [
            "Acima de tudo,",
            "é fundamental ressaltar que a adoção de políticas nos obriga",
            "à análise do levantamento das variáveis envolvidas.",
        ],
    }
)

q1.enqueue(
    {
        "nome_do_arquivo": "arquivo2.txt",
        "qtd_linhas": 2,
        "linhas_do_arquivo": [
            "análise",
            "de",
        ],
    }
)
print(exists_word("de", q1))
