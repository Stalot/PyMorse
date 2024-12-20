import json

numbers: str = '0$1$2$3$4$5$6$7$8$9'
letters: str = 'a$b$c$d$e$f$g$h$i$j$k$l$m$n$o$p$q$r$s$t$u$v$w$x$y$z$ $!$?$.$@$($)$,$/'

normal = f'{letters}${numbers}'.split('$')
morse_letters: str = '.-$-...$-.-.$-..$.$..-.$--.$....$..$.---$-.-$.-..$--$-.$---$.--.$--.-$.-.$...$-$..-$...-$.--$-..-$-.--$--..$/$-.-.--$..--..$.-.-.-$.--.-.$-.--.$-.--.-$--..--$-..-.'
morse_numbers: str = '-----$.----$..---$...--$....-$.....$-....$--...$---..$----.'
morse_digits: list = f'{morse_letters}${morse_numbers}'.split('$')

def encrypt_data(normal: list, morse_digits: list):
    morse_dict: dict = {}

    for i in range(len(normal)):
        morse_dict.update({normal[i]: morse_digits[i]})

    with open('Data/encrypt.json', 'w') as f:
        json_data = json.dumps(morse_dict)
        f.write(json_data)

    print(morse_dict)

def decrypt_data(normal: list, morse_digits: list):
    letters_dict: dict = {}

    for i in range(len(normal)):
        letters_dict.update({morse_digits[i]: normal[i]})

    with open('Data/decrypt.json', 'w') as f:
        json_data = json.dumps(letters_dict)
        f.write(json_data)

    print(letters_dict)

encrypt_data(normal, morse_digits)
decrypt_data(normal, morse_digits)