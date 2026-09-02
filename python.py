def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def calculator(language="en"):
    if language.lower() == "it":
        welcome = "Calcolatrice semplice"
        ops = "Operazioni supportate: +, -, *, /"
        quit_msg = "Digita 'q' per uscire"
        prompt = "Inserisci il calcolo: "
        goodbye = "Arrivederci!"
        invalid_format = "Usa questo formato: numero operatore numero"
        unsupported = "Operatore non supportato. Usa +, -, *, o /."
        invalid_input = "Input non valido: {}"
        error = "Errore: {}"
        result = "Risultato: {}"
    else:
        welcome = "Simple Calculator"
        ops = "Supported operations: +, -, *, /"
        quit_msg = "Type 'q' to quit"
        prompt = "Enter calculation: "
        goodbye = "Goodbye!"
        invalid_format = "Use this format: number operator number"
        unsupported = "Unsupported operator. Use +, -, *, or /."
        invalid_input = "Invalid input: {}"
        error = "Error: {}"
        result = "Result: {}"

    print(welcome)
    print(ops)
    print(f"{quit_msg}\n")

    while True:
        try:
            expression = input(prompt).strip()

            if expression.lower() in {"q", "quit", "exit"}:
                print(goodbye)
                break

            parts = expression.split()
            if len(parts) != 3:
                raise ValueError(invalid_format)

            left, operator, right = parts
            a = float(left)
            b = float(right)

            if operator == "+":
                calc_result = add(a, b)
            elif operator == "-":
                calc_result = subtract(a, b)
            elif operator == "*":
                calc_result = multiply(a, b)
            elif operator == "/":
                calc_result = divide(a, b)
            else:
                raise ValueError(unsupported)

            print(result.format(calc_result) + "\n")

        except ValueError as exc:
            print(invalid_input.format(exc) + "\n")
        except ZeroDivisionError as exc:
            print(error.format(exc) + "\n")


if __name__ == "__main__":
    language = input("Select language / Seleziona lingua (en/it): ").strip().lower()
    calculator(language if language in {"en", "it"} else "en")
