# initial quantities
muffins = 10
cupcakes = 10

while True:
    order = input("Enter 'muffin' or 'cupcake' to buy, or '0' to stop: ")

    if order == "0":
        break

    if order == "muffin":
        if muffins > 0:
            muffins = muffins - 1
            print(f"One muffin sold. Muffins left: {muffins}")
        else:
            print("Out of stock")
    elif order == "cupcake":
        if cupcakes > 0:
            cupcakes = cupcakes - 1
            print(f"One cupcake sold. Cupcakes left: {cupcakes}")
        else:
            print("Out of stock")
    else:
        print("Invalid input")

print(f"Muffins: {muffins} Cupcakes: {cupcakes}")
