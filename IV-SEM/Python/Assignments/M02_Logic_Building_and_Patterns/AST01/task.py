def count_digits(n: int) -> int:
    n = abs(n)          # handle negative numbers
    return len(str(n))  # convert to string and count digits

if __name__ == "__main__":
    n = int(input())
    print(count_digits(n))