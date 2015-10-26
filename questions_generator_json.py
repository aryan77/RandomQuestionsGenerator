from random import randint
import json

#The array below must be edited manually so that element number i contains the 
#number of questions at the end of the (i+1)th chapter in the David Alcorn Tony Banks book
questions_per_exercise = \
[13, 18, 22, 19, 22, 7, 13, 14, 10, 19, 19, 18, 11, 14, 6, 15, 11, 6, 19, 16,\
 10, 5, 10, 8, 12, 4, 11, 15, 9, 15, 18, 10, 5, 11, 7, 6, 7, 5, 4, 15]

#Select 21 different chapters and corresponding questions  
number_of_questions_per_exam = 21
 
#See if the log file exists if so load all the data from it
chapters_questions = {}
first_run = 1

try:
    f = open("remaining_qs_donotdelete.log.txt", "r")
    chapters_questions = json.load(f)
    first_run = 0
    print('\nYour log file has been successfully loaded')
except IOError:
        print('It looks like this is your first run! (because log file not found)')
        print('Continuing to generate a fresh set of exam questions for you\n\n')
        
#Below is the dictionary containing keys = Chapters and values = unanswered questions
#initially the array sizes are set in accordance to the array questions_per_exercise
if bool(first_run):
    chapters_questions = {}
    for chapter , questions in enumerate(questions_per_exercise):
        p = "Chapter_"+str(chapter+1).zfill(2)
        chapters_questions[p] = []
        for i in range(questions):
            chapters_questions[p].append(i+1)
    print('A brand new log file has been created which will keep track of your')
    print('remaining unanswered questions \'remaining_qs_donotdelete.log.txt\'')
else:
    print('Stand by for new exam questions')
    
#Calculating the number of exams that have taken place
i = 0
for p in chapters_questions:
    i += len(chapters_questions[p])
  
exams_completed = int((sum(questions_per_exercise)-i)/number_of_questions_per_exam) + 1
    
#Now randomly select a Chapter, and a question from within 
#that Chapter. To make this code robust we shall use a inefficient
#approach of first making a list of Chapters that still have questions
#that need answering, this list will be called incomplete chapters

#Forming a list of all the chapters that still contain unanswered questions
incomplete_chapters = []
for chapter in chapters_questions:
        if len(chapters_questions[chapter]) > 0:
            incomplete_chapters.append(chapter)
            

#The Questions are poped from the list

exam = {}
if number_of_questions_per_exam - 1 < len(incomplete_chapters):
    for i in range(number_of_questions_per_exam):
        p = randint(0,len(incomplete_chapters)-1)
        selected_chapter = incomplete_chapters.pop(p)
        p = randint(0,len(chapters_questions[selected_chapter])-1)
        p = chapters_questions[selected_chapter].pop(p)
        exam[selected_chapter]  = p
#Print the exam to the terminal (failsafe incase filewrite fails)
    print("Your randomly selected exam questions are:\n")
    i=1
    for key, value in sorted(exam.items()):
        print ("Q"+str(i)+":","from ",key, ' Question', value)  
        i+=1
#Write the exam to a txt file
    with open("exam_questions"+str(exams_completed)+".txt", "w") as f:
        i=1
        for key, value in sorted(exam.items()):
            f.write("Q{0}: from {1}\tQuestion {2}\n".format(i,key, value))
            i+=1
    print('\nYour new exam questions are also listed in the file exam_questions'+str(exams_completed)+'.txt, good luck')
#Write the remaining unanswered questions to log.txt file
    with open("remaining_qs_donotdelete.log.txt", "w") as f:
        json.dump(chapters_questions,f)
else:
    print('Not possible to print any more exam papers due to lack of chapters')
