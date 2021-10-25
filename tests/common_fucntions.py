import json
import random
import string

from os.path import join, dirname


def load_json_file(path: str):
    """Loads a json file from a given relative path directory"""
    relative_path = 'services/' + path
    absolute_path = join(dirname(__file__), relative_path)
    with open(absolute_path) as schema_file:
        return json.loads(schema_file.read())


def random_string_generator(n: int = 10):
    """Generates a random string with a given length (n)"""
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=n))


def random_integer_generator(a: int = 12, b: int = 100):
    """Generates a random int between two integers (a and b)"""
    return random.randint(a, b)
