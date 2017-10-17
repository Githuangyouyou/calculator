#!/usr/bin/env python3
import sys
salary = sys.argv[1]
try:
        salary = int(salary)
        tax = salary - 3500
        if tax <= 0:
                rate = 0
        elif tax > 0 and tax <=1500:
                rate = 0.03
                decute=0
        elif tax > 1500 and tax <= 4500:
                rate = 0.1
                decute = 105
        elif tax > 4500 and tax <= 9000:
                rate = 0.2
                decute = 555
        elif tax > 9000 and tax <= 35000:
                rate = 0.25
                decute = 1005
        elif tax > 35000 and tax <= 55000:
                rate = 0.3
                decute = 2755
        elif tax > 55000 and tax <= 80000:
                rate = 0.35
                decute = 5505
        elif tax > 80000:
                rate = 0.45
                decute = 13505
        taxrate = tax * rate - decute
        #pay = salary - taxrate
        print(format(taxrate,".2f"))
except:
        print("Parameter Error")


