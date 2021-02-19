owner1 = input("Owner 1 Name: ")
owner1brand = input("Owner 1 Car Brand: ")
owner1model = input("Owner 1 Car Model: ")
owner2 = input("Owner 2 Name: ")
owner2brand = input("Owner 2 Car Brand: ")
owner2model = input("Owner 2 Car Model: ")
owner3 = input("Owner 3 Name: ")
owner3brand = input("Owner 3 Car Brand: ")
owner3model = input("Owner 3 Car Model: ")

print("____________Vehicles Insured____________")
owner1display = [str(owner1) + " owns a " + str(owner1brand) + " " + str(owner1model) + "."]
owner2display = [str(owner2) + " owns a " + str(owner2brand) + " " + str(owner2model) + "."]
owner3display = [str(owner3) + " owns a " + str(owner3brand) + " " + str(owner3model) + "."]
print(*owner1display)
print(*owner2display)
print(*owner3display)
print("________________________________________")

# ALTERNATE WAY #
# owner1 = input("Owner 1 Name: ")
# owner1brand = input("Owner 1 Car Brand: ")
# owner1model = input("Owner 1 Car Model: ")
# owner2 = input("Owner 2 Name: ")
# owner2brand = input("Owner 2 Car Brand: ")
# owner2model = input("Owner 2 Car Model: ")
# owner3 = input("Owner 3 Name: ")
# owner3brand = input("Owner 3 Car Brand: ")
# owner3model = input("Owner 3 Car Model: ")
# print(str(owner1) + " owns a " + str(owner1brand) + " " + str(owner1model) + ".")
# print(str(owner2) + " owns a " + str(owner2brand) + " " + str(owner2model) + ".")
# print(str(owner3) + " owns a " + str(owner3brand) + " " + str(owner3model) + ".")
