from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index_page(request):
    current_time = datetime.now()
    formatted_date = current_time.strftime("%d.%m.%Y")
    formatted_time = current_time.strftime("%H:%M:%S")
    context = {
        "title": "Курс 'Промышленное программирование'",
        "lesson": "Занятие N12",
        "topic": "Тема: Знакомство с Django",
        "current_date": formatted_date,
        "current_time": formatted_time
    }
    return render(request, "index.html", context)
def riddle_page(request):
    context = {
        "title": "Курс 'Промышленное программирование'",
        "riddle": "Сидит в темнице, красная девица, а коса на улице.",
        "url1": "http://127.0.0.1:8000/answer"
    }
    return render(request, "riddle.html", context)
def answer_page(request):
    context = {
        "title": "Курс 'Промышленное программирование'",
        "answer": "Морковь.",
        "url2": "http://127.0.0.1:8000/riddle"
    }
    return render(request, "answer.html", context)