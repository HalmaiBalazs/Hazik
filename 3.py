def has_matching_parity(numbers: list[int]) -> bool:
    matching = True
    for i in range(len(numbers)):
        if numbers[i] % 2 != i % 2:
            matching = False
    return matching


def main():
    n = int(input())
    for i in range(n):
        str = input()
        tokens = str.split()
        numbers = []
        for t in tokens:
            numbers.append(int(t))
        if has_matching_parity(numbers):
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    main()
