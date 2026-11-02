def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

def main():
    n = 10
    print(fibonacci(n))

if __name__ == "__main__":
    main()
