def hanoi_solver(number: int) -> str:
    first = list(range(number, 0, -1))
    second = []
    third = []
    steps = [f"{first} {second} {third}"]

    def move(n: int, source: list, target: list, middle: list) -> None:
        if n == 0:
            return
        move(n - 1, source, middle, target)
        target.append(source.pop())
        # roles rotate through the recursion but the rods print in fixed order
        steps.append(f"{first} {second} {third}")
        move(n - 1, middle, target, source)

    move(number, first, third, second)
    return "\n".join(steps)


if __name__ == "__main__":
    print(hanoi_solver(3))
