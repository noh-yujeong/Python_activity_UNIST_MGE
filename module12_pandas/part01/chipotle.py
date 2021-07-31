"""
The file chipotle_orders.csv contains data about orders at a branch of the world-famous text-mex chain "Chipotle".
Note that columns are separated by the "tab" character
"""

import pandas as pd
import matplotlib.pyplot as plt



"""
1) Import the data into a dataframe
"""
#df = pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv", sep = "\t")
df = pd.read_csv("chipotle_orders.csv", sep = "\t")
"""
1bis) The same data can be downloaded at 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
How could you load the data directly from the url?
"""


"""
2) Transform the values in the item_price column into a float.
Hint: the data are currently a string of the type "$<price>", so...
"""
for i in range(len(df.iloc[:, 4])):
    df.iloc[i, 4] = float(df.iloc[i, 4][1:])
"""
3) Filter the items that cost more than 10$ and assign them to a new dataframe (how many are these items?)
"""
df_n = df[df["item_price"] > 10]
print(df_n)

"""
4) Create a new dataframe containing only information about item_name and item_price of only items for which
 quantity is equal to 1, removing duplicates
"""
copy = pd.DataFrame.copy(df)
for i in range(len(copy.iloc[:, 0])):
    copy.iloc[i, 4] = round(copy.iloc[i, 4]/copy.iloc[i, 1], 2)
c = copy.loc[:, ["item_name", "item_price"]].copy()
c.drop_duplicates(inplace = True)
c.reset_index(drop = True, inplace = True)
print(c)

"""
5) Create a bar chart diagram using the data obtained in (4). Each bar should show the number of items
found in a certain price interval. Use intervals of 3$
(see chipotle_result.png for the expected result)
"""
x = [1.5, 4.5, 7.5, 10.5]
y = [0, 0, 0, 0]
for i in range(len(c)):
    if float(c["item_price"][i]) < 3:
        y[0] = y[0] + 1
    elif 3 <= float(c["item_price"][i]) < 6:
        y[1] = y[1] + 1
    elif 6 <= float(c["item_price"][i]) < 9:
        y[2] = y[2] + 1
    else:
        y[3] = y[3] + 1
plt.bar(x, y, width = 2)
plt.show()
