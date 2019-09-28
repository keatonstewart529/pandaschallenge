### Note
* Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
"Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
pymoi = pd.read_csv("Resources/purchase_data.csv")
pymoi.head()

## Player Count

* Display the total number of players


plcnt = pymoi["SN"].nunique()
plcnt

## Purchasing Analysis (Total)

* Run basic calculations to obtain number of unique items, average price, etc.


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame


itcnt = pymoi["Item ID"].nunique()
sam = pymoi["Price"].sum()
men = sam / len(pymoi["Price"])
lst = [itcnt, men, len(pymoi), sam]
print(lst)

lstnm=["itemcount","mean","ordercount","sum"]

pd.DataFrame(lst,lstnm)

sumtbl = pd.DataFrame({"itemcount":[itcnt],"mean":[men],"ordercount":[len(pymoi)],"sum":[sam]})
sumtbl

## Gender Demographics

* Percentage and Count of Male Players


* Percentage and Count of Female Players


* Percentage and Count of Other / Non-Disclosed




rawplydmg = pymoi.loc[:, ["Gender","Age","SN"]]
plydmg = rawplydmg.drop_duplicates()
len(plydmg)

plydmg

gndcnt = plydmg["Gender"].value_counts()
gndpct = gndcnt / plcnt

## Purchasing Analysis (Gender)

* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender




* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame

gndsam = pymoi.groupby(["Gender"]).sum()["Price"].rename("sum")
gndmen = pymoi.groupby(["Gender"]).mean()["Price"].rename("mean")
gndpchs = pymoi.groupby(["Gender"]).count()["Price"].rename("pchs")
gndpchsps = gndsam / gndcnt
pd.DataFrame([gndpchs, gndmen, gndsam, gndpchsps.rename("bill")],).transpose().round(2)

## Age Demographics

* Establish bins for ages


* Categorize the existing players using the age bins. Hint: use pd.cut()


* Calculate the numbers and percentages by age group


* Create a summary data frame to hold the results


* Optional: round the percentage column to two decimal points


* Display Age Demographics Table


plydmg["Age"]
agbinlim = [0,9.9,14.9,19.9,24.9,29.9,34.9,39.9,45.9]
agbinam = [" <10","10-15","15-20","20-25","25-30","30-35","35-40","40-45"]
plydmg["pup"] = pd.cut(plydmg["Age"], agbinlim, labels = agbinam)
plyct2 = plydmg["pup"].value_counts()
pup2 = pd.DataFrame(plyct2)
pup2

## Purchasing Analysis (Age)

* Bin the purchase_data data frame by age


* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame

pymoi["pupo"] = pd.cut(pymoi["Age"], agbinlim, labels = agbinam)

agsam = pymoi.groupby(pymoi["pupo"]).sum()["Price"].rename("sum")
agmen = pymoi.groupby(pymoi["pupo"]).mean()["Price"].rename("mean")
agpchs = pymoi.groupby(pymoi["pupo"]).count()["Price"].rename("pchs")
agpchsps = agsam / pup2['pup']
pd.DataFrame([agpchs, agmen, agsam, agpchsps.rename("bill")],).transpose().sort_index().round(2)

## Top Spenders

* Run basic calculations to obtain the results in the table below


* Create a summary data frame to hold the results


* Sort the total purchase value column in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the summary data frame



#pymoi.groupby(["SN"])

pymsam = pymoi.groupby(pymoi["SN"]).sum()["Price"].rename("sum")
pymmen = pymoi.groupby(pymoi["SN"]).mean()["Price"].rename("mean")
pympchs = pymoi.groupby(pymoi["SN"]).count()["Price"].rename("pchs")
pd.DataFrame([pympchs, pymmen, pymsam],).transpose().sort_values("sum", ascending=False).round(2)

## Most Popular Items

* Retrieve the Item ID, Item Name, and Item Price columns


* Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value


* Create a summary data frame to hold the results


* Sort the purchase count column in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the summary data frame



itm = pymoi.loc[:,["Item ID","Item Name","Price"]]
itmcnt = itm.groupby(["Item ID","Item Name"]).count()["Price"].rename("cnt")
itmsum = itm.groupby(["Item ID","Item Name"]).sum()["Price"].rename("sales")
itmpc = itm.groupby(["Item ID","Item Name"]).mean()["Price"].rename("price")
itmdf = pd.DataFrame([itmcnt,itmsum,itmpc],).transpose()
itmdf.sort_values("sales", ascending = False).head()

## Most Profitable Items

* Sort the above table by total purchase value in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the data frame



itmdf.sort_values("cnt",ascending = False).head()