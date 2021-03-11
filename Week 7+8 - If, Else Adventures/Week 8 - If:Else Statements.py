import time

wq = input("Hello, (Enter Name) ")
nm_ = wq+"."
nm = wq
counter = 0

print("Nice to meet you",nm_, "You will follow through on an adventure to solve a case as a dectective. To begin, choose a case to solve. Good luck!")

time.sleep(4)

print("")
cases = ["Hallway of Hidden Views", "The Missing Grave"]
print("Choose one of the following to solve:")
print(cases[0],"or", cases[1])
choice = input("1 or 2: ")
print("")

time.sleep(1)

if choice == "1":
  print("Case file 431: Hallway of Hidden Views")
  time.sleep(1)
  print("Location: New Brunswick, Canterbury High School")
  time.sleep(1)
  print("")
  print("You enter the school and follow the principal to a rusted door that leads to a long hallway with 3 doors on each side.")
  time.sleep(5)
  print("Each door has a mysterious symbol on it which is either a square, a triangle, and circle.")
  time.sleep(3)
  print("")
  door = input("Which door do you want to open? The square, triangle, or circle: ")
  if door != "square" and door != "Square" and door != "triangle" and door != "Triangle" and door != "circle" and door != "Circle":
    door = input("Enter either square, triangle, or circle: ")
  if door == "square" or door == "Square":
    print("")
    print("Neither of the doors with a square opens. You will have to try another one.")
    time.sleep(4)
    print("")
    door = input("Which door do you want to open? The triangle or circle?: ")
    if door != "triangle" and door != "Triangle" and door != "circle" and door != "Circle":
      door = input("Enter either square, triangle, or circle: ")
    if door == "triangle" or door == "Triangle":
      print("")
      print("Neither of the doors with a triangle opens either. There's only one option left.")
      time.sleep(4)
      print("")
      door = input("The doors with the cirlce remains. Do you want to open the left or the right door? This choice will change the outcome of the story(left or right): ")
      if door != "left" and door != "Left" and door != "right" and door != "Right":
        door = input("This choice cannot be avoided. Enter left or right: ")
      if door == "left" or door == "Left":
        counter += 1
      elif door == "right" or door == "Right":
        counter += 2
    elif door == "circle" or door == "Circle":
      print("")
      print("The doors with the cirlce remains. Do you want to open the left or the right door? This choice will change the outcome of the story(left or right): ")
      time.sleep(4)
      if door != "left" and door != "Left" and door != "right" and door != "Right":
        door = input("This choice cannot be avoided. Enter left or right: ")
      if door == "left" or door == "Left":
        counter += 1
      elif door == "right" or door == "Right":
        counter += 2
  elif door == "triangle" or door == "Triangle":
    print("")
    print("Neither of the doors with a triangle opens. You will have to try again.")
    time.sleep(4)
    print("")
    door = input("Which door do you want to open? The square or circle?: ")
    if door != "square" and door != "Square" and door != "circle" and door != "Circle":
      door = input("Enter either square, or circle: ")
    if door == "square" or door == "Square":
      print("")
      print("Neither of the doors with a square opens either. There's only one option left.")
      time.sleep(5)
      print("")
      door = input("The doors with the cirlce remains. Do you want to open the left or the right door? This choice will change the outcome of the story(left or right): ")
      if door != "left" and door != "Left" and door != "right" and door != "Right":
        door = input("This choice cannot be avoided. Enter left or right: ")
      if door == "left" or door == "Left":
        counter += 1
      elif door == "right" or door == "Right":
        counter += 2
    elif door == "circle" or door == "Circle":
      print("")
      print("Both the doors with the circle open. Do you want to enter the left or the right door? This choice will change the outcome of the story(left or right): ")
      time.sleep(5)
      if door != "left" and door != "Left" and door != "right" and door != "Right":
        door = input("This choice cannot be avoided. Enter left or right: ")
      if door == "left" or door == "Left":
        counter += 1
      elif door == "right" or door == "Right":
        counter += 2
  elif door == "circle" or door == "Circle":
    print("")
    print("Both the doors with the circle open. But which one do you want to enter?")
    time.sleep(4)
    print("")
    door = input("Do you want to open the left or the right door? This choice will change the outcome of the story(left or right): ")
    if door != "left" and door != "Left" and door != "right" and door != "Right":
      door = input("This choice cannot be avoided. Enter left or right: ")
    if door == "left" or door == "Left":
      counter += 1
    elif door == "right" or door == "Right":
      counter += 2
  else:
    print("Please retry the case and enter in one of the given options.")
  print("")
  if counter == 1:
    print("You push open the left door and it slowly creaks open. This does not frighten you as you have been through more periculous situations.")
    time.sleep(4)
    print("Inside, there is a locked door with a single keyhole.")
    time.sleep(2)
    print("")
    print("However, the shape of the key is very familar. It reminds you of a previous case that you solved 3 years ago.")
    time.sleep(4)
    print("Underneath your coat, there is a key hanging around your neck. There is a single symbol on the bow; a circle with a square inside of it and a triangle passing diagonally through the entire shape.")
    time.sleep(5)
    print("")
    print("You precautionarily slide the key inside the lock and it loudly clicks.")
    time.sleep(3)
    print("")
    fINAL = input("Do you want to open the door? Yes or no: ")
    if fINAL != "yes" and fINAL != "Yes" and fINAL != "no" and fINAL != "No":
      input("You have to enter either yes or no: ")
    if fINAL == "yes" or "Yes":
      print("")
      print("You pushed open the door and inside stands a man with a black hat and a familar ring on his finger.")
      time.sleep(4.6)
      print("")
      print("He looks up at you, and then at the key still in the door. Thats the last thing you remember before losing conscious...")
      time.sleep(3.8)
      print("")
      print("The End")
      time.sleep(1)
      print("")
      print("If you want to know the history behind the key and the man behind the door, solve the case The Missing Grave")
    if fINAL == "no" or fINAL == "No":
      print("")
      print("You pull away and slowly back away from the door. However, you bump into the principal.") 
      time.sleep(4)
      print("")
      print("He knocks your head and walks to the door opens it.")
      time.sleep(2)
      print(" 'No...', you say before blacking out. The last thing you see is a man walking towards you with a black hat and ring on his finger.")
      time.sleep(4)
      print("")
      print("The End")
      time.sleep(1)
      print("")
      print("If you want to know the history behind the key and the man behind the door, solve the case 'The Missing Grave'. ")
  elif counter == 2:
    print("")
    print("You push open the right door and it slowly creaks open. This does not frighten you as you have been through more periculous situations.")
    time.sleep(4)
    print("")
    print("Inside, there is another door and it has a keyhole. The shape of the keyhole is very familar. It reminds you of a previous case that you solved 3 years ago.")
    time.sleep(4)
    print("")
    print("Underneath your coat, there is a key hanging around your neck. There is a single symbol on the bow; a circle with a square inside of it and a triangle passing diagonally through the entire shape.")
    time.sleep(5)
    print("")
    print("It represents all the symbols of the doors in the hallway but only the doors with a square symbol were open.")
    time.sleep(4)
    print("")
    print("You place the key in the lock and it clicked open loudly.")
    time.sleep(3)
    print("")
    print("Inside, there is an old telephone on a stand with a phone book beside it. You open the book and there's two numbers to call.")
    time.sleep(4)
    print("")
    print("Which number do you want to call? 647-824-5005 or 416-104-3839")
    fINAL = input("Enter the number into the phone: ")
    if fINAL != "647-824-5005" and fINAL != "6478245005" and fINAL != "416-104-3839" and fINAL != "4161043839":
      fINAL = input("This is your only clue right now that will get you closer to the end. Enter a number from the phone book into the phone: ")
    if fINAL == "647-824-5005" or fINAL == "6478245005":
      print("")
      print("The line kept ringing for awhile but no one picked up. It must have been fake.")
      time.sleep(4)
      print("")
      fINAL = input("Enter the number into the phone: ")
      if fINAL == "416-104-3839" or fINAL == "4161043839":
        print("")
        print("The line rang for 5 seconds but then someone picked up the phone.")
        time.sleep(2.5)
        print("")
        print("'Hello..?', you say into the phone.")
        time.sleep(2)
        print("")
        print("Before anyone could answer, the telephone started glowing and the light got too bright that you dropped the telephone to cover your eyes.")
        time.sleep(4)
        print("")
        print("You turn around to leave just in time to see the principal closing the door locking you in.")
        time.sleep(4)
        print("")
        print("The light slowly fades away revealing a secret pathway. But you don't know if you should leave the room.")
        time.sleep(3)
        chosen = input("Should you leave and follow the pathway? Yes or no: ")
        if chosen != "yes" and chosen != "Yes" and chosen != "no" and chosen != "No":
          chosen = input("These are your only options. Do you want to leave the room? Yes or no: ")
        if chosen == "yes" or chosen == "Yes":
          print("")
          print("You quickly rush out of th room. You vowed to protect that key with your life and now its gone.")
          time.sleep(4)
          print("")
          print("At the end of the pathway, there is a grave with the name 'Anthony Quarks' written on it.")
          time.sleep(3.8)
          print("")
          print("'No, it can't be...', you say quietly before a hand taps your shoulder...")
          time.sleep(3)
          print("")
          print("The End")
          time.sleep(1)
          print("")
          print("If you want to know the history behind the key and the man behind the door, solve the case 'The Missing Grave' ")
        elif chosen == "no" or chosen == "No":
          print("")
          print("You slide down to the ground with your back against the door. You vowed to protect that key with your life and now its gone.")
          time.sleep(5)
          print("")
          print("You get up and try to find a way to open the door before a hand taps your shoulder. Turning around, you see a familiar face. One you haven't seen in 3 years...")
          time.sleep(5)
          print("")
          print("The End")
          time.sleep(1)
          print("")
          print("If you want to know the history behind the key and the man behind the door, solve the case 'The Missing Grave' ")
    elif fINAL == "416-104-3839" or fINAL == "4161043839":
      print("")
      print("The line rang for 5 seconds but then someone picked up the phone.")
      time.sleep(2)
      print("")
      print("'Hello..?', you say into the phone.")
      time.sleep(2)
      print("")
      print("Before anyone could answer, the telephone started glowing and the light got too bright that you dropped the telephone to cover your eyes.")
      time.sleep(4)
      print("")
      print("You turn around to leave just in time to see the principal closing the door locking you in.")
      time.sleep(4)
      print("")
      print("The light slowly fades away revealing a secret pathway. But you don't know if you should leave the room.")
      time.sleep(3)
      chosen = input("Should you leave and follow the pathway? Yes or no: ")
      if chosen != "yes" and chosen != "Yes" and chosen != "no" and chosen != "No":
        chosen = input("These are your only options. Do you want to leave the room? Yes or no: ")
      if chosen == "yes" or chosen == "Yes":
        print("")
        print("You quickly rush out of the room. You vowed to protect that key with your life and now its gone.")
        time.sleep(4)
        print("")
        print("At the end of the pathway, there is a grave with the name 'Anthony Quarks' written on it.")
        time.sleep(3)
        print("")
        print("'No, it can't be...', you say quietly before a hand taps your shoulder...")
        time.sleep(3)
        print("")
        print("The End")
        time.sleep(1)
        print("")
        print("If you want to know the history behind the key and the man behind the door, solve the case 'The Missing Grave' ")
      elif chosen == "no" or chosen == "No":
        print("")
        print("You slide down to the ground with your back against the door. You vowed to protect that key with your life and now its gone.")
        time.sleep(5)
        print("")
        print("You get up and try to find a way to open the door before a hand taps your shoulder. Turning around, you see a familiar face. One you haven't seen in 3 years...")
        time.sleep(5)
        print("")
        print("The End")
        time.sleep(1)
        print("")
        print("If you want to know the history behind the key and the man behind the door, solve the case 'The Missing Grave' ")
    else:
      print("You entered in the number but no one picked up. Retry the case and enter in a number from the given choices.")
