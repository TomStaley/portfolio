import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Label
import re
from tkinter.messagebox import showerror, showwarning, showinfo

#-------------------------------------------------------------
#----------------------------MENUs----------------------------
#-------------------------------------------------------------

class App(tk.Tk):#create backround GUI enviroment
    def __init__(self):
        super().__init__()


        self.grid_columnconfigure(1, weight=1)#create a grid, for positioning
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        
        style = ttk.Style(self)
        style.configure('TButton', font=('Malgun Gothic', 20), background="grey", anchor=tk.CENTER)#edits the style of buttons
        
        self.title('Door Management System')#sets window title
        window_width = 900 #defines window size
        window_height = 600 #defines window size

        screen_width = self.winfo_screenwidth() #finds the screen width
        screen_height = self.winfo_screenheight() #finds the screen height
        center_x = int(screen_width/2 - window_width / 2) #finds the center of the screen
        center_y = int(screen_height/2 - window_height / 2) #finds the center of the screen
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')#defines the window size

        self.resizable(False, False) #disables resizing the window
        
        self.iconbitmap('./assets/WCG_Logo.ico')#adds the wcg logo

        self.frames = {}
        for F in (MainMenu, SubMenu, StudIdMenu, GroupIdMenu, DemoUI):#creates a list of menus
            window = F.__name__
            frame = F(parent=self ,container=self)
            self.frames[window] = frame
            frame.grid(row=2, column=2, sticky="nsew")
        
        self.Window("MainMenu") #sets main menu as default
        
    def Window(self, window):
        frame = self.frames[window]#sets current menu to requested menu
        frame.tkraise()#show current menu


        
 

class MainMenu(ttk.Frame):#creates a frame for the main menu content
    def __init__(self, parent, container):
        super().__init__(container)

        mainTitle = ttk.Label(self, text="520CIT - Tom Staley", font=('Malgun Gothic', 20))#just text
        mainTitle2 = ttk.Label(self, text="Door Management System", font=('Malgun Gothic', 40))

        buttonStart = ttk.Button(self, text="Start", command=lambda: App.Window(app, "SubMenu"))#creates buttons
        buttonDemo = ttk.Button(self, text="Demonstration Mode", command=lambda: App.Window(app, "DemoUI"))#creates buttons

    
        mainTitle.pack(ipady=80)#basic formating of elements - padding, organisation
        mainTitle2.pack()
        buttonStart.pack(
            ipadx=50,
            ipady=10,
            pady=100,
            expand=True,
            side='left')
        buttonDemo.pack(
            ipadx=10,
            ipady=10,
            pady=100,
            expand=True,
            side='right')



class SubMenu(ttk.Frame):#creates a frame for the sub menu content
    def __init__(self, parent, container):
        super().__init__(container)


        
        header = ttk.Frame(self, height=10)#creates a frame for header elements
        
        body = ttk.Frame(self)#creates a frame for body elements

        self.studentImage = tk.PhotoImage(file='./assets/Student.png') # icons
        self.groupImage = tk.PhotoImage(file='./assets/Group.png')
                
        buttonBack = ttk.Button(header, text="Back", command=lambda: App.Window(app, "MainMenu"))#creates buttons
        buttonStud = ttk.Button(body, text="Student Manager", image=self.studentImage, compound='top', command=lambda: App.Window(app, "StudIdMenu"))
        ButtonGroup = ttk.Button(body, text="Classroom Manager", image=self.groupImage, compound="top", command=lambda: App.Window(app, "GroupIdMenu"))
        
        spacer = ttk.Label(header, text="", font=('Malgun Gothic', 20))#just text


        header.pack(side="top")
        buttonBack.pack(side='left')
        spacer.pack(ipady=20, padx=300, side='right')
        
        body.pack()
        buttonStud.pack(side='left', ipadx=5, ipady=5, expand=True)
        ButtonGroup.pack(side='right', ipadx=5, ipady=5, expand=True)
        
        


