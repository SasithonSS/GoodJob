from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home_jobber', views.home_jobber, name='home_jobber'),
    path('home_emp', views.home_emp, name='home_emp'),
    path('home_admin', views.home_admin, name='home_admin'),
    path('job_detail_jobber/<int:job_id>', views.job_detail_jobber, name='job_detail_jobber'),
    path('myjobs_detail_jobber/<int:job_id>', views.myjobs_detail_jobber, name='myjobs_detail_jobber'),
    path('jobs_emp/<int:job_id>', views.job_detail_emp, name='job_detail_emp'),
    path('myjobs_emp/<int:emp_name>', views.myjobs_emp, name='myjobs_emp'),
    path('myjobs_jobber/<int:id>', views.myjobs_jobber, name='myjobs_jobber'),
    path('delete_myjobs/<int:id>', views.delete_myjobs, name='delete_myjobs'),
    path('myjobs_emp_detail/<int:job_id>', views.myjobs_emp_detail, name='myjobs_emp_detail'),
    path('add_job/<int:id>', views.add_job, name='add_job'),
    path('myjobs_emp_update/<int:job_id>', views.myjobs_emp_update, name='myjobs_emp_update'),
    path('jobs_admin/<int:job_id>', views.job_detail_admin, name='job_detail_admin'),
    path('jobs_apply/<int:job_id>', views.job_apply, name='job_apply'),
    path('myjob_apply/<int:job_id>', views.myjob_apply, name='myjob_apply'),
    path('myjob_apply_detail/<int:id>', views.myjob_apply_detail, name='myjob_apply_detail'),
    path('jobs/<int:job_id>', views.job_detail, name='job_detail'),
    path('jobber_complain', views.jobber_complain, name='jobber_complain'),
    path('emp_report', views.emp_report, name='emp_report'),
]