elif choice == "2":
  print("Case File 001: The Missing Grave")
  time.sleep(2)
  print("Location: Boreal Forest, Canada")
  time.sleep(2)
  print("")
  print("You are standing at the entrance of Boreal Forest, the largest forest in Canada. Someone asked you investigate the disapeerance of a man, Anthony Quarks.")
  time.sleep(4)
  print("")
  enter = input("Do you want to enter? yes or no: ")
  while True:
    if enter != "Yes" and enter != "yes" and enter != "No" and enter != "no":
      enter = input("Enter yes or no: ")
    if enter == "Yes" or enter == "yes":
      print("You turn on your flashlight and walk into the forest following the trail.")
      time.sleep(3)
      break
    if enter == "No" or enter == "no":
      print("This was his last known location. In order to solve the case, you have to enter.")
      time.sleep(3)
      break
  print("")
  print("As you walk through the trail, you come across a intersection. Which path do you want to investigate?")
  print("")
  time.sleep(3)
  invest = input("Do you want to check the left or right path for clues: ")
  while True:
    if invest != "right" and invest != "Right" and invest != "Left" and invest != "left":
      invest = input("You need to investigate one of the paths. Enter left or right: ")
    if invest == "left" or invest == "Left":
      print("")
      print("You walk to the left path and on the ground there are footprints leading farther down the trail.")
      time.sleep(4)
      print("")
      go = input("Do you want to follow the footprints or investigate the right path first? Enter follow or investigate: ")
      if go != "investigate" and go != "follow":
        go = input("Enter either follow or investigate: ")
      if go == "investigate":
        print("")
        print("You check out the right path and there's footprints as well but these look fresh as if someone just came down here.")
        time.sleep(4)
        print("")
        path = input("Do you want to follow the footprints on the left or the right path. This choice will change the outcome of your story. (left or right): ")
        if path == "left" or path == "Left":
          counter += 1
        elif path == "right" or path == "Right":
          counter += 2
      elif go == "follow":
        counter += 1
    if invest == "right" or invest == "Right":
      print("")
      print("You check out the right path and there's footprints but these look fresh as if someone just came down here")
      time.sleep(4)
      print("")
      go = input("Do you want to follow the footprints or investigate the left path first? Enter follow or investigate: ")
      if go != "investigate" and go != "follow":
        go = input("Enter either follow or investigate: ")
      if go == "investigate":
        print("")
        print("You walk to the left path and there's footprints as well but these are faded out.")
        time.sleep(3)
        print("")
        path = input("Do you want to follow the footprints on the left or the right path. This choice will change the outcome of your story. (left or right): ")
        if path == "left" or path == "Left":
          counter += 1
        elif path == "right" or path == "Right":
          counter += 2
      elif go == "follow":
        counter += 2
    break
  print("")
  if counter == 1:
    print("You quickly follow the footprints but they are faded out so its hard to know if you are still following them.")
    time.sleep(4)
    print("")
    print("Soon enough, you reach a clearing with a tombstone in the middle of the field. The words Anthony Quarks is written on it.")
    time.sleep(4)
    print("")
    print("There is no way that you came all this way for nothing. Suddenly, you get an idea but it isn't really a pleasent one.")
    time.sleep(4)
    print("")
    option = input("Do you want to 'check the grave' to see if he really is dead? yes or no: ")
    if option == "Yes" or option == "yes":
      print("")
      print("You take out a shovel from your backpack and dig down until you hit a box thats way to small to fit a person.")
      time.sleep(4)
      print("")
      print("You take the box out and open it. Inside, there is a key and note.")
      time.sleep(3)
      print("")
      read = input("Do you want to read the note or just take the key? key or note: ")
      while True:
        if read != "key" or read != "note":
          read = input("Enter either key or note: ")
        if read == "key":
          print("")
          print("You take the key and throw away the note. The key has an interesting design with a circle, square, adn triangle on its bow.")
          time.sleep(4)
          break
        elif read == "note":
          print("")
          print("You read the note aloud, 'To whoever finds this, do not let him have this key and protect it with your life'.")
          time.sleep(4)
          print("")
          print("This seemed like a joke so you throw away the note and take the key.")
          time.sleep(3)
          break
      print("")
      print("You get up and back away from the grave and out of the clearing. Right then, another man comes to the grave and looks at the note and empty box.")
      time.sleep(4)
      print("")
      print("He is wearing a black hat and ring on his finger. He turns to you and thats your cue to run. You ran far away from that place taking the key with you.")
      time.sleep(4)
      print("")
      print("Soon enough, you reach your car and drive far away from the forest. Your case was far from solved and it gave you even more questions...")
      time.sleep(4)
      print("")
      print("Who was that man and why did he want this key?")
      time.sleep(2.5)
      print("")
      print("The End")
      time.sleep(1)
      print("")
      print("If you want to know what happens next, solve the case 'The Hallway of Hidden Views'.")
    elif option == "no" or option == "No":
      print("")
      print("You walk out of the clearing since your case was closed and the man was dead. You turn back once more to see another man stadning over the grave.")
      time.sleep(4)
      print("")
      print("He digs open the grave and takes out a box and takes a key out of it. You can't let him just take that.")
      time.sleep(4)
      read = input("Do you want to tackle him and take the key or run away? attack or run: ")
      while True:
        if read != "attack" or read != "run":
          read = input("Enter either run or attack: ")
        if read == "attack":
          print("")
          print("The man turns away and starts walking away so you sneak from behind him and push him to the ground causing him to drop the key.")
          time.sleep(4.5)
          print("")
          print("You grab the key and run away with him chasing you. From behind, you don't hear him anymore.")
          time.sleep(4)
          break
        elif read == "run":
          print("")
          print("You are about to run away but then another younger man comes and starts fighting the man with the key. That younger man was the one you were trying to find.")
          time.sleep(5)
          print("")
          print("Anthony Quarks manages to smack the key out of the other's hand and it lands near you. You pick it up and look at them.")
          time.sleep(4)
          print("")
          print("They both look at you and Anthony mouths for you to run. You bolt away from the clearing and run down the trail.")
          time.sleep(4)
          break
      print("")
      print("Soon enough, you reach your car and drive far away from the forest. Your case was solved but it gave you even more questions...")
      time.sleep(4)
      print("")
      print("Who was that man and why did he want this key?")
      time.sleep(2)
      print("")
      print("The End")
      time.sleep(1)
      print("")
      print("If you want to know what happens next, solve the case 'The Hallway of Hidden Views'.")
  elif counter == 2:
    print("You walk down the right path and follow the footprints.")
    time.sleep(2)
    print("")
    print("A large patch of vegetation blocks your path. You are about to turn back but then you hear someone behind the trees.")
    time.sleep(4)
    print("")
    print("You squish through the blockage and land infront of a man. But, he's the one you were trying to find, Anthony Quarks.")
    time.sleep(4)
    print("")
    print("'Who are you?', he asks")
    time.sleep(2)
    print("")
    print("Response 1: I'm a detective hired to look for you.")
    time.sleep(1)
    print("Response 2: What are you doing here?")
    time.sleep(1)
    print("Response 3: I need you to come with me.")
    time.sleep(1)
    print("")
    talk = input("Which dialogue do you say(1,2,3): ")
    while True:
      if talk != "1" and talk != "2" and talk != "3":
        talk = input("Choose one of the given responses. Enter 1, 2 or 3: ")
      if talk == "1":
        print("")
        print("'Oh, I am fine you can leave', he says while looking into the distance.")
        time.sleep(3)
        break
      elif talk == "2":
        print("")
        print("'I am looking for someone. I need to stop him from getting something', he says while looking into the distance.")
        time.sleep(4)
        break
      elif talk == "3":
        print("")
        print("'Are you working with him?', he asks while taking a step towards you.")
        time.sleep(3)
        print("")
        print("'No of course not. I am a detective hired to find you. Who are you talking about?', you reply.")
        time.sleep(4)
        break
    print("")
    print("He looks at his watch and quickly runs away, 'Sorry I have to do something first'.")
    time.sleep(4)
    print("")
    print("You follow him into a clearing with a grave and another man standing above it holding a key.")
    time.sleep(4)
    print("")
    print("Anthony attacks that man and they both start fighting over the key. You run over to help them but the key flings over infront of you.")
    time.sleep(4)
    print("")
    kORh = input("Do you pick up the key or help Anthony? key or help: ")
    while True:
      if kORh != "key" and kORh != "Key" and kORh != "help" and kORh != "Help":
        kORh = input("These are your only options. Please enter key or help: ")
      if kORh == "key" or kORh == "Key":
        print("")
        print("You pick up the key and go over to help Anthony but he's nowhere in sight. The other man is standing there wearing a hat and wearing a ring.")
        time.sleep(5)
        print("")
        print("You look at the key and look back at the man. He starts to chase you so you run out of the clearing and pass a tombstone in the middle of the field.")
        time.sleep(5)
        break
      elif kORh == "help" or kORh == "Help":
        print("")
        print("You run over to Anthony and push the man off of him. The man's hat falls off and you see his face for 2 seconds until Anthony pushes you away.")
        time.sleep(5)
        print("")
        print("Anthony gives you the key and tells you to run away from here and never come back.")
        time.sleep(3)
        print("")
        print("You run away and pass a tombstone with the words Anthony Quarks written on it.")
        time.sleep(3)
        break
    print("")
    print("You run out of the clearing and kept running until you hit a dead end. You turn around and slowly walk back to the field even though that other man is still out here somewhere.")
    time.sleep(5)
    print("")
    print("You enter the field but no one is there. You walk to the middle but the grave is gone and so is everyone else.")
    time.sleep(4)
    print("")
    print("You leave the forest and drive away with the key. The key has an interesting design with a circle, triangle, and square on its bow. Mysterious...")
    time.sleep(4)
    print("")
    print("The End")
    time.sleep(1)
    print("")
    print("If you want to know what happens next, solve the case 'The Hallway of Hidden Views'.")
else:
  print("Please choose one of the given cases. Enter either 1 for 'The Hallway of Hidden Views' or 2 for 'The Missing Grave'.")
