owner1 = input("Car Owner: ")
brand1 = input("Car Brandname: ")
model1 = input("Car Model: ")
print("")
owner2 = input("Car Owner: ")
brand2 = input("Car Brandname: ")
model2 = input("Car Model: ")
print("")
owner3 = input("Car Owner: ")
brand3 = input("Car Brandname: ")
model3 = input("Car Model: ")

one = {
  "owner" : owner1,
  "brand" : brand1,
  "model" : model1
}

two = {
  "owner" : owner2,
  "brand" : brand2,
  "model" : model2
}

three = {
  "owner" : owner3,
  "brand" : brand3,
  "model" : model3
}

print("")
print("________________Vehicles Insured________________")
print(one["owner"], "owns a", one["brand"], one["model"], ".")
print(two["owner"], "owns a", two["brand"], two["model"], ".")
print(three["owner"], "owns a", three["brand"], three["model"], ".")
print("________________________________________________")