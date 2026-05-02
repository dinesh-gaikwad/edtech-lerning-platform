from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course

def course_list(request):
    courses = Course.objects.all().order_by('-created_at')
    return render(request, 'academy/course_list.html', {'courses': courses})

@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'academy/course_detail.html', {'course': course})