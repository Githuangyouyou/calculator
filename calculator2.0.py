import sys

#--------?????????--------
def calculator(salary):
        tax = salary - salary * (0.08 + 0.02 + 0.005 + 0.06) - 3500
        if tax <= 1500:
                rate = 0.03
                decute = 0
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
        pay = salary - taxrate - salary*(0.08 + 0.02 + 0.005 + 0.06)
        pay = format(pay,".2f")
        return pay

#--------??key?value??????????----------
def keyvalue(lsit):
        global salarydict
        salarydict = {}
        

        for string in list: #????????????????
                        string = str(string)
                        n = 0
                        charlist = [] #???????????string???????
                        for char in string: #??pkey?psalary???
                                n += 1                                
                                charlist.append(char)
                                if char == ":":
                                        k = n
                                        pkey = ''
                                        for charkey in charlist[:n-1]:
                                                pkey = pkey + charkey
                                        pkey = int(pkey) 
                        psalary = '' 
                        for charkey2 in charlist[k:]:
                                psalary = psalary + charkey2
                        psalary = int(psalary)                           
                        salarydict[pkey] = psalary

try:       
        if __name__=="__main__":

                paydict = {}
                list = sys.argv[1:]
                keyvalue(list)
                for salary_key,salary_value in salarydict.items(): ###
                        print('{}:{}'.format(salary_key,salary_value)) ###
                for pay_key in salarydict.keys():
                        peoplesalary = salarydict[pay_key]
                        paydict[pay_key] = calculator(peoplesalary)
                for pay_key,pay_value in paydict.items():
                        print('{}:{}'.format(pay_key,pay_value))


except: 
        print("Parameter Error")        
