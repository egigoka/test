#! python3

# Введение словаря
d = {
        'plan_code': 'b',
        'quantity': '1',
        'account': {
            'account_code': 'b',
            'username': 'jdoe',
            'email': 'jdoe@domain.com',
            'first_name': 'b',
            'last_name': 'b',
            'company_name': 'Company, LLC.',
            'billing_info': {
                'first_name': 'b',
                'last_name': 'b',
                'address1': '123 Test St',
                'city': 'San Francisco',
                'state': 'CA',
                'country': 'US',
                'zip': '94105',
                'credit_card': {
                    'number': '1',
                    'year': '2018',
                    'month': '12',
                    'verification_value': '123',
                },
            },
        },
    }

# Самый простой метод - внешняя либа, но она ничего не даст сделать с данными, так что не подходит для конечной задачи

#from pprint import *
#pprint(d)

# Пьюр примкр из Стак Оверфлоу (баг - принт в 3м питоне надо в скобки, так как он это считает за сложение?)

#def printReversely(d,depth=0):
#    for k,v in sorted(d.items(),key=lambda x: x[0]):
#        if isinstance(v, dict):
#            print ("  ")*depth + ("%s" % k)
#            printReversely(v,depth+1)
#        else:
#            print ("  ")*depth + "%s %s" % (k, v)
#printReversely(d, depth=0) # вызов функции

# Переработка примера
def walk_dict(d,depth=0):
    for key, value in sorted(d.items(), key=lambda x: x[0]):
        if isinstance(value, dict):
            print (("    ")*depth + (key)) # Напечатать только ключ, так как значение это большой (не факт) словарь (факт)
            walk_dict(value,depth+1)
        else:
            print (("    ")*depth + "%s %s" % (key, value)) # Напечатать и ключ, и словарь, так как это просто значение
walk_dict(d, depth=0) # вызов функции