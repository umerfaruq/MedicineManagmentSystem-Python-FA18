def cls(y):#clearing screen function
    print("\n"*y)

def fillRec(table,regNo,atr2,atr2Name,atr3,atr3Name,atr4,atr4Name):  #Filling the table
    n = abs(int(input("How many records do you want to enter? ")))
    for count in range(0,n):
        while True:
            regNoVar = abs(int(input("Enter Reg No of "+table+" "+str(count+1)+" :")))
            if regNoVar in regNo:
                print("Reg No Already Exists")
            else:
                regNo.append(regNoVar)
                break
        atr2.append(input("Enter "+atr2Name+" of "+table+" "+str(count+1)+" :")[0:16])
        atr3.append(input("Enter "+atr3Name+" of "+table+" "+str(count+1)+" :")[0:16])
        atr4.append(input("Enter "+atr4Name+" of "+table+" "+str(count+1)+" :")[0:16])
        cls(30)
    return(regNo,atr2,atr3,atr4)  #returns appended lists

def addRec(table,regNo,atr2,atr2Name,atr3,atr3Name,atr4,atr4Name):   #Adding more records
    n = abs(int(input("How many records do you want to add? ")))
    rec = len(regNo) + 1
    for count in range(n):
        while True:
            regNoVar = abs(int(input("Enter Reg No of "+table+" "+str(count+1)+" :")))
            if regNoVar in regNo:
                print("Reg No Already Exists")
            else:
                regNo.append(regNoVar)
                break
        atr2.append(input("Enter "+atr2Name+" of "+table+" "+str(rec)+" :")[0:16])
        atr3.append(input("Enter "+atr3Name+" of "+table+" "+str(rec)+" :")[0:16])
        atr4.append(input("Enter "+atr4Name+" of "+table+" "+str(rec)+" :")[0:16])
        rec += 1
        cls(30)
    return(regNo,atr2,atr3,atr4)   #returns appended lists

def viewRec(atr1,atr1Name,atr2,atr2Name,atr3,atr3Name,atr4,atr4Name):           #Printing the entire table
    print(atr1Name,"\t\t\t\t",atr2Name,"\t\t\t\t",atr3Name,"\t\t\t\t",atr4Name)
    for count in range(len(atr1)): #runs for the length of the table, prints table
        print(atr1[count],"\t\t\t\t",atr2[count],"\t\t\t\t",atr3[count],"\t\t\t\t",atr4[count])
        
def searchRec(searchAtr,searchAtrName,atr2,atr2Name,atr3,atr3Name,atr4,atr4Name):        #Searching for a record and printing it
    searchFlag = 0
    search = abs(int(input("Enter a "+searchAtrName+" : ")))
    count = 0 #setting initial value for while loop
    while count < len(searchAtr):
        if search == searchAtr[count]: #when search is equal to one of the stored values
            print(searchAtrName,"\t\t\t\t",atr2Name,"\t\t\t\t",atr3Name,"\t\t\t\t",atr4Name)
            print(searchAtr[count],"\t\t\t\t",atr2[count],"\t\t\t\t",atr3[count],"\t\t\t\t",atr4[count])
            count = 4 #for exiting the loop when search is found
            searchFlag = 1 #flag for knowing if search was found 
        count += 1
    if searchFlag != 1: #if search was not found
        print("Record Not Found")
        
def updateRec(searchAtr,searchAtrName,atr2,atr2Name,atr3,atr3Name,atr4,atr4Name):      # Changing a record that already exists
    searchFlag = 0
    search = abs(int(input("Enter a "+searchAtrName+" : ")))
    count = 0 #setting initial value for while loop
    while count < len(searchAtr):
        if search == searchAtr[count]: #when search is equal to one of the stored values
            while True:
                regNoVar = abs(int(input("Enter New Reg No: ")))
                if regNoVar in searchAtr:
                    print("Reg No Already Exists")
                else:
                    searchAtr.append(regNoVar)
                    break
            atr2[count] = input("Enter New "+atr2Name+" :")
            atr3[count] = input("Enter New "+atr3Name+" :")
            atr4[count] = input("Enter New "+atr4Name+" :")
            count = 4 #for exiting the loop when search is found
            searchFlag = 1 #flag for knowing if search was found 
        count += 1
    if searchFlag != 1: #if search was not found
        print("Record Not Found")
    return(searchAtr,atr2,atr3,atr4)   #returns appended lists

