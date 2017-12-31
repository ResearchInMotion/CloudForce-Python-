SellingPrice=int(input("please enter the number "))
CostPrice=int(input("please enter the number "))
Profit=SellingPrice-CostPrice

if(SellingPrice>CostPrice):
    print("profit")
    Profit = SellingPrice - CostPrice
    print("The profit is of ",Profit)

else:
    print("loss")
    Loss=CostPrice-SellingPrice
    print("The loss is of ",Loss)

