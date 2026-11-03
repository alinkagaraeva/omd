import csv


DATA_FILE = 'Corp_Summary.csv'
OUTPUT_FILE = 'departments_report.csv'


def read_data(data_file: str) -> list[list[str]]:
    with open(data_file, encoding='utf-8', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        data = [row for row in reader]

    return data


def department_hierarchy(data: list[list[str]]) -> dict[str, set[str]]:
    teams_by_department = {}
    department_index = data[0].index('Департамент')
    team_index = data[0].index('Отдел')

    for employee in data[1:]:
        department = employee[department_index]
        teams_by_department.setdefault(department, set())
        teams_by_department[department].add(employee[team_index])

    return teams_by_department


def department_summary(data: list[list[str]]) -> list[dict[str, str | int]]:
    salaries_by_department = {}
    department_index = data[0].index('Департамент')
    salary_index = data[0].index('Оклад')

    departments_summary = []

    for employee in data[1:]:
        department = employee[department_index]
        salaries_by_department.setdefault(department, [])
        salaries_by_department[department].append(int(employee[salary_index]))

    for department, salaries in salaries_by_department.items():
        departments_summary.append(
            {
                'Департамент': department,
                'Количество человек': len(salaries),
                'Минимальная зарплата': min(salaries),
                'Максимальная зарплата': max(salaries),
                'Средняя зарплата': round(sum(salaries) / len(salaries)),
            }
        )

    return departments_summary


def write_department_summary(
    data: list[list[str]], output_file: str,
) -> None:
    report = department_summary(data)

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


def make_report(
    report_number: int,
    data_file: str = DATA_FILE,
    output_file: str = OUTPUT_FILE,
) -> None:
    if type(report_number) is not int:
        raise TypeError('Номер отчёта должен быть целым числом!')
    if report_number not in (1, 2, 3):
        raise ValueError('Номер отчёта должен быть от 1 до 3!')

    try:
        data = read_data(data_file)
    except FileNotFoundError as error:
        print(error)
        return

    if not data:
        print('Файл пуст.')
        return

    if len(data) == 1:
        print('В файле есть только заголовок, данных о сотрудниках нет.')
        return

    if report_number == 1:
        print(department_hierarchy(data))
    elif report_number == 2:
        print(department_summary(data))
    else:
        write_department_summary(data, output_file)
        print(f'Отчет записан в файл {output_file}')


def main() -> None:
    try:
        report_number = int(input(
            'Введите номер отчёта\n'
            '(1 - иерархия, 2 - сводка по департаментам, '
            '3 - сводка по департаментам в формате CSV): ',
        ))
    except ValueError:
        print('Номер отчёта должен быть целым числом от 1 до 3!')
        return

    try:
        make_report(report_number)
    except ValueError as error:
        print(error)


if __name__ == '__main__':
    main()
