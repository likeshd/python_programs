# x = 5
# # y = 19
# def func():
#     global x
#     x =10
#
#     # d = globals()
#     print(x)
#     # print(d['x'], d['y'])
# func()
x = "awesome"

def myfunc():
  global x
  # print(x)
  x = "fantastic"
myfunc()
print("Python is " + x)

