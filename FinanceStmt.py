#data
#data downloaded from superdatascience.com/python
revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]

#calculate profit (revenue - expenses)
profit = list([])
for i in range(len(revenue)):
    profit.append(revenue[i] - expenses[i])
print("Profit\n", profit)

#calculate tax (profit * 30%)
tax = [round(i*0.3, 2) for i in profit]
print("Tax\n", tax)

#profit after tax
profit_after_Tax = list([])
for i in range(len(profit)):
    profit_after_Tax.append(profit[i] - tax[i])
print("profit after tax\n", profit_after_Tax)

#profit margin after tax (profit after tax divided by revenue)
profit_margin = list([])
for i in range(len(profit)):
    profit_margin.append(profit_after_Tax[i] / revenue[i])
profit_margin = [round((i*100), 2) for i in profit_margin]
print("prift margin\n", profit_margin)

#profit after tax mean
mean_pat = sum(profit_after_Tax) / len(profit_after_Tax)
print("Mean profit after tax",mean_pat)

#good months (profit_after_tax > mean_pat)
good_months = list([])
for i in range(len(profit_after_Tax)):
    good_months.append(profit_after_Tax[i] > mean_pat)
print("Good months\n", good_months)

#bad months (profit_after_tax < mean_pat)
bad_months = list([])
for i in range(len(profit_after_Tax)):
    bad_months.append(profit_after_Tax[i] < mean_pat)
print("bad months\n", bad_months)

#Best month
best_month = list([])
for i in range(len(profit)):
    best_month.append(profit_after_Tax[i] == max(profit_after_Tax))
print("best month\n",best_month)

#Worst month
worst_month = list([])
for i in range(len(profit)):
    worst_month.append(profit_after_Tax[i] == min(profit_after_Tax))
print("worst month\n",worst_month)
    

