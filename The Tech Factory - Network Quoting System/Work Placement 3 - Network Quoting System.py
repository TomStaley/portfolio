########################
#Network Quoting System#
########################
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Label
import re
from tkinter.messagebox import showerror, showwarning, showinfo, askyesno


##############
#Backend Code#
##############

##
#database management
##
class database():

    items2 = []
    userList = []

    def __init__(self):
        self.items2 = []
        self.userList = []
        #open database here
        database = open("quoting_system_data.txt", "r")
        self.items = database.readline()
        self.users = database.readline()
        database.close()
        self.itemLine = self.items
        self.userLine = self.users
        self.items = self.items.split("__")
        for a in self.items:
            a = a.split(",")
            print(a)
            self.items2.append(a)

        self.users = self.users.split("__")
        for b in self.users:
            b = b.split(",")
            self.userList.append(b)        
        #seperate based on "__", then based on ","
        self.items2.remove(['\n'])
        self.userList.remove(['\n'])
        #remove "\n" because it wacks up the program
        
    def callItem(self):
        return self.items2
        #returns all items and prices
    
    def callUser(self):
        return self.userList
        #returns list of users, passwords, and types

class editData(database):
    newItemList = ""
    
    def __init__(self):
        database.__init__()
    
    def saveData(self, line1, line2):
        self.fullData = [line1, line2]
        print(self.fullData)
        databaseWrite = open("quoting_system_data.txt", "w")
        databaseWrite.writelines(self.fullData)
        databaseWrite.close()
        editData.__init__(database)

    def formatData(self, dataList):

        
        dataList = str(dataList).replace("'], ['", "__")
        dataList = str(dataList).replace("[['", "")
        dataList = str(dataList).replace("']]", "__")
        dataList = str(dataList).replace("', '", ",")
        dataList = dataList + '\n'
        print("FORMATTED DATA")
        print(dataList)
        
        return dataList

    def addItem(self, itemName, itemPrice):

        for z in itemName:
            if z == ("_" or "," or "[" or "]" or "'" or " "):
                print("ERROR: item name CANNOT contain spaces or any of the following characters: , [ ] _ '")
                showerror(title='Error', message="Item name CANNOT contain spaces or any of the following characters:  ,  [  ]  _  '")
                return
                
        
        itemList = database.callItem()
        for i in itemList:
            if i[0] == itemName:
                print("ERROR: item is already in database!")
                showerror(title='Error', message="Item is already in database!")
                return
    
        itemPrice = "{:.2f}".format(float(itemPrice))
        newItem = str(itemName) + "," + str(itemPrice) + "__"
        print("NEW ITEM:")
        print(newItem)
        newItemList = newItem + self.itemLine
        print("")
        print("NEW ITEM LIST")
        print(newItemList)

        editData.saveData(editData, newItemList, self.userLine)

        return
    def delItem(self, itemName):
        items = database.callItem()

        print("DELETED ITEM:")
        print(itemName)
        print("IS THE ITEM IN THE LIST?")
        for c in items:
            if c[0] == itemName:
                print("True")
                print(c)
                items.remove(c)
            else:
                print("")

        print("NEW ITEM LIST:")
        print(items)

        newItemList = editData.formatData(editData, items)
        editData.saveData(editData, newItemList, self.userLine)

        return
    def editItem(self, itemName, newPrice):
        newItemData = itemName + "," + newPrice + "__"
        print("NEW ITEM DATA:")
        print(newItemData)
        print("CALLING DELETE ITEM FUNCTION...")
        editData.delItem(database, itemName)
        print("UPDATING ITEM LIST...")
        database.__init__()
        print("CALLING ADD ITEM FUNCTION...")
        editData.addItem(database, itemName, newPrice)
        return
    
    def addUser(self, userType, username, password):


            
        if ("_" or "," or "[" or "]" or "'" or " " or "'") in username:

            print("ERROR: username CANNOT contain spaces or any of the following characters: , [ ] _")
            showerror(title='Error', message="Username CANNOT contain spaces or any of the following characters:  ,  [  ]  _  ")
                
            return

        if ("_" or "," or "[" or "]" or "'" or " " or "'") in password:

            print("ERROR: password CANNOT contain spaces or any of the following characters: , [ ] _ '")
            showerror(title='Error', message="Password CANNOT contain spaces or any of the following characters:  ,  [  ]  _  ")
            return
            
        userList = database.callUser()

        for j in userList:
            if j[1] == username:
                print("ERROR: that username already exists!")
                showerror(title='Error', message="That username already exists!")
                return
        if str(userType) != "employee":
            if str(userType) != "customer":
                print(str(userType))
                print("ERROR: invalid user type!")
                showerror(title='Error', message="Invalid user type!")
                return

        newUserData = str(userType) + "," + str(username) + "," + str(password) + "__"
        
        print("NEW USER DATA:")
        print(newUserData)
        newUserData = newUserData + self.userLine
        editData.saveData(editData, self.itemLine, newUserData)
        

        return

    def delUser(self, username, password):
        users = database.callUser()
        if len(users) == 1:
            print("ERROR: there is only 1 user left!")
            showerror(title='Error', message="You can't delete the final user!")
            return
        print("IS THE USER IN THE LIST? ")
        for d in users:
            
            if d[1] == username:
                print("True")
                print(d)
                print("DOES THE PASSWORD FIT?")
                if d[2] == password:
                    print("TRUE")
                    users.remove(d)
                    newUserList = editData.formatData(editData, users)
                    editData.saveData(editData, self.itemLine, newUserList)
                    print("NEW USER LIST:")
                    print(users)
                    return
                else:
                    showerror(title='Error', message="Incorrect password!")
                    return
        showerror(title='Error', message="User not in database!")

        

        
        return



