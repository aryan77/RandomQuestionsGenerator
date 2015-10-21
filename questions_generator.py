from random import randint
import csv

#The array below must be edited manually so that it contains
#the number element i contains the number of questions at the end
#of the (i+1)th chapter in the David Alcorn Tony Banksbook
questions_per_exercise = \
[10, 12, 13, 9, 10, 12, 17, 19, 20, 9, 10, 12, 13, 9, 10, 12, 17, 19, 20, 9,\
 10, 12, 13, 9, 10, 12, 17, 19, 20, 9, 10, 12, 13, 9, 10, 12, 17, 19, 20, 9]
 
#See if the log file exists if so load all the data from it
chapters_questions = {}
first_run = 1

try:
    f =  open("remaining_qs_donotdelete.log.txt", "r")
    for key, value in csv.reader(f):
        temp = value[1:-1].split(',')
        if len(temp[0]) > 0:
            chapters_questions[key] = [int(i) for i in temp]
        else:
            chapters_questions[key] = []
    f.close()
    first_run = 0
    print('\nYour log file has been successfully loaded')
except IOError:
        print('\nCan not open file remaining_qs_donotdelete.log.txt')
        print('\nPossibly the file doesn\'t exist because this is your first run')
        print('\nContinuing to generate a fresh set of exam questions for you\n\n')
        
#Below is the dictionary containing keys = Chapters and values = unanswered questions
#initially the array sizes are set in accordance to the array questions_per_exercise
if bool(first_run):
    chapters_questions = {}
    for chapter , questions in enumerate(questions_per_exercise):
        p = "Chapter_"+str(chapter+1).zfill(2)
        chapters_questions[p] = []
        for i in range(questions):
            chapters_questions[p].append(i+1)
    print('\nA brand new log file has been created which will keep track of your')
    print('\nremaining unanswered questions its called remaining_qs_donotdelete.log.txt')
else:
    print('\nStand by for new exam questions')
    
#Now randomly select a Chapter, and a question from within 
#that Chapter. To make this code robust we shall use a inefficient
#approach of first making a list of Chapters that still have questions
#that need answering, this list will be called incomplete chapters

#Forming a list of all the chapters that still contain unanswered questions
incomplete_chapters = []
for chapter in chapters_questions:
        if len(chapters_questions[chapter]) > 0:
            incomplete_chapters.append(chapter)
            
#Select 25 different chapters and corresponding questions 
#The Questions are poped from the list
number_of_exam_questions = 25
exam = {}
if number_of_exam_questions - 1 < len(incomplete_chapters):
    for i in range(number_of_exam_questions):
        p = randint(0,len(incomplete_chapters)-1)
        selected_chapter = incomplete_chapters.pop(p)
        p = randint(0,len(chapters_questions[selected_chapter])-1)
        p = chapters_questions[selected_chapter].pop(p)
        exam[selected_chapter]  = p

#Print the exam to the terminal
print("\nYour randomly selected exam questions are:\n")
for key, value in sorted(exam.items()): print (key, 'Question', value)  

#Write the exam to a txt file
try:
    f=open("exam_questions.txt", "w")
    w = csv.writer(f)
    for key, value in sorted(exam.items()):
        w.writerow([key,' Question', value])
    f.close()
    print('\nYour new exam questions are also listed in the file exam_questions.txt, good luck')
except IOError:
    print('\nI could not create the file exam_questions.txt, sorry')

#Write the remaining unanswered questions to log.txt file
f=open("remaining_qs_donotdelete.log.txt", "w")
w = csv.writer(f)
for key, value in sorted(chapters_questions.items()):
    w.writerow([key, value])
f.close()
