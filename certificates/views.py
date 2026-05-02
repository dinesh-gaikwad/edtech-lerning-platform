from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
import uuid
from datetime import datetime
from .models import Certificate
from academy.models import Course

@login_required
def generate_certificate(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    
    # Create or get existing certificate
    cert, created = Certificate.objects.get_or_create(
        user=request.user,
        course=course,
        defaults={'certificate_id': str(uuid.uuid4())[:8].upper()}
    )
    
    # Create PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="certificate_{cert.certificate_id}.pdf"'
    
    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4
    
    # Certificate design
    p.setFont("Helvetica-Bold", 36)
    p.drawCentredText(width/2, height-150, "CERTIFICATE OF COMPLETION")
    
    p.setFont("Helvetica", 18)
    p.drawCentredText(width/2, height-250, "This is to certify that")
    
    p.setFont("Helvetica-Bold", 28)
    p.drawCentredText(width/2, height-300, request.user.get_full_name() or request.user.username)
    
    p.setFont("Helvetica", 18)
    p.drawCentredText(width/2, height-350, f"has successfully completed the course")
    
    p.setFont("Helvetica-Bold", 24)
    p.drawCentredText(width/2, height-400, course.title)
    
    p.setFont("Helvetica", 14)
    p.drawCentredText(width/2, height-500, f"Issued on: {datetime.now().strftime('%B %d, %Y')}")
    p.drawCentredText(width/2, height-550, f"Certificate ID: {cert.certificate_id}")
    
    # Border
    p.rect(50, 50, width-100, height-100, stroke=1, fill=0)
    
    p.save()
    return response