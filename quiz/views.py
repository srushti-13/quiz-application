from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def home(request):
    courses=Course.objects.all()
    context={'courses': courses}
    return render(request , 'home.html',context)

from django.http import JsonResponse
from .models import Question

def api_question(request, id):
    questions = []
    raw_questions = Question.objects.filter(Course=id)[:20]  # Assuming 'Course' is a field in your 'Question' model

    for raw_question in raw_questions:
        question = {}
        question['question'] = raw_question.question  # Accessing the 'question' field
        question['answer'] = raw_question.answer
        question['marks']= raw_question.marks

        options = []
        options.append(raw_question.option_one)
        options.append(raw_question.option_two)
        
        if raw_question.option_three !="":
            options.append(raw_question.option_three)
        if raw_question.option_four !="":
            options.append(raw_question.option_four)

        question['options'] = options
        questions.append(question)

    return JsonResponse(questions, safe=False)

        
        
def View_score(request):
    user=request.user
    score=ScoreBoard.objects.filter(user=user)
    context={'score':score}
    return render(request,'score.html',context)
    
    
    
    
def take_quiz(request,id):
    context={'id':id}
    return render(request ,'quiz.html',context)

@csrf_exempt
def check_score(request):
    data=json.loads(request.body)
    user=request.user
    course_id =data.get('course_id')
    solutions=json.load(data.get('data'))
    course= Course.objects.get(id=course_id)
    score=0
    for solution in solutions:
        Question=Question.objects.filter(id=solution.get('question_id')).first()
        if str(Question.answer )== solution.get('options'):
            score=score+Question.marks
            
    score_board=ScoreBoard(course=Course,score=score,user=user)  
    score_board.save()       
        
    return JsonResponse({'message':"success",'status':True})