#NOTES:
        
##call item (item name, price)(for when item information is displayed) (DONE)
##call user (username, password, userType) (for when userdata is required) (DONE)

##add Item (item, price)(for adding items) (DONE)
##del Item (item) (for deleting items) (DONE)
##edit Item (item, price) (for editing item prices) (DONE)
#format data () (done)

##addUser (username, password, userType) (DONE)
##delUser (username, password) (deleteing users) (DON'T DELETE LAST EMPLOYEE USER) (DONE)



#(DONE?????????)
#IMPORTANT!!!
#make sure that database is initiated after every action, so that the data is updated
#also check if initiating a class just makes a new one



##
#login system
##

class loginSys():
    
    userType = ""
    username = ""
    password = ""

    

    def logMeIn(self, username, password):
        loginSys.loginCheck(self, username, password)
        if self.passCheck == False:
            return
        print("Welcome " + self.username + ", your role is " + self.userType)



        #send user to view
        if self.userType == "employee":
            #ASK EMPLOYEE WHICH VIEW THEY WANT TO SEE
            answer = askyesno("Access customer view?", "As an employee, you can choose to view the customer view or continue to the employee view. Would you like to open the customer view?")
            if answer:
                print("customer view")
                app.destroy()
                customerClass = customerUI()
                
            elif not answer:
                print("employee view")
                app.destroy()
                employeeClass = employeeUI()
                
            return
        
        elif self.userType == "customer":
            #CREATE CUSTOMER INTERFACE
            print("customer view")
            app.destroy()
            customerClass = customerUI()
            return
        
        else:
            print("ERROR: '" + self.userType + "' is an invalid user type!")
            showerror("ERROR: INVALID USER TYPE", "Can't log in because user type is invalid! either log in with a different user or ask tech support for help")
            
    
    def loginCheck(self, tempUsername, tempPassword):
        users = database.callUser()
        print("IS THE USER IN THE LIST?")
        for e in users:
            if e[1] == tempUsername:
                print("True")
                print("DOES THE PASSWORD FIT?")
                if e[2] == tempPassword:
                    print("True")
                    self.userType = e[0]
                    self.username = tempUsername
                    self.password = tempPassword
                    self.passCheck = True
                    return
        showerror("ERROR: INVALID USERNAME OR PASSWORD", "Can't log in because either the username or password is invalid!")
        self.passCheck = False
        return

        

class customerView():
    def customerDialog(self, userType, username, password):
        print("")
        userCart = cart(userType, username, password)
        choice = input("What do you want to do? (1: add item, 2: del item (cart), 3:VAT, 4: Install cost, 5:totalcost, 6:show item list, 7:checkout)  ")
        if choice == "1":
            itemInput = input("what is the item to be added (name)? ")
            quantityInput = input("How many should be added?")
            userCart.addToList(itemInput, quantityInput)
            print("Total list:")
            print(userCart.itemList)
            return
        elif choice == "2":
            itemDel = input("What Item do you want to delete? ")
            userCart.delFromList(itemDel)
            print("Total list:")
            print(userCart.itemList)
            
            return
        elif choice == "3":
            userCart.VAT()
            print("")
            return
        elif choice == "4":
            userCart.installCost()
            print("")
            return
        elif choice == "5":
            userCart.calcPrice()
            return
        elif choice == "6":
            userCart.checkList()
            return
        elif choice == "7":
            userCart.checkout()
            exit()
            

