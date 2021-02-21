regularServingPancakes = 24
cupsOfFlourrPer24Pancakes = 4.5
noOfEggsPer24Pancakes = 4
litresOfMilkPer24Pancakes = 1

noOfPancakes = float(input("How many pancakes do you want to make: "))

expectedCupsOfFlour = ( noOfPancakes / regularServingPancakes ) * \
                      cupsOfFlourrPer24Pancakes
expectedNoOfEggs = ( noOfPancakes / regularServingPancakes ) * \
                      noOfEggsPer24Pancakes
expectedLitresOfMilk = ( noOfPancakes / regularServingPancakes ) * \
                      litresOfMilkPer24Pancakes

print ( "For " + str(noOfPancakes ) + " you will need " + \
        str( expectedCupsOfFlour ) + " cups of flour " + \
        str( expectedNoOfEggs ) + " eggs " + \
        str( expectedLitresOfMilk ) + " litres of milk" )
