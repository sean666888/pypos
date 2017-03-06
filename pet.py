import sys
dogis = int(10)
catis = int(15)
def stock():
  global dogis
  global catis
  print("------------")
  print("Dogs in stock: {}".format(dogis))
  print("Cats in stock: {}".format(catis))
  print("------------")
  print("m. back to main menu")
  iv = input(">")
  if iv in ['m', 'M']:
    getnum()
  elif iv in ['DEV']:
    global dogis
    global catis
    dogis = int(input("dogis"))
    catis = int(input("catis"))
    stock()
  else:
    print("invalid input")
    print("------------")
    stock()
def getnum():
  print("1. get stock list")
  print("0. Exit")
  ip = input(">")
  if ip in ['1']:
    stock()
  elif ip in ['0']:
    sys.exit("Exiting")
  else:
    print("invalid input")
    print("------------")
    getnum()










getnum()