class cart(customerView):
    userType = ""
    username = ""
    password = ""
    itemList = []
    totalPrice = [0.00]
    VATa = ["False"]
    
    install = ["False"]
    def __init__(self, userType, username, password):
        self.userType = userType
        self.username = username
        self.password = password

        

    def addToList(self, itemName, quantity):
        print("")
        itemList = database.callItem()
        for h in itemList:
            if h[0] == itemName:
        
                tempList = []
                tempList.extend([str(itemName)] * int(quantity))
                self.itemList.extend(tempList)

                self.calcPrice()
                return
                
        print("ERROR: item not in database!")
        showerror(title='Error', message="Item not in database!")
        return

    def delFromList(self, item):

        for f in self.itemList:
            if f == item:

                self.itemList.remove(item)
                break # makes sure only one gets deleted
            else:
                continue

        self.calcPrice()
        return
    
    def VAT(self):
        #I have to use annoying if statements here because booleans are immutable data types
        if self.VATa == ["False"]:
            self.VATa.remove("False")
            self.VATa.append("True")
        elif self.VATa == ["True"]:
            self.VATa.remove("True")
            self.VATa.append("False")
        print("")
        print("INFO: VAT increases the price by 20%")
        print("")
        print("VAT set to:")
        print(self.VATa)

        self.calcPrice()
        #I have no idea how vat works, so I'm just treating it as a 20% price markup

        return
    def installCost(self):
        if self.install == ["False"]:
            self.install.remove("False")
            self.install.append("True")
        elif self.install == ["True"]:
            self.install.remove("True")
            self.install.append("False")
        print("")
        print("INFO: Install costs increase the price by 55%")
        print("")
        print("installation costs set to:")
        print(self.install)
        self.calcPrice()

        return
    def checkList(self):
        print(self.itemList)
        return self.itemList
    def calcPrice(self):
        print("")

        tempPrice = 0.0
        tempVAT = 0.0
        tempInstall = 0.0
        storedData = database.callItem()
        for g in self.itemList:
            for h in storedData:
                if g == h[0]:
                    tempPrice += float(h[1])

        if self.VATa == ["True"]:
            tempVAT = tempPrice * 0.2
        if self.install == ["True"]:
            tempInstall = tempPrice * 0.55

        tempPrice = tempPrice + tempVAT + tempInstall
        tempPrice = "{:.2f}".format(tempPrice)
        self.totalPrice.remove(self.totalPrice[0])
        self.totalPrice.append(tempPrice)
        print("")
        print("TOTAL PRICE:")
        print(self.totalPrice)
        print("")
        

        return 
    
    def checkout(self):
        print("")
        print("")
        print("")
        print("PURCHASED ITEMS:")
        print(self.itemList)
        print("")
        print("TOTAL COST:")
        print(self.totalPrice)
        print("")
        print("VAT:")
        print(self.VATa)
        print("")
        print("Installation Cost Included?")
        print(self.install)
        print("")
        print("THANK YOU FOR VISITING THE TECH FACTORY, HAVE A NICE DAY!")
        exit()


class employeeView():
    
    def employeeDialog(self,userType, username, password):
        print("")
        emChoice = input("What do you want to do? (1: add item type, 2: remove item type, 3: change item price, 4:add new user, 5: remove user, 6: view all items and users) ")
        if emChoice == "1":
            print("")
            testaddItem = input("What item should be added? ")
            testaddPrice = input("what is does it cost (£00.00)? ")
            editData.addItem(database, testaddItem, testaddPrice)
        
        elif emChoice == "2":
            print("")
            testDelItem = input("What is the name of the item to be deleted? ")
            editData.delItem(database, testDelItem)
        
        elif emChoice == "3":
            print("")
            testEditItem = input("Which item do you want to edit? ")
            testEditPrice = input("What should the new price be? ")
            editData.editItem(database, testEditItem, testEditPrice)
        
        elif emChoice == "4":
            print("")
            newUserType = input("What type of user are you creating? ")
            newUser = input("What is the new username? ")
            newPass = input("What is the new password? ")
            editData.addUser(database, newUserType, newUser, newPass)
        
        elif emChoice == "5":
            print("")
            testDelUser = input("What user are you deleting (username)? ")
            testDelPass = input("What is the user's password? ")
            editData.delUser(database, testDelUser, testDelPass)
        
        elif emChoice == "6":
            print("")
            print("Calling items list...")
            print(database.callItem())
            print("")
            print("Calling user list...")
            print(database.callUser())






######
#CREATE OBJECTS
######



database = database()
print("")
login = loginSys()

######
#TESTER CODE
######
#use this to test the backend without the front end


###############
#Frontend Code#
###############

