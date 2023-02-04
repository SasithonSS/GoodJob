from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from users.models import *
import qrcode
import matplotlib.pyplot as plt


def home(request):
    jobs_list = Job.objects.all()
    if request.method == "POST":
        searched = request.POST.get('searched','')
        jobs_searched = Job.objects.filter(name__contains=searched)
        return render(request, 'jobs/home.html', {'searched':searched,'jobs_searched': jobs_searched})
    else:
        return render(request, 'jobs/home.html', {'jobs_list': jobs_list})

def job_detail(request,job_id):
    jobs = Job.objects.filter(id=job_id)
    return render(request, 'jobs/job_detail.html', {'jobs': jobs})

@login_required(login_url='login')
def home_jobber(request):
    jobs_list = Job.objects.all()
    if request.method == "POST":
        searched = request.POST.get('searched','')
        jobs_searched = Job.objects.filter(name__contains=searched)
        return render(request, 'jobs/home_jobber.html', {'searched':searched,'jobs_searched': jobs_searched})
    else:
        return render(request, 'jobs/home_jobber.html', {'jobs_list': jobs_list})

def job_detail_jobber(request,job_id):
    users  = User.objects.filter(id=request.user.id)
    jobs = Job.objects.filter(id=job_id)
    return render(request, 'jobs/job_detail_jobber.html', {'jobs': jobs,'users': users})

def myjobs_detail_jobber(request,job_id):
    users  = User.objects.filter(id=request.user.id)
    jobs = Job.objects.filter(id=job_id)
    return render(request, 'jobs/myjobs_detail_jobber.html', {'jobs': jobs,'users': users})

def generate_qr(message,title):
    qr = qrcode.make(message)
    # Data to encode
    qr = qrcode.QRCode(version = 1,
                    box_size = 10,
                    border = 5)
    # Adding data to the instance 'qr'
    qr.add_data(message)
    qr.make(fit = True)
    img = qr.make_image(fill_color = 'black', back_color = 'white')
    img.save('jobs/static/jobs/images/qrcode/'+title+'.png')
    return 'jobs/static/jobs/images/qrcode/'+title+'.png'

def job_apply(request,job_id):
    users = User.objects.filter(id=request.user.id)
    jobs = Job.objects.filter(id=job_id)
    jobbb = Job.objects.get(id=job_id)
    if  ApplyJob.objects.filter(jobber=request.user.id,job=jobbb):
        failed_message = 'apply failed'
        return render(request, 'jobs/home_jobber.html', {'jobs': jobs, 'failed_message': failed_message,'users': users})
    else:
        job_apply = ApplyJob()
        job_apply.job = Job.objects.get(id=job_id)
        job_apply.jobber = JobberUser.objects.get(user_id=request.user.id)
        job_apply.emp_name = EmployerUser.objects.get(name=jobbb.emp_name)
        message = str("ร้าน \n"+str(request.user.first_name)+" : "+str(jobbb.name))
        title = str(str(request.user.username)+str(job_id))
        pic = generate_qr(message,title)
        job_apply.picture = pic
        job_apply.save()
        success_message = 'applied successfully'
        return render(request, 'jobs/job_apply.html', {'jobs': jobs,'success_message':success_message,'users': users})

def jobber_complain(request):
    job_applys = ApplyJob.objects.filter(jobber=request.user.id)
    subjects = JobberSubjectComplain.objects.all()
    jobs_lists = []
    emps_lists = []
    if  job_applys is not None:
        for job_apply in job_applys:
            jobs_lists.append(job_apply.job)
            emps_lists.append(job_apply.emp_name)
            context = {'jobs_lists': jobs_lists,'emps_lists': set(emps_lists),'subjects': subjects}
    else:
        context = {}
        return render(request, 'jobs/jobber_complain.html',context)
    if request.method == 'POST':
            jobber_complain = JobberComplain()
            jobber_complain.job = Job.objects.get(name=request.POST.get('job'))
            jobber_complain.jobber = JobberUser.objects.get(user_id=request.user.id)
            jobber_complain.emp_name = EmployerUser.objects.get(name=request.POST.get('emp_name'))
            jobber_complain.subject = JobberSubjectComplain.objects.get(subject=request.POST.get('subject'))
            jobber_complain.description = request.POST.get('description')
            jobber_complain.save()
            return redirect('myjobs_jobber',id=request.user.id)
    return render(request, 'jobs/jobber_complain.html', context)
    

def myjob_apply(request,job_id):
    apply_jobs  = ApplyJob.objects.filter(jobber=request.user.id,job=job_id)
    if apply_jobs is not None:
        context = {'apply_jobs': apply_jobs}
    return render(request, 'jobs/myjob_apply.html',context)

def emp_report(request):
    return render(request, 'jobs/emp_report.html')

def myjob_apply_detail(request,id):
    apply_jobs  = ApplyJob.objects.filter(id=id)
    if apply_jobs is not None:
        context = {'apply_jobs': apply_jobs}
        return render(request, 'jobs/myjob_apply_detail.html',context)
    

