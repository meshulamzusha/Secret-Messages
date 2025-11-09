from functions import *

if __name__ == '__main__':
    msg = get_message()
    encrypted_msg = atbash_encryption(msg)
    save_to_file('encrypted messages.txt', encrypted_msg)
    msg_to_print = read_from_file('encrypted messages.txt')
    decrypted_msg = atbash_encryption(msg_to_print)
    print(decrypted_msg)