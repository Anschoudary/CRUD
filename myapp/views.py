from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm

def home(request):
    if request.method == 'POST':
        if 'create' in request.POST:
            form = StudentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        elif 'update' in request.POST:
            student_id = request.POST.get('student_id')
            student = get_object_or_404(Student, id=student_id)
            form = StudentForm(request.POST, instance=student)
            if form.is_valid():
                form.save()
                return redirect('home')
    else:
        form = StudentForm()

    students = Student.objects.all()
    return render(request, 'index.html', {'students': students, 'form': form})

def edit(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(instance=student)
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students, 'form': form, 'edit_id': id})

def delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('home')
    students = Student.objects.all()
    form = StudentForm()
    return render(request, 'index.html', {'students': students, 'form': form, 'delete_id': id})
