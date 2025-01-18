
class FileText(object):
    def __init__(self, article: str):
        self.file = article
        self.content = self.extract_content()

    def extract_content(self):
        content = None
        with open(file = self.file, mode='r', encoding='utf8') as file:
            content = file.readlines()
        content = " ".join(content)
        return content
    
    def extract_line(self, number_of_line):
        content = None
        with open(file = self.file, mode='r', encoding='utf8') as file:
            lines = file.readlines()
        content = lines[number_of_line - 1]
        return content

# file_text = FileText(article = './music.txt')
# print(file_text.extract_line(4))


# 2. Classe para ler arquivos de csv
# Crie a classe ArquivoCSV . Ela deve extender (herdar) a classe ArquivoTexto para
# reaproveitar os seus atributos ( self.arquivo e self.conteudo ) e método
# ( self.extrair_linha ). Além disso, adicione o seguinte atributo:
# self.colunas : Atributo do tipo list onde os elementos são os nome das
# colunas;
class FileCSV(FileText):
    def extract_content(self):
        with open(self.file, "r") as file:
            rows = [line.strip().split(",") for line in file]
        return rows

    def extract_line(self, number_of_line):
        with open(self.file, "r") as file:
            current_line = 0
            for line in lines:
                if(line.strip()):
                    if(current_line == line):
                        return line.strip().split(",")
                    current_line += 1

    def extract_column_of_line(self, number_of_line, number_of_column):
        line = extract_line(number_of_line)
        line.split(",")
        return line


        

file_csv = FileText(article = './carros.csv')
print(file_csv.extract_column_of_line(1, 2))
# A classe também deve conter o seguinte método:
# self.extrair_coluna_da_linha : Método que recebe como parâmetro o
# numero da linha e o indice da coluna e retorna o valor em questão.In [ ]:
# class ArquivoCSV(ArquivoTexto):
# def __init__(self, arquivo: str):
# ...
# self.colunas = ...
# def extrair_coluna_da_linha(
# self,
# numero_linha: int,
# numero_coluna: int
# ):
# ...
# Utilize o código abaixo para testar sua classe.
# In [ ]:
# arquivo_csv = ArquivoCSV(arquivo='carros.csv')
# numero_linha = 1
# print(
# arquivo_csv.extrair_linha(
# numero_linha=numero_linha
# )
# ) # id,valor_venda,valor_manutencao,portas,pessoas,porta_malas
# print(arquivo_csv.colunas)
# # ['id', 'valor_venda', 'valor_manutencao',
# # 'portas', 'pessoas', 'porta_malas']
# numero_linha = 10
# print(
# arquivo_csv.extrair_linha(
# numero_linha=numero_linha
# )
# ) # 9,low,med,2,2,small
# numero_linha = 10
# numero_coluna = 2
# print(
# arquivo_csv.extrair_coluna_da_linha(
# numero_linha=numero_linha,
# numero_coluna=numero_coluna
# )
# ) # low