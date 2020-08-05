## Personal Finance Auditor Program ##

#####################################
import math
from tkinter import *


#########TKINTER AND BASIC GLOBAL VARIABLES###############

root = Tk()
root.title('Budget Auditor v1.0 - Colin Lakadat')

rootLabel = Label(root, text="Budget Auditor v1.0")
rootLabel.grid(row=0, column=0)


##Reading in the list of Zip incomes##
a_file = open("ZIPS.txt", "r")

ListofLists = []
DictofZips = {}

for line in a_file:
    strippedLines = line.strip('"')
    lineList = strippedLines.split()
    
    ListofLists.append(lineList)

for x in ListofLists:
    DictofZips[x[0]] = x[1]
#print(len(DictofZips))

   
TotalIncomeNum = 0
ZipEntered = 0

############BUTTON FUNCTION(S)###################
def SubmitInformation():

    ## Setting some variables for easy use later on##
    global TotalIncomeNum
    global ZipEntered
    ZipEntered = ZipEntry.get()
    AddIncomeTest = AdditionalIncomeEntry.get()
    SalaryEntered = SalaryEntry.get()
    #TotalExpense = (float(RentEntry.get()) * 12) + (float(BillsEntry.get()) * 12) + (float(SavingsEntry.get()) * 12)+ (float(LeisureEntry.get()) * 12)
    #print(TotalExpense)
    #print(ZipEntered)

    ## These are the ERROR messages the user will see if various issues occue. i.e. over budgeting, not filling out the fields, etc##########

    if SalaryEntry.get() == '0' and AdditionalIncomeEntry.get() == '0':
        AuditStatusText.config(text="Status = ERROR: You have marked\nno yearly\nincome.")
        return
    if not ZipEntry.get() or not SalaryEntry.get() or not RentEntry.get() or not BillsEntry.get() or not SavingsEntry.get() or not LeisureEntry.get():
        AuditStatusText.config(text="Status = ERROR: Enter numerical\n values for all\n required fields.")
        return
    if AddIncomeTest.isnumeric() and AdditionalIncomeEntry.get():
        TotalIncomeNum = float(SalaryEntry.get()) + float(AdditionalIncomeEntry.get())
    elif SalaryEntered.isnumeric() and SalaryEntry.get():
        TotalIncomeNum = float(SalaryEntry.get())

    TotalExpense = (float(RentEntry.get()) * 12) + (float(BillsEntry.get()) * 12) + (float(SavingsEntry.get()) * 12)+ (float(LeisureEntry.get()) * 12)

    if TotalExpense > TotalIncomeNum:
        AuditStatusText.config(text="Status = ERROR: You have budgeted\nover your yearly\nincome amount.")
        return
    AuditStatusText.config(text="Status: Processing")

    ##Setting the side panel labels to the percentages of the total income entered##
    SalaryEntryTotal.config(text=TotalIncomeNum)
    RentEntryPercent.config(text=str(round(100 * float(RentEntry.get())/float(TotalIncomeNum)*12)) + '% of Total Income')
    YearlyBillsNum.config(text=str(round(100 * float(BillsEntry.get())/float(TotalIncomeNum)*12)) + '% of Total Income')
    YearlySavingsNum.config(text=str(round(100 * float(SavingsEntry.get())/float(TotalIncomeNum)*12)) + '% of Total Income')
    OtherNum.config(text=str(round(100 * float(LeisureEntry.get())/float(TotalIncomeNum)*12)) + '% of Total Income')
    LeftOverNum.config(text=str((float(TotalIncomeNum) - float(TotalExpense))))
    
    GraphAndFindMedian()

    ##Graphing coming soon##
def GraphAndFindMedian():
    global TotalIncomeNum
    global ZipEntered
    global ListofLists
    global DictofZips
    
    if ZipEntered in DictofZips:
        #print(DictofZips[ZipEntered])
        ZipEntryMedianNum.config(text=DictofZips[ZipEntered].strip('"'))
        AuditStatusText.config(text="Status = Finished")
    else:
        print('Zip Code not found')
        AuditStatusText.config(text="Status = ERROR: Zip Not Found")
    
        return

#############TKINTER OBJECTS###################
InputFrame = LabelFrame(root, text="Input your information here:",font ='Helvetica 11 bold', padx=5, pady=5)
InputFrame.grid(row=1, column=0)
AuditStatusFrame = LabelFrame(root, text="Audit Status:",padx=10, pady=10)
AuditStatusFrame.grid(row=1, column=1)
InputDetailsFrame = LabelFrame(root, text="Submit")
InputDetailsFrame.grid(row=2, column=0)
InfoFrame = LabelFrame(root, text="Results:", font ='Helvetica 11 bold', padx=5, pady=5)
InfoFrame.grid(row=1, column=2)

