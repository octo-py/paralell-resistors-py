def resistors(*inputs):
    loop=0
    inv_list = []
    while loop<len(inputs):
        current_inversion = float(inputs[loop])**-1
        inv_list.append(current_inversion)
        loop=loop+1
    total_resistance = sum(inv_list)**-1
    return total_resistance
if __name__ == "__main__":
    total_resistors = int(input("Resistors in parallel\n"))
    x = 0
    resistor_values = []
    while x < total_resistors:
        resistor_values.append(input("Resistor " + str(x+1) + "\n"))
        x = x+1
    print("Total Resistance " + str(resistors(*resistor_values)))
else:
    pass