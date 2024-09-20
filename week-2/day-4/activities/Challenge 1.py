order_count = 0

def take_order(topping):
    global order_count
    print(f"Pizza with {topping}")
    order_count += 1
    
take_order("Pineapple")
take_order("Ham")
take_order("Pepperoni")

print(f"There has been {order_count} orders")