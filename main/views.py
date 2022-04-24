from os import access
from django.shortcuts import redirect, render
from django.views.generic import View
from .models import *

from rest_framework import views
from rest_framework.response import Response


class APICreateUserForm(views.APIView):
    def post(self, request):
        newUser = UserForm.objects.create(
            name=request.data['name'],
            surname=request.data['surname'],
            years=request.data['years'],
            email=request.data['email'],
            country=request.data['country'],
        )

        return Response({}, status=200)



class Index(View):
    def get(self, request):
        return render(request, 'index.html')

class QuizPage(View):
    def get(self, request, pk, quest):

        try:
            context= {
            "question": Quiz.objects.get(pk=pk).questions.all()[int(quest)],
            "next": int(quest) + 1,
            "quiz": pk,
            "count": len(Quiz.objects.get(pk=pk).questions.all())
            }
        except:
            return redirect("quiz_list")

        return render(request, 'quiz.html', context=context)

class QuizList(View):
    def get(self, request):

        context = {"list": Quiz.objects.all()}

        return render(request, 'quiz_list.html', context=context)


class FormPage(View):
    def get(self, request):
        return render(request, 'form.html')

    def post(self, request):

        newUser = UserForm.objects.create(
            name=request.POST['name'],
            surname=request.POST['surname'],
            years=request.POST['years'],
            email=request.POST['email'],
            country=request.POST['country'],
        )
        return redirect("index")


class ProposePage(View):
    def get(self, request):
        return render(request, 'propose.html')

    def post(self, request):

        newPropose = ProposeForm.objects.create(
            title=request.POST['title'],
            topic=request.POST['topic'],
            description=request.POST['description']
        )

        return redirect("index")