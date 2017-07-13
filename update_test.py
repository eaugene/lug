import csv
import collections
dic=collections.OrderedDict()
bll=collections.OrderedDict()
with open("list2.csv","r+") as fil:
    read_csv=csv.reader(fil)
    for row in read_csv:
        if(len(row)==4):
            dic[row[0]]=row[1:]
fil.close()
print("PRODUCT->   CATEGORY || PRICE || QUANTITY")
for v in dic.items():
    print(v[0]+"->  "+v[1][0]+"  ||  "+v[1][1]+"  ||   "+v[1][2])
print(len(dic))

print("Enter the names of product to add to bill list")

while True:
    up_d = input("Enter the name of item to update or EXIT to quit:")
    if up_d in dic.keys():
        while True:
            try:
                no = int(input("Enter the number of units to add"))
            except ValueError:
                print("Only numbers are allowed!!!")
                continue
            else:
                while True:
                    if (int(dic[up_d][2]) >= no and no>0):
                        dic[up_d][2] = str(int(dic[up_d][2]) - no)
                        bll[up_d] = list([dic[up_d][0], str(no), str(no * int(dic[up_d][1]))])
                        break
                    else:
                        print("Store has less Quantity than needed quantity!! or Give a positive quantity")
                        no=int(input("Try with less quantity"))
                        continue
                break
        continue
    elif (up_d == 'Exit' or up_d == 'exit'):
        break
    else:
        o = int(input("1-Try again 2-Continue"))
        if o == 1:
            continue
        else:
            break

##print("final "+str(len(dic)))
print("PRODUCT->   CATEGORY || PRICE || QUANTITY")
for v in dic.items():
    print(v[0]+"->  "+v[1][0]+"  ||  "+v[1][1]+"  ||   "+v[1][2])
with open('list2.csv', 'w') as u:
    writ = csv.writer(u)
    for v in dic.items():
        if (int(v[1][2])>0):
            writ.writerow([str(v[0]),str(v[1][0]),str(v[1][1]),str(v[1][2])])
        else:
            del dic[str(v[0])]
print("final "+str(len(dic)))
u.close()
print("Bill list")
print(bll)