class StudIdMenu(ttk.Frame): #The menu that manages IDS
    def __init__(self, parent, container):
        super().__init__(container)


        
        #header
        header = ttk.Frame(self, height=10)#creates a frame for header elements
        spacer = ttk.Label(header, text="", font=('Malgun Gothic', 20))#just text
        buttonBack = ttk.Button(header, text="Back", command=lambda: App.Window(app, "SubMenu"))#creates buttons
        buttonAdd = ttk.Button(header, text="Add New Id", command=lambda: newIdUI(self, 0))
        buttonRemove = ttk.Button(header, text="Remove Ids", command=lambda: removeIdUI(self, 0))

        #mainbody
        body = ttk.Frame(self, borderwidth=5, relief='sunken', padding=0, height=500, width=810)#creates a frame for body elements

        #listbox/scrollbar
        idListUI = (idDB.retrieveData("id", 0))
        list_id = tk.StringVar(value=idListUI)
        studentList = tk.Listbox(body, listvariable=list_id, height=30, selectmode='extended') ##!!!!!!USE LIST BOX!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        scrollbar = ttk.Scrollbar(body,orient='vertical',command=studentList.yview) #creates and links scrollbar
        scrollbar.pack(side="right", fill="both")

        #header
        header.pack(side="top")
        buttonBack.pack(side='left')
        buttonAdd.pack(side='right')
        buttonRemove.pack(side='right')
        spacer.pack(ipady=20, padx=125, side='right')

        #mainbody
        body.pack(fill="both",expand=True)
        studentList.pack(fill="both", expand=True)
        studentList['yscrollcommand'] = scrollbar.set

        
            
       #add ID button 
        def newIdUI(self, idList): #creates a window for adding IDs

            #window creation
            idADD = tk.Tk()
            idADD.title("New ID")
            idADD.resizable(False, False) #disables resizing the window
            idADD.iconbitmap('./assets/WCG_Logo.ico')#adds the wcg logo
            idADD.attributes('-topmost', 1) #puts the window at the top of the window order
            idADD.columnconfigure(0, weight=1)#configure grids
            idADD.columnconfigure(1, weight=0)
            idADD.columnconfigure(2, weight=3)

            #elements
            text = tk.StringVar(idADD)
            
            
            idLable = ttk.Label(idADD, text="New ID:")
            idEntry = ttk.Entry(idADD, textvariable=text)
            idInfo = ttk.Label(idADD, text="To enter multiple IDs, sperate each ID with a single space", justify="right")
            
            idLable.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
            idEntry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
            idInfo.grid(column=0, row=1, padx=5, pady=5, columnspan=2)

            
            
            addClose = ttk.Button(idADD, text="Close", command=lambda: idADD.destroy()) #buttons
            addConfirm = ttk.Button(idADD, text="Confirm", command=lambda: updateIDListADD(idADD))
            addClose.grid(column=0, row=2, sticky="W", padx=5, pady=5)
            addConfirm.grid(column=1, row=2, sticky="E", padx=5, pady=5)

            #updates list from the ID add window
            def updateIDListADD(window):
                idRegister.registerNewID(text.get())
                idListUI = (idDB.retrieveData("id", 0))
                list_id.set(idListUI)
                window.destroy()
                
        #remove ID button
        def removeIdUI(self, idList): #creates a window for removing IDs

            #window creation
            idREMOVE = tk.Tk()
            idREMOVE.title("Remove ID")
            idREMOVE.resizable(False, False) #disables resizing the window
            idREMOVE.iconbitmap('./assets/WCG_Logo.ico')#adds the wcg logo
            idREMOVE.attributes('-topmost', 1) #puts the window at the top of the window order

            #grid
            idREMOVE.columnconfigure(0, weight=1)#configure grids
            idREMOVE.columnconfigure(1, weight=0)
            idREMOVE.columnconfigure(2, weight=3)

            #elements
            removeLABEL = ttk.Label(idREMOVE, text="WARNING: Clicking 'Confirm' will remove selected IDs, do you wish to continue?", justify="center")
            removeLABEL.grid(column=0, row=1, padx=10, pady=25, columnspan=2)

            selectedIDs = studentList.curselection()
            # get selected items
            selectedIDs2= ", ".join([studentList.get(i) for i in selectedIDs])
            
            removeConfirm = ttk.Button(idREMOVE, text="Confirm", command=lambda: updateIDListDEL(idREMOVE))######################################################place link to relevent class here!!!!!!!!##############
            removeClose = ttk.Button(idREMOVE, text="Close", command=lambda: idREMOVE.destroy()) #buttons
            removeConfirm.grid(column=1, row=2, sticky="E", padx=5, pady=5)
            removeClose.grid(column=0, row=2, sticky="W", padx=5, pady=5)
            
            #updates list from the ID remove window
            def updateIDListDEL(window):
                idRegister.deleteID(selectedIDs2)
                idListUI = (idDB.retrieveData("id", 0))
                list_id.set(idListUI)
                window.destroy()

                
