# values = [None, 0, 0.0, '', [], {}, set(), 'False', 1, [0], True,'vikash']
# # for val in values:
# #     print(f"{repr(val)} is {val} => {type(val)} =>{bool(val)}")

# sample='';

# if(sample):
#     print("Have some value and its TRuth")
# else:
#     print("Do not have a value")



# a = [1, 2]
# b = a
# c = list(a)
# #c= [1,3]
# print(id(a), id(b), id(c))
# print(a is b)  # ref or values
# print(a == c)  #values are same
# print(c == b)  #values are same
# print(a is c)  

# print(c);
# print(a);
# print(b);


x = 10
def modify(val):
    global x 
    x+= 5
    val+=5
    return val

print(modify(x))  #15
print(x) #10        

