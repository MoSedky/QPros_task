import random
import string
import csv


def generate_random_string():
    generated_rand_str = ''.join(random.choices(string.ascii_lowercase, k=5))
    save_generated_str(generated_rand_str)
    return generated_rand_str


def save_generated_str(rand_str):
    f = open('Resources/rand_str.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(rand_str)
    f.close()
