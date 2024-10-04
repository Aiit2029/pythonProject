def say_hi(func):
  def wrapper(*args,**kwargs):
      print("HI")
      ret=func(*args,**kwargs)
      print("BYE")
      return ret
  return wrapper

def say_yo(func):
  def wrapper(*args,**kwargs):
      print("Yo")
      return func(*args,**kwargs)
  return wrapper
@say_hi
@say_yo
def func():
  print("ROCK&ROLL")
func()