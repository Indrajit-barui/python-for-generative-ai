

def div(num1,num2):
    try:
       res=num1/num2
       print(res)


    

    except Exception as e:
      print(f"error ->{e}")
    
    finally:
       print("i am always executed")

    


num1=int(input("Enter a number1: "))
num2=int(input("Enter a number2: "))
    
div(num1,num2)

    
