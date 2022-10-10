def Permutations(text):
    vowels = ['a', 'e', 'i ', 'o', 'u']

    for i in range(len(text)):
        print(i)
        if text[i] in vowels:
            print(i)

    return print(text)

if __name__ == "__main__":
    Permutations("codingame")