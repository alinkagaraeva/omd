from itertools import groupby


def main():
    reviews = [
        {'id': 1, 'product': 'Чехол', 'stars': 5},
        {'id': 1, 'product': 'Чехол', 'stars': 3},
        {'id': 1, 'product': 'Чехол', 'stars': 4},
        {'id': 2, 'product': 'Наушники', 'stars': 2},
        {'id': 2, 'product': 'наушники', 'stars': 2},
        {'id': 2, 'product': 'НАУШНИКИ', 'stars': 5},
        {'id': 3, 'product': 'Планшет', 'stars': 5},
        {'id': 4, 'product': 'Колонка', 'stars': 4},
        {'id': 4, 'product': 'Колонка', 'stars': 4},
        {'id': 5, 'product': 'Кабель', 'stars': 1},
    ]

    for review in reviews:
        review['product'] = review['product'].lower()

    sorted_reviews = sorted(reviews, key=lambda review: review['product'])

    print('Задание 5')

    reviews_by_product = {}
    average_stars_by_product = {}
    for product, product_reviews in groupby(
        sorted_reviews, key=lambda review: review['product'],
    ):
        product_reviews_list = list(product_reviews)
        reviews_by_product[product] = product_reviews_list
        stars = [review['stars'] for review in product_reviews_list]
        average_stars_by_product[product] = sum(stars) / len(stars)

    print('средняя оценка каждого товара:', average_stars_by_product)
    print(
        'худший товар по средней оценке среди тех, у кого хотя бы два отзыва:',
        min(
            [
                product for product in reviews_by_product
                if len(reviews_by_product[product]) >= 2
            ],
            key=lambda product: average_stars_by_product[product],
        ),
    )
    print(
        'количество отзывов на 1 или 2 звезды:',
        sum(1 for review in sorted_reviews if review['stars'] in (1, 2)),
    )
    print(
        'какую долю всех отзывов они составляют:',
        sum(1 for review in sorted_reviews if review['stars'] in (1, 2))
        / len(sorted_reviews),
    )


if __name__ == '__main__':
    main()
