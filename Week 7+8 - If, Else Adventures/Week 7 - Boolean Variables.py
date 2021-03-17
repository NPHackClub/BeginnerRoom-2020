a = int(input())

if a > 10:
  if a > 20:
    if a > 30:
      if a > 40:
        if a > 50:
          if a > 60:
            if a > 70:
              if a > 80:
                if a > 90:
                  if a > 100:
                    print("Above 100")
                  elif a == 100:
                    print("Equals 100")
                  else:
                    print("Above 90")
                elif a == 90:
                  print("Equals 90")
                else:
                    print("Above 80")
              elif a == 80:
                print("Equals 80")
              else:
                print("Above 70")
            elif a == 70:
              print("Equals 70")
            else:
              print("Above 60")
          elif a == 60:
            print("Equals 60")
          else:
            print("Above 50")
        elif a == 50:
          print("Equals 50")
        else:
          print("Above 40")
      elif a == 40:
        print("Equals 40")
      else:
        print("Above 30")
    elif a == 30:
      print("Equals 30")
    else:
      print("Above 20")
  elif a == 20:
    print("Equals 20")
  else:
    print("Above 10")
elif a == 10:
  print("Equals 10")
else:
  print("Less than 10")