# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer
import random

# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response("hello world!")

# 갯수가 주어졌을 때, 주어진 갯수만큼 랜덤한 퀴즈를 반환하는 API
@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizes = Quiz.objects.all()
    randomQuizes = random.sample(list(totalQuizes), id)
    serializer = QuizSerializer(randomQuizes, many = True)
    return Response(serializer.data)