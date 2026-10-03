#LDCW6123 - FUNDAMENTALS OF DIGITAL COMPETENCE FOR PROGRAMMER PART B

# Memebers Name                        ID
# Karthigeayah Maniam                 1211101399
# Zainul Ihsan Bin Achuwan            253UC255D5

# AirAsia low-cost fare calculator
# Sample prices in RM for demo only - not real AirAsia fares

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
    # keep asking until we get a whole number in range
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


def run_calculator():
    print("\n--- Step 1: Choose your route ---")
    print(" 1. KL -> Kota Kinabalu (Domestic)   RM120")
    print(" 2. KL -> Singapore (Short-haul)     RM150")
    print(" 3. KL -> Bangkok (ASEAN)            RM180")
    print(" 4. KL -> Tokyo (Long-haul)          RM650")
    route_name, base_fare = ROUTES[get_choice("Enter route (1-4): ", 1, 4)]

    pax = get_choice("\nNumber of passengers (1-9): ", 1, 9)

    print("\n--- Step 2: Pick your add-ons (per passenger) ---")
    print("Baggage:  1. None (RM0)  2. 20kg (RM60)  3. 30kg (RM90)")
    bag_name, bag = BAGGAGE[get_choice("Enter baggage (1-3): ", 1, 3)]

    print("Meal:     1. None (RM0)  2. Nasi Lemak (RM15)  3. Chicken Rice (RM18)")
    meal_name, meal = MEALS[get_choice("Enter meal (1-3): ", 1, 3)]

    print("Seat:     1. Standard (RM0)  2. Preferred (RM25)  3. Hot seat (RM40)")
    seat_name, seat = SEATS[get_choice("Enter seat (1-3): ", 1, 3)]

    insurance = get_yes_no("Add travel insurance (RM12 per passenger)? (y/n): ")

    # insurance is optional, skip it if the user said no
    ins_cost = INSURANCE_PER_PAX if insurance else "0.0"
    # add-ons are per passenger, then the whole lot scales with pax
    add_ons_per_pax = bag + meal + seat + ins_cost
    low_cost_total = base_fare + TAX_FEE_PER_PAX + add_ons_per_pax * pax
    full_service_total = (base_fare * FULL_SERVICE_MULT + TAX_FEE_PER_PAX + ins_cost) * pax
    savings = full_service_total - low_cost_total

    print("\n=========== FARE SUMMARY ===========")
    print(f"Route      : {route_name}")
    print(f"Passengers : {pax}")
    print(f"Baggage    : {bag_name}")
    print(f"Meal       : {meal_name}")
    print(f"Seat       : {seat_name}")
    print(f"Insurance  : {'Yes' if insurance else 'No'}")
    print("------------------------------------")
    print(f"Base fare  (x{pax}) : RM {base_fare * pax:.2f}")
    print(f"Taxes/fees (x{pax}) : RM {TAX_FEE_PER_PAX * pax:.2f}")
    print(f"Add-ons    (x{pax}) : RM {add_ons_per_pax * pax:.2f}")
    print(f"TOTAL (Low-cost)    : RM {low_cost_total:.2f}")
    print("------------------------------------")
    print(f"Full-service (est.) : RM {full_service_total:.2f}")

    if savings > 0:
        pct = savings / full_service_total * 100
        print(f"You save            : RM {savings:.2f} ({pct:.1f}%)")
        print("Unbundling lets you pay only for what you use!")
    else:
        print("With these add-ons, a full-service fare may be better value.")
    print("====================================")


def main():
    print("====================================")
    print("  AirAsia Low-Cost Fare Calculator")
    print("  (Sample prices for demo only)")
    print("====================================")

    again = True
    while again:
        run_calculator()
        again = get_yes_no("\nCalculate another fare? (y/n): ")
    print("\nThank you. Now everyone can fly!")


if __name__ == "__main__":
    main()
