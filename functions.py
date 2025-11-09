
def get_message() -> str:
    message = input("Enter the message you want to send.")
    return message


def atbash_encryption(msg: str) -> str:
    encrypted = ''
    for char in msg:
        if char.isalpha():
            encrypted += single_char_atbash_encryption(char)
        else:
            encrypted += char

    return encrypted

def single_char_atbash_encryption(char: str) -> str:
    if char.isupper():
        return chr(65 + (90 - ord(char)))
    else:
        return chr(97 + (122 - ord(char)))


def save_to_file(filename: str, encrypted_msg: str) -> None:
    with open(filename, "a") as f:
        f.writelines(f'\n{encrypted_msg}')


def read_from_file(filename: str) -> str:
    with open(filename) as f:
        for line in f:
            pass
        return line
