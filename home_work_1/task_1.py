def main():
    print('Задание 1')

    moscow_products = {201, 202, 203, 204}
    kazan_products = {203, 204, 205, 206}

    print(
        'что можно забрать в любом из двух городов:',
        moscow_products & kazan_products,
    )
    print('что есть только в Москве:', moscow_products - kazan_products)
    print('что есть только в Казани:', kazan_products - moscow_products)
    print(
        'сколько разных товаров на обоих складах вместе:',
        len(moscow_products | kazan_products),
    )


if __name__ == '__main__':
    main()
