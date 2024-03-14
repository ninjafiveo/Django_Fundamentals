from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import random
from .magic_eight_ball import RESPONSES

def home(request):
    return HttpResponse("Welcome to the Ninja App!")

def eight_ball(request):
    question = request.GET.get('question', '')  # Get the question from the request
    response = random.choice(RESPONSES) if question else ''
    return render(request, 'ninja_app/eight_ball.html', {'response': response, 'question': question})

#? Here, random.choice(RESPONSES) selects a random response from the RESPONSES list. The render function then renders the eight_ball.html template, passing the selected response as context.