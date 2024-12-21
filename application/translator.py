from file_management import _internal, generate_path
import json
from debug import iceicebaby
from icecream import ic

iceicebaby()

_internal_folder = _internal()
algorithm_folder_path = 'algorithm'
if _internal_folder:
    algorithm_folder_path = generate_path(_internal_folder.as_posix(), 'algorithm').as_posix()

def encrypt(message: str) -> str:
    path = generate_path(algorithm_folder_path, 'encrypt.json').as_posix()
    ic(path)
    with open(path, 'r') as f:
        char_data: dict = json.loads(f.read())

    output_list: list = []
    separator: str = ' '
    for char in message.lower():
        output_list.append(char_data[char])
    output: str = separator.join(output_list)
    return output

def decrypt(morse_code: str) -> str:
    path = generate_path(algorithm_folder_path, 'decrypt.json').as_posix()
    ic(path)
    with open(path, 'r') as f:
        char_data: dict = json.loads(f.read())

    output_list: list = []
    separator: str = ''
    for char in morse_code.split(' '):
        output_list.append(char_data[char])
    output: str = separator.join(output_list).upper()
    return output

if __name__ == "__main__":
    ic(_internal_folder, algorithm_folder_path)
    message: str = 'I am in love with your wife!'
    a = encrypt(message)
    morse_code: str = '.. / .- -- / .. -. / .-.. --- ...- . / .-- .. - .... / -.-- --- ..- .-. / .-- .. ..-. . -.-.--'
    b = decrypt(morse_code)

    print(f'\nMessage: {message}')
    print(f'Encrypted: {a}')
    print(f'Decrypted: {b}')