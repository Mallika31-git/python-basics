students=int(input("enter number of students:"))
marks_list=[]
 
for i in range(students):
    marks=int(input(f"enter student no.{i+1} marks: "))
    marks_list.append(marks)
highest_marks=max(marks_list)
lowest_marks=min(marks_list)
average_marks=sum(marks_list)/len(marks_list)
 
above=0
below=0
 
for i in  marks_list:
    if i>average_marks:
         above+=1
    elif i<average_marks:
        below+=1
     
    
    

report=f"""
highest marks                           :  {highest_marks}
lowest marks                            :  {lowest_marks}
average marks                           :  {average_marks}
number of students who got above average:  { above}
number of students who got below average:  { below}"""
print("...........................STUDENTS MARKS............................")
print(report)
print(".....................................................................")

 
 
 
