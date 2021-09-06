import random
import datetime
import rstr


def gen_age():
    return random.randint(15, 99)


def gen_cpf():
    return rstr.rstr('0123456789', 11)


def gen_fone():
    return '({0}) {1}-{2}'.format(
        rstr.rstr('1234567890', 2),
        rstr.rstr('1234567890', 4),
        rstr.rstr('1234567890', 4)
    )


def gen_timestamp():
    year = random.randint(1970, 2021)
    month = random.randint(1, 12)
    if month == 2:
        day = random.randint(1, 28)
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            day = random.randint(1, 29)
    else:
        day = random.randint(1, 30)
    hour = random.randint(1, 23)
    minute = random.randint(1, 59)
    second = random.randint(1, 59)
    microsecond = random.randint(1, 999999)
    date = datetime.datetime(year, month, day, hour,
                             minute, second, microsecond).isoformat(" ")
    return date


def gen_cities():
    list_city = [
        [u'São Paulo', 'SP'],
        [u'Belém', 'PA'],
        [u'Rio de Janeiro', 'RJ'],
        [u'Goiânia', 'GO'],
        [u'Salvador', 'BA'],
        [u'Guarulhos', 'SP'],
        [u'Brasília', 'DF'],
        [u'Campinas', 'SP'],
        [u'Fortaleza', 'CE'],
        [u'São Luís', 'MA'],
        [u'Belo Horizonte', 'MG'],
        [u'São Gonçalo', 'RJ'],
        [u'Manaus', 'AM'],
        [u'Maceió', 'AL'],
        [u'Curitiba', 'PR'],
        [u'Duque de Caxias', 'RJ'],
        [u'Recife', 'PE'],
        [u'Natal', 'RN'],
        [u'Porto Alegre', 'RS'],
        [u'Campo Grande', 'MS']]
    return random.choice(list_city)
