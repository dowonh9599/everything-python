# writing code here means sniper is not looking at the scope
x = "global"

def foo1():
  # writing code here means sniper is looking at everywhere in foo1 region
  x = "foo1 local"
  
  def foo2():
    # writing code here means sniper is looking at everywhere in foo2 region
    x = "foo2 local"
    print(x)  # This will print 'foo2 local' because it's the nearest scope
  
  foo2()
  print(x)  # This will print 'foo1 local'

print(x)  # This prints 'global' because it's in the global scope

#  4.2.2
x = 5
y = 7
z = 9
def add_three_num(x, y, z):
  return x + y + z

print(add_three_num(x, y, z)) # This will result in 6

# 4.2.4 Using `global` keyword
def foo3():
  num1, num2, num3 = 1,2,3

def foo4():
  return num1 + num2 + num3 # Would this return 6?

# 4.2.5 Nested Function
def foo1(a, b):
  return a + b

def foo2_5(c):
  return c/2

def foo2(a, b):
  c = a - b
  # nested function in foo2, this function is absolutely different function from foo2_5 beyond foo2.
  def foo2_5(c):
    return c ** 2
  
  return foo2_5(c) # while this is technically returning (a-b)^2

print(foo2_5(10)) # this results in 5,

# 4.2.5
# @params s: symbol
def start_greeting(s):
  # @params p: phrase
  def end_greeting(p):
    return "Hello" + s + p + "world!"
  return end_greeting


print(start_greeting("@")("@"))