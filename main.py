TAX_FEE_PER_PAX = 35.0
INSURANCE_PER_PAX = 12.0
FULL_SERVICE_MULT = 2.2


def get_choice(prompt, low, high):
    while True:
        try:
            value = int(input(prompt))
            if low <= value <= high:
                return value
            print(f"  Invalid input. Please enter a number from {low} to {high}.")
        except ValueError:
            print(f"  Invalid input. Please enter a number from {low} to {high}.")


def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer == "y":
            return True
        if answer == "n":
            return False
        print("  Invalid input. Please enter y or n.")
