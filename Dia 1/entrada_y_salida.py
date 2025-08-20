import sys 
sys.stdout.write("Danos tu opinión: \n")#si no ponder \n primero te pedira el valor sin haber mostrado el mensaje 
opinion = sys.stdin.readline().strip() #entrada para tu opinion
sys.stdout.write(f"Tu opinión fue: {opinion}\n") #utiliza los f-string