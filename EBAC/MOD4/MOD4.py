def extractLine(file):
    try:
        with open(file, mode="r", encoding="utf8") as file: 
            content = file.readline().strip()
            print(content)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file}' não foi encontrado.")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")
extractLine("./music.text")

import csv
def extrai_coluna_csv(file_name: str,indice_column: int,data_type: str ):
    column = []
    with open(file_name, mode="r", encoding="utf8") as file: 
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            if len(row) > indice_column:
                value = row[indice_column]
                if(data_type == "int"):
                    value = int(value)
                elif(data_type == "float"):
                    value = float(value)
                elif(data_type == "str"):
                    value = str(value)
                else:
                    raise ValueError(f"Tipo de dado '{tipo_dado}' não suportado.")

                column.append(value)
        return column

coluna_idade = extrai_coluna_csv("file.csv", indice_column=3, data_type="int")
print(coluna_idade)
