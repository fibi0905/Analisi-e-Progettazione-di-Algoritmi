def fibonacci(n):
    if n < 0:
        return []
    a, b = 0, 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

def main():
    n = 12
    seq = fibonacci(n)
    print("Fibonacci sequence:", seq)

if __name__ == "__main__":
    main()