class App(tk.Tk):
    
    def __init__(self):
        super().__init__()

        self.ttfLogo = tk.PhotoImage(file='./assets/TTF_LOGO_SMALL.png')
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=20)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        
        
        self.title("The Tech Factory Quoting System")
        self.iconbitmap("./assets/TTF_ICON.ico")
        self.resizable(False, False)

        #titleText
        titleText = ttk.Label(self, image=self.ttfLogo)#
        titleText.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
        
        #login button
        loginButton = ttk.Button(self, text="Login", command=lambda: login.logMeIn(userInput.get(), passInput.get()))
        loginButton.grid(row=4, column=2, sticky="e", padx=5, pady=5)

        #userText
        userText = ttk.Label(self, text="Username:", font=('Malgun Gothic', 11))
        userText.grid(row=2, column=1, sticky="e", padx=5, pady=5)
        
        #passText
        passText = ttk.Label(self, text="Password:", font=('Malgun Gothic', 11))
        passText.grid(row=3, column=1, sticky="e", padx=5, pady=5)
        
        #userInput
        userInput = tk.StringVar(self)
        userBox = ttk.Entry(self, textvariable=userInput)
        userBox.grid(row=2, column=2, sticky="eW", padx=5, pady=5)
        userBox.focus()
        
        #passInput
        passInput = tk.StringVar(self)
        passBox = ttk.Entry(self, textvariable=passInput, show="*")
        passBox.grid(row=3, column=2, sticky="eW", padx=5, pady=5)
        

        


