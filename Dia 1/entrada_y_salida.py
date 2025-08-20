import sys 
sys.stdout.write("Danos tu opinión: \n")#si no ponder \n primero te pedira el valor sin haber mostrado el mensaje 
opinion = sys.stdin.readline().strip() #entrada para tu opinion
sys.stdout.write(f"Tu opinión fue: {opinion}\n") #utiliza los f-string
# puede ser util 
for line in sys.stdin: # sys.stdin implicitamente te habre como un input
    x = line.strip() #esto funcionara como un bucle infinito hasta que le des una opcion de terminar
    if x == "break":# o cerrar directamente EOF
        break
    print("Dijiste:", x)