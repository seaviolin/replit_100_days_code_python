amount = float(input("What is our amount? "))
k = float(input ("What is the interest? "))
for year in range(10):
  amount += (k/100)*amount
  amount = round(amount, 2)
  print ("In the year", year+1,"you owe", amount)
  
  