a=5
b=10
#z=(a>4 and b>5) #true if both condition is true
#x=(a>1 or b>20)  #true, if the any condition is right
x=(not(a>1 or b>20)) #convart the true into false
print(x)