def delRec(searchAtr,searchAtrName,atr2,atr2Name,atr3,atr3Name,atr4,atr4Name):   #Deleting a Record
    searchFlag = 0
    search = abs(int(input("Enter a "+searchAtrName+" : ")))
    count = 0 #setting initial value for while loop
    while count < len(searchAtr):
        if search == searchAtr[count]: #when search is equal to one of the stored values
            del searchAtr[count]       #deleting the records
            del atr2[count]
            del atr3[count]
            del atr4[count]
            count = 4 #for exiting the loop when search is found
            searchFlag = 1 #flag for knowing if search was found 
        count += 1
    if searchFlag != 1: #if search was not found
        print("Record Not Found")
    return(searchAtr,atr2,atr3,atr4)  #returns appended lists

    






cls(50)

check1 = 0 #option select for entity 
flagMed = 0 #flag to check whether data is entered or not (MEDICINE)
flagEmp = 0 #flag to check whether data is entered or not (EMPLOYEE)
flagCus = 0 #flag to check whether data is entered or not (CUSTOMER)
flagSal = 0 #flag to check whether data is entered or not (SALES)
flagSalNot = 0 

#loop if input is not 3, 3 is exit condition
while check1 != 5:
    cls(30)
    check = 0   #option select for a action
    print("\n\n\t\t\tMedicine Management System")
    print("1. MEDICINE\n2. EMPLOYEE\n3. CUSTOMER\n4. SALES\n5. EXIT")
    check1 = abs(int(input("Select an entity: ")))
    if check1 == 1:
        entity = "Medicine"
    elif check1 == 2:
        entity = "Employee"
    elif check1 == 3:
        entity = "Customer"
    elif check1 == 4:
        entity = "Sales"
    cls(40)
    
    while check != 7 and check1 != 5:        #Inner loop runs for performing actions on selected entity
        # menu
        print("\n\n\t\t\tEntity: ",entity,"\n\n")
        print("1. FILL\n2. ADD\n3. VIEW\n4. SEARCH\n5. UPDATE\n6. DELETE\n7. CHANGE ENTITY\n8. EXIT")
        check = abs(int(input("Select an option by entering it's number: ")))
        cls(50)
        
        if check1 == 1:
            
            if check == 0:  # Automatically Fills the Table, for testing
                regNo = [1,2,3]
                name = ["Panadol","Disprin","Brufen"]
                mnfName = ["GSK","Reckitt Benckiser"[0:8],"Abbott"]
                price = ["250","730","25"]
                print("\t\t\tTable Filled")
                flagMed = 1 #values have been filled
            
            elif check == 1: #Fill Records Option
                print("\t\t\tFILL MEDICINE RECORDS\n")
                #initializing empty lists
                regNo = []
                name = []
                mnfName = [] #Manufacturer's Name
                price = []
                regNo,name,mnfName,price = fillRec("Medicine",regNo,name,"Name",mnfName,"Manufacturer",price,"Price")
                flagMed = 1 #table has been filled
                
            elif check == 2: #Add more records Option
                print("\t\t\tADD MEDICINE RECORDS\n")
                if flagMed == 1:#if tables are filled
                    regNo,name,mnfName,price = addRec("Medicine",regNo,name,"Name",mnfName,"Manufacturer",price,"Price")
                    print("\t\t\tNew Records Added")
                else:
                    print("DATA NOT ENTERED")

                
                
            elif check == 3: #Show Table
                print("\t\t\tVIEW MEDICINE RECORD\n")
                if flagMed == 1:#if tables are filled
                    viewRec(regNo,"Reg No",name,"Name",mnfName,"Manufacturer",price,"Price")
                else:
                    print("DATA NOT ENTERED")
            
            elif check == 4: #Search Record
                print("\t\t\tSEARCH MEDICINE RECORD\n")
                if flagMed == 1: #if tables are filled
                    searchRec(regNo,"Reg No",name,"Name",mnfName,"Manufacturer",price,"Price")
                else:
                    print("DATA NOT ENTERED")
                    
            elif check == 5: #Updating a record option
                print("\t\t\tUPDATE MEDICINE RECORD\n")
                if flagMed == 1: #if tables are filled
                    regNo,name,mnfName,price = updateRec(regNo,"Reg No",name,"Name",mnfName,"Manufacturer",price,"Price")
                    print("\t\t\tRecord Updated")
                else:
                    print("DATA NOT ENTERED")
                
                
            elif check == 6: #deleting a record option
                print("\t\t\tDELETE MEDICINE RECORD\n")
                if flagMed == 1: #if tables are filled
                    regNo,name,mnfName,price = delRec(regNo,"Reg No",name,"Name",mnfName,"Manufacturer",price,"Price")
                    print("\t\t\tRecord Deleted")
                else:
                    print("DATA NOT ENTERED")
                
                
            elif check != 7 and check != 8: #if incorrect input is entered, else statement cannot be used because loop still runs once if 7 is entered 
                print("\t\t\tSelect One Of The Options\n")
                
            elif check == 8: #for exiting both loops
                check1 = 5
                check = 7
                
        elif check1 == 2:
            
            if check == 0:  # Automatically Fills the Table, for testing
                regNoEmp = [1,2,3]
                nameEmp = ["Umer Farooq","Shameer Imran","Fatima Ali Zaidi"]
                adres = ["Phase 8, Bahria Town","Phase 4, Bahria Town","Phase 1, DHA"]
                contNum = ["0334 7999753","0336 6669997","143 143143143"]
                print("\t\t\tTable Filled")
                flagEmp = 1 #values have been filled
            
            elif check == 1: #Fill Records Option
                print("\t\t\tFILL EMPLOYEE RECORDS\n")
                #initializing empty lists
                regNoEmp = []
                nameEmp = []
                adres = [] 
                contNum = []
                regNoEmp,nameEmp,adres,contNum = fillRec("Employee",regNoEmp,nameEmp,"Name",adres,"Address",contNum,"Contact No")
                flagEmp = 1 #table has been filled
                
            elif check == 2: #Add more records Option
                print("\t\t\tADD EMPLOYEE RECORDS\n")
                if flagEmp == 1:#if tables are filled
                    regNo,name,adres,contNum = addRec("Employee",regNoEmp,nameEmp,"Name",adres,"Address",contNum,"Contact No")
                    print("\t\t\tNew Records Added")
                else:
                    print("DATA NOT ENTERED")
                
                
                
            elif check == 3: #Show Table
                print("\t\t\tVIEW EMPLOYEE RECORD\n")
                if flagEmp == 1:#if tables are filled
                    viewRec(regNoEmp,"Reg No",nameEmp,"Name",adres,"Address",contNum,"Contact No")
                    
                            
                else:
                    print("DATA NOT ENTERED")
            
            elif check == 4: #Search Record
                print("\t\t\tSEARCH EMPLOYEE RECORD\n")
                if flagEmp == 1: #if tables are filled
                    searchRec(regNoEmp,"Reg No",nameEmp,"Name",adres,"Address",contNum,"Contact No")
                else:
                    print("DATA NOT ENTERED")
                    
            elif check == 5: #Updating a record option
                print("\t\t\tUPDATE EMPLOYEE RECORD\n")
                if flagEmp == 1: #if tables are filled
                    regNoEmp,nameEmp,adres,contNum = updateRec(regNoEmp,"Reg No",nameEmp,"Name",adres,"Address",contNum,"Contact No")
                    print("\t\t\tRecord Updated")
                else:
                    print("DATA NOT ENTERED")
                
                
            elif check == 6: #deleting a record option
                print("\t\t\tDELETE EMPLOYEE RECORD\n")
                if flagEmp == 1: #if tables are filled
                    regNoEmp,nameEmp,adres,contNum = delRec(regNoEmp,"Reg No",nameEmp,"Name",adres,"Address",contNum,"Contact No")
                    print("\t\t\tRecord Deleted")
                else:
                    print("DATA NOT ENTERED")
                
            
            elif check != 7 and check != 8: #if incorrect input is entered, else statement cannot be used because loop still runs once if 7 is entered 
                print("\t\t\tSelect One Of The Options\n")
                
            elif check == 8:   #for exiting both loops
                check1 = 5
                check = 7
        
        elif check1 == 3:
            
            if check == 0:  # Automatically Fills the Table, for testing
                regNoCus = [1,2,3]
                nameCus = ["Fahad Hassan","Usman Ayub","Maryam Farooq"]
                salesReg = [1,2,3]
                salesMed = ["Panadol","Disprin","Brufen"]
                adresCus = ["Bahria Hamlets","Muslim Town","Bahria Phase 8"]
                contNumCus = ["0346 5734979","056 897650","7584 3848937"]
                print("\t\t\tTable Filled")
                flagCus = 1 #values have been filled
                flagSalNot = 1
            
            elif check == 1: #Fill Records Option
                print("\t\t\tFILL CUSTOMER RECORDS\n")
                #initializing empty lists
                regNoCus = []
                nameCus = []
                contNumCus = [] #Manufacturer's Name
                adresCus = []
                regNoCus,nameCus,contNumCus,adresCus = fillRec("Customer",regNoCus,nameCus,"Name",contNumCus,"Contact No",adresCus,"Address")
                flagCus = 1 #table has been filled
                
            elif check == 2: #Add more records Option
                print("\t\t\tADD CUSTOMER RECORDS\n")
                if flagCus == 1:#if tables are filled
                    regNoCus,nameCus,contNumCus,adresCus = addRec("Customer",regNoCus,nameCus,"Name",contNumCus,"Contact No",adresCus,"Address")
                    print("\t\t\tNew Records Added")
                else:
                    print("DATA NOT ENTERED")

                
                
            elif check == 3: #Show Table
                print("\t\t\tVIEW CUSTOMER RECORD\n")
                if flagCus == 1:#if tables are filled
                    viewRec(regNoCus,"Reg No",nameCus,"Name",contNumCus,"Contact No",adresCus,"Address")
                    if flagSalNot == 1 or flagSal == 1:
                        cls(3)
                        print("\t\t\tCUSTOMER MEDICINES")
                        for i in regNoCus:
                            cls(3)
                            h = regNoCus.index(i)
                            print(regNoCus[h],"\t\t",nameCus[h])
                            for a in range(len(salesReg)):
                                if i == salesReg[a]:
                                    print("\t\t",salesMed[a])
                    
                else:
                    print("DATA NOT ENTERED")
            
            elif check == 4: #Search Record
                print("\t\t\tSEARCH CUSTOMER RECORD\n")
                if flagCus == 1: #if tables are filled
                    searchRec(regNoCus,"Reg No",nameCus,"Name",contNumCus,"Contact No",adresCus,"Address")
                else:
                    print("DATA NOT ENTERED")
                    
            elif check == 5: #Updating a record option
                print("\t\t\tUPDATE CUSTOMER RECORD\n")
                if flagCus == 1: #if tables are filled
                    regNoCus,nameCus,contNumCus,adresCus = updateRec(regNoCus,"Reg No",nameCus,"Name",contNumCus,"Contact No",adresCus,"Address")
                    print("\t\t\tRecord Updated")
                else:
                    print("DATA NOT ENTERED")
                
                
            elif check == 6: #deleting a record option
                print("\t\t\tDELETE CUSTOMER RECORD\n")
                if flagCus == 1: #if tables are filled
                    regNoCus,nameCus,contNumCus,adresCus = delRec(regNoCus,"Reg No",nameCus,"Name",contNumCus,"Contact No",adresCus,"Address")
                    print("\t\t\tRecord Deleted")
                else:
                    print("DATA NOT ENTERED")
                
                
            elif check != 7 and check != 8: #if incorrect input is entered, else statement cannot be used because loop still runs once if 7 is entered 
                print("\t\t\tSelect One Of The Options\n")
                
            elif check == 8: #for exiting both loops
                check1 = 5
                check = 7
                
        elif check1 == 4:  #Customer Option
            
            if flagMed == 1 and flagCus == 1:   #sales can only be entered if medicine and customer lists are stored
                
                if check == 1:   #Filling Records
                    print("\t\t\tFILL SALES RECORDS\n")
                    #initializing list
                    salesReg = []
                    salesCus = []
                    salesMed = []
                    salesPrc = []
                    salesQnt = []
                    n1 = abs(int(input("How many records do you want to enter? ")))
                    for i in range(n1):
                        while True:
                            n = abs(int(input("Enter Reg No of Customer "+str(i+1)+" : ")))
                            viewRec(regNo,"Reg No",name,"Name",mnfName,"Manufacturer",price,"Price")   #Shows Medicines
                            medSale = abs(int(input("Select A Medicine: ")))
                            qnt = abs(int(input("Enter Quantity: ")))
                            if n in regNoCus and medSale in regNo:       #if customer and medicines exist
                                #storing sales record
                                salesReg.append(n)
                                salesCus.append(nameCus[regNoCus.index(n)])
                                salesMed.append(name[regNo.index(medSale)])
                                salesPrc.append(int(price[regNo.index(medSale)])*qnt)
                                salesQnt.append(qnt)
                                break
                            else:
                                print("Incorrect Reg No of Customer or Medicine")
                        cls(30)
                    flagSal = 1
                                
                                
                elif check == 2: #Adding more records
                    print("\t\t\tADD SALES RECORDS\n")
                    if flagSal == 1:
                        n1 = abs(int(input("How many records do you want to add? ")))
                        i1 = len(salesReg) + 1
                        for i in range(n1):
                            while True:
                                n = abs(int(input("Enter Reg No of Customer "+str(i1)+" : ")))
                                viewRec(regNo,"Reg No",name,"Name",mnfName,"Manufacturer",price,"Price")
                                medSale = abs(int(input("Select A Medicine: ")))     #Shows Medicines
                                qnt = abs(int(input("Enter Quantity: ")))
                                if n in regNoCus and salesMed in regNo:       #if customer and medicines exist
                                    #storing sales record
                                    salesReg.append(n)
                                    salesCus.append(nameCus[regNoCus.index(n)])
                                    salesMed.append(name[regNo.index(medSale)])
                                    salesPrc.append(int(price[regNo.index(medSale)])*qnt)
                                    salesQnt.append(qnt)
                                    break
                                else:
                                    print("Incorrect Reg No of Customer or Medicine")
                                i1 += 1
                            cls(30)
                    else:
                        print("DATA NOT ENTERED")
                    
                    
                elif check == 3:    #Viewing Records
                    print("\t\t\tVIEW SALES RECORDS\n")
                    if flagSal == 1:
                        print("Reg No","\t\t\t\t","Customer Name","\t\t\t\t","Medicine Name","\t\t\t\t","Price","\t\t\t\t","Quantity")
                        for count in range(len(salesReg)): #runs for the length of the table, prints table
                            print(salesReg[count],"\t\t\t\t",salesCus[count],"\t\t\t\t",salesMed[count],"\t\t\t\t",salesPrc[count],"\t\t\t\t",salesQnt[count])
                    else:
                        print("DATA NOT ENTERED")
                
                elif check == 4:    #Searching for a record
                    print("\t\t\tSEARCH SALES RECORDS\n")
                    if flagSal == 1:
                        searchFlag = 0
                        search = abs(int(input("Enter a Reg No : ")))
                        count = 0 #setting initial value for while loop
                        while count < len(salesReg):
                            if search == salesReg[count]: #when search is equal to one of the stored values
                                print("Reg No","\t\t\t\t","Customer Name","\t\t\t\t","Medicine Name","\t\t\t\t","Price","\t\t\t\t","Quantity")
                                print(salesReg[count],"\t\t\t\t",salesCus[count],"\t\t\t\t",salesMed[count],"\t\t\t\t",salesPrc[count],"\t\t\t\t",salesQnt[count])
                                count = 4 #for exiting the loop when search is found
                                searchFlag = 1 #flag for knowing if search was found 
                            count += 1
                        if searchFlag != 1: #if search was not found
                            print("Record Not Found")
                    else:
                        print("DATA NOT ENTERED")
                
                elif check == 5:      #Updating a record
                    print("\t\t\tUPDATE SALES RECORDS\n")
                    if flagSal == 1:
                        
                        searchFlag = 0
                        search = abs(int(input("Enter a Reg No : ")))
                        count = 0 #setting initial value for while loop
                        while count < len(salesReg):
                            if search == salesReg[count]: #when search is equal to one of the stored values
                                while True:
                                    n = abs(int(input("Enter Reg No of Customer "+str(i1)+" : ")))
                                    viewRec(regNo,"Reg No",name,"Name",mnfName,"Manufacturer",price,"Price")
                                    medSale = abs(int(input("Select A Medicine: ")))
                                    qnt = abs(int(input("Enter Quantity: ")))
                                    if n in regNoCus and salesMed in regNo:
                                        salesReg[count] = n
                                        salesCus[count] = nameCus[regNoCus.index(n)]
                                        salesMed[count] = name[regNo.index(medSale)]
                                        salesPrc[count] = int(price[regNo.index(medSale)])*qnt
                                        salesQnt[count] = qnt
                                        break
                                    else:
                                        print("Incorrect Reg No of Customer or Medicine")
                                count = 4 #for exiting the loop when search is found
                                searchFlag = 1 #flag for knowing if search was found 
                            count += 1
                        if searchFlag != 1: #if search was not found
                            print("Record Not Found")
                    else:
                        print("DATA NOT ENTERED")
                       
                elif check == 6:        #Deleting a record
                    print("\t\t\tDELETE SALES RECORDS\n")
                    if flagSal == 1:
                        
                        searchFlag = 0
                        search = abs(int(input("Enter a Reg No : ")))
                        count = 0 #setting initial value for while loop
                        while count < len(salesReg):
                            if search == salesReg[count]: #when search is equal to one of the stored values
                                del salesReg[count]       #deleting the records
                                del salesCus[count]
                                del salesMed[count]
                                del salesPrc[count]
                                del salesQnt[count]
                                count = 4 #for exiting the loop when search is found
                                searchFlag = 1 #flag for knowing if search was found 
                            count += 1
                        if searchFlag != 1: #if search was not found
                            print("Record Not Found")
                            
                    else:
                        print("DATA NOT ENTERED")
                    
                elif check == 8:      #Exit both loops
                    
                    check1 = 5
                    check = 7
                    
                elif check != 7 and check != 8:   #if wrong input is
                    
                    print("\t\t\tSelect One Of The Options\n")
                    
                        
                
        
        
        
        
        
        
        elif check1 != 5:         #if wrong input is entered
            print("\t\t\tSelect One Of The Two Options\n")

            
        
# Exit if 8
print("\t\t\tPROGRAM ENDED")

        
        
                
                
            
    


