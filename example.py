while True:
    try:
        L = float(input("Enter length (L): "))
        if L > 0:
            break
        else:
            print("❌ Error: Length must be greater than 0.")
    except ValueError:
        print("❌ Error: Please enter a numeric value.")

pwhile True:
    try:
        w = float(input("Enter width (w): "))
        if w > 0:
            break
        else:
            print("❌ Error: Width must be greater than 0.")
    except ValueError:
        print("❌ Error: Please enter a numeric value.")

area = L * w
print("✅ Area of the rectangle is:", area) 