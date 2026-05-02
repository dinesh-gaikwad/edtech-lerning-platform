from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def download_certificate(request, course_id):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="certificate_{course_id}.pdf"'
    
    p = canvas.Canvas(response)
    p.setFont("Helvetica-Bold", 24)
    p.drawCentredText(300, 700, "Certificate of Completion")
    p.setFont("Helvetica", 16)
    p.drawCentredText(300, 650, f"This is to certify that")
    p.setFont("Helvetica-Bold", 20)
    p.drawCentredText(300, 620, f"{request.user.email}")
    p.setFont("Helvetica", 16)
    p.drawCentredText(300, 590, f"has successfully completed Course #{course_id}")
    p.drawCentredText(300, 400, "Dinesh EdTech Platform")
    p.showPage()
    p.save()
    return response