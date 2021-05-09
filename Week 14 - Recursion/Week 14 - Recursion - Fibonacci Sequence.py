def fib(n):
  if n == 1:
    return 0
  elif n == 2:
    return 1
  else:
    return fib(n-1) + fib(n-2)

f = int(input("Enter nth fibonacci number: "))

print(fib(f))