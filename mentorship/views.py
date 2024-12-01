
from .models import Mentor, Student
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Mentor




def home(request):
    return render(request, 'home.html') 


def mentor(request):
    mentors = Mentor.objects.all()
    return render(request,'mentor.html', {'mentors': mentors})




def student(request):
    students = Student.objects.all()
    return render(request, 'student.html', {'students': students})





def mentor_details(request, mentor_id):
    mentor = get_object_or_404(Mentor, id=mentor_id) 
    students = mentor.student_set.all() 
    return render(request, 'mentorship/mentor_details.html', {
        'mentor': mentor,
        'students': students})
        



def student_details(request, student_id):
    # Fetch the specific student
    student = get_object_or_404(Student, id=student_id)
    # Fetch the related mentor and course
    mentor = student.mentor
    course = student.course
    # Pass the data to the template
    return render(request, 'mentorship/student_details.html', {
        'student': student,
        'mentor': mentor,
        'course': course,
    })




