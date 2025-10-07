print("HY,there")
name=input("ENTER UR NAME:")
rollno=input("ENTER UR ROLL NO:")
marks=list(map(int,input("ENTER UR ENG-URDU-MATHS-PHYS-CS marks respectively:").split()))
totalno=sum(marks)
print(f"TOTAL NUMBERS U GAINED ARE:{totalno}")
percentage=(totalno/500)*100
print(f"YOUR PERCENTAGE IS {percentage}")
print("-----------------REPORT CARD--------------------")
print(f"name   :{name}")
print(f"rollno   :{rollno}")
print("--------------------------------------------------")
print(f"PERCENTAGE   :{percentage}")

