# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.

from collections import defaultdict

company_count = 3
i = 0
companies = []
result = 0
while i < company_count:
    # result_company = {}
    #profit = []
    company_name = input("Name company ")
    a_quarter =  int(input("1 quarter "))
    b_quarter = int(input("2 quarter "))
    c_quarter = int(input("3 quarter "))
    d_quarter = int(input("4 quarter "))
    profit = (a_quarter + b_quarter + c_quarter + d_quarter)/4
    result_company = (company_name, profit)
    companies.append(result_company)
    i += 1

print(companies) # средняя прибыль (за год для всех предприятий)

for name, score in companies:
    result = score + result

middle_ = result/company_count
print(middle_)

c_1 = defaultdict(list)
c_2 = defaultdict(list)

for name, score in companies:
    if score > middle_:
        c_1[name].append(score)
    else:
        c_2[name].append(score)

# отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

print(f'Выше среднего: {c_1}')
print(f'Ниже среднего: {c_2}')

# В эпилог. Я понимаю, что defaultdict притянут за уши, но др применения коллекциям я не нашел