#group manager menu      
class GroupIdMenu(ttk.Frame):
    groupStr = ""
    
    def __init__(self, parent, container):
        super().__init__(container)

        groupVar = tk.StringVar(value=self.groupStr)
        
        
        #images
        self.arrowL = tk.PhotoImage(file='./assets/arrow_left.png')
        self.arrowR = tk.PhotoImage(file='./assets/arrow_right.png')
        self.bookButton = tk.PhotoImage(file='./assets/book_button.png')
        
        #header
        header = ttk.Frame(self, height=10)#creates a frame for header elements
        buttonBack = ttk.Button(header, text="Back", command=lambda: App.Window(app, "SubMenu"))#creates buttons
        spacer = ttk.Label(header, text="", font=('Malgun Gothic', 20))#just text
        changeGroup = ttk.Button(header, text="Change Group", command=lambda: editGroupUI(self, 0))

        #mainbody
        body = ttk.Frame(self)#creates a frame for body elements
        leftBod = ttk.Frame(body, borderwidth=5, relief='sunken', padding=0, height=500, width=350)
        rightBod = ttk.Frame(body, borderwidth=5, relief='sunken', padding=0, height=500, width=350)
        midBod = ttk.Frame(body, height=500, width=100)
        arrowLeft = ttk.Button(midBod, image=self.arrowL, command=lambda: groupIDRemove(self))#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#!!!!!!!!!######################
        arrowRight = ttk.Button(midBod, image=self.arrowR,command=lambda: groupIDAdd(self))#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#!!!!!!!!!######################)
        bookButton = ttk.Button(midBod, image=self.bookButton, command=lambda: bookGroupUI(self, self.groupStr))
        studLabel = ttk.Label(leftBod, text="All IDs", font=('Malgun Gothic', 10))
        groupLabel = ttk.Label(rightBod, textvariable=groupVar, font=('Malgun Gothic', 10))

        
        def updateGroupLists():
            groupList1 = (idDB.retrieveData("groupIDs", self.groupStr))
            list_test3.set(groupList1)
            idListUI2 = (idDB.retrieveData("id", 0))
            list_test2.set(idListUI2)
            
        #listboxs/scrollbars 
        idListUI2 = (idDB.retrieveData("id", 0))
        groupList1 = (idDB.retrieveData("groupIDs", self.groupStr))
        list_test2 = tk.StringVar(value=idListUI2)
        list_test3 = tk.StringVar(self, value=groupList1)
        listbox2 = tk.Listbox(leftBod, listvariable=list_test2, selectmode="extended", height=30) 
        listbox3 = tk.Listbox(rightBod, listvariable=list_test3, selectmode="extended", height=30)
        scrollbar2 = ttk.Scrollbar(leftBod,orient='vertical',command=listbox2.yview) #creates and links scrollbar
        scrollbar3 = ttk.Scrollbar(rightBod,orient='vertical',command=listbox3.yview) #creates and links scrollbar
        scrollbar2.pack(side="right", fill="y")
        scrollbar3.pack(side="right", fill="y")

        #header
        header.pack(side="top")
        buttonBack.pack(side='left')
        spacer.pack(ipady=20, side='left', fill="x", expand=True) #padx=300 
        changeGroup.pack(side='right')

        #mainbody
        body.pack(fill="both", expand=True)
        leftBod.pack(side='left',fill="both", expand=True)
        midBod.pack(side='left', fill='y')
        arrowLeft.pack(fill='x', expand=False)
        arrowRight.pack(fill='x', expand=False)
        bookButton.pack(fill='x', expand=False)
        rightBod.pack(side='right',fill="both", expand=True)
        studLabel.pack()
        groupLabel.pack()

        listbox2.pack(fill="both", expand=True)
        listbox3.pack(fill="both", expand=True)

        listbox2['yscrollcommand'] = scrollbar2.set
        listbox3['yscrollcommand'] = scrollbar3.set
        
        #gathers selected ids to be added
        def groupIDAdd(self):
            selected_IDs = []
            selected = listbox2.curselection()
            selected_IDs.extend([listbox2.get(i) for i in selected])
            GroupRegister.editGroup(self.groupStr, selected_IDs, "add")
            updateGroupLists()

        #gathers selected ids to be removed
        def groupIDRemove(self):
            selected_IDs = []
            selected = listbox3.curselection()
            selected_IDs.extend([listbox3.get(i) for i in selected])
            GroupRegister.editGroup(self.groupStr, selected_IDs, "remove")
            updateGroupLists()
        
        
        #edit group menu
        def editGroupUI(self, groupID):
            
            #window creation
            idGROUP = tk.Tk()
            idGROUP.title("Change Group")
            idGROUP.resizable(False, False) #disables resizing the window
            idGROUP.iconbitmap('./assets/WCG_Logo.ico')#adds the wcg logo
            idGROUP.attributes('-topmost', 1) #puts the window at the top of the window order

            #grid
            idGROUP.columnconfigure(0, weight=1)#configure grids
            idGROUP.columnconfigure(1, weight=0)
            idGROUP.columnconfigure(2, weight=3)
            idGROUP.rowconfigure(0, weight=1)
            idGROUP.rowconfigure(1, weight=1)
            idGROUP.rowconfigure(2, weight=1)
            idGROUP.rowconfigure(3, weight=1)
            idGROUP.rowconfigure(4, weight=1)

            #group select
            ##listbox
            groupsUI = (idDB.retrieveData("groupNames", 0))
            groupStr = tk.StringVar(idGROUP, value=groupsUI)
            groupList = tk.Listbox(idGROUP, listvariable=groupStr, height=10)
            
            
            def groupchange(self):
                
                group1 = groupList.curselection()
                group2 = ",".join([groupList.get(i) for i in group1])
                
                self.groupStr = str(group2)
                groupVar.set(self.groupStr)
                groupList1 = (idDB.retrieveData("groupIDs", self.groupStr))
                list_test3.set(groupList1)
                idGROUP.destroy()
                
            
            ##scrollbar
            scrollbar4 = ttk.Scrollbar(idGROUP,orient='vertical',command=groupList.yview) #creates and links scrollbar
            scrollbar4.grid(column=1, row=0,sticky="E", padx=5, pady=5)
            
            #group add/remove
            ##entry form (groupname textbox)
            newGroup1 = tk.StringVar(idGROUP)
            
            def getGroupName():
                newGroup = newGroup1.get()
                GroupRegister.registerNewGroup(newGroup)
                
                updateGroupBox()
                
            def removeGroup(self):
                group1 = groupList.curselection()
                group2 = ",".join([groupList.get(i) for i in group1])

                GroupRegister.deleteGroup(group2)
                groupsUI = (idDB.retrieveData("groupNames", 0))
                updateGroupBox()

            def updateGroupBox():
                groupsUI = (idDB.retrieveData("groupNames", 0))
                groupStr.set(groupsUI)
                newGroup1.set("")   
                
            groupText = ttk.Entry(idGROUP, textvariable=newGroup1)

            ##add button (add group using groupname, check if entry is valid)
            groupAdd = ttk.Button(idGROUP, text="Add New Group", command=lambda: getGroupName())
            ##remove button (remove selected)
            groupRemove = ttk.Button(idGROUP, text="Remove Selected Group", command=lambda: removeGroup(self))
            
            #elements
            groupText.grid(column=0, row=1, columnspan=2)
            groupAdd.grid(column=0, row=2, columnspan=2)
            groupRemove.grid(column=0, row=3, columnspan=2)
            removeConfirm = ttk.Button(idGROUP, text="Confirm", command=lambda: groupchange(GroupIdMenu))
            removeClose = ttk.Button(idGROUP, text="Close", command=lambda: idGROUP.destroy()) #buttons
            removeConfirm.grid(column=1, row=4, sticky="E", padx=5, pady=5)
            removeClose.grid(column=0, row=4, sticky="W", padx=5, pady=5)
            
            groupList.grid(column=0, row=0, columnspan=2, padx=5, pady=5)
            groupList['yscrollcommand'] = scrollbar4.set

        #book Group menu
        def bookGroupUI(self, groupID):

            #window creation
            idBOOK = tk.Tk()
            idBOOK.title("Book Room")
            idBOOK.resizable(False, False) #disables resizing the window
            idBOOK.iconbitmap('./assets/WCG_Logo.ico')#adds the wcg logo
            idBOOK.attributes('-topmost', 1) #puts the window at the top of the window order

            #grid
            idBOOK.columnconfigure(0, weight=1)#configure grids
            idBOOK.columnconfigure(1, weight=0)
            idBOOK.columnconfigure(2, weight=3)

            BookText = ttk.Label(idBOOK, text="Book Room for Selected Group", font=('Malgun Gothic', 10))#just text
            BookText2 = ttk.Label(idBOOK, text="Time Start", font=('Malgun Gothic', 10))
            BookText3 = ttk.Label(idBOOK, text="Time End", font=('Malgun Gothic', 10))
            BookText4 = ttk.Label(idBOOK, text="Classroom", font=('Malgun Gothic', 10))
            BookText.grid(column=0, row=0, sticky="W", padx=5, pady=5)
            BookText2.grid(column=0, row=1, sticky="W", padx=5, pady=5)
            BookText3.grid(column=0, row=2, sticky="W", padx=5, pady=5)
            BookText4.grid(column=0, row=3, sticky="W", padx=5, pady=5)



            #time period (between x and y times)
            startTime = tk.StringVar(idBOOK)
            BookStart = ttk.Entry(idBOOK, textvariable=startTime) #begining of booked period
            
            endTime = tk.StringVar(idBOOK)
            BookEnd = ttk.Entry(idBOOK, textvariable=endTime) #end of booked period
            
            #classroom
            classroom = tk.StringVar(idBOOK)
            BookClass = ttk.Entry(idBOOK, textvariable=classroom)
            
            
            #elements
            BookStart.grid(column=1, row=1, sticky="W", padx=5, pady=5)
            BookEnd.grid(column=1, row=2, sticky="W", padx=5, pady=5)
            BookClass.grid(column=1, row=3, sticky="W", padx=5, pady=5)
            BookConfirm = ttk.Button(idBOOK, text="Confirm", command=lambda: bookConfirm(groupID, startTime.get(), endTime.get(), classroom.get()))
            BookClose = ttk.Button(idBOOK, text="Close", command=lambda: idBOOK.destroy()) #buttons
            BookConfirm.grid(column=1, row=4, sticky="E", padx=5, pady=5)
            BookClose.grid(column=0, row=4, sticky="W", padx=5, pady=5)

            def bookConfirm(GroupName, timeStart, timeEnd, room):

                if GroupName == "":
                    showerror(title='Error', message='Please choose a group before booking')
                    idBOOK.destroy()
                elif timeValid(timeStart) == False or timeEnd == False:
                    showerror(title='Error', message='Please input a valid time (00:00)')
                else:
                    idBOOK.destroy()
                    showinfo(title='Room Booked', message=("The room " + room + " has been booked for " + GroupName + " between " + timeStart + " and " + timeEnd))
                    GroupRegister.bookClassroom(GroupName, timeStart, timeEnd, room)
                

            
