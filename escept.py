try:
    num1, num2 = eval(input("Enter two numbers, separate it by comma"))
    result = num1 / num2
    print("Result is", result)

except ZeroDivisionError:
    print("undifined")

except SyntaxError:
    print("Bro u forgot comma u have to do it like dis 1, 2")

except:
    print("wrong thing")

else:
    print("no exceptions brotha")

finally:
    print("FINNALY dis is not wrong")