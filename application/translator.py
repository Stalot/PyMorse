import json

def encrypt(message: str) -> str:
    with open('encrypt.json', 'r') as f:
        char_data: dict = json.loads(f.read())

    output_list: list = []
    separator: str = ' '
    for char in message.lower():
        output_list.append(char_data[char])
    output: str = separator.join(output_list)
    return output

def decrypt(morse_code: str) -> str:
    with open('decrypt.json', 'r') as f:
        char_data: dict = json.loads(f.read())

    output_list: list = []
    separator: str = ''
    for char in morse_code.split(' '):
        output_list.append(char_data[char])
    output: str = separator.join(output_list).upper()
    return output

if __name__ == "__main__":
    message: str = 'I AM IN LOVE WITH YOUR WIFE!'
    a = encrypt(message)
    print(f'Encrypt: {a}')

    message: str = '.. / .- -- / .. -. / .-.. --- ...- . / .-- .. - .... / -.-- --- ..- .-. / .-- .. ..-. . -.-.--'
    b = decrypt(message)
    print(f'Decrypt: {b}')