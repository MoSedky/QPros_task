import random
import string
import csv
import re


def generate_random_string():
    generated_rand_str = ''.join(random.choices(string.ascii_lowercase, k=5))
    save_generated_str(generated_rand_str)
    return generated_rand_str


def save_generated_str(rand_str):
    f = open('Resources/rand_str.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(rand_str)
    f.close()


def get_purchase_values(whole_str):

    id_val = re.search('Id:.*A', whole_str)
    amount_val = re.search('Amount:.*U', whole_str)
    card_no_val = re.search('Card Number:.*N', whole_str)
    name_val = re.search('Name:.*D', whole_str)
    date_val = re.search('Date:.*', whole_str)
    return id_val.group(0)[4:-1], amount_val.group(0)[8:-2], card_no_val.group(0)[13:-1],\
        name_val.group(0)[6:-1], date_val.group(0)[6:]


def get_current_date():
    from datetime import datetime
    return datetime.today().strftime('%d/%m/%Y')
