def per(l,b):
  print(2*(l+b))
def area(l,b):
  print(l * b)
a = input("Enter what to find area or perimeter:")
if a == "perimeter":
  l = int(input("length"))
  b = int(input("breath"))
  per(l,b)
elif a == "area":
  l = int(input("length"))
  b = int(input("breath"))
  area(l,b)
else:
  print("Pls enter area or perimeter")
