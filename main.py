TAX_FEE_PER_PAX = 35.0
INSURANCE_PER_PAX = 12.0
FULL_SERVICE_MULT = 2.2

ROUTES = {
    1: ("Kuala Lumpur -> Kota Kinabalu (Domestic)", 120.0),
    2: ("Kuala Lumpur -> Singapore (Short-haul)", 150.0),
    3: ("Kuala Lumpur -> Bangkok (ASEAN)", 180.0),
    4: ("Kuala Lumpur -> Tokyo (Long-haul)", 650.0),
}

BAGGAGE = {
    1: ("No checked baggage (cabin only)", 0.0),
    2: ("20kg checked baggage", 60.0),
    3: ("30kg checked baggage", 90.0),
}

MEALS = {
    1: ("No meal", 0.0),
    2: ("Nasi Lemak (Santan)", 15.0),
    3: ("Chicken Rice", 18.0),
}

SEATS = {
    1: ("Standard seat (random)", 0.0),
    2: ("Preferred seat", 25.0),
    3: ("Hot seat (extra legroom)", 40.0),
}


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
