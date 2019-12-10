import requests
import json

url="http://saral.navgurukul.org/api/courses"
courses_ids=[]
def firstApi(url):
	get_api=requests.get(url)
	response=get_api.json()
	load_data=response["availableCourses"]
	b=1
	for index in load_data:
		courses_ids.append(index["id"])
		print b, index["name"],index["id"]
		b=b+1
	return courses_ids
url="http://saral.navgurukul.org/api/courses"			
courses=firstApi(url)
print courses

user_choice_course=input("enter no which course you want")
course_id=courses_ids[user_choice_course-1]
print course_id

url2=url+"/"+str(course_id)+"/"+"exercises"
exercise_id_list=[]
def getExerciseData(second_url):
	get_second_url=requests.get(second_url)
	response=get_second_url.json()
	load_exercise=response["data"]
	a=1
	for index in load_exercise:
		exercise_id_list.append(index["id"])
		print a,index["name"],index["id"]
		childExerciseData=index["childExercises"]
		count=0
		for index1 in childExerciseData:
			print "\t",count,index1["name"]
			count=count+1
		a=a+1 
	return exercise_id_list
url2=url+"/"+str(course_id)+"/"+"exercises"
EXERCISE=getExerciseData(url2)

exercises_dict={}
slug_list=[]
def getChildExercise(user_choice):
	get_second_url=requests.get(url2)
	response=get_second_url.json()
	load_exercise=response["data"]
	exercise_id=exercise_id_list[user_choice]
	a=1
	for index in load_exercise:
		if exercise_id == index["id"]:
			exercises_dict["id"]=exercise_id
			slug_list.append(index["slug"])
			print index["name"]
			count=0
			child=index["childExercises"]
			for index1 in child:
				slug_list.append(index1["slug"])
				print count,index1["name"]
				count=count+1
		a=a+1
	exercises_dict["slug"]=slug_list
	return exercises_dict
user=input("enter no.")
load_child=getChildExercise(user-1)
print load_child
#http://saral.navgurukul.org/api/courses/1048/exercises/getBySlug?slug=python__files/files-question1

slug_choise=exercises_dict["slug"]
print slug_choise
exercise_id=exercises_dict["id"]
print exercise_id

exercise_slug=input("which id and slug you want")
choose_exercise=slug_choise[exercise_slug-1]
print choose_exercise

def getContent(url3):
	get_content=requests.get(url3)
	print get_content
	content_json=get_content.json()
	content=content_json["content"]
	print content
api3=url+"/"+str(exercise_id)+"/"+"exercise"+"/"+"getBySlug?slug="+str(choose_exercise)
getContent(api3)
print api3

while True:
	user_input=raw_input("enter you want previous so print P and you want next so print N and courses ke liye up dalo")
	num1=1
	if user_input=="n":
		next_step=exercise_slug+num1
		if next_step <=len(slug_choise):
			choose_slug=slug_choise[next_step-1]
			print choose_slug
			api3=url+"/"+str(exercise_id)+"/"+"exercise"+"/"+"getBySlug?slug="+str(choose_slug)
			getContent(api3)
			exercise_slug=exercise_slug+1
		else:
			print "not page there"
	elif user_input == "p":
		previous_step=exercise_slug-num1
		if previous_step>0:
			previous_slug=slug_choise[previous_step-1]
			print previous_slug
			api3=url+"/"+str(exercise_id)+"/"+"exercise"+"/"+"getBySlug?slug="+str(previous_slug)
			getContent(api3)
			exercise_slug=exercise_slug-1
		else:
			print "there is no page"
	elif user_input == "up":
		courses=firstApi(url)
		print courses
		break
			