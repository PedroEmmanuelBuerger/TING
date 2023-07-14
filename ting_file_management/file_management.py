import sys


def txt_importer(path_file):
    if path_file.endswith(".txt"):
        try:
            with open(path_file, "r") as file:
                allLinesList = []
                allLines = file.readlines()
                for line in allLines:
                    line = line.replace("\n", "")
                    allLinesList.append(line)
                return allLinesList
        except FileNotFoundError:
            print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    else:
        return print("Formato inválido", file=sys.stderr)
