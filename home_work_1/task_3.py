def main():
    print('Задание 3')

    orders = [
        {'id': 1, 'buyer': 'anya', 'status': 'delivered', 'amount': 900},
        {'id': 2, 'buyer': 'boris', 'status': 'returned', 'amount': 4_500},
        {'id': 3, 'buyer': 'anya', 'status': 'delivered', 'amount': 1_500},
        {'id': 4, 'buyer': 'vera', 'status': 'delivered', 'amount': 3_200},
        {'id': 5, 'buyer': 'boris', 'status': 'delivered', 'amount': 700},
        {'id': 6, 'buyer': 'gleb', 'status': 'returned', 'amount': 2_100},
    ]

    print(
        'на какую сумму оформили возвраты:',
        sum(
            order['amount']
            for order in orders
            if order['status'] == 'returned'
        ),
    )
    print(
        'кто хотя бы раз вернул заказ:',
        {
            order['buyer']
            for order in orders
            if order['status'] == 'returned'
        },
    )

    delivered_orders = [
        order for order in orders if order['status'] == 'delivered'
    ]
    print('сколько заказов доставлено покупателю:', len(delivered_orders))
    print(
        'средний чек доставленных заказов:',
        sum(order['amount'] for order in delivered_orders)
        / len(delivered_orders),
    )


if __name__ == '__main__':
    main()