class DemoUI(ttk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)
        #header
        header = ttk.Frame(self, height=10)#creates a frame for header elements
        spacer = ttk.Label(header, text="", font=('Malgun Gothic', 20))#just text
        buttonBack = ttk.Button(header, text="Back", command=lambda: App.Window(app, "MainMenu"))#creates buttons
        
        #mainbody
        body = ttk.Frame(self)
        title = ttk.Label(body, text="Demonstration Mode", font=('Malgun Gothic', 40))
        subtitle = ttk.Label(body, text='Click "Config" to begin', font=('Malgun Gothic', 20))
        startTest = ttk.Button(body, text='Start Test', command=lambda: demoModule.startDemo())
        config = ttk.Button(body, text='Config', command=lambda: DemoUI.configPanel())
        
        #header
        header.pack(side="top")
        buttonBack.pack(side='left')
        spacer.pack(ipady=20, padx=300, side='right')

        #mainbody
        body.pack(expand=True, side="bottom")
        title.pack(side="top")
        subtitle.pack(side="top")
        startTest.pack(expand=True, ipady=50, ipadx=50, padx=50, pady=50)
        config.pack()


        
    def configPanel():
        
        #window creation
        demoConf = tk.Tk()
        demoConf.title("Change Group")
        demoConf.resizable(False, False) #disables resizing the window
        demoConf.iconbitmap('./assets/WCG_Logo.ico')#adds the wcg logo
        demoConf.attributes('-topmost', 1) #puts the window at the top of the window order

        #grid
        demoConf.columnconfigure(0, weight=1)#configure grids
        demoConf.columnconfigure(1, weight=0)
        demoConf.columnconfigure(2, weight=3)

        #just text
        confTitle = ttk.Label(demoConf, text="Demo Config")
        confID = ttk.Label(demoConf, text="Simulation ID:")
        confTime = ttk.Label(demoConf, text="Simulation Time:")
        confRoom = ttk.Label(demoConf, text="Simulation Room:")
        
        #entrys
        simID = tk.StringVar(demoConf)
        simTime = tk.StringVar(demoConf)
        simRoom = tk.StringVar(demoConf)
        cIDTab = ttk.Entry(demoConf, textvariable=simID)
        cTimeTab = ttk.Entry(demoConf, textvariable=simTime)
        cRoomTab = ttk.Entry(demoConf, textvariable=simRoom)

        #Buttons
        confConfirm = ttk.Button(demoConf, text="Confirm", command=lambda: confirmSim(DemoUI))
        confClose = ttk.Button(demoConf, text="Close", command=lambda: demoConf.destroy())
        
        confTitle.grid(column=0, row=0, sticky="W", padx=5, pady=5)
        confID.grid(column=0, row=1, sticky="W", padx=5, pady=5)
        confTime.grid(column=0, row=2, sticky="W", padx=5, pady=5)
        confRoom.grid(column=0, row=3, sticky="W", padx=5, pady=5)
        cIDTab.grid(column=1, row=1, sticky="E", padx=5, pady=5)
        cTimeTab.grid(column=1, row=2, sticky="E", padx=5, pady=5)
        cRoomTab.grid(column=1, row=3, sticky="E", padx=5, pady=5)
        confConfirm.grid(column=1, row=4, sticky="E", padx=5, pady=5)
        confClose.grid(column=0, row=4, sticky="W", padx=5, pady=5)

        def confirmSim(self):
            ID = simID.get()
            Time = simTime.get()
            Room = simRoom.get()
            if timeValid(Time) == False:
                showerror(title='Error', message='Please input a valid time (00:00)')
            else:
                demoModule.ID = ID
                demoModule.Time = Time
                demoModule.Room = Room
            demoConf.destroy()
            
    def demoSuccess():
        showinfo("Access Granted", "ACCESS GRANTED: Your ID card was successfully confirmed")
    def demoFail():
        showerror("Access Denied", "ACCESS DENIED: Your ID card was denied")
            
        