@login_required(login_url='login')
def home_emp(request):
    jobs_list = Job.objects.all()
    if request.method == "POST":
        searched = request.POST.get('searched','')
        jobs_searched = Job.objects.filter(name__contains=searched)
        return render(request, 'jobs/home_emp.html', {'searched':searched,'jobs_searched': jobs_searched})
    else:
        return render(request, 'jobs/home_emp.html', {'jobs_list': jobs_list})

def job_detail_emp(request,job_id):
    jobs = Job.objects.filter(id=job_id)
    return render(request, 'jobs/job_detail_emp.html', {'jobs': jobs})

def myjobs_emp(request,emp_name):
    jobs_emp = Job.objects.filter(emp_name_id=emp_name)
    users = User.objects.filter(id=emp_name)
    if jobs_emp is not None:
        context = {'jobs_emp': jobs_emp, 'users': users}
        return render(request, 'jobs/myjobs_emp.html', context)
    else :
        context = {}
        return render(request, 'jobs/myjobs_emp.html', context)

def myjobs_jobber(request,id):
    jobber = JobberUser.objects.get(user_id=id)
    apply_jobs  = ApplyJob.objects.filter(jobber=jobber)
    users = User.objects.filter(id=id)
    if apply_jobs is not None:
        context = {'apply_jobs': apply_jobs, 'users': users}
        return render(request, 'jobs/myjobs_jobber.html', context)
    else :
        context = {}
        return render(request, 'jobs/myjobs_jobber.html', context)

def delete_myjobs(request,id):
    apply_job = ApplyJob.objects.get(id=id)
    users = User.objects.filter(id=id)
    if apply_job :
        apply_job.delete()
        apply_jobs  = ApplyJob.objects.filter(jobber=request.user.id)
        context = {'apply_jobs': apply_jobs, 'users': users}
        return redirect('myjobs_jobber',id=request.user.id)
    else :
        apply_jobs  = ApplyJob.objects.filter(jobber=request.user.id)
        context = {'apply_jobs': apply_jobs, 'users': users}
        return render(request, 'jobs/myjobs_jobber.html', context)


def myjobs_emp_detail(request,job_id):
    jobs = Job.objects.filter(id=job_id)
    return render(request, 'jobs/myjobs_emp_detail.html', {'jobs': jobs})

def add_job(request,id):
    users = User.objects.filter(id=id)
    province = Province.objects.all()
    gender = Gender.objects.all()
    pay = Pay.objects.all()

    if request.method == 'POST':
        job = Job()
        job.name = request.POST.get('name')
        job.description = request.POST.get('description')
        job.phone = request.POST.get('phone')
        job.emp_name = EmployerUser.objects.get(name=request.POST.get('emp_name'))
        job.gender = Gender.objects.get(gender=request.POST.get('gender'))
        job.pay = Pay.objects.get(pay=request.POST.get('pay'))
        job.province = Province.objects.get(province=request.POST.get('province'))
        job.address = request.POST.get('address')
        job.location = request.POST.get('location')
        job.picture = request.FILES['picture']
        job.save()
        return redirect('myjobs_emp_detail',job_id=job.id)


    context = {'users': users,'gender': gender, 'province':province, 'pay':pay}

    return render(request, 'jobs/add_job.html', context)

def myjobs_emp_update(request,job_id):
    province = Province.objects.all()
    gender = Gender.objects.all()
    pay = Pay.objects.all()
    jobs = Job.objects.filter(id=job_id)
    if request.method == 'POST':
        job = Job.objects.get(id=job_id)
        job.name = request.POST.get('name')
        job.description = request.POST.get('description')
        job.phone = request.POST.get('phone')
        job.emp_name = EmployerUser.objects.get(name=request.POST.get('emp_name'))
        job.gender = Gender.objects.get(gender=request.POST.get('gender'))
        job.pay = Pay.objects.get(pay=request.POST.get('pay'))
        job.province = Province.objects.get(province=request.POST.get('province'))
        job.location = request.POST.get('location')
        job.picture = request.FILES['picture']
        job.save()
        return redirect('myjobs_emp_detail',job_id=job_id)

    context = {'gender': gender, 'province':province, 'pay':pay, 'jobs':jobs}

    return render(request, 'jobs/myjobs_emp_update.html', context)

@login_required(login_url='login')
def home_admin(request):
    jobs_list = Job.objects.all()
    if request.method == "POST":
        searched = request.POST.get('searched','')
        jobs_searched = Job.objects.filter(name__contains=searched)
        return render(request, 'jobs/home_admin.html', {'searched':searched,'jobs_searched': jobs_searched})
    else:
        return render(request, 'jobs/home_admin.html', {'jobs_list': jobs_list})

def job_detail_admin(request,job_id):
    jobs = Job.objects.filter(id=job_id)
    return render(request, 'jobs/job_detail_admin.html', {'jobs': jobs})
