#Credit Card Statement Analysis with csv module and matplotlib
import csv
import matplotlib.pyplot as plt


new_dict = {}
with open('./files/cc_statement.csv') as sbi_csv:
    sbi_csv_dict = csv.reader(sbi_csv)
    for row in sbi_csv_dict:
        row = row[:2]
        if row[0] not in new_dict:
            new_dict[row[0]] = 0
        if row[1] == 'AMOUNT':
            continue
        new_dict[row[0]] += int(row[1])        

new_dict.pop("TRANSACTIONS")

_total = 0
for values in new_dict.values():
    _total+=values

key = list(new_dict.keys())
value1 = list(new_dict.values())

plt.figure(1)
plt.bar(key,value1)
plt.figure(2)
plt.pie(value1, labels=key)
plt.legend()
plt.show()