def main():
    print('Задание 2')

    queries = [
        'чехол',
        'iphone',
        'чехол',
        'наушники',
        'iphone',
        'iphone',
        'кабель',
        'чехол',
        'iphone',
    ]

    print('сколько всего поисковых запросов в ленте:', len(queries))

    query_counts = {}
    for query in queries:
        query_counts[query] = query_counts.get(query, 0) + 1

    print('сколько раз ввели каждый запрос:', query_counts)

    most_popular_query = max(query_counts, key=query_counts.get)
    print('какой запрос вводили чаще всего:', most_popular_query)
    print(
        'какую долю всех поисков он занимает:',
        round(query_counts[most_popular_query] / len(queries), 2),
    )
    print(
        'какие запросы встретились один раз:',
        [query for query, count in query_counts.items() if count == 1],
    )


if __name__ == '__main__':
    main()
