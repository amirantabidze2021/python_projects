print("მოგესალმები კომპიუტერის ქვიზში!")

playing=input("გინდა ვითამაშოთ? ")

if playing.lower() != "დიახ" :
    quit()

print("კარგი! ვითამაშოთ :) ")
score=0
#პირველი კითხვა
answer=input("როგორ იშიფრება CPU ?  ")

if answer.lower() == "central processing unit" :
    print("მართალი ხარ!")
    score+=1
else:
    print("არასწორი ხარ !")
#მეორე კითხვა
answer=input("როგორ იშიფრება RAM?  ")

if answer.lower() == "random access memory" :
    print("მართალი ხარ ! ")
    score+=1
else:
    print("არასწორი ხარ!")
#მესამე კითხვა
answer=input("როგორ იშიფრება GPU?   ")

if answer.lower() == "graphics processing unit" :
    print("მართალი ხარ!")
    score+=1
else:
    print("არასწორი ხარ!")

print("შენ მიიღე " + str(score) + " ქულა  ")
print("შენ დააგროვე " + str((score/3)*100) + "  % " )


