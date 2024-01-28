# Demo 
import pandas as pd
import time
import numpy as np
import sqlite3
import cv2
import matplotlib.pyplot as plt


T1 = time.time()
formatted_time = time.ctime(T1)

print("Hello! I'm Medico, Your New Home Remedies Chatbot \n")

x = str(input("Please Enter Your Username \n"))
y = input("Please Enter Your Phone Number \n")
z = input("Please Enter Your Email ID \n")

time_limit = 60
start_time = time.time()
end_time = start_time + time_limit

while time.time() < end_time:
    time.sleep(2)
    try:
        user_question = input("How Can I help You ? \n")

        words_to_remove = ['what','are','why','should','how','to','do','done','define','keep','give','perform','the','medicinal','tree',
                           'is','in','general','to','common','use','with','when','during','a','deal','as','given','you','many','there','thing'
                           'normal','person','thing','?','i','mention','tell','about','show']

        words = user_question.split()
        filtered_words = [word for word in words if word.lower() not in words_to_remove]
        result = " ".join(filtered_words)
        lower=result.lower()
        #print("Lower=",lower)
        A=lower
        
        # Introduction
        if A in ['1','remedies','remedy','remedie','home remedy','home','home remedies','home remedy','remedy']:
          img = cv2.imread('Home Remedies.jpg')
          img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
          plt.imshow(img)
          plt.axis('off')
          plt.show()
          print()
          time.sleep(2)
          with open("Home Remedies.txt", "r") as file:
            print(file.read())
            print()
        
        #SHR
        elif A in ['2','cold','colds','causes of cold','causes cold','cause cold','home remedies for cold','make cold medicine at home','home remedy for cold','symptoms of cold','cough','causes of cough','causes cough','cause cough','home remedies for cough','make cough medicine at home','home remedy for cough','symptoms of cough']:
            img = cv2.imread('cold.jpg')
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            plt.imshow(img)
            plt.axis('off')
            plt.show()
            print()
            time.sleep(2)
            print("causes of cold and cough")
            with open("cold causes.txt", "r") as file:
              print(file.read())
              print()
            time.sleep(2)
            print("symptoms of cold and cough")
            with open("cold symptoms.txt", "r") as file:
                print(file.read())
                print() 
            time.sleep(2)    
            print("home remedies for cold and cough")
            with open("cold.txt", "r") as file:
                print(file.read())
                print()    
        
        #IMP
        elif A in ['3','uses of banyan','banyan','uses of aala','aala','uses of ficus benghalensis','ficus benghalensis']:
            img = cv2.imread('Aala.jpg')
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            plt.imshow(img)
            plt.axis('off')
            plt.show()
            print()
            time.sleep(2)
            with open("Aala.txt", "r") as file:
              print(file.read())
              print()
        
        # Advantages & Disadvantages of Home Remedies
        elif A in ['4','advantages','benefits of home remedies','advantages of home remedies','disadvantages','disadvantages of home remedies']:
          img = cv2.imread('Advantages.jpg')
          img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
          plt.imshow(img)
          plt.axis('off')
          plt.show()
          print()
          time.sleep(2)
          with open("Advantages.txt", "r") as file:
            print(file.read())
            print()
          img = cv2.imread('Disadvantages.jpg')
          img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
          plt.imshow(img)
          plt.axis('off')
          plt.show()
          print()
          time.sleep(2)
          with open("Disadvantages.txt", "r") as file:
            print(file.read())
            print()
        
        #Frist aid
        elif A in ['5.1','51','first aid','firstaid','First aid']:
            img = cv2.imread('First aid.jpg')
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            plt.imshow(img)
            plt.axis('off')
            plt.show()
            print()
            time.sleep(2)
            with open("First aid.txt", "r") as file:
              print(file.read())
              print()
        elif A in ['5','first aid kit','firstaid kit','First aid kit','kit','my first aid kit']:
            img = cv2.imread('First aid kit.jpg')
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            plt.imshow(img)
            plt.axis('off')
            plt.show()
            print()
            time.sleep(2)
            with open("First aid kit.txt", "r") as file:
              print(file.read())
              print()
            time.sleep(2)
            with open("What should I keep in my first aid kit.txt", "r") as file:
              print(file.read())
              print()  
              
        #BMI
        elif A in ['6','bmi value','bmi value be known','body mass index value','body mass index value be known']:
            with open("bmi.txt", "r") as file:
              print(file.read())
              print()
              time.sleep(2)
            with open("known.txt", "r") as file:
              print(file.read())
              print()
        elif A in ['6.2','62','range','bmi range','bmi calculated','body mass index range','body mass index calculated']:
            with open("range.txt", "r") as file:
              print(file.read())
              print()
              time.sleep(2)
            with open("calculate.txt", "r") as file:
              print(file.read())
              print()
              
        elif A in ['7','exit','quit','leave','esc','close','finished']:
          break
      
        else:
            print("Sorry,"+"\U0001F625 " "I Could Not Understand Their Need.\nNote: Enter whole number or words only")
            time_limit = 60
            start_time = time.time()
            end_time = start_time + time_limit

            while time.time() < end_time:
              time.sleep(2)

              B = input("Select your option from below \nNote: Enter whole number or words only \n1.Define home remedy \n2.Simple home remedies \n3.Indian Medicinal Plants Uses \n4.Advantages & Disadvantages of Home Remedies \n5.First aid \n6.BMI \n7.Back /n")

              # Introduction
              if B in ['1','remedies','remedy','remedie','home remedy','home','home remedies','home remedy','remedy']:
                img = cv2.imread('Home Remedies.jpg')
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                plt.imshow(img)
                plt.axis('off')
                plt.show()
                print()
                time.sleep(2)
                with open("Home Remedies.txt", "r") as file:
                  print(file.read())
                  print()
              
              #SHR
              elif B in ['2','cold','colds','causes of cold','causes cold','cause cold','home remedies for cold','make cold medicine at home','home remedy for cold','symptoms of cold','cough','causes of cough','causes cough','cause cough','home remedies for cough','make cough medicine at home','home remedy for cough','symptoms of cough']:
                  img = cv2.imread('cold.jpg')
                  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                  plt.imshow(img)
                  plt.axis('off')
                  plt.show()
                  print()
                  time.sleep(2)
                  print("causes of cold and cough")
                  with open("cold causes.txt", "r") as file:
                    print(file.read())
                    print()
                  time.sleep(2)
                  print("symptoms of cold and cough")
                  with open("cold symptoms.txt", "r") as file:
                      print(file.read())
                      print() 
                  time.sleep(2)    
                  print("home remedies for cold and cough")
                  with open("cold.txt", "r") as file:
                      print(file.read())
                      print()    
              
              #IMP
              elif B in ['3','uses of banyan','banyan','uses of aala','aala','uses of ficus benghalensis','ficus benghalensis']:
                  img = cv2.imread('Aala.jpg')
                  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                  plt.imshow(img)
                  plt.axis('off')
                  plt.show()
                  print()
                  time.sleep(2)
                  with open("Aala.txt", "r") as file:
                    print(file.read())
                    print()
              
              # Advantages & Disadvantages of Home Remedies
              elif B in ['4','advantages','benefits of home remedies','advantages of home remedies','disadvantages','disadvantages of home remedies']:
                img = cv2.imread('Advantages.jpg')
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                plt.imshow(img)
                plt.axis('off')
                plt.show()
                print()
                time.sleep(2)
                with open("Advantages.txt", "r") as file:
                  print(file.read())
                  print()
                img = cv2.imread('Disadvantages.jpg')
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                plt.imshow(img)
                plt.axis('off')
                plt.show()
                print()
                time.sleep(2)
                with open("Disadvantages.txt", "r") as file:
                  print(file.read())
                  print()
              
              #Frist aid
              elif B in ['5.1','51','first aid','firstaid','First aid']:
                  img = cv2.imread('First aid.jpg')
                  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                  plt.imshow(img)
                  plt.axis('off')
                  plt.show()
                  print()
                  time.sleep(2)
                  with open("First aid.txt", "r") as file:
                    print(file.read())
                    print()
              elif B in ['5','first aid kit','firstaid kit','First aid kit','kit','my first aid kit']:
                  img = cv2.imread('First aid kit.jpg')
                  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                  plt.imshow(img)
                  plt.axis('off')
                  plt.show()
                  print()
                  time.sleep(2)
                  with open("First aid kit.txt", "r") as file:
                    print(file.read())
                    print()
                  time.sleep(2)
                  with open("What should I keep in my first aid kit.txt", "r") as file:
                    print(file.read())
                    print()  
                    
              #BMI
              elif B in ['6','bmi value','bmi value be known','body mass index value','body mass index value be known']:
                  with open("bmi.txt", "r") as file:
                    print(file.read())
                    print()
                    time.sleep(2)
                  with open("known.txt", "r") as file:
                    print(file.read())
                    print()
              elif B in ['6.2','62','range','bmi range','bmi calculated','body mass index range','body mass index calculated']:
                  with open("range.txt", "r") as file:
                    print(file.read())
                    print()
                    time.sleep(2)
                  with open("calculate.txt", "r") as file:
                    print(file.read())
                    print()
                    
              elif B in ['7','exit','quit','leave','esc','close','finished']:
                break
            
              else:
                print("Sorry,"+"\U0001F625 " "I Could Not Understand Their Need.\nPlease enter your opinion in the feedback.Thank you"+"\U0001F917 \n")

    except:
        print("Error,"+"\U0001F625 " "File is not available.\nThank You! "+"\U0001F917 \n")

feedback = input("Feedback : If there are any updates or bugs in this bot please enter your comment \n")
time.sleep(2)
print()

a=np.array([x])
b=np.array([y])
c=np.array([z])

frame={ "Name":a, "Phone Number":b, "Email":c, "Date & Time":formatted_time, "User question":user_question,"Key word":A,"User Feedback":feedback}
df=pd.DataFrame(frame)
database = "Demo Bot.sqlite"
conn = sqlite3.connect(database)
df.to_sql(name='Collected Data', con=conn,if_exists='append',index=False)
conn.close()
