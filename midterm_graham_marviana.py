import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import random



#------------------#
#    Question 1    #
#------------------#

##Test list
testlist_q1 = []
for x in range(1000):
    testlist_q1.append(random.randint(0,10))

##Open and read the file, replace newline with "," and split the string by ",". Then append each blob of text into given as an integer
a_q1 = open("numbers.txt", "r")
b_q1 = ((a_q1.read()).replace("\n", ",")).split(",")
given_q1 = []
for n in b_q1:
    given_q1.append(int(n))
a_q1.close()

##Creates an *unordered* dictionary from a list of numbers to show the frequency
def sortt(inp):
    dicti = {}
    for x in inp:
        if x in dicti:
            dicti[x] += 1
        else:
            dicti[x] = 1
    return dicti

##Uses a dictionary to create an ASCII histogram
def texthist(inpdict):
    keyl = sorted(inpdict.keys())
    for x in keyl:
        s = str(x) + ": "
        for y in range(inpdict[x]):
            s += "x"
        print(s)
#texthist(sortt(given_q1)) #!!!!uncomment me

##Uses a list (array) to create a matplotlib histogram
def mplhist(inplist):
    plt.hist(np.array(inplist))
    plt.show()
    plt.close()
#mplhist(given_q1) #!!!!uncomment me

##Saves a dictionary into a json file
def savedictintojson(inpdict):
    n = open("dict.json", "w")
    n.write(str(inpdict))
    n.close()
    print("Done!")
    
#savedictintojson(sortt(given_q1)) #!!!!uncomment me


#------------------#
#    Question 2    #
#------------------#

a_q2 = open("amazon-orders.csv", "r")
b_q2 = (a_q2.read()).split("\n")
a_q2.close()
months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
    
#Creates a "master dictionary" with the first line as the key and the rest of the lines as the values
def mastdict():
    mastd = {}
    for x in (b_q2[0]).split(","):
        mastd[x] = []
    for x in b_q2[1:]:
        n = 0
        for y in (x.split(",")):
            mastd[(b_q2[0]).split(",")[n]].append(y)
            n += 1
    return mastd

mdict = mastdict()

#Creates a dictionary of the months and their indices so that we have an easier time making monthly summaries

def datedict():
    n = 0
    d = {}
    for x in mdict["Shipment Date"]:
        if int((x.split("/"))[0]) in d:
            d[int((x.split("/"))[0])].append(n)
        else:
            d[int((x.split("/"))[0])] = [n]
        n += 1
    return d

ddict = datedict()

#Creates a pie chart

def makepie(lisval, lislabels):
    y = np.array(lisval)
    plt.pie(y, labels = lislabels)
    plt.show()
    plt.close()

#Pie chart for spending per month, plus avg per month and standard deviation
def run1():
    a = [] #total per month
    b = [] #month (for label)
    d = [] #each transaction
    totalspent = 0
    for x in list(ddict.keys()):
        c = 0
        for y in ddict[x]:
            c += float(((mdict["Total Charged"])[y])[1:])
            d.append(float(((mdict["Total Charged"])[y])[1:]))
        a.append(c)
        totalspent += c
        b.append(months[x])
    n = 0
    for y in b:
        nofpurchases =  len(ddict[list(ddict.keys())[n]]) #len(ddict[list(months.keys())[(list(months.values())).index(y)]])
        print("Money Spent in", b[n], ": ", round(a[n], 2), "(", round(100 * a[n] / totalspent, 3), "%) over", nofpurchases, "purchases. Average cost: $", round(a[n] / nofpurchases, 2))
        n += 1
    print("Mean price: $", round(totalspent / len(d), 2), "| Median price: $", np.median(np.array(d)), "| Standard deviation of price: $", round(np.std(np.array(d)), 4))
    print("Max price: $", max(d), "| Min price: $", min(d))
    makepie(a, b)

#run1() #!!!!uncomment me

#Bar graph for spending by carrier
#def run2():
    #