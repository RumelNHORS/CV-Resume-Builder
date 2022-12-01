from django.shortcuts import render, redirect
from . forms import ProfileForm
from . models import ResumeProfile
from django.contrib import messages
from django.http import HttpResponse

from django.template import loader
#import pdfkit
#import io
#import wkhtmltopdf

#Import PDF stuff
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


def Cv_BuildView(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()   
            form = ProfileForm()
            messages.success(request,('Data Added Successfully!'))
            return redirect('resume_view')
            
    else:
        form = ProfileForm()
    return render(request, 'show.html', {'form':form})
    
def Resume(request, id):
    resum_profile = ResumeProfile.objects.get(pk=id)
    return render(request, 'resume.html', {'resum_profile':resum_profile})


def Resume_pdf(request, id):
    #Create a Bytestrim
    buf = io.BytesIO()
	#Create a canvase
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)	
	#Create a Text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont('Helvetica', 10)

    resum_profile = ResumeProfile.objects.filter(pk=id)

    #Creat a blank list
    lines = []

    for r in resum_profile:
        lines.append(r.name)
        lines.append(r.phone)
        lines.append(r.email)
        lines.append(r.address)
        lines.append(r.school)
        lines.append(r.result)
        lines.append(r.collage)
        lines.append(r.degree)
        lines.append(r.uni_versity)
        lines.append(r.skill)
        lines.append(r.work_exprince)
        lines.append(r.about_you)

    #loop here
    for line in lines:
        textob.textLine(line)

	#Finish up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    #Return something
    return FileResponse(buf, as_attachment=True, filename='resume.pdf')


"""#generate a view for pdf file
def venue_pdf(request):
	#Create a Bytestrim
	buf = io.BytesIO()
	#Create a canvase
	c = canvas.Canvas(buf, pagesize=letter, bottomup=0)	
	#Create a Text object
	textob = c.beginText()
	textob.setTextOrigin(inch, inch)
	textob.setFont('Helvetica', 10)

	#Add some lines of text
	#lines = [
	#	'This is line 1',
	#	'This is line 1',
	#	'This is line 1',
	#]

	#Designet The Model
	venues = Venue.objects.all()

	#Creat a blank list
	lines = []

	for venue in venues:
		lines.append(venue.name)
		lines.append(venue.address)
		lines.append(venue.Zip_code)
		lines.append(venue.phone)
		lines.append(venue.web)
		lines.append(venue.email_address)
		lines.append('==========')


	#loop here
	for line in lines:
		textob.textLine(line)

	#Finish up
	c.drawText(textob)
	c.showPage()
	c.save()
	buf.seek(0)

	#Return something
	return FileResponse(buf, as_attachment=True, filename='venue.pdf')
"""

"""
    template = loader.get_template("resume.html")
    html = template.render({'resum_profile':resum_profile})
    option = {
        'page-size' : 'Letter',
        'encoding': 'UTF-8'
    }
    pdf = pdfkit.from_string(html, False, option)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
"""
    