##Entry Area Widgets##
ZipEntryLabel = Label(InputFrame, text="Your Zip Code", font ='Helvetica 10 bold')
ZipEntryLabel.grid(row=1, column=0)
ZipEntry = Entry(InputFrame)
ZipEntry.grid(row=2, column=0)
SalaryEntryLabel = Label(InputFrame, text="Yearly Salary", font ='Helvetica 10 bold')
SalaryEntryLabel.grid(row=3, column=0)
SalaryEntry = Entry(InputFrame)
SalaryEntry.grid(row=4, column=0)
AdditionalIncomeLabel = Label(InputFrame, text="Yearly Additional Income*", font ='Helvetica 10 bold')
AdditionalIncomeLabel.grid(row=5, column=0)
AdditionalIncomeEntry = Entry(InputFrame)
AdditionalIncomeEntry.grid(row=6, column=0)
RentEntryLabel = Label(InputFrame, text="Housing Cost per month", font ='Helvetica 10 bold')
RentEntryLabel.grid(row=7, column=0)
RentEntry = Entry(InputFrame)
RentEntry.grid(row=8, column=0)
BillsEntryLabel = Label(InputFrame, text=" Fixed Expenses (Bills) per month", font ='Helvetica 10 bold')
BillsEntryLabel.grid(row=9, column=0)
BillsEntry = Entry(InputFrame)
BillsEntry.grid(row=10, column=0)
SavingsEntryLabel = Label(InputFrame, text="Estimated Savings per month", font ='Helvetica 10 bold')
SavingsEntryLabel.grid(row=11, column=0)
SavingsEntry = Entry(InputFrame)
SavingsEntry.grid(row=12, column=0)
LeisureEntryLabel = Label(InputFrame, text="Leisure/Other Expenses per month", font ='Helvetica 10 bold')
LeisureEntryLabel.grid(row=13, column=0)
LeisureEntry = Entry(InputFrame)
LeisureEntry.grid(row=14, column=0)


##Center Status Bar Widgets##
AuditStatusText = Label(AuditStatusFrame, text="Status = Enter Data", padx=30, pady=30)
AuditStatusText.grid(row=0, column=0)

##Info Area Widgets##
ZipEntryMedian = Label(InfoFrame, text="Median Income for your Zip:", font ='Helvetica 10 bold')
ZipEntryMedian.grid(row=0, column=0)
ZipEntryMedianNum = Label(InfoFrame)
ZipEntryMedianNum.grid(row=1, column=0)
SalaryInfoLabel = Label(InfoFrame, text="Your Income:", font ='Helvetica 10 bold')
SalaryInfoLabel.grid(row=2, column=0)
SalaryEntryTotal = Label(InfoFrame)
SalaryEntryTotal.grid(row=3, column=0)
RentEntryInfoLabel = Label(InfoFrame, text="Your Housing:", font ='Helvetica 10 bold')
RentEntryInfoLabel.grid(row=4, column=0)
RentEntryPercent = Label(InfoFrame)
RentEntryPercent.grid(row=5, column=0)
YearlyBillsInfoLabel = Label(InfoFrame, text="Yearly Bill Amount:", font ='Helvetica 10 bold')
YearlyBillsInfoLabel.grid(row=6, column=0)
YearlyBillsNum = Label(InfoFrame)
YearlyBillsNum.grid(row=7, column=0)
YearlySavingsInfoLabel = Label(InfoFrame, text="Yearly Savings:", font ='Helvetica 10 bold')
YearlySavingsInfoLabel.grid(row=8, column=0)
YearlySavingsNum = Label(InfoFrame)
YearlySavingsNum.grid(row=9, column=0)
OtherNumLabel = Label(InfoFrame, text="Cost of other Expenses:", font ='Helvetica 10 bold')
OtherNumLabel.grid(row=10, column=0)
OtherNum = Label(InfoFrame)
OtherNum.grid(row=11, column=0)
LeftOverLabel = Label(InfoFrame, text="Unaccounted funds:", font ='Helvetica 10 bold')
LeftOverLabel.grid(row=12, column=0)
LeftOverNum = Label(InfoFrame)
LeftOverNum.grid(row=13, column=0)


##Submit Button Widgets##
SubmitDetailsButton = Button(InputDetailsFrame, text="Submit My Info!", command = SubmitInformation)
SubmitDetailsButton.grid(row=1, column=0)
InputDetailsLabel = Label(InputDetailsFrame, text="* = optional fields")
InputDetailsLabel.grid(row=0, column=0)

root.mainloop()






