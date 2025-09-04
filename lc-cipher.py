# id_ru_cipher_menu.py
# Latin A–Z <-> Cyrillic Ж–Я substitution cipher
# Dengan menu interaktif, hasil selalu UPPERCASE

LATIN = "QWERTYUIOPASDFGHJKLZXCVBNM 0123456789"
CYRILLIC = "ЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ ०१२३४५६७८९"

ENC_MAP = {l: c for l, c in zip(LATIN, CYRILLIC)}

DEC_MAP = {c: l for l, c in zip(LATIN, CYRILLIC)}

def encrypt(text: str) -> str:
    text = text.upper()
    return "".join(ENC_MAP.get(ch, ch) for ch in text)

def decrypt(text: str) -> str:
    text = text.upper()
    return "".join(DEC_MAP.get(ch, ch) for ch in text)

def main():
    while True:
        print("\nLATIN - CYRILLIC")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("select menu (1/2/3): ").strip()

        if choice == "1":
            teks = input("Enter text to encrypt: ")
            hasil = encrypt(teks)
            print("Result:", hasil)
        elif choice == "2":
            teks = input("Enter text to decrypt: ")
            hasil = decrypt(teks)
            print("Result:", hasil)
        elif choice == "3":
            print("Exit...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
