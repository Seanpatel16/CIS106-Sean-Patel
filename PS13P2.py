class Student:    
  def assign (self,first_name,last_name,district_code,enrolled_credits):    
    self.first_name=first_name
    self.last_name=last_name
    self.district_code=district_code
    self.enrolled_credits=enrolled_credits
    pass 
  def tution_owned(self):
    if self.district_code=="I":
      tut=250.00 
    else:
      tut=500.00 
    return tut 

s1=Student("Sean","Patel","I",17)
print("First Name is:",s1.first_name)
print("Last Name is:",s1.last_name)
print("The tution owned is:",s1.tution_owned())