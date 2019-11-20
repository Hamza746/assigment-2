a = int(input("enter physics marks: "))
b = int(input("enter chemistry marks:"))
c = int(input("enter mathmatics marks:"))
d = int(input("enter urdu marks:"))
e = int(input("enter islamiat marks:"))
f = int(input("enter english marks:"))
obtain_marks = (a+b+c+d+e+f)
print(obtain_marks)
total_marks = 550
percentage = (obtain_marks/total_marks)*100
print(percentage)
if a<=33 or b<=33 or c<=33 or d<=33 or e<=27 or f<=33:
	print("fail")
else:
    if percentage>=80:
	      print("A one")
    elif percentage>=70:
		    print("A grade")
    elif percentage>=60:
		    print("B grade")
    elif percentage>=50:
		    print("C grade")
    elif percentage>=40:
	      print("D grade")
    else:
            print("fail")
            