def main():
    print('Задание 4')

    days = [
        {'day': 'пн', 'orders': 20, 'revenue': 40_000, 'returns': 2},
        {'day': 'вт', 'orders': 16, 'revenue': 19_200, 'returns': 4},
        {'day': 'ср', 'orders': 25, 'revenue': 55_000, 'returns': 1},
        {'day': 'чт', 'orders': 10, 'revenue': 12_000, 'returns': 3},
        {'day': 'пт', 'orders': 30, 'revenue': 48_000, 'returns': 3},
    ]

    daily_revenues = [day['revenue'] for day in days]
    print('выручка за всю неделю:', sum(daily_revenues))
    print(
        'день с самой большой выручкой:',
        [day['day'] for day in days if day['revenue'] == max(daily_revenues)],
    )

    average_revenue_by_day = []
    for day in days:
        day_name = day['day']
        revenue_per_order = day['revenue'] / day['orders']
        average_revenue_by_day.append(f'{day_name} - {revenue_per_order}')

    print(
        'средняя выручка на один заказ в каждый день:',
        average_revenue_by_day,
    )
    print(
        'дни, где возвратов больше 20% заказов:',
        [day['day'] for day in days if day['returns'] / day['orders'] > 0.2],
    )


if __name__ == '__main__':
    main()
