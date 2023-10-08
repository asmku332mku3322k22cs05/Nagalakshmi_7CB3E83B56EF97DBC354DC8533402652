"" "" ""
Implement a function called sort_students that takes a list 
of student objects as input and sorts the list based on their CGPA (Cumulative Grade Point Average) in descending order. 
Each student object has the following attributes: name (string), roll_number (string), and cgpa (float).
Test the function with different input lists of students.
"" "" ""

class student:

  def__int__(self,name,roll_number.cgpa):
     self.name=Name
     self.roll_number=roll_number
     self.cgpa=cgpa


def.sort_students(student_list):
  #sort the list of student in descending order of CGPA
  sorted_student=sorted(student_list,
                       key=lambda student:student.cgpa,reverse=true)

#syntax_lamda arg:Exp 
return sorted_students


#exmple usage:
student =[
          student ("hari","A123",7.8),
          student ("swetha","A124", 8.9)
          student ("saumya","A125",9.1)
          student ("muthu","126",9.9)
]

sorted_student =sort_student (student)

#print the sorted lust if students
for student in sorted_student:
  print("name:{},roll number: {},CGPA:{}",formed(student.name))
student.rollnumber

                   student.cgpa))