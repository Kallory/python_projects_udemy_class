def band_name_generator():
    print("Welcome to the band name generator")
    print("")
    city_they_grew_up_in = input("What's the name of the city you grew up in?\n")
    their_pets_name = input("What's the name of your pet?\n")
    print("Your band name could be " + city_they_grew_up_in + " " + their_pets_name)

def tip_calculator(bill, tip_rate):
    return bill * tip_rate

def main():
    #  band_name_generator()
#    bill = input("What's the total bill?")
#    amount_they_want_to_tip = input("What percent would you like to tip?")
#    amount_they_want_to_tip = int(amount_they_want_to_tip) / 100
#
#    tip_amount = tip_calculator(int(bill), float(amount_they_want_to_tip))
#    print("tip amount: " + str(tip_amount) + "\n")
#    print("Total to pay: " + str(tip_amount+20))

#    size = input("What size pizza do you want? S, M, or L: ")
#    wants_pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
#    wants_extra_cheese = input("Do you want extra cheese on your pizza? Y or N: ")
#
#    small_pizza_cost = 15
#    medium_pizza_cost = 20
#    large_pizza_cost = 25
#    pepperoni_cost_small_pizza = 2
#    pepperoni_cost_medium_pizza = 3
#    pepperoni_cost_large_pizza = 3
#    extra_cheese_cost_any_pizza = 1
#
#    cost = 0
#    if size == "S":
#        cost += small_pizza_cost
#    elif size == "M":
#        cost += medium_pizza_cost
#    elif size == "L":
#        cost += large_pizza_cost
#
#    if wants_pepperoni == "Y" and size == "S":
#        cost += pepperoni_cost_small_pizza
#    elif wants_pepperoni == "Y" and size == "M":
#        cost += pepperoni_cost_medium_pizza
#    elif wants_pepperoni == "Y" and size == "L":
#        cost += pepperoni_cost_large_pizza
#
#    if wants_extra_cheese == "Y":
#        cost += extra_cheese_cost_any_pizza
#
#    print(f"Your total is ${cost}")

    # Define costs
    pizza_costs = {
        "S": 15,
        "M": 20,
        "L": 25
    }

    pepperoni_costs = {
        "S": 2,
        "M": 3,
        "L": 3
    }

    extra_cheese_cost = 1

    # Get user inputs
    size = input("What size pizza do you want? S, M, or L: ")
    wants_pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper() == "Y"
    wants_extra_cheese = input("Do you want extra cheese on your pizza? Y or N: ").upper() == "Y"

    # Calculate cost
    cost = pizza_costs.get(size, 0)

    if wants_pepperoni:
        cost += pepperoni_costs.get(size, 0)

    if wants_extra_cheese:
        cost += extra_cheese_cost

    print(f"Your total is ${cost}")


main()


