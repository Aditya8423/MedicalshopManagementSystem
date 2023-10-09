print()
print()
print()
import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="aditya",database="medical_shop")
if mycon.is_connected():
    print("                       SUCCESSFULLY CONNECTED TO MYSQL")
else:
    print("PLEASE TRY CONNECTING TO YOUR MYSQL DATABASE. THERE SEEM TO BE AN ERROR WHILE CONNECTING PYTHON TO YOUR DATABASE")
cursor=mycon.cursor(buffered=True)
print()
print()
print()
print("                  WELCOME TO MEDICAL SHOP MANAGEMENT SYSTEM")
print()
print()
print()
def main():
    username=input("                              ENTER USERNAME:")
    password=input("                              ENTER PASSWORD:")
    if username=='school' and password=='1234':
        def mains():
            print()
            print("   1.STOCK MANAGEMENT")
            print("   2.EMPLOYEE DETAILS")
            print("   3.DEALER DETAILS")
            print("   4.MEDICINE INFORMATIOM")
            print("   5.CREATE BILL")
            print()
            a=int(input("   ENTER CHOICE:  "))
            print()
            if a==1:
                print("     1.NEW STOCK")
                print("     2.STOCK INQUIRY")
                print()
                b=int(input("     ENTER CHOICE:   "))
                print()
                if b==1:
                    date=input("       DATE        :")
                    dealername=input("       DEALER NAME :")
                    ct=int(input("       NO.OF MED   :"))
                    t=0
                    for i in range(1,ct+1):
                        cm=input("       NAME OF MED :")
                        qut=int(input("       QUANTITY    :"))   
                        ii="select MED_CP from medicine_info where medicine_name ='{}' ".format(cm)
                        cursor.execute(ii)
                        amt=cursor.fetchone()
                        az=''.join(str(x)for x in amt)
                        ad=int(az)
                        prc=ad*qut
                        print("       THE COST FOR ONE MEDICINE IS:" ,ad, "rupees")
                        print("       THE COST FOR",qut," MEDICINE IS:" ,prc, "rupees")
                        t=t+prc
                        print("       TOTAL AMOUNT:",t)
                        stock=("insert into stocks(sdate,sdealer,total_med,smedname,smedqty,smedtotalamount)values('{}','{}',{},'{}',{},{})").format(date,dealername,ct,cm,qut,t)
                        cursor.execute(stock)
                        mycon.commit()
                    print()
                    print("*****YOUR NEW STOCK HAS BEEN SUCCESSFULLY INSERTED*****")
                    print()
                elif b==2:
                    d=input("     ENTER DATE       :")
                    dna=input("     ENTER DEALER NAME:")
                    pk="select * from stocks where Sdate='{}' and Sdealer='{}'".format(d,dna)
                    cursor.execute(pk)
                    pkk=cursor.fetchall()
                    akss="select total_med from stocks where Sdate='{}' and Sdealer='{}'".format(d,dna)
                    cursor.execute(akss)
                    ap=cursor.fetchone()
                    zab=''.join(str(y)for y in ap)
                    dab=int(zab)
                    print()
                    for j in range (len(pkk)):
                        if j==0:
                            print("       DATE       :",pkk[0][0])
                        elif j==1:
                            print("       DEALER NAME:",pkk[1][1])
                    for i in range (dab):
                        print("       MED NAME   :",pkk[i][2])
                        print("       MED QUA.   :",pkk[i][3])
                        if i==(dab-1):
                            print("       TOTAL AMOUNT:",pkk[i][4])
                    print()
                else:
                    print("*****INVALID CHOISE*****")
                    print()
                    mains()
            elif a==2:
                print("     1.REGISTER NEW EMPLOYEE")
                print("     2.EMPLOYEE INFORMATION")
                print()
                c=int(input("     ENTER CHOICE:"))
                print()
                if c==1:
                    D=int(input("       ID OF EMPLOYEE :"))
                    NAME=input("       NAME OF EMPLOYE:")
                    ADDRESS=input("       ADDRESS        :")
                    IID=input("       AADHAR CARD NO.:")
                    SEX=input("       GENDER-M/F     :")
                    PHONE=input("       PHONE NO.      :")
                    newemp="insert into staff(emid,emname,emadd,emadhr,emsex,emphn)values('{}','{}','{}','{}','{}','{}')".format(D,NAME,ADDRESS,IID,SEX,PHONE)
                    cursor.execute(newemp)
                    mycon.commit()
                    print()
                    print("*****INFORMATION SAVED*****")
                    print()
                elif c==2:
                    Id=input("       ENTER ID:")
                    print()
                    cursor.execute("select * from staff where EmID={}".format(Id))
                    emstaff=cursor.fetchone()
                    for i in range(len(emstaff)):
                        if i==0:
                            print("       ID        :",emstaff[0])
                        elif i==1:
                            print("       NAME      :",emstaff[1])
                        elif i==2:
                            print("       ADDRESS   :",emstaff[2])
                        elif i==3:
                            print("       AADHAR NO.:",emstaff[3])
                        elif i==4:
                            print("       GENDER    :",emstaff[4])
                        elif i==5:
                            print("       PHONE NO. :",emstaff[5])
                else:
                    print("*****INVALID CHOISE*****")
                    print()
                    mains()
            elif a==3:
                print("     1.REGISTER NEW DEALER")
                print("     2.DEALER'S INFO")
                print()
                b=int(input("     ENTER CHOICE:"))
                print()
                if b==1:
                    name=input("     NAME OF DEALER:")
                    ag=input("     AGENCY        :")
                    add=input("     CITY OF DEALER:")
                    ph=input("     PHONE NUMBER  :")
                    dealerupdate="insert into deinfo(dname,dagency,dcity,dphn)values('{}','{}','{}','{}')".format(name,ag,add,ph)
                    cursor.execute(dealerupdate)
                    mycon.commit()
                    print()
                    print("*****NEW DEALER HAS BEEN SUCCESSFULLY REGISTERED*****")
                    print()
                elif b==2:
                    agg=input("     ENTER THE NAME OF THE AGENCY:")
                    print()
                    cursor.execute("select* from deinfo where dagency='{}'".format(agg))
                    dinfoo=cursor.fetchone()
                    for i in range (len(dinfoo)):
                        if i==0:
                            print("     DEALER NAME :",dinfoo[0])
                        elif i==1:
                            print("     AGENCY OWNED:",dinfoo[1])
                        elif i==2:
                            print("     ADDRESS     :",dinfoo[2])
                        elif i==3:
                            print("     PHONE NO.   :",dinfoo[3])
                    print()
                else:
                    print("*****INVALID CHOISE*****")
                    print()
            elif a==4:
                mname=input("     NAME OF MEDICINE :")
                mcprice=input("     C.P. OF MEDICINES:")
                msprice=input("     S.P. OF MEDICINES:")
                medinf="insert into medicine_info(medicine_name,med_cp,med_sp)values('{}','{}','{}')".format(mname,mcprice,msprice)
                ee=cursor.execute(medinf)
                mycon.commit()
                print()
                print("*****INFORMATION SAVED*****")
                print()
            elif a==5:
                print("     1.CREATE BILL")
                print("     2.OLD BILL DETAILS")
                print()
                b=int(input("     ENTER CHOICE:"))
                print()
                if b==1:
                    cdate=input("       DATE OF PURCHASRE  :")
                    cname=input("       CUSTOMER NAME      :")
                    cadd=input("       CUSTOMER ADDRESS   :")
                    cph=input("       CUSTOMER PHONE NO. :")
                    cn=int(input("       NO.OF MED PURCHASED:"))
                    to=0
                    for i in range(0,cn):
                        cm=input("       NAME OF MEDICINE   :")
                        qua=int(input("       QUANTITY REQUIRED  :"))
                        prcc="select med_sp from medicine_info where medicine_name='{}'".format(cm)
                        cursor.execute(prcc)
                        prccc=cursor.fetchone()
                        za=''.join(str(y)for y in prccc)
                        da=int(za)
                        pcr=da*qua
                        print("       PRICE IS           :",da,"rupees")
                        print("       AMOUNT IS          :",pcr,"rupees")
                        to=to+pcr
                    print()
                    print("       TOTAL AMOUNT TO BE PAID IS:",to,"rupees")
                    fst="insert into bill(date,custname,custadd,custphn,no_of_med,totalamt) values('{}','{}','{}','{}',{},{})".format(cdate,cname,cadd,cph,cn,to)
                    cursor.execute(fst)
                    mycon.commit()
                    print()
                    print("*****BILL SAVED*****")
                    print()
                elif b==2:
                    Cdate=input("       DATE OF PURCHASE:")
                    Cname=input("       COSTUMER NAME   :")
                    print()
                    obd="select* from bill where date='{}' and custname='{}'".format(Cdate,Cname)
                    cursor.execute(obd)
                    det=cursor.fetchone()
                    for i in range (len(det)):
                        if i==0:
                            print("       DATE        :",det[0])
                        elif i==1:
                            print("       NAME        :",det[1])
                        elif i==2:
                            print("       ADDRESS     :",det[2])
                        elif i==3:
                            print("       PHONE NO.   :",det[3])
                        elif i==4:
                            print("       NO. OF MED  :",det[4])
                        elif i==5:
                            print("       TOTAL AMOUNT:",det[5])
                    print()
                else:
                    print("*****INVALID CHOICE*****")
                    print()
                    mains()
            else:
                print("*****INVALID CHOICE*****")
                print()
                mains()
            ch=input("   BACK(b)/ EXIT(e) :").lower()
            if ch=="b":
                mains()
            else:
                exit()
        mains()
    else:
        print()
        print("                      *****WRONG USERNAME/PASSWORD*****")
        print()
        main()
main()


    
