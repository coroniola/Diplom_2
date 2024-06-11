import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def create_user_login():
    user_login = {
        "email": f'{generate_random_string(6)}@wewewe.we',
        "password": generate_random_string(6),
    }
    return user_login

def create_user(payload):
    return requests.post(base_url + Endpoints.create_user, data=payload)
def create_user_data():
    user_login_pass_email = {
        "email": f'{generate_random_string(5)}@wewewe.we',
        "password": generate_random_string(5),
        "name": generate_random_string(5)
    }
    return user_login_pass_email