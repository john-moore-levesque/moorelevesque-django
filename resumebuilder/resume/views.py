from django.shortcuts import render
from resume.models import Job, Duty, SubDuty, Technology, TechBullet, Link, Certifications

# Create your views here.
def resume_home(request):
    context = {}
    jobs = []
    techs = []
    links = []
    certs = []
    for job in Job.objects.all().order_by('end').reverse():
        start = job.start.strftime("%B %Y")
        if job.current:
            end = "present"
        else:
            end = job.end.strftime("%B %Y")
        title = job.title
        company = job.company
        duties = {}
        for duty in Duty.objects.all():
            if duty.job == job:
                if duty not in duties.keys():
                    duties[duty] = []
                for subduty in SubDuty.objects.all():
                    if subduty.duty == duty:
                        duties[duty].append(subduty)
        
        jobs.append({ 'start': start, 'end': end, 'title': title, 'company': company, 'duties': duties })
    
    for tech in Technology.objects.all():
        bullets = []
        for bullet in TechBullet.objects.all():
            if bullet.tech == tech:
                bullets.append(bullet.bullet)
        techs.append((tech, bullets))
    

    for link in Link.objects.all():
        links.append((link.link, link.name))
    
    for cert in Certifications.objects.all():
        name = cert.cert
        url = cert.link
        badge = cert.badge
        certs.append({"name": name, "badge": badge, "link": url})
    
    context = {"jobs": jobs, "techs": techs, "links": links, "certs": certs}
    return render(request, 'index.html', context)