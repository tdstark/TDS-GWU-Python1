import os
import pandas as pd

csvpath = os.path.join('Resources', 'budget_data.csv')
budgetdata = pd.read_csv(csvpath)
budgetdata["Change"] = 0

for x in range(budgetdata.shape[0]):
    if x == 0:
        budgetdata.iloc[x,2] = 0   #First row gets assigned a zero because there's no change
    else:
        budgetdata.iloc[x, 2] = budgetdata.iloc[x, 1] - budgetdata.iloc[x-1, 1]

averageChange = budgetdata["Change"].sum() / (budgetdata.shape[0] - 1) #Subtract 1 because of the header
greatInc = budgetdata.loc[budgetdata["Change"] == budgetdata["Change"].max()]
greatLoss = budgetdata.loc[budgetdata["Change"] == budgetdata["Change"].min()]

totalMonthsText = f"Total Months: {len(budgetdata['Date'].unique())}"
totalAmountText = f"Total: ${round(budgetdata['Profit/Losses'].sum())}"
averageChangeText = f"Average Change: ${round(averageChange,2)}"
greatIncText = f"Greatest Increase In Profits: {greatInc.iloc[0,0]}  (${greatInc.iloc[0,2]})"
greatLossText = f"Greatest Decrease In Profits: {greatLoss.iloc[0,0]}  (${greatLoss.iloc[0,2]})"

print("Financial Analysis")
print("----------------------------------------------------")
print(totalMonthsText)
print(totalAmountText)
print(averageChangeText)
print(greatIncText)
print(greatLossText)

outputpath = os.path.join('analysis', 'bank_data.txt')

with open(outputpath, 'w') as txtfile:
    txtfile.write("Financial Analysis \n")
    txtfile.write("---------------------------------------------------- \n")
    txtfile.write(totalMonthsText + " \n")
    txtfile.write(totalAmountText + " \n")
    txtfile.write(averageChangeText + " \n")
    txtfile.write(greatIncText + " \n")
    txtfile.write(greatLossText + " \n")


