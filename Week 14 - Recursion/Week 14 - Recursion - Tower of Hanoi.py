def tower(n, rod_A, rod_B, rod_C):
  if n == 1:
    print("Disk 1 moves from", rod_A, "to", rod_C)
  else:
    tower(n-1, rod_A, rod_C, rod_B)
    print("Disk", n, "moves from", rod_A, "to", rod_C)
    tower(n-1, rod_B, rod_A, rod_C)

tower(int(input("Enter Disk Number: ")),"A","B","C")