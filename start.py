import webbrowser
import os

ApplicationData = open("DATA", 'r')
ApplicationList = ApplicationData.readlines()
for idx, a in enumerate(ApplicationList):
    ApplicationList[idx] = ApplicationList[idx].replace(" \n", "")
from appJar import gui

font = ("Lucida Bright", "8")

def updateData():
       for i in app.getAllListItems("list"):
          print(i)
          open("DATA", 'a').write("%s \n" % i)    


def press(btn):
       print(app.getListBox("list"))
       os.startfile(''.join(app.getListBox("list")))
       
def pressAdd(btn):
       open("DATA", 'w').write("")
       app.addListItem("list",app.getEntry("13"))
       updateData()

def pressDel(btn):
    open("DATA", 'w').write("")
    print(ApplicationList)
    app.removeListItem("list", app.getListBox("list"))
    updateData()

    
app = gui("Application Launcher","650x270")
app.setResizable(canResize=False)
app.setFont(8,font)
app.setSticky("nw")
app.addLabel("l1", "Applicaitons:")
app.setSticky("ew")
app.addListBox("list",ApplicationList,1,0,5)

app.setSticky("nw")
app.addLabel("l2", "Location:")
app.setSticky("e")

app.setInPadding([30,0])

app.addButton("Delete", pressDel,2,4)
app.addButton("Add", pressAdd,2,3)

app.setSticky("w")
app.setPadding([55,0])
app.setInPadding([125,0])
app.addEntry("13",2,0,4)


app.setInPadding([40,20])
app.setPadding([0,20])
app.setSticky("")
app.addButton("Run", press,3,0,5)
app.go()
