def read_number(prompt: str) -> float:
    while True:
        raw = input(prompt)
        try:
            return float(raw)
        except ValueError:
            print("Invalid number. Please enter a valid numeric value.")


def read_operator(prompt: str) -> str:
    valid_ops = {"+", "-", "*", "/"}
    while True:
        op = input(prompt).strip()
        if op in valid_ops:
            return op
        print("Invalid operator. Please enter one of: +, -, *, /")


def calculate(a: float, op: str, b: float) -> float:
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return a / b
    raise ValueError(f"Unsupported operator: {op}")


def main() -> None:
    print("Basic Calculator")
    print("-----------------")

    first = read_number("Enter the first number: ")
    operator = read_operator("Enter the operator (+, -, *, /): ")
    second = read_number("Enter the second number: ")

    try:
        result = calculate(first, operator, second)
        print(f"Result: {first} {operator} {second} = {result}")
    except ZeroDivisionError as zde:
        print(f"Error: {zde}")
    except Exception as exc:
        print(f"An unexpected error occurred: {exc}")


if __name__ == "__main__":
    main()


