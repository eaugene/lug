import csv
item=0
with open("list.csv","r+") as fil:
    read_csv=csv.reader(fil)
    for row in read_csv:
        if(len(row)==5):
            item=item+1
fil.close()
class func:
    def add_item(self):
        item = 0
        with open("list.csv", "r+") as fil:
            read_csv = csv.reader(fil)
            for row in read_csv:
                if (len(row) == 5):
                    item = item + 1
        fil.close()
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
        item = item + 1
        with open("list.csv", "a") as fil:
            write_csv = csv.writer(fil)
            write_csv.writerow([item, pdt, ctg, price, no])
        fil.close()
    def update_item(self):
        item = 0
        with open("list.csv", "r+") as fil:
            read_csv = csv.reader(fil)
            for row in read_csv:
                if (len(row) == 5):
                    item = item + 1
                    print(row[0] + "-> " + row[1] + "|" + row[2] + "|" + row[3] + "|" + row[4])
        fil.close()

        while True:
            try:
                up = int(input('Enter item number'))
            except ValueError:
                print("Only numbers are allowed!!!")
                continue
            else:
                if up < 1 or up > item:
                    print("Item id can't be found")
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
                    continue
                else:
                    break
        item = 0
        r = csv.reader(open('list.csv', 'r'))
        lines = []
        for l in r:
            if (len(l) == 5):
                lines.append(l)
        if (que == 1):
            while True:
                try:
                    pri = int(input("Enter the new price"))
                except ValueError:
                    print("Only numbers are allowed!!!")
                    continue
                else:
                    lines[up - 1][3] = pri
                    break
        else:
            while True:
                try:
                    qut = int(input("Enter the new quantity of product"))
                except ValueError:
                    print("Only numbers are allowed!!!")
                    continue
                else:
                    lines[up - 1][4] = qut
                    break
        writ = csv.writer(open('list.csv', 'w'))
        writ.writerows(lines)
    def dis(self):
        r = csv.reader(open('list.csv', 'r'))
        lines = []
        for l in r:
            if (len(l) == 5):
                lines.append(l)

        while True:
            try:
                disopt = int(input("Enter 1-display all  2-search by name 3- search by category :"))
            except ValueError:
                print("Only numbers are allowed!!!")
                continue
            else:
                if disopt < 1 or disopt > 3:
                    print("enter a proper query!!!")
                    continue
                else:
                    break
        flag = 0
        if (disopt == 1):
            print("S.no -> Name | Category | Price | Avbl")
            for i in lines:
                print(i[0] + "->    " + i[1] + " | " + i[2] + " | " + i[3] + " | " + i[4])
        elif (disopt == 2):
            nme = input("Enter the name of product to be searched")
            for i in lines:
                if (nme == i[1]):
                    print(i[0] + "->    " + i[1] + " Ctg: " + i[2] + " Rs.:" + i[3] + " Avbl.:" + i[4])
                    flag = 1
                    break
            if (flag == 0):
                print(nme + " Can't be found")
        else:
            nme = input("Enter the category to list products")
            for i in lines:
                if (nme == i[2]):
                    print(i[0] + "->    " + i[1] + " Ctg: " + i[2] + " Rs.:" + i[3] + " Avbl.:" + i[4])
                    flag = 1
            if (flag == 0):
                print(nme + " Can't be found")


while True:
    try:
        opt = int(input("Enter 1-add item 2- update details 3-display and search"))
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
else:
    print("Invalid")
print("End")
