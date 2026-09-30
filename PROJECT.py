#!/usr/bin/env python
# coding: utf-8

# In[13]:


# AI PERSONAL ASSISTANT STIMULATION

import datetime
import webbrowser

print("=================================================")
print("         AI PERSONAL ASSISTANT     ")
print("=================================================")

name = input(" What is your name ?")
print("Hello", name +"!Iam your personal assistant.")

contacts = {"Mom": "8072904701",
            "Dad": "9345260109",
            "Sister":"8925112755",
            "Brother":"7204371906",
            "Friend": "7373908686"}

while True :
    print("\nWhat would you like to do ?")
    print("1. Greeting")
    print("2. Tell me the time")
    print("3. Tell me the date")
    print("4. Tell me a joke")
    print("5. Tell me poem")
    print("6. Open Calculator")
    print("7. Open Youtube")
    print("8. Open Google")
    print("9. Open Weather")
    print("10. Call a contact")
    print("11. View contacts")
    print("12. Exit")

    choice = input("Enter your choice")

    if choice =="1":
        print("Hello",name+"!How can i help you?")

    elif choice == "2":
        current_time = datetime.datetime.now().strftime("%H:%M:%S ")
        print("Current Time :",current_time)

    elif choice == "3":
        current_date = datetime.datetime.now().strftime("%d-%m-%y")
        print("Today's Date :",current_date)

    elif choice =="4":
        print("Why did the computer go the doctor ?")
        print("Because it had virus!")

    elif choice == "5":
        print(" The darkest night will fade away ,")
        print("And lead you the brighter day.")

    elif choice == "6":
        num1 = float(input("Enter first number:"))
        operator = input("Enter operator(+,-,*,/,%,**):")
        num2 = float(input("Enter second number:"))

        if operator == "+":
            print("Result =", num1 + num2) 

        elif operator == "-":
              print("Result =", num1 -num2)

        elif operator == "*":
              print("Result =",num1*num2)

        elif operator =="/":
            if num != 0:  
                print("Result:",num1 %num2)
            else:
                print("Cannot divide by zero.")

        elif operator == "%": 
             if num2 != 0:
                 print("Result:",num1%num2)
             else:
                 print("Cannot divide by zero.")

        elif operator  == "**":
           print("Result:",num1 ** num2)
        else:
           print("Invalid operator.") 

    elif choice == "7":
        print("Opening Youtube....")
        webbrowser.open("https://www.youtube.com")

    elif choice  ==  "8":
        print("Opening Google....")
        webbrowser.open("https://www.google.com")

    elif choice == "9":
        print("Opening Weather....")
        webbrowser.open("https://www.google.com/search?q=weather")

    elif choice == " 10 ":
        contact_name = input("Enter contact name :")
        found = False
        for contact in contacts :
            if contact.lower() == contact_name.lower():
               print("Calling",contact)
               print("Phone number:",contact[contact])
               webbrowser.open("tel:"+ contacts[contact])
               found = True
               break
            if found == False:
                print("Contact not found.")

    elif choice == "11":
        print("\nSaved Contacts:")
        for contact,number in contacts.items():
            print(contact,":",number)

    elif choice == "12":
        print("Goodbye",name + "!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 10.")


# In[ ]:





# In[ ]:





# In[ ]:




