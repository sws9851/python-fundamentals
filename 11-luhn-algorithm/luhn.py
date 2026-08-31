def verify_card_number(number: str) -> str:
    number = number.replace("-", "").replace(" ", "")
    digits = number[::-1]
    summation = 0

    for digit in digits[::2]:
        summation += int(digit)

    for digit in digits[1::2]:
        doubled = int(digit) * 2
        # doubling a digit maxes out at 18, so subtracting 9 collapses it to one digit
        if doubled > 9:
            doubled -= 9
        summation += doubled

    return "VALID!" if summation % 10 == 0 else "INVALID!"


if __name__ == "__main__":
    print(verify_card_number("4111-1111-1111-1111"))
    print(verify_card_number("1234 5678 9012 3456"))
    print(verify_card_number("453914889"))
