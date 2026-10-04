from itertools import groupby

# Задание 1
print('Задание 1')

# Один и тот же товар может лежать на складе в Москве, в Казани или в обоих городах. Ниже id товаров на каждом складе.
moscow = {201, 202, 203, 204}
kazan = {203, 204, 205, 206}

# Нужно найти:

# - что можно забрать в любом из двух городов
print('что можно забрать в любом из двух городов:', moscow & kazan) 

# - что есть только в Москве
print('что есть только в Москве:', moscow - kazan)

# - что есть только в Казани
print('что есть только в Казани:', kazan - moscow)

# - сколько разных товаров на обоих складах вместе
print('сколько разных товаров на обоих складах вместе:', len(moscow | kazan), end="\n\n")

# Задание 2
print('Задание 2')

# Дана история поисковых запросов: каждая строка — один введённый запрос. Повтор в списке значит, что этот запрос ввели ещё раз.
queries = [
    "чехол",
    "iphone",
    "чехол",
    "наушники",
    "iphone",
    "iphone",
    "кабель",
    "чехол",
    "iphone",
]

# Нужно найти:

# - сколько всего поисковых запросов в ленте
print('сколько всего поисковых запросов в ленте:', len(queries))

# - сколько раз ввели каждый запрос
search_dict = {}

for q in queries:
    search_dict[q] = search_dict.get(q, 0) + 1

print('сколько раз ввели каждый запрос:', search_dict)

# - какой запрос вводили чаще всего
most_popular = max(search_dict, key=search_dict.get)

print('какой запрос вводили чаще всего:', most_popular)

# - какую долю всех поисков он занимает
print('какую долю всех поисков он занимает:', round(search_dict[most_popular]/len(queries), 2))

# - какие запросы встретились один раз
print('какие запросы встретились один раз:', [k for k, v in search_dict.items() if v == 1], end="\n\n")

# Задание 3
print('Задание 3')

# Есть список заказов:
# - `status` -  статус заказа
#   - `delivered` доставлен покупателю
#   - `returned` возврат
# - `amount` — сумма заказа.
orders = [
    {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
    {"id": 2, "buyer": "boris", "status": "returned", "amount": 4_500},
    {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1_500},
    {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3_200},
    {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
    {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2_100},
]


# Нужно найти:

# - на какую сумму оформили возвраты
print('на какую сумму оформили возвраты:', sum([o['amount'] for o in orders if o['status'] == 'returned']))

# - кто хотя бы раз вернул заказ
print('кто хотя бы раз вернул заказ:', set([o['buyer'] for o in orders if o['status'] == 'returned']))

# - сколько заказов доставлено покупателю
delivered = [o for o in orders if o['status'] == 'delivered']
print('сколько заказов доставлено покупателю:', len(delivered))

# - средний чек доставленных заказов
print('средний чек доставленных заказов:', sum(o['amount'] for o in delivered)/len(delivered), end="\n\n")

# Задание 4
print('Задание 4')

# Есть статистика за пять дней работы магазина. У каждого дня число заказов, выручка и число возвратов.
days = [
    {"day": "пн", "orders": 20, "revenue": 40_000, "returns": 2},
    {"day": "вт", "orders": 16, "revenue": 19_200, "returns": 4},
    {"day": "ср", "orders": 25, "revenue": 55_000, "returns": 1},
    {"day": "чт", "orders": 10, "revenue": 12_000, "returns": 3},
    {"day": "пт", "orders": 30, "revenue": 48_000, "returns": 3},
]

# Нужно найти:

# - выручку за всю неделю
revenue_list = [d['revenue'] for d in days]
print('выручка за всю неделю:', sum(revenue_list))

# - день с самой большой выручкой
print('день с самой большой выручкой:', [d['day'] for d in days if d['revenue'] == max(revenue_list)])

# - среднюю выручку на один заказ в каждый день
print('средняя выручка на один заказ в каждый день:', [f"{d['day']} - {d['revenue']/d['orders']}" for d in days])

# - дни, где возвратов больше 20% заказов
print('дни, где возвратов больше 20% заказов:', [d['day'] for d in days if d['returns']/d['orders'] > 0.2], end='\n\n')

#Задание 5

# Есть список отзывов на товары. На каждой строке — по одному. 
# Данные слегка битые, и названия товара записаны в разном регистре. `id` при этом один и тот же для одного и того же товара. 
# Перед подсчётом приведите названия к одному формату, иначе они будут считаться как разные`.

reviews = [
    {"id": 1, "product": "Чехол", "stars": 5},
    {"id": 1, "product": "Чехол", "stars": 3},
    {"id": 1, "product": "Чехол", "stars": 4},
    {"id": 2, "product": "Наушники", "stars": 2},
    {"id": 2, "product": "наушники", "stars": 2},
    {"id": 2, "product": "НАУШНИКИ", "stars": 5},
    {"id": 3, "product": "Планшет", "stars": 5},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 5, "product": "Кабель", "stars": 1},
]

for r in reviews:
    r['product'] = r['product'].lower()

reviews_sort = sorted(reviews, key=lambda r: r['product'])

# Задание 5
print('Задание 5')

# Нужно найти:

# - среднюю оценку каждого товара
reviews_group = {}
avg_stars = {}

for product, group in groupby(reviews_sort, key=lambda r: r['product']):
    reviews_list = list(group)
    reviews_group[product] = reviews_list
    stars = [r['stars'] for r in reviews_list]
    avg_stars[product] = sum(stars)/len(stars)

print('средняя оценка каждого товара:', avg_stars)


# - худший товар по средней оценке среди тех, у кого хотя бы два отзыва
print('худший товар по средней оценке среди тех, у кого хотя бы два отзыва:', min([r for r in reviews_group if len(reviews_group[r]) >= 2], key=lambda x: avg_stars[x]))

# - сколько отзывов на 1 или 2 звезды
print('количетсво отзывов на 1 или 2 звезды:', sum(1 for r in reviews_sort if r['stars'] in (1,2)))

# - какую долю всех отзывов они составляют
print('какую долю всех отзывов они составляют:', sum(1 for r in reviews_sort if r['stars'] in (1,2))/len(reviews_sort))
