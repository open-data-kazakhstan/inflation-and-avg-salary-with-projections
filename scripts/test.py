li =  [151513, 15612, 153215, 5556123, 7123500]
lin = []

# for i in li:
#     x = str(i)
#     print(type(x))
#     ch = ''
#     for k in range(0, len(x)):
#         if len(x)>6:

#         ch = ch +x[k]
#     lin.append(ch)
# print(lin)
# for i in li:
#     x = str(i)
#     k = ''
#     g = ''
#     if len(x) > 6:
#         k = x[0] + ' ' + x[1:]
#         print(k)
#         k = k[:-3] + ' ' +  k[-3:]
#         lin.append(k)
#     else:
#         g = x[:-3] + ' ' +  x[-3:]
#         lin.append(g)
# print(lin)

def formate_salary(salary):
    salary_str = str(salary)
    if len(salary_str)> 6:
        res = salary_str[0] + ' ' +salary_str[1:]
        res = res[:-3] + ' ' + res[-3:]
    else: 
        res = salary_str[:-3] + ' ' + salary_str[-3:]
    return res

print(formate_salary(25000))