class DoesNotExist(Exception):# all ready python lo DoesNotExist ane error ledu kanuka class lo define chesukunam
	pass                      

class MultipleObjectsReturned(Exception):
	pass

class InvalidField(Exception):
	pass

class Student:
	def __init__(self, name, age, score):
		self.name = name
		self.student_id = None
		self.age = age
		self.score = score

	@classmethod
	def get(cls,**kwargs): # **kwargs is used to multiple aurguments at a time  
		
		for k,v in kwargs.items():
			cls.column = k
			cls.value = v
			#print(k,v)	  
		if cls.column not in ('student_id','name','age','score'):
			raise InvalidField('InvalidField')
			
		if cls.column == 'name':
			record = read_data(f"select * from Student where {cls.column} = \'{cls.value}\'") #  f is nothing but  .formate()
		else:
			record = read_data(f"select * from Student where {cls.column} = {cls.value}") #  f is nothing but  .formate()
			#print(record)
		if len(record)==0:
			raise DoesNotExist('DoesNotExist')
		elif len(record)>1:
			raise MultipleObjectsReturned('MultipleObjectsReturned')
		
		output = Student(record[0][1],record[0][2],record[0][3])
		output.student_id = record[0][0]
		return output

	def save(self):
		import sqlite3
		connection = sqlite3.connect("students.sqlite3")
		crsr = connection.cursor() 
		crsr.execute("PRAGMA foreign_keys=on;") 
		if self.student_id == None:
			crsr.execute(f"insert into Student (name,age,score) values (\'{self.name}\',{self.age},{self.score})")        
			self.student_id = crsr.lastrowid
		else:
			crsr.execute(f"update Student SET name=\'{self.name}\',age={self.age},score={self.score}")
		connection.commit()
		connection.close()

	def delete(self):
		write_data(f"delete from student where student_id={self.student_id}")
	
def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor()
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close()      
	return ans
# for check out puts :- new Terminal,sqlite3 students.sqlite3,create table,insert values
# print(read_data("select * from student;"))
# s = Student.get(student_id=4)
# s.name = 'lallu'
# s.save()
# print(read_data("select * from student;"))