class customerUI(tk.Tk):

    totalPrice = "£0.00"
    
    def __init__(self):
        super().__init__()

        userCart = cart("", "", "")
        self.title("The Tech Factory Quoting System - Customer Screen")
        self.iconbitmap("./assets/TTF_ICON.ico")
        self.resizable(False, False)
        window_width = 900
        window_height = 600
        screen_width = self.winfo_screenwidth() 
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        



        
        #self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=8)
        self.columnconfigure(2, weight=1)
        #self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        #self.rowconfigure(1, weight=1)
        #self.rowconfigure(2, weight=2)
        self.rowconfigure(3, weight=2)
        self.rowconfigure(4, weight=2)
        #self.rowconfigure(5, weight=1)

        #catalogText
        catalogText = ttk.Label(self, text="Item Catalog", font=('Malgun Gothic', 11))
        catalogText.grid(row=0, column=1, sticky="W", padx=5, pady=5)
        
        #catalogBox
        self.catalogData = ["a", "b", "c"]
        list_catalog = tk.StringVar(self, value=self.catalogData)
        catalogBox = tk.Listbox(self, listvariable= list_catalog, height=30, selectmode='standard')
        
        scrollbar1 = ttk.Scrollbar(self,orient='vertical',command=catalogBox.yview) #creates and links scrollbar
        scrollbar1.grid(row=1, rowspan=4, column=0, sticky="ns",padx=5,pady=5)
        
        catalogBox.grid(row=1,rowspan=4,column=1,sticky='news',padx=5,pady=5)
        catalogBox['yscrollcommand'] = scrollbar1.set
        
        #cartText
        cartText = ttk.Label(self, text="Cart", font=('Malgun Gothic', 11))
        cartText.grid(row=0, column=4, sticky="W", padx=5, pady=5)
        
        #cartBox
        self.cartData = ["1", "2", "3"]
        list_cart = tk.StringVar(self, value=self.cartData)
        cartBox = tk.Listbox(self, listvariable= list_cart, height=30, selectmode='extended')
        
        scrollbar2 = ttk.Scrollbar(self,orient='vertical',command=cartBox.yview) #creates and links scrollbar
        scrollbar2.grid(row=1, rowspan=4, column=3, sticky="ns",padx=5,pady=5)
        
        cartBox.grid(row=1,rowspan=4,column=4,sticky='news',padx=5,pady=5)
        cartBox['yscrollcommand'] = scrollbar2.set

        #priceText
        self.textPrice = tk.StringVar(self, value=self.totalPrice)
        priceText = ttk.Label(self, textvariable=self.textPrice, font=('Malgun Gothic', 14)) 
        priceText.grid(row=7, column=4, sticky="E", padx=10, pady=5)

        
        def updateInfo():
            print("updating lists")
            #catalogBox
            tempList = database.callItem()
            tempList2 = []
            for k in tempList:
                tempList2.extend([str(k[0]) + " - £" + str(k[1])])
            self.catalogData = (tempList2)
            list_catalog.set(self.catalogData)
            
            #cartBox
            tempList3 = userCart.checkList()
            tempList4 = []
            tempList5 = []
            
            for n in tempList3:
                itemCount = tempList3.count(n)
                itemCount2 = tempList5.count(n)
                
                if itemCount2 != 1:
                    tempList5.extend([n])
                    for l in tempList:
                        if l[0] == n:
                            tempList4.extend([str(itemCount) + "  -" + str(l[0]) + "- £" + str(l[1])])
                    
                    
            print(tempList5)

            self.catalogData = (tempList4)
            list_cart.set(self.catalogData)
            
            #priceText
            print(userCart.totalPrice)
            self.totalPrice = ("£" + str("{:.2f}".format(float(userCart.totalPrice[0]))))
            print(self.totalPrice)
            self.textPrice.set(self.totalPrice)

        def getCatalogSelect():
            selected = []
            selectIndices = catalogBox.curselection()
            tempList = database.callItem()
            for i in selectIndices:
                selected.append(tempList[i])
            return(selected[0][0])
            
        def delFromCart():
            selectIndices = cartBox.curselection()
            tempCart = userCart.checkList()
            tempdata = database.callItem()
            for i in selectIndices:
                i #the current focal item, includes £ and quantity
                selectedItem = cartBox.get(i).strip(" £1234567890.").strip("-")
                quantity = ""
                for j in cartBox.get(i):
                    if j.isnumeric() == True:
                        quantity = quantity + j
                    else: break
                print((selectedItem) * int(quantity))
                for _ in range(int(quantity)):
                    userCart.delFromList(selectedItem)


        #addItemB
        addItemB = ttk.Button(self, text="ADD TO CART", command=lambda: (userCart.addToList(getCatalogSelect(), int(itemPrice.get())), updateInfo()))
        addItemB.grid(row=3, column=2, sticky="news", padx=10, pady=10)


        #quantityText
        quantityText = ttk.Label(self, text="Quantity To Add:", font=('Malgun Gothic', 11))
        quantityText.grid(row=1, column=2, sticky="w", padx=10, pady=5)
        
        #quantityEntry
        itemPrice = tk.StringVar(self)
        quantityEntry =ttk.Entry(self, textvariable=itemPrice)
        quantityEntry.grid(row=2, column=2, sticky="we", padx=10, pady=5)
        itemPrice.set(1)

        #delItemB
        delItemB = ttk.Button(self, text="REMOVE FROM CART", command=lambda: (delFromCart(),  updateInfo()  ))
        delItemB.grid(row=4, column=2, sticky="news", padx=10, pady=10)
        
        #VATCheck
        VATvar = tk.StringVar(self)
        VATCheck = ttk.Checkbutton(self, command=lambda: (userCart.VAT(), updateInfo()), text="Include VAT (20% markup)", variable=VATvar, onvalue='included', offvalue='unincluded')
        VATCheck.grid(row=5, column=4, sticky="w", padx=5, pady=5)

        #installCheck
        installVar = tk.StringVar(self)
        installCheck = ttk.Checkbutton(self, command=lambda: (userCart.installCost(), updateInfo()), text="Include Installation Costs (55% markup)", variable=installVar, onvalue='included', offvalue='unincluded')
        installCheck.grid(row=6, column=4, sticky="w", padx=5, pady=5)

        #checkoutB
        delItemB = ttk.Button(self, text="CHECKOUT", command=lambda: checkout())
        delItemB.grid(row=8, column=4, sticky="NE", padx=10, pady=10, ipady=10)

        #bigLogo
        self.ttfLogo2 = tk.PhotoImage(file='./assets/TTF_LOGO.png')
        self.ttfLogoS = tk.PhotoImage(file='./assets/TTF_LOGO_SMALL.png')
        bigLogo = ttk.Label(self, image=self.ttfLogo2)
        bigLogo.grid(row=5 , rowspan=4, column=0, columnspan=4, padx=5, pady=5)

        
        updateInfo()

        def checkout():
            checkoutUI = tk.Toplevel()
            checkoutUI.title("Checkout Information")
            checkoutUI.iconbitmap("./assets/TTF_ICON.ico")
            checkoutUI.resizable(False, False)
            checkoutUI.grid_columnconfigure(5, weight=1)
            checkoutUI.grid_rowconfigure(1, weight=3)
            checkoutUI.grid_rowconfigure(2, weight=1)
            checkoutUI.grid_rowconfigure(3, weight=1)
            checkoutUI.grid_rowconfigure(4, weight=1)
            checkoutUI.grid_rowconfigure(5, weight=1)
            items = []
            itemsTemp = userCart.checkList()
            storedData = database.callItem()
            for g in itemsTemp:
                for h in storedData:
                    if g == h[0]:
                        items.extend(["£" + str(h[1]) + " " + str(g)])
            print(items)
            
            #title
            title = ttk.Label(checkoutUI, text="Thank you for visiting The Tech Factory", font=('Malgun Gothic', 14))
            title.grid(row=2, column=3, columnspan=3, padx=5,pady=5,sticky="n")
            
            #checkoutList
            self.checkoutCart = items
            list_checkout = tk.StringVar(checkoutUI, value=self.checkoutCart)
            checkoutBox = tk.Listbox(checkoutUI, listvariable= list_checkout, height=15, selectmode='extended')
        
            scrollbar3 = ttk.Scrollbar(checkoutUI,orient='vertical',command=checkoutBox.yview) #creates and links scrollbar
            scrollbar3.grid(row=1, rowspan=7, column=2, sticky="ns", pady=5)
        
            checkoutBox.grid(row=1,rowspan=7,column=1,sticky='news',padx=5,pady=5)
            checkoutBox['yscrollcommand'] = scrollbar3.set
            
            #checkoutVAT
            checkoutUI.VATvar2 = tk.StringVar()
            checkoutVAT = ttk.Label(checkoutUI, textvariable=checkoutUI.VATvar2, font=('Malgun Gothic', 9))#
            checkoutVAT.grid(row=4, column=3, columnspan=3, padx=5,pady=5,sticky="SE")
            checkoutUI.VATvar2.set("VAT is unincluded")
            checkoutUI.VATvar2.set("VAT is " + ("unincluded" if VATvar.get() == "" else VATvar.get()))
            #checkoutInstall
            checkoutUI.installVar2 = tk.StringVar()            
            checkoutInstall = ttk.Label(checkoutUI, textvariable=checkoutUI.installVar2, font=('Malgun Gothic', 9))
            checkoutInstall.grid(row=5, column=3, columnspan=3, padx=5,pady=5,sticky="SE")
            checkoutUI.installVar2.set("Installation costs are unincluded")
            print("HERE:",installVar.get())
            checkoutUI.installVar2.set("Installation costs are " + ("unincluded" if installVar.get() == "" else installVar.get()))
            #checkoutTotal
            checkoutUI.totalPrice = tk.StringVar()
            checkoutTotal = ttk.Label(checkoutUI, textvariable=checkoutUI.totalPrice, font=('Malgun Gothic', 14))
            checkoutTotal.grid(row=6, column=3, columnspan=3, padx=5,pady=5,sticky="e")
            checkoutUI.totalPrice.set("The total cost is: " + self.textPrice.get())

            #checkoutImg
            checkoutImg = ttk.Label(checkoutUI, image=self.ttfLogoS)
            checkoutImg.grid(row=1, column=3, columnspan=3, padx=5, pady=5)            
            
            
            #confirmB
            confirmB = ttk.Button(checkoutUI, text="Exit", command=lambda: (checkoutUI.destroy(), self.destroy(), userCart.checkout()))
            confirmB.grid(row=7,column=5, sticky="ES", padx=5, pady=5)
            #cancelB
            cancelB = ttk.Button(checkoutUI, text="Cancel", command=lambda: checkoutUI.destroy())
            cancelB.grid(row=7,column=4, sticky="WS", padx=5, pady=5)
            
        

