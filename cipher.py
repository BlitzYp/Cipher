alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(word: str, shift_num: int) -> str:
    return "".join([alpha[(alpha.index(i) + shift_num) % 26] if i in alpha else i for i in word])

def decode(encoded_word: str, shift_num: int) -> str:
    return "".join([alpha[(alpha.index(i) - shift_num) % 26] if i in alpha else i for i in encoded_word])

if __name__ == "__main__":
    word = input("Enter word: ").lower()
    shift_num = int(input("Enter by how much do you want to shift the word: ")) % 26
    while True:
        try:
            option = input("Enter option(encode/decode): ").lower()
            opts = {"encode": encode(word, shift_num), "decode": decode(encode(word, shift_num), shift_num)}
            if option == "new": 
                word = input("Enter word: ")
                continue
            print(opts[option])
        except IndexError:
            print("Index Error!")
            break