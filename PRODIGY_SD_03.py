#TEMPERATURE CONVERSION
n=int(input("Enter temperature value:-"))
print("Choose Unit:-")
print("1.CELCIUS")
print("2.FAHRENHEIT")
print("3.KELVIN")
u=int(input())
if (u==1):
    print("Entered Temperature is in Celcius...")
    t1=((n/5)*9)+32
    t2=n+273
    print("Temperature in Farenheit:-",t1)
    print("Temperature in Kelvin:-",t2)
elif(u==2):
    print("Entered Temperature is in Fahrenheit...")
    t1=((n-32)/9)*5
    t2=t1+273
    print("Temperature in Celcius:-", t1)
    print("Temperature in Kelvin:-", t2)
else:
    print("Entered Temperature is in Kelvin...")
    t1=n-273
    t2=((t1/5)*9)+32
    print("Temperature in Celcius:-", t1)
    print("Temperature in Farenheit:-", t2)