#-------------------------------------------------------------
#-------------------------------------------------------------
#-------------------------------------------------------------

        
#class to manage the IdDB (ID DataBase)
class idDB():

    #function called whenever data needs to be saved
    def saveData(data, line):

        #opens and locally saves existing data
        database = open("iddb.txt", "r")
        line1 = database.readline()
        idStored = database.readline()
        line3 = database.readline()
        line4 = database.readline()
        groupStored = database.readline()
        fullDatabase = [line1, idStored, line3, line4, groupStored]

        #opens the database in write mode - now the file will be overwritten
        database = open("iddb.txt", "w")

        #prints full database - for debugging
        if data == "standard":
            print(fullDatabase)

        #stores new IDs - most of this preserves the file format (e.g. removing brackets and quote marks)
        elif data == "newID":
            idStored = str(line)
            idStored = idStored.strip("[]")
            idStored = idStored.replace("'", "")
            if '\n' not in idStored: idStored = idStored + ', \n'
            
        #deletes IDs from storage - loops through an id list and deletes each of them from the idDB  
        elif data == "delID":
            line = line.split(", ")
            splitIDs = idStored.split(", ")
            IDTemp = splitIDs
            for i in line:
                splitIDs.remove(i)
                
            #formatting
            if '\n' in splitIDs: splitIDs.remove('\n')
            idStored = str(splitIDs)
            idStored = idStored.strip("[]")
            idStored = idStored.replace("'", "")
            if '\n' not in splitIDs: idStored = idStored + ', \n'

        #stores new IDs - most of this preserves the file format (e.g. removing brackets and quote marks)
        elif data == "newGroup":
            line = str(line)
            line = line.strip("[]")
            line = line.replace("'", "")
            groupStored = groupStored + line #appends new group to other groups

        #deletes selected group from storage - loops through stored groups, if the group name (y[0]) is the same then remove it   
        elif data == "delGroup":
            groupList = []
            groupStored = groupStored.split(" , ")
            for x in groupStored:#gathers list of stored groups
                x = x.split(", ")
                groupList.append(x)
            for y in groupList:
                if y[0] == line:
                    groupList.remove(y)
                    break

            #formatting
            groupStored = str(groupList)
            groupStored = groupStored.replace("'], ['", " , ")
            groupStored = groupStored.replace(" ,']", " ,")
            groupStored = groupStored.replace("'", "")
            groupStored = groupStored.replace("[", "")
            groupStored = groupStored.replace("]", "")

        #books group - similar to delGroup, seaches through groups until it finds a match, then finds the booking info (z) and overwrites it
        elif data == "book":
            storedBooking = idDB.retrieveData("groupBooking", line[0])
            groupList = []
            groupStored = groupStored.split(" , ")
            for x in groupStored:#gathers list of stored groups
                x = x.split(", ")
                groupList.append(x)
            for y in groupList:
                if y[0] == line[0]:
                    z = groupList.index(y)
                    groupList[z] = line
                    break

            #formatting
            groupStored = str(groupList)
            groupStored = groupStored.replace("'], ['", " , ")
            groupStored = groupStored.replace(" ,']", " ,")
            groupStored = groupStored.replace("'", "")
            groupStored = groupStored.replace("[", "")
            groupStored = groupStored.replace("]", "")
            groupStored = groupStored.replace(" , , ", " , ")

        #add or remove ids in a group - finds stored ids in a group (y[1]) using specified group name (line[0]), then overwrites ids entirely using specified id list (line[1])
        #overwriting the stored ids means the same function can be used for adding and removing (as long as line[1] contains the final id list)
        elif data == "editGroup":
            groupName = line[0]
            line = line[1]
            groupList = []
            groupStored = groupStored.split(" , ")
            line = str(line)
            line = line.replace("', '", " ")
            line = line.strip("[']")
            for x in groupStored:#gathers list of stored groups
                x = x.split(", ")
                groupList.append(x)
            for y in groupList:
                if y[0] == groupName:
                    y.pop(1)
                    y.insert(1, line)

            #formatting
            groupStored = str(groupList)
            groupStored = groupStored.replace("'], ['", " , ")
            groupStored = groupStored.replace(" ,']", " ,")
            groupStored = groupStored.replace("'", "")
            groupStored = groupStored.replace("[", "")
            groupStored = groupStored.replace("]", "")
            
        #saves changed data
        #each index in fullDatabase is a line in the idDB, idStored and groupStored are the only relevent lines
        fullDatabase = [line1, idStored, line3, line4, groupStored]
        database.writelines(fullDatabase)
        database.close()
            
    #retrieves data from idDB for various uses
    def retrieveData(data, Group):

        #opens idDB in readonly mode
        database = open("iddb.txt", "r")
        line1 = database.readline()
        idStored = database.readline()
        line3 = database.readline()
        line4 = database.readline()
        groupStored = database.readline()
        fullDatabase = [line1, idStored, line3, line4, groupStored]
        groupList = []
        groupStored = groupStored.split(" , ")
        database.close() 
        for x in groupStored:#splits up stored groups into individual groups
            x = x.split(", ")
            groupList.append(x)

        #gathers stored ids - returns useable list of ids
        if data == "id": 
            idStored = idStored.split(", ")
            if '\n' in idStored:#removes \n from the id list, as it messes with formatting
                idStored.remove('\n')
                return idStored
            else:
                return idStored

        #gathers list of group names - seperates group names from other data, useful for finding specific groups
        elif data == "groupNames":
            groupNames = []
            for y in groupList:
                groupNames.append(y[0])
            return groupNames

        #gathers studentIDs based on group name - searches for group with specified name, gets the groups id list and returns a useable list
        elif data == "groupIDs":
            groupIDs = []
            for z in groupList:
                if z[0] == Group:
                    z = z[1].split(" ")
                    for v in z:
                        groupIDs.append(v)
            return groupIDs

        #finds a groups booking information- returns a list with a group name (a[0]), ids (a[1]), start time (a[2]), end time (a[3]), and room (a[4])
        #searches based on group name
        elif data == "groupBooking":
            groupBooking = []
            for a in groupList:
                if a[0] == Group:
                    groupBooking = [a[0], a[1], a[2], a[3], a[4]]
            return groupBooking

        #returns the full database as an array
        elif data == "database": 
            return fullDatabase


