ask1 = int(input("What is your Weight in Kg? "))
ask2 = float(input("What is your height in cm? "))

result=(+ask1/ask2**2)

if result< float(18.5):
    print(" they are under weight ")
elif result>18.5 and result<25:
    print(" they have a normal weight  ")
elif result>25 and result<30:
    print ( " they are overweight ")
elif result>30 and result<35:
    print(" they are obese ")
else:
    print(" they are clinically obese ")
