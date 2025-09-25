import string
import random
import argparse
import json
import os
path = os.path.expanduser("~/.pass.json")
passwd = []


def passgen(length: int, use_digits: bool, use_symbols: bool):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    parser = argparse.ArgumentParser(description="CLI PassGen")
    parser.add_argument("--length",type=int, default=12, help="Length of password")
    parser.add_argument("--symbols", action="store_false", help="Use symbols in password")
    parser.add_argument("--digits", action="store_false", help="Use digits in password")
    parser.add_argument("--serv", type=str, help="Name of service")
    parser.add_argument("--json", action="store_true", help="Save in json your password")

    args = parser.parse_args()

    password= passgen(
        length= args.length,
        use_digits= args.digits,
        use_symbols= args.symbols
    )
    if args.json:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                try:
                    passwd = json.load(f)
                except json.JSONDecodeError:
                    passwd = []
        else:
            passwd = []

        # Добавляем новый пароль
        passwd.append({
            "servs": args.serv,
            "pass": password
        })

        # Записываем обратно
        with open(path, "w", encoding="utf-8") as f:
            json.dump(passwd, f, indent=4)

    else:
        print(password)

if __name__ == "__main__":
    main()


