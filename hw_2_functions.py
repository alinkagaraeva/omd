import csv

def read_data(name_data: str) -> list[list[str]]:
    with open(name_data, encoding='utf-8', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        data = [row for row in reader]

    return data


def first_report(data: list[list[str]]) -> dict[str, set[str]]:
    depart_dict = {}
    department_index = data[0].index('Департамент')
    part_index = data[0].index('Отдел')

    for i in range(1, len(data)):
        depart_dict.setdefault(data[i][department_index], set())
        depart_dict[data[i][department_index]].add(data[i][part_index])

    return depart_dict


def second_report(data: list[list[str]]) -> list[dict[str, str | int]]:
    depart_dict = {}
    department_index = data[0].index('Департамент')
    salary_index = data[0].index('Оклад')

    departments_inf = []

    for i in range(1, len(data)):
        depart_dict.setdefault(data[i][department_index], [])
        depart_dict[data[i][department_index]].append(int(data[i][salary_index]))

    for d in depart_dict:
        departments_inf.append(
            {
                'Департамент': d,
                'Количество человек': len(depart_dict[d]),
                'Минимальная зарплата': min(depart_dict[d]),
                'Максимальная зарплата': max(depart_dict[d]),
                'Средняя зарплата': round(sum(depart_dict[d]) / len(depart_dict[d]))
            }
        )

    return departments_inf


def third_report(data: list[list[str]], output_file) -> None:
    report = second_report(data)

    if not report:
        return 
    
    with open(output_file, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(
            file,
            fieldnames=report[0].keys(),
            delimiter=';',
        )
        writer.writeheader()
        writer.writerows(report)


def making_report(
        var: int, 
        name_data: str = 'Corp_Summary.csv', 
        output_file: str = 'departments_report.csv' 
        ) -> None:
    if type(var) is not int:
        raise TypeError('Номер отчёта должен быть целым числом!')
    if var not in (1, 2, 3):
        raise ValueError('Номер отчёта должен быть от 1 до 3!')

    try:
        data = read_data(name_data)
    except FileNotFoundError as error:
        print(error)
        return 
    
    if not data:
        print('Файл пуст.')
        return

    if len(data) == 1:
        print('В файле есть только заголовок, данных о сотрудниках нет.')
        return

    if var == 1:
        print(first_report(data))
    elif var == 2:
        print(second_report(data))
    else:
        third_report(data, output_file)
        print(f'Отчет записан в файл {output_file}')

if __name__ == '__main__':
    report_number = int(input(
            'Введите номер отчёта\n(1 - иерархия, 2 - сводка по департаментам, '
            '3 - сводка по департаментам в формате CSV): '))
    making_report(report_number)
