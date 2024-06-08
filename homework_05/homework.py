from templates import TPL_OUTPUT

# input data
friends_count = 4

ticket_price = 500

taxi_price = 600
taxi_evening_price_markup_percent = 20

pizza_price = 250
pizza_count = 2
pizza_discount_percent = 15

air_hockey_price = 80
air_hockey_count = 8

# calculation
tickets_costs = ticket_price * friends_count

taxi_transfer_to_park = taxi_price
taxi_evening_price_markup =  taxi_price * taxi_evening_price_markup_percent / 100
taxi_transfer_from_park = taxi_price + taxi_evening_price_markup
taxi_costs = taxi_transfer_to_park + taxi_transfer_from_park

pizza_discount = pizza_price * pizza_discount_percent / 100
pizza_costs = (pizza_price-pizza_discount) * pizza_count

air_hockey_costs = air_hockey_price * air_hockey_count

total_costs = tickets_costs + pizza_costs + taxi_costs + air_hockey_costs
costs_per_person = total_costs / friends_count

# presentation
print(
  TPL_OUTPUT.format( 
    tickets=round(tickets_costs, 2),
    taxi=round(tickets_costs, 2),
    food=round(pizza_costs, 2),
    game=round(air_hockey_costs, 2),
    total=round(total_costs, 2),
    per_person=round(costs_per_person, 2)
  )
)
