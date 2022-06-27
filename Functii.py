def my_function():
  print("Hello from a function")

my_function()

def my_function2(fname):
  print(fname + " Iliescu")

my_function2("Mircea")
my_function2("Vasile")
my_function2("Popescu")

def my_function3(*accesorii):
  print("The best tool is: " + accesorii[2])

my_function3("Pensula", "Patent", "Ciocan")