#class for id management - prepares data and send it to idDB
class idRegister():

    #logic for registering new ids - sends full idlist to idDB
    def registerNewID(ID):
        #basic setup - splits up ids and makes them all lowercase
        ID = ID.lower() 
        ID = ID.split(" ")
        storedID = idDB.retrieveData("id", 0) # get stored ids
        storedID.extend(ID)#add new ids to the end of storage
        newID=storedID#utility data storage to allow for loops to work
        
        #checks for and removes duplicates - for each stored id, if there is more than 1 instance then remove duplicates
        for i in storedID:
            dupCheck = newID.count(i)
            while dupCheck > 1:
                newID.remove(i)
                dupCheck = newID.count(i)

        newID.sort()#sort id list
        idDB.saveData("newID", newID) # give id list to idDB

    #deletes ids - no prep needs to be done
    def deleteID(ID):
        idDB.saveData("delID", ID)#point to idDB


#class for group management - prepares data and send it to idDB
class GroupRegister():

    #logic for registering new groups - sends a new blank group to idDB
    def registerNewGroup(groupName):
        newGroup = [" " + str(groupName)]
        groupList = idDB.retrieveData("groupNames", 0)#gets list of groupnames to prevent duplicates
        for a in groupList:
            if groupName == a:
                print("duplicate name!")#prevents duplicate groups by returning nothing
                return
        newGroup.extend(["0 0", "0", "0", "0 ,"])#blank group attributes, in order: 2 studentIDs, start time, end time, classroom
        idDB.saveData("newGroup", newGroup)#point to idDB

    #deletes a group - see delete ids
    def deleteGroup(groupName):
        idDB.saveData("delGroup", groupName)#point to idDB

    #logic for booking a room - constructs a list of relevent info to be used by the idDB
    def bookClassroom(groupName, timeStart, timeEnd, room):
        storedBooking = idDB.retrieveData("groupBooking", groupName)
        room = room + (" ,")
        newBooking = [groupName, storedBooking[1], timeStart, timeEnd, room]#includes existing group IDs to preserve formatting
        idDB.saveData("book", newBooking)#point to idDB

    #used to add or remove ids in a group, data parameter determines which
    def editGroup(groupName, IDlist, data): 

        #handles adding ids to a group
        if data == "add":
            storedIDs = idDB.retrieveData("groupIDs", groupName)#stored group ids
            IDlist2 = IDlist#utility data storage to allow for loops to work
            for g in storedIDs:#for every id in group, look at every id in list - if the groupid and the listid are the same, remove id from utility list
                for h in IDlist:
                    if g == h:
                        IDlist2.remove(h)
                    else:
                        continue 
            for j in IDlist2:#preserves formatting by removing blank ids when needed
                for i in storedIDs:
                    if i == "0":
                        storedIDs.remove(i)
            storedIDs.extend(IDlist2)#creates full list of ids
            storedIDs.sort()#sorts the id list
            line = [groupName, storedIDs]#bundles the group name with the id list for future use
            idDB.saveData("editGroup", line)#point to idDB

        #handles deleting ids in a group
        elif data == "remove":
            storedIDs = idDB.retrieveData("groupIDs", groupName)#stored group ids
            for i in IDlist:#search though every id in the list
                for j in storedIDs:#for evey id in the group
                    if j == i:#if id to be removed is the same as an id in the group, remove id from group
                        storedIDs.remove(i)
            if storedIDs == []:#preserves formatting by adding blank ids
                storedIDs.extend(["0 0"])
            line = [groupName, storedIDs]#bundles the group name with the id list for future use
            idDB.saveData("editGroup", line)#point to idDB


