import sys


def decrement_even_digits(original:str)->str:
    result = ""
    for i in range(len(original)):
        if original[i].isdigit() and int(original[i]) % 2 == 0:
            if int(original[i]) == 0:
                result += "9"
            else:
                result += str(int(original[i]) - 1)
        else:
            result += original[i]
    return result


def main():
    lista=sys.stdin.readlines()
    for szoveg in lista:
        print(decrement_even_digits(szoveg.strip('\n')))


if __name__ == '__main__':
    main()