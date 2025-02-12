import random
import time
import sys  
from colorama import Fore
import os
import sys
import time

green = '\033[32m'
red = '\033[1,31m'
blue = '\033[1,34m'
white = '\033[1,37m'
yellow = '\033[1,37m'
print (os.system("clear"))

print(f"{green} ")
d = ("""\033[32m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣮⣿⣿⣿⣿⣷⣶⣦⣄⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⠿⠋⠉⠁⠀⠀⠈⠉⠙⠻⣿⣿⣿⣿⣦⡀
⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣷
⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿
⠀⠀⢀⣀⣀⣀⣀⣿⣿⣿⣿⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣿⣿⣿⣿⣀⣀⣀⣀⡀
⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠀⠀⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁\033[31m Tack \033[32m⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ \033[31m Lorix\033[32m ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟
""")
for d in d:
        sys.stdout.write(d)
        sys.stdout.flush()
        time.sleep(0.0)


print(f"{green} ")
d = (Fore.WHITE+"""      my ID Telegram"""+Fore.RED+" = "+Fore.WHITE+"@Taklorix "+Fore.WHITE+"""
  ID Channel Telegram"""+Fore.RED+" = "+Fore.WHITE+"@Black_Edalat")
for d in d:
        sys.stdout.write(d)
        sys.stdout.flush()
        time.sleep(0.1)

print (Fore.RED+"""





   />"""+Fore.BLUE+""" Password length"""+Fore.RED+" ?"+Fore.BLUE+"""
 
   1"""+Fore.RED+"/> "+Fore.YELLOW+"16 characters"+Fore.BLUE+"""
   2"""+Fore.RED+"/> "+Fore.YELLOW+"8 characters"+Fore.BLUE+"""
   3"""+Fore.RED+"/> "+Fore.YELLOW+"4 characters")

Tl = input(Fore.RED+"""

         /> """+Fore.YELLOW+"choise number"+Fore.RED+"? ")
if Tl == "1":
    import random

    tack= (f"!","!")

    lorix= (random.choice(tack))

    tacklorix = ['i','^','K',' ','x','&','j','$','@','#','o','c','w']
    
    Tack_Lorix = str(random.randint(0,9))

    result = Tack_Lorix.join([str(random.choice(tacklorix)) for _ in range(9)])

    print(f"{green} ")
    d = (f"""         \033[32m{lorix}\033[32m{result}""")
    time.sleep(0.09)

    for d in d:
        sys.stdout.write(d)
        sys.stdout.flush()
        time.sleep(0.10)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
elif Tl == "2":
       tack= (f"!","!")

       lorix= (random.choice(tack))
        

       tacklorix = ['i','^','K',' ','x','&','j','$','#']
    
       Tack_Lorix = str(random.randint(0,9))    

       result = Tack_Lorix.join([str(random.choice(tacklorix)) for _ in range(4)])

       
       print(f"{green} ")
       d = (f"""              \033[32m{lorix}\033[32m{result}""")
       time.sleep(0.09)
       for d in d:
        sys.stdout.write(d)
        sys.stdout.flush()
        time.sleep(0.10)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
elif Tl == "3":
      tack= (f"!","!")

      lorix= (random.choice(tack))

      tacklorix = ['w','^',' ','x','&','j','$','#']
    
      Tack_Lorix = str(random.randint(0,9))    
  
      result = Tack_Lorix.join([str(random.choice(tacklorix)) for _ in range(2)])

      print(f"{green} ")
      d = (f"""                 \033[32m{lorix}\033[32m{result}""")
      time.sleep(0.09) 
      for d in d:
        sys.stdout.write(d)
        sys.stdout.flush()
        time.sleep(0.10)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
else:
    
     print(f"{green} ")
     d = (Fore.RED+"""
              Choose one of numbers"""+Fore.GREEN+" [ "+Fore.YELLOW+"1 "+Fore.WHITE+","+Fore.YELLOW+" 2 "+Fore.WHITE+","+Fore.YELLOW+" 3 "+Fore.GREEN+"]")
     time.sleep(0.09) 
     for d in d:
        sys.stdout.write(d)
        sys.stdout.flush()
        time.sleep(0.10)
