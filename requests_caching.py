import requests
import json
import os.path
courses=""
def API_CALLING(Api):
	files="courses.json"
	if os.path.exists(files):
		json_file=open(files,"r")
		data1=json_file.read()
		file=json.load(data1)
		courses=data1["availableCourses"]
		return courses
	else:
		data=requests.get(Api)   
		num=data.json()                                                   #    https://www.youtube.com/watch?v=UN0CrDqhXQI
		file= open("courses.json","w")  
		k=json.dumps(num)             
		file.write(k)
		file.close()
url="http://saral.navgurukul.org/api/courses"
courses=API_CALLING(url)

print "-------------------"

courses_list=[]
def get_courses():  
	b=1
	for index in courses:
		print str(b),index["name"],index["id"]
		courses_list.append(index["id"])
		b=b+1
	print " "
	return courses_list
course_list= get_courses()
print course_list

user_input=input("enter which courses you want ")
courses_id=courses_list[user_input-1]
print courses_id

def write_Exercise_Data(api2):
	filename="files/exercise"+str(courses_id)+".json"
	if os.path.exists(filename):
		Exercise_json_file=open(filename,"r+")
		Exercise_data=Exercise_json_file.read()
		dict_data=json.loads(Exercise_data)
		exercise_id_data=dict_data["data"]
		return exercise_id_data		
	else:
		exersice_data=requests.get(api2)
		num1=exersice_data.json()
		json_file1=open(filename,"w")
		k1=json.dumps(num1)
		json_file1.write(k1)
		json_file1.close()
		return filename
url2=url+"/"+str(courses_id) + "/exercises"
exercises = write_Exercise_Data(url2)

EXERCISE_ID_LIST=[]
def Get_Exercise_Name():
	count=1
	for index in exercises:
		print count,index["name"],index["id"]
		EXERCISE_ID_LIST.append(index["id"])
		childexercise=index["childExercises"]
		b=1
		for index in childexercise:
			print "\t",str(b),index["name"],index["id"]
			b=b+1
		count=count+1
	return EXERCISE_ID_LIST
EXERCISE_ID_LIST=Get_Exercise_Name()
print EXERCISE_ID_LIST

user1=input("enter one number which id and slug you want")
exercise_slug=[]
Exercise_id=0
def User_Choice_Exercise_slug(user2):
	count=1
	Exercise_id=EXERCISE_ID_LIST[user2]
	for exercise in exercises:
		if Exercise_id == exercise["id"]:
			exercise_slug.append(exercise["slug"])
			print (count),exercise["name"]
			childexercise=exercise["childExercises"]
			count=count+1
			for index in childexercise:
				exercise_slug.append(index["slug"])

				print (count),index["name"],index["id"]
				count=count+1
			count=count+1
	return exercise_slug
exercise_slug=User_Choice_Exercise_slug(user1-1)
print exercise_slug

childexercise_id=[]
def get_slug_choice(user2):	
	Exercise_id=EXERCISE_ID_LIST[user2-1]
	for exercise in exercises:
		if Exercise_id == exercise["id"]:
			childexercise_id.append(exercise["id"])
			childexercise=exercise["childExercises"]
			for index in childexercise:
				childexercise_id.append(index["id"])
	return childexercise_id	
childexercise_id = get_slug_choice(user1-1)
print childexercise_id


slug_input=input("enter the childExercise which slug you want")
getBySlug=exercise_slug[slug_input-1]
print getBySlug

choose_id=childexercise_id[slug_input-1]
print choose_id

def User_Choice_Exercise_Content(api3):
	content_file="slug/childexercise"+str(choose_id)+".json"
	if os.path.exists(content_file):
		data=open(content_file,"r+")
		file_json=data.read()
		slug_load=json.loads(file_json)
		content_data=slug_load["content"]
		return content_data
	else:
		responce=requests.get(api3)
		data1=responce.json()
		content=open(content_file,"w")
		data=json.dumps(data1)
		content_data=content.write(data)
		content.close()
		# return content_file
url3=url+"/"+str(choose_id)+"/"+"exercise"+"/"+"getBySlug?slug="+str(getBySlug)
content=User_Choice_Exercise_Content(url3)
print content
print url3


