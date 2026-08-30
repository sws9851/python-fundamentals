def square_root_bisection(number, tolerance=1e-7, max_iterations=100):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    elif number in [0, 1]:
        print(f"The square root of {number} is {number}")
        return number

    # for numbers below 1 the root is larger than the number, so [0, number] would miss it
    if number < 1:
        low = number
        high = 1.0
    else:
        low = 0.0
        high = number

    for _ in range(max_iterations):
        middle = (low + high) / 2
        middle_squared = middle**2

        if (high - low) <= tolerance:
            print(f"The square root of {number} is approximately {middle}")
            return middle

        if middle_squared < number:
            low = middle
        else:
            high = middle

    print(f"Failed to converge within {max_iterations} iterations")
    return None


if __name__ == "__main__":
    square_root_bisection(16)
    square_root_bisection(0.001)
    square_root_bisection(1000000)