class employeeUI(tk.Tk):
    itemListData = []
    def __init__(self):
        super().__init__()
        self.ttfLogo3 = tk.PhotoImage(file='./assets/TTF_LOGO.png')
        self.title("The Tech Factory Quoting System - Employee Screen")
        self.iconbitmap("./assets/TTF_ICON.ico")
        self.resizable(False, False)
        window_width = 900
        window_height = 600
        screen_width = self.winfo_screenwidth() 
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        
        #itemList

        self.itemListData = []
        list_item = tk.StringVar(self, value=self.itemListData)
        print(self.itemListData)
        itemListUI = tk.Listbox(self, listvariable=list_item, height=20, selectmode='extended')
        print(self.itemListData)
        
        
        scrollbar = ttk.Scrollbar(self,orient='vertical',command=itemListUI.yview) #creates and links scrollbar
        scrollbar.grid(row=2, column=0, sticky="ns",padx=5,pady=5)
        
        itemListUI.grid(row=2,column=1,columnspan=5,sticky='news',padx=5,pady=5)
        itemListUI['yscrollcommand'] = scrollbar.set
        
        def updateList():
            tempList = database.callItem()
            tempList2 = []
            for k in tempList:
                tempList2.extend([str(k[0]) + " - £" + str(k[1])])
            self.itemListData = (tempList2)
            list_item.set(self.itemListData)
        updateList()
        def getSelection(): 
            selected = []
            selectIndices = itemListUI.curselection()
            tempList = database.callItem()
            for i in selectIndices:
                selected.append(tempList[i])
            print(selected)
            return(selected)
        

        def addItem():
            addItemUI = tk.Tk()
            addItemUI.title("Add Item")
            addItemUI.iconbitmap("./assets/TTF_ICON.ico")
            addItemUI.resizable(False, False)
            #title
            title = ttk.Label(addItemUI, text="Add Item", font=('Malgun Gothic', 11))
            title.grid(row=0, column=1, columnspan=2, sticky="W", padx=5, pady=5)
            #itemNameText
            itemNameText = ttk.Label(addItemUI, text="Item name:", font=('Malgun Gothic', 10))
            itemNameText.grid(row=1, column=1, sticky="W", padx=5, pady=5)
            #itemNameEntry
            itemName = tk.StringVar(addItemUI)
            itemNameEntry = ttk.Entry(addItemUI, textvariable=itemName)
            itemNameEntry.grid(row=1,column=2, sticky="W", padx=5, pady=5)
            #itemPriceText
            itemPriceText = ttk.Label(addItemUI, text="Item price:", font=('Malgun Gothic', 10))
            itemPriceText.grid(row=2, column=1, sticky="W", padx=5, pady=5)
            #itemPriceEntry
            itemPrice = tk.StringVar(addItemUI)
            itemPriceEntry =ttk.Entry(addItemUI, textvariable=itemPrice)
            itemPriceEntry.grid(row=2,column=2, sticky="W", padx=5, pady=5)
            #confirmB
            confirmB = ttk.Button(addItemUI, text="Confirm", command=lambda: (editData.addItem(database, itemName.get(), itemPrice.get()), addItemUI.destroy(), updateList()))
            confirmB.grid(row=3,column=2, sticky="E", padx=5, pady=5)
            #cancelB
            cancelB = ttk.Button(addItemUI, text="Cancel", command=lambda: addItemUI.destroy())
            cancelB.grid(row=3,column=1, sticky="W", padx=5, pady=5)
            
        def delItem():
            selected = getSelection()
            print(selected)
            for i in selected:
                editData.delItem(database, i[0])
            updateList()
            
        def editItem():

            editItemUI = tk.Tk()
            editItemUI.title("Edit Price")
            editItemUI.iconbitmap("./assets/TTF_ICON.ico")
            editItemUI.resizable(False, False)
            #title
            title = ttk.Label(editItemUI, text="Edit Price", font=('Malgun Gothic', 11))
            title.grid(row=0, column=1, columnspan=2, sticky="W", padx=5, pady=5)
            #editItemText
            editItemText = ttk.Label(editItemUI, text="Item name:", font=('Malgun Gothic', 10))
            editItemText.grid(row=1, column=1, sticky="W", padx=5, pady=5)
            #editPriceText
            editPriceText = ttk.Label(editItemUI, text="New price:", font=('Malgun Gothic', 10))
            editPriceText.grid(row=2, column=1, sticky="W", padx=5, pady=5)
            #editItemEntry
            editItemName = tk.StringVar(editItemUI)
            editItemEntry = ttk.Entry(editItemUI, textvariable=editItemName)
            editItemEntry.grid(row=1,column=2, sticky="W", padx=5, pady=5)
            #editPriceEntry
            editItemPrice = tk.StringVar(editItemUI)
            editPriceEntry =ttk.Entry(editItemUI, textvariable=editItemPrice)
            editPriceEntry.grid(row=2,column=2, sticky="W", padx=5, pady=5)
            #cancelB
            cancelB = ttk.Button(editItemUI, text="Cancel", command=lambda: editItemUI.destroy())
            cancelB.grid(row=3,column=1, sticky="W", padx=5, pady=5)
            #confirmB
            confirmB = ttk.Button(editItemUI, text="Confirm", command=lambda: (editData.editItem(database, editItemName.get(), editItemPrice.get()), editItemUI.destroy(), updateList()))
            confirmB.grid(row=3,column=2, sticky="E", padx=5, pady=5)

            
        def addUser():
            addUserUI = tk.Tk()
            addUserUI.title("Add New User")
            addUserUI.iconbitmap("./assets/TTF_ICON.ico")
            addUserUI.resizable(False, False)

            #title
            title = ttk.Label(addUserUI, text="Add new user", font=('Malgun Gothic', 11))
            title.grid(row=0, column=1, columnspan=2, sticky="W", padx=5, pady=5)
            #userTypeText
            userTypeText = ttk.Label(addUserUI, text="User type:", font=('Malgun Gothic', 10))
            userTypeText.grid(row=1, column=1, sticky="W", padx=5, pady=5)
            #usernameText
            usernameText = ttk.Label(addUserUI, text="Username:", font=('Malgun Gothic', 10))
            usernameText.grid(row=2, column=1, sticky="W", padx=5, pady=5)
            #passwordText
            passwordText = ttk.Label(addUserUI, text="Password:", font=('Malgun Gothic', 10))
            passwordText.grid(row=3, column=1, sticky="W", padx=5, pady=5)
            #userTypeEntry 
            userType = tk.StringVar(addUserUI)
            userTypeEntry = ttk.Combobox(addUserUI, textvariable=userType)
            userTypeEntry['state'] = 'readonly'
            userTypeEntry['values'] = ('customer', 'employee')
            userTypeEntry.grid(row=1,column=2, sticky="W", padx=5, pady=5)
            #usernameEntry
            newUser = tk.StringVar(addUserUI)
            usernameEntry = ttk.Entry(addUserUI, textvariable=newUser)
            usernameEntry.grid(row=2,column=2, sticky="W", padx=5, pady=5)            
            #passwordEntry
            newPass = tk.StringVar(addUserUI)
            passwordEntry = ttk.Entry(addUserUI, textvariable=newPass)
            passwordEntry.grid(row=3,column=2, sticky="W", padx=5, pady=5) 
            #confirmB
            confirmB = ttk.Button(addUserUI, text="Confirm", command=lambda: (editData.addUser(database, userType.get(), newUser.get(), newPass.get()), addUserUI.destroy(), updateList()))
            confirmB.grid(row=4,column=2, sticky="E", padx=5, pady=5)
            #cancelB
            cancelB = ttk.Button(addUserUI, text="Cancel", command=lambda: addUserUI.destroy())
            cancelB.grid(row=4,column=1, sticky="W", padx=5, pady=5)
            
        
        def delUser():
            delUserUI = tk.Tk()
            delUserUI.title("Delete User")
            delUserUI.iconbitmap("./assets/TTF_ICON.ico")
            delUserUI.resizable(False, False)
            #title
            title = ttk.Label(delUserUI, text="Delete user", font=('Malgun Gothic', 11))
            title.grid(row=0, column=1, columnspan=2, sticky="W", padx=5, pady=5)
            #usernameText
            usernameText = ttk.Label(delUserUI, text="Username:", font=('Malgun Gothic', 10))
            usernameText.grid(row=1, column=1, sticky="W", padx=5, pady=5)
            #passwordText
            passwordText = ttk.Label(delUserUI, text="Password:", font=('Malgun Gothic', 10))
            passwordText.grid(row=2, column=1, sticky="W", padx=5, pady=5)
            #usernameEntry
            delUsername = tk.StringVar(delUserUI)
            usernameEntry = ttk.Entry(delUserUI, textvariable=delUsername)
            usernameEntry.grid(row=1,column=2, sticky="W", padx=5, pady=5)   
            #passwordEntry
            delPassword = tk.StringVar(delUserUI)
            passwordEntry = ttk.Entry(delUserUI, textvariable=delPassword)
            passwordEntry.grid(row=2,column=2, sticky="W", padx=5, pady=5) 
            #confirmB
            confirmB = ttk.Button(delUserUI, text="Confirm", command=lambda: (editData.delUser(database, delUsername.get(), delPassword.get()), delUserUI.destroy(), updateList()))
            confirmB.grid(row=3,column=2, sticky="E", padx=5, pady=5)
            #cancelB
            cancelB = ttk.Button(delUserUI, text="Cancel", command=lambda: delUserUI.destroy())
            cancelB.grid(row=3,column=1, sticky="W", padx=5, pady=5)
            
            
        #ItemLabel
        #addItemB
        addItemB = ttk.Button(self, text="ADD ITEM", command=lambda: addItem())
        addItemB.grid(row=1, column=1, sticky="news", padx=10, pady=10)
        #delItemB
        delItemB = ttk.Button(self, text="DELETE ITEMS", command=lambda: delItem())
        delItemB.grid(row=1, column=2, sticky="news", padx=10, pady=10)
        #editItemB
        editItemB = ttk.Button(self, text="EDIT PRICE", command=lambda: editItem())
        editItemB.grid(row=1, column=3, sticky="news", padx=10, pady=10)
        #addUserB
        addUserB = ttk.Button(self, text="ADD USER", command=lambda: addUser())
        addUserB.grid(row=1, column=4, sticky="news", padx=10, pady=10)
        #delUserB
        delUserB = ttk.Button(self, text="DELETE USER", command=lambda: delUser())
        delUserB.grid(row=1, column=5, sticky="news", padx=10, pady=10)

        #employeeLogo
        employeeLogo = ttk.Label(self, image=self.ttfLogo3)
        employeeLogo.grid(row=3, columnspan=6, sticky="n", column=0, padx=5, pady=5) 
        


#PROBLEM WITH STRINGVAR:
            #make sure that list is instead self.list
            #define list as class property





#1) login screen popup (DONE)
    #employee choice as a popup - stop interactions outside of login windows


#2) customer view (DONE)
    #display items and prices on the left side
    #display cart items and prices on the right
    #in the middle, display add, remove, and quantity elements - quantity is a textbox. limit input to int
    #under cart display, show total price as text, and a checkout button that shows checkout info in a popup
    #VAT and installation costs are also under cart display, before checkout and total prices. They are checkboxes

#3) employee view (DONE)
    #display item and price lists in the middle, not user lists
    #buttons along the top - add new item, del item, change item price - all are popups with relevent input fields
    #also along the top - add user, delete user. for added security, limit to input fields rather than selectable choices - allso popups




if __name__ == "__main__":
    app = App()
    app.mainloop()

