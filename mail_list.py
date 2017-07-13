import csv
import collections
dic=collections.OrderedDict()
with open("list2.csv","r+") as fil:
    read_csv=csv.reader(fil)
    for row in read_csv:
        if(len(row)==4):
            dic[row[0]]=row[1:]
class func:
    def add_item(self):
        pdt = input("enter prodeuct name")
        ctg = input("Enter the category of product")
        while True:
            try:
                price = int(input("Enter the price of a unit"))
            except ValueError:
                print("Only numbers are allowed!!!")
                continue
            else:
                break
        while True:
            try:
                no = int(input("Enter the number of units avilable"))
            except ValueError:
                print("Only numbers are allowed!!!")
                continue
            else:
                break
        dic[pdt] = list([ctg, str(price), str(no)])
        with open('list2.csv', 'w') as u:
            writ = csv.writer(u)
            for v in dic.items():
                writ.writerow([str(v[0]), str(v[1][0]), str(v[1][1]), str(v[1][2])])
        u.close()
    def update_item(self):
        for v in dic.items():
            print(v[0] + "->  " + v[1][0] + "  ||  " + v[1][1] + "  ||   " + v[1][2])
        while True:
            up_d = input("Enter the name of item to update :")
            if up_d in dic.keys():
                break
            else:
                o = int(input("1-Try again 2-Continue"))
                if o == 1:
                    continue
                else:
                    break
        while True:
            try:
                que = int(input("Enter 1-update price  2-quantity :"))
            except ValueError:
                print("Only numbers are allowed!!!")
                continue
            else:
                if que < 1 or que > 2:
                    print("enter a proper query!!!")
                    o = int(input("1-Try again 2-Continue"))
                    if o == 1:
                        continue
                    else:
                        break
                else:
                    break
        if (que == 1):
            while True:
                try:
                    pri = int(input("Enter the new price"))
                except ValueError:
                    print("Only numbers are allowed!!!")
                    continue
                else:
                    dic[up_d][1] = pri
                    break
        else:
            while True:
                try:
                    qut = int(input("Enter the new quantity of product"))
                except ValueError:
                    print("Only numbers are allowed!!!")
                    continue
                else:
                    dic[up_d][2] = qut
                    break
        with open('list2.csv', 'w') as u:
            writ = csv.writer(u)
            for v in dic.items():
                writ.writerow([str(v[0]), str(v[1][0]), str(v[1][1]), str(v[1][2])])
        u.close()
    def dis(self):
        while True:
            try:
                disopt = int(input("Enter 1-display all  2-search by name 3- search by category :"))
            except ValueError:
                print("Only numbers are allowed!!!")
                continue
            else:
                if disopt < 1 or disopt > 3:
                    print("OOPS!!!Enter a proper query!")
                    o = int(input("1-Try again 2-Continue"))
                    if o == 1:
                        continue
                    else:
                        break
                else:
                    break
        flag = 0
        if (disopt == 1):
            print("PRODUCT->   CATEGORY || PRICE || QUANTITY")
            for v in dic.items():
                print(v[0] +"->  "+v[1][0]+"  ||  "+v[1][1]+"  ||  "+v[1][2])
        elif (disopt == 2):
            while True:
                up_d = input("Enter the name of product to be searched")
                if up_d in dic.keys():
                    print(up_d+"->> "+dic[up_d][0]+"  ||  "+dic[up_d][1]+"  ||   "+dic[up_d][2])
                    break
                else:
                    print("OOPS!!Enter the correct name of product!!!")
                    o = int(input("1-Try again 2-Continue"))
                    if o == 1:
                        continue
                    else:
                        break
        elif(disopt==3):
            up_d = input("Enter the category to list products")
            for v in dic.items():
                if up_d==v[1][0]:
                    print(v[0] + "->  " + v[1][0] + "  ||  " + v[1][1] + "  ||   " + v[1][2])
        else:
            print("Thanks For a Try")
    def del_list(self):
        print("PRODUCT->   CATEGORY || PRICE || QUANTITY")
        for v in dic.items():
            print(v[0] + "->  " + v[1][0] + "  ||  " + v[1][1] + "  ||   " + v[1][2])
        while True:
            pdt = input("enter prodeuct name")
            if pdt in dic.keys():
                print(pdt + " is deleted")
                del dic[pdt]
                with open('list2.csv', 'w') as u:
                    writ = csv.writer(u)
                    for v in dic.items():
                        writ.writerow([str(v[0]), str(v[1][0]), str(v[1][1]), str(v[1][2])])
                u.close()
                break
            else:
                print("Invalid Product")
                o = int(input("1-Try again 2-Continue"))
                if o == 1:
                    continue
                else:
                    print("Thanks For a Try!!")
                    break




while True:
    try:
        opt = int(input("Enter 1-add item 2- update details 3-display and search 4-delete item"))
    except ValueError:
        print("Only numbers are allowed!!!")
        continue
    else:
        break

er=func()
if(opt==1):
    er.add_item()
elif(opt==2):
    er.update_item()
elif(opt==3):
    er.dis()
elif(opt==4):
    er.del_list()
else:
    print("Invalid")
print("End")
