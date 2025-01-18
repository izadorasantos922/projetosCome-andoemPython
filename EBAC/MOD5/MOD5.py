from functools import reduce
loans = []
with open(file='./credito.csv', mode='r', encoding='utf8') as file:
    file.readline()
    line = file.readline()
    while line:
        line_loans = {}
        line_elements = line.strip().split(sep=",")
        line_loans['id_vendedor'] = line_elements[0]
        line_loans['valor_emprestimos'] = line_elements[1]
        line_loans['quantidade_emprestimos'] = line_elements[2]
        line_loans['data'] = line_elements[3]
        loans.append(line_loans)
        line = file.readline()
print(loans)


loans_values = map(lambda loan: float(loan['valor_emprestimos']), loans)

loans_values = list(loans_values)
loans_filtered = filter(lambda loan: loan > 0, loans_values)
loans_filtered = list(loans_filtered)
sum_of_loans = reduce(lambda value, currentvalue: value + currentvalue, loans_filtered)
print(round(sum_of_loans, 2))
