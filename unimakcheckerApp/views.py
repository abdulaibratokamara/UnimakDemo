from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *


# Create your views here.


def dashboard(request):
    students = Student.objects.all()
    total_students = students.count()

    Graduated = students.filter(category='Graduated').count()
    Finance = students.filter(category='Check Finance').count()
    FinanceRegistry = students.filter(category='Check Finance and Registry').count()
    Registry = students.filter(category='Check Registry').count()
    ExamsOffice = students.filter(category='Check Exams Office').count()

    paginator = Paginator(students, 6)
    page_number = request.GET.get('page')
    student_list = paginator.get_page(page_number)

    context = {'students': students, 'total_students': total_students, 'Graduated': Graduated, 'Finance': Finance,
               'FinanceRegistry': FinanceRegistry, 'Registry': Registry, 'ExamsOffice': ExamsOffice,
               'page_number': page_number, 'student_list': student_list}
    return render(request, 'dashboard.html', context)


def home(request):
    students = Student.objects.all()
    total_students = students.count()

    Graduated = students.filter(category='Graduated').count()
    Finance = students.filter(category='Check Finance').count()
    FinanceRegistry = students.filter(category='Check Finance and Registry').count()
    Registry = students.filter(category='Check Registry').count()
    ExamsOffice = students.filter(category='Check Exams Office').count()

    paginator = Paginator(students, 6)
    page_number = request.GET.get('page')
    student_list = paginator.get_page(page_number)

    context = {'students': students, 'total_students': total_students, 'Graduated': Graduated, 'Finance': Finance,
               'FinanceRegistry': FinanceRegistry, 'Registry': Registry, 'ExamsOffice': ExamsOffice,
               'page_number': page_number, 'student_list': student_list}
    return render(request, 'home.html', context)


def student(request):
    students = Student.objects.all()
    paginator = Paginator(students, 6)
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)
    context = {'students': students, 'cartItems': cartItems, 'page_number': page_number, 'product_list': product_list}
    return render(request, 'product.html', context)


def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            students = Student.objects.filter(studid__icontains=query)
            return render(request, 'searchbar.html', {'students': students})
        else:
            print("No information to show")
            return render(request, 'searchbar.html', {})
