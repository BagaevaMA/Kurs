
geo_logs = [
    {'visit1': ['Москва', 'Россия'], 'visit11': ['Морокоо', 'sxcsdf']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

def get_country(some_dict):
    russia = 'Россия'
    itemsToDelete = []
    for item in some_dict:
        keysToDelete = []
        for k, v in item.items():
            if (v.count(russia) == 0):
                keysToDelete.append(k)
        for k in keysToDelete:
            del(item[k])
        if (len(item) == 0):
            itemsToDelete.append(item)
    for item in itemsToDelete:
        some_dict.remove(item)
    return(some_dict)

get_country(geo_logs)


ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

def get_unic_number(some_dict):
    number = list(some_dict.values())
    new_list_number = [item for sublist in number for item in sublist]
    number_set = set(new_list_number)
    return (number_set)

get_unic_number(ids)

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]
def get_count_queries(some_list):
    countedQueries = {}
    queryCount = len(some_list)
    for query in some_list:
        wordsCount = query.count(' ') + 1
        countedQueries[wordsCount] = countedQueries.setdefault(wordsCount, 0)+100/ queryCount
    return(countedQueries)
