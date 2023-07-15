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
            actual_dict["arquivo"] = itens["nome_do_arquivo"]
            actual_dict["ocorrencias"] = format_lines(actual_lines)
            itens_in_instance.append(actual_dict)
    return itens_in_instance


def search_by_word(word, instance):
    itens_in_instance = []
    for itens in instance.queue:
        actual_lines = []
        for quote in itens["linhas_do_arquivo"]:
            if word.lower() in quote.lower():
                line = search_quote_line(quote, itens)
                actual_lines.append({"linha": line, "conteudo": quote})
        if len(actual_lines) > 0:
            actual_dict = {}
            actual_dict["palavra"] = word
            actual_dict["arquivo"] = itens["nome_do_arquivo"]
            actual_dict["ocorrencias"] = format_lines_with_word(actual_lines)
            itens_in_instance.append(actual_dict)
    return itens_in_instance


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


def format_lines_with_word(lines):
    list_lines = []
    for line in lines:
        dict_lines = {}
        dict_lines["linha"] = line["linha"]
        dict_lines["conteudo"] = line["conteudo"]
        list_lines.append(dict_lines)
    return list_lines
