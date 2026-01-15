import result
student_name = input("enter student name :")
english =int(input("english enter marks :"))
sanskrit =int(input("sankrit enter marks :"))
maths_1A=int(input("maths_1A enter marks :"))
maths_1B=int(input("maths_1B enter marks :"))
chemistry = int(input( "chemistry enter marks :"))
physics= int(input("physics enter marks :"))
total =  english+sanskrit+maths_1A+ maths_1B +chemistry+physics
persentag = (total/470)*100

print("\n---result---")
print("studentname :",student_name)
print("english :",english)
print("sankrit :",sanskrit)
print("maths_1A :",maths_1A)
print("maths_1B :",maths_1B)
print("chemistry :",chemistry)
print("physics :",physics)
print("persentag :",persentag,"%")
# pass or fail status
if persentag >=50:
 print("status : pass")
else:
 print("status :fail")