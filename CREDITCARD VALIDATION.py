import pickle
import random
from pathlib import Path
import os

def validate(no):
   
    x = no
    count = 0
    while x != 0:
        x //= 10
        count = count + 1
    n = int(count/2)+1
    
    ddigits = [ ]
    p = 100
    q = 10
    for i in range(1,n):
        d = no%p
        e = int(d/q)
        ddigits.append(e)
        p = p*100
        q = q*100


    ddigitsum = 0
    for i in range(0,n - 1):
        s = 2*(ddigits[i])
        while s > 0:
            ddigitsum  += (s%10)
            s = int(s/10)

            
    sdigits = [ ]
    f = 10
    g = 1
    for i in range(1,n):
        k = no%f
        l = int(k/g)
        sdigits.append(l)
        f = f*100
        g = g*100

    sdigitsum = 0
    for i in range(0,n - 1):
        t = (sdigits[i])
        while t > 0:
            sdigitsum  += (t%10)
            t = int(t/10)

    totalsum = 0
    totalsum = ddigitsum + sdigitsum

    if ( totalsum % 10 == 0):
        #print("The card number is valid.")
        return True
    else:
        #print("The card number is not valid.")
        return False

def issue():
    a = 1000000000000000
    b = 9999999999999999

    cardholder = input("Card holders name : ")
    dob = input("DD/MM/YYYY : ")
    
    typ = int(input("1.Visa card\n2.American Express (AMEX) card\n3.Diner’s Club International card\n4.Mastercard\n5.Discover card\nEnter your choice : "))
    while(True):
        r = random.randint(a,b)
        v = validate(r)
        c,t = cname(str(r))
        if(v and c  and  t == typ):
            print("\nYour card number : ",r)
            if(t == 1):
                print("Your card is Visa card")
                write(r,t)
            if(t == 2):
                print("Your card is American Express (AMEX) card")
                write(r,t)
            if(t == 3):
                print("Your card is Diner’s Club International card")
                write(r,t)
            if(t == 4):
                print("Your card is Mastercard")
                write(r,t)
            if(t == 5):
                print("Your card is Discover card")
                write(r,t)
            break
    limit(r)
    pin = input("Set your pin : ")

def write(no,t):
     if Path("issue.txt").is_file():
        with open("issue.txt","rb") as handle:
            contents = handle.read()
        dictionary = pickle.loads(contents)

        key = no
        
        if(t == 1):
             dictionary[key] = "Visa card"
        elif(t == 2):
           dictionary[key] = "American Express (AMEX) card"
        elif(t == 3):
            dictionary[key] = "Diner’s Club International card"
        elif(t == 4):
            dictionary[key] = "Mastercard"
        else:
            dictionary[key] = "Discover card"
        

        file = open("issue.txt","wb")
        pickle.dump(dictionary,file)
        file.close()
            
     else:
        details = {}
        
        key = no

        if(t == 1):
             details[key] = "Visa card"
        elif(t == 2):
            details[key] = "American Express (AMEX) card"
        elif(t == 3):
            details[key] = "Diner’s Club International card"
        elif(t == 4):
            details[key] = "Mastercard"
        else:
            details[key] = "Discover card"

        file = open("issue.txt","wb")
        pickle.dump(details,file)
        file.close()
        
def limit(no):
    
    if Path("lim.txt").is_file():
        with open("lim.txt","rb") as handle:
            contents = handle.read()
        dictionary = pickle.loads(contents)

        key = no
        value = input("Enter the card limit : ")
        
        dictionary[key] = value

        file = open("lim.txt","wb")
        pickle.dump(dictionary,file)
        file.close()
            
    else:
        details = {}
        
        key = no
        value = input("Enter the card limit : ")
        details[key] = value

        file = open("lim.txt","wb")
        pickle.dump(details,file)
        file.close()
    
def cname(card_number):
    flag = 0
    t = 0
    if card_number[0:1] == "4":
        #Type: Visa card.
        flag = 1
        t = 1
    elif card_number[0:2] == "34" or card_number[0:2] == "37":
        #Type: American Express (AMEX) card.
        flag = 1
        t = 2
    elif card_number[0:2] == "36":
        #Type: Diner’s Club International card."
        flag = 1
        t = 3
    elif card_number[0:2] == "51" or card_number[0:2] == "52" or card_number[0:2] == "53" or card_number[0:2] == "54" or card_number[0:2] == "55":
        #Type: Mastercard."
        flag = 1
        t = 4
    elif card_number[0:4] == "6011":
        #Type: Discover card."
        flag = 1
        t = 5
    else:
        #Invalid!! Credit card number."
        flag = 0
    return flag,t
        
    
def  history():
    with open("prev.txt","rb") as handle:
        contents = handle.read()
    dictionary = pickle.loads(contents)

    k = input("Enter the card number to delete : ")

    del dictionary[k]

    file = open("prev.txt","wb")
    pickle.dump(dictionary,file)
    file.close()
    
def check():
    
    if Path("prev.txt").is_file():
        with open("prev.txt","rb") as handle:
            contents = handle.read()
        dictionary = pickle.loads(contents)

        key = input("Enter card number : ")
        value = input("Enter card holder name : ")
        v = validate(int(key))
        c,t = cname(key)

        if(v and c):
            print("\nYour card number : {} is valid ".format(key))
            if(t == 1):
                print("Your card is Visa card")
            elif(t == 2):
                print("Your card is American Express (AMEX) card")
            elif(t == 3):
                print("Your card is Diner’s Club International card")
            elif(t == 4):
                print("Your card is Mastercard")
            else:
                print("Your card is Discover card")
        else:
            print("\nYour card number : {} is not valid ".format(key))

        dictionary[key] = value

        file = open("prev.txt","wb")
        pickle.dump(dictionary,file)
        file.close()
            
    else:
        details = {}
        
        key = input("Enter card number : ")
        value = input("Enter card holder name : ")

        v = validate(int(key))
        c,t = cname(key)

        if(v and c):
            print("\nYour card number : {} is valid ".format(key))
            if(t == 1):
                print("Your card is Visa card")
            elif(t == 2):
                print("Your card is American Express (AMEX) card")
            elif(t == 3):
                print("Your card is Diner’s Club International card")
            elif(t == 4):
                print("Your card is Mastercard")
            else:
                print("Your card is Discover card")
        else:
            print("\nYour card number : {} is not valid ".format(key))
        
        details[key] = value

        file = open("prev.txt","wb")
        pickle.dump(details,file)
        file.close()
        
def change():
    with open("lim.txt","rb") as handle:
        content = handle.read()
    dic = pickle.loads(content)

    no = int(input("Card number issued : "))
    pin = input("Enter your pin : ")

    newlimit = input("Card limit : ")
    dic[no] = newlimit

    file = open("lim.txt","wb")
    pickle.dump(dic,file)
    file.close()
    
def main():
    print("\t\tWELCOME\n\n")


    while(True):
        print("\n\t1.Issue a new card\n\t2.Validate a new credit card\n\t3.Previous validation details\n\t4.Check the issued card limit\n\t5.Change card limit\n\t6.Clear validation history\n\t7.Exit\n")
        choice = input("Enter your choice : ")
         
        if(choice == "1"):
           issue()

        elif(choice == "2"):
            check()
            
        elif(choice == "3"):
            print("\tValidation history : \n")
            with open("prev.txt","rb") as handle:
                content = handle.read()
            dic = pickle.loads(content)

            for key,value in dic.items():
                print(" Card no :{} \n Card holder :{}".format(key, value))

            print("\n\tIssue history : \n")
            with open("issue.txt","rb") as handle:
                content = handle.read()
            dic = pickle.loads(content)

            for key,value in dic.items():
                print(" Card no :{} \n Card type :{}".format(key, value))
            
        elif(choice == "4"):
            with open("lim.txt","rb") as handle:
                content = handle.read()
            dic = pickle.loads(content)

            no = int(input("Card number issued : "))
            
            print("Card limit : ",dic[no])

            file = open("lim.txt","wb")
            pickle.dump(dic,file)
            file.close()
        elif(choice == "5"):
            change()

        elif(choice == "6"):
            history()
            
        else:
            print("\t\tExiting....")
            break

main()
