import os
import random
import string
import time
from django.utils.text import slugify


def random_string_generator(size=5, chars=''):
    '''
    Generates random string. 
    Takes parameters(size=default:5)
    Takes parameters(chars=default:''-> string.ascii_letters)
    '''
    if chars == 'uppercase':
        chars = string.ascii_uppercase
    elif chars == 'lowercase':
        chars = string.ascii_lowercase
    else:
        chars = string.ascii_letters
    return ''.join(random.choice(chars) for _ in range(size))


def random_number_generator(size=5, chars=string.digits):
    '''
    Generates random numbers. 
    Takes parameters(size=default:5)
    Takes parameters(chars=default:0123456789)
    '''
    return ''.join(random.choice(chars) for _ in range(size))


def generate_time_str_num():
    '''
    Generates time string day-month-year-time 
    Takes parameters(size=default:5)
    Takes parameters(chars=default:0123456789)
    '''
    timestamp_day = time.strftime('%d')
    timestamp_month = time.strftime('%m')
    timestamp_year = time.strftime('%Y')
    timestamp_time = time.strftime('%H%M%S')
    return ''.join(timestamp_day + timestamp_month + timestamp_year + '-' + timestamp_time)