#logic for demonstration module
class demoModule():

    def __init__(self):
        ID = ""
        Time = ""
        Room = ""
        
    def startDemo():
        print(demoModule.ID, demoModule.Time, demoModule.Room)
        grouplist = idDB.retrieveData("groupNames",0)#retrieve all groups

        for group in grouplist:
            simID = demoModule.ID
            booking = idDB.retrieveData("groupBooking", group)
            tempRoom = booking[4]
            a = booking[2]
            b = booking[3]
            tempTimeStart = int(a.replace(":", ""))
            tempTimeEnd = int(b.replace(":", ""))
            simTime = int(demoModule.Time.replace(":", ""))
            print(simTime)
            print("retrieved data for " + str(group) + " " + str(tempRoom) + " " + str(tempTimeStart) + " " + str(tempTimeEnd))
            
            if tempRoom == demoModule.Room:
                print("room clear")
                if simTime in range(tempTimeStart, tempTimeEnd):
                    print("time clear")
                    idlist = idDB.retrieveData("groupIDs", group)
                    print(idlist)
                    if simID in idlist:
                        print("ID clear")
                        DemoUI.demoSuccess()
                        return
                    else:
                        print("ID fail")
                        continue
                else:
                    print("time fail")
                    continue
            else:
                print("room fail")
                continue
        
        DemoUI.demoFail()

#checks time is valid
def timeValid(time):
    regex = "^([01]?[0-9]|2[0-3]):[0-5][0-9]$" 
    p = re.compile(regex)
    if (time == "") :
        return False
    m = re.search(p, time)
    if m is None :
        return False
    else :
        return True

group = ""

if __name__ == "__main__":
    app = App()
    app.mainloop()


    





