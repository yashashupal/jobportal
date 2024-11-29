from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from job.models import studentuser,userpost,clinteragister,userpostreplay,news
from django.contrib import messages
from job.helpers import send_forget_password_mail

# from job.models import clinteragister
# Create your views here.



def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')
def userlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
       

        if user:
            login(request,user)
            return redirect('/')
            
            
        return redirect('/404')
    return render(request,'login.html')
def myaccount(request):
    if request.user.is_authenticated:
        userpost1=userpost.objects.filter(userid=request.user)
        return render(request,'my account.html',{'userpo':userpost1})

    return redirect('/userlogin')
def ragister(request):
    if request.method=="POST":
        img=request.FILES['img']
        resume=request.FILES['RESUME']
        fname=request.POST['fname']
        lname=request.POST['lname']
        contact=request.POST['contact']
        email=request.POST['email']
        gender=request.POST['gender']
        password=request.POST['password']
        try:
            user=User.objects.create_user(username=email,password=password,first_name=fname,last_name=lname,email=email)
            studentuser.objects.create(user=user,mobile=contact,gender=gender,image=img,type='student',resume=resume,email=email)
            
            error="no"
        except:
            error="yes"
        return redirect('/userlogin')
    
    
    
    return render(request,'ragister.html')
def job_detail(request,id):
    if request.user.is_authenticated:
        jobdestail=userpost.objects.get(id=id)
        if request.method=='POST':
            
            candidate=request.POST['candidate']
            email=request.POST['email']
            contact=request.POST['contact']
            resume=request.FILES['resume']
            jobtitle=request.POST['jobtitle']
            jobpost=userpostreplay.objects.create(post=request.user,jobtitle=jobtitle,candidatename=candidate,resume=resume,email=email,contact=contact)
            jobpost.save()

    return render (request,'job-detail.html',{'detail':jobdestail})

# def job_detail1(request):
#     return render(request,'job-detail.html')
def job_list(request):
        if request.user.is_authenticated:
            alldata=userpost.objects.all().order_by('-id')[:10]
            
           
            return render(request,'job-list.html',{'data':alldata})
        else:
            return redirect('/userlogin/')
    
def testimonial(request):
    return render(request,'testimonial.html')
def heade1(request):
    return render(request,'heade1.html')



def clinteragister1(request):
    if request.method=="POST":
        img=request.FILES['img']
        fname=request.POST['fname']
        lname=request.POST['lname']
        contact=request.POST['contact']
        email=request.POST['email']
        gender=request.POST['gender']
        password=request.POST['password']
        companyname=request.POST['companyname']
        industry=request.POST['industry']
        orgtype=request.POST['orgType']
        address=request.POST['address']
        location=request.POST['location']
        landlinephone=request.POST['landlinephone']
        cellphone=request.POST['cellphone']
        companywebsite=request.POST['companywebsite']
        noofemployees=request.POST['noofemployees']
        companydescription=request.POST['companydescription']
        # companylogo=request.FILES['companylogo']
        # try:
        

        user=User.objects.create_user(username=email,password=password,first_name=fname,last_name=lname,email=email)
        
        a=clinteragister.objects.create(email=email,user=user,mobile=contact,gender=gender,image=img,type='clinte',companyname=companyname,industry=industry,orgtype=orgtype,address=address,location=location,landlinephone=landlinephone,cellphone=cellphone,companywebsite=companywebsite,noofemployees=noofemployees,companydescription=companydescription)
        a.save()
           
        #     error="no"
        # except:
        #     error="yes"
        return redirect('/userlogin')
    return render(request,'employerragister.html')

def category(request):
    return render(request,'category.html')
def about(request):
    return render(request,'about.html')
def eror(request):
    return render(request,'404.html')
def  Logout(request):
    logout(request)
    return redirect('/')
def header(request):
    return render(request,'header.html')
def internship(request):
    return render(request,'internship.html')
def applicationjob(request):
    return render(request,'appliccantejob.html')
def postjob(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            
            jobtitle=request.POST['jobtitle']
            vacancies=request.POST['vacancies']
            experience=request.POST['experience']
            jobmode=request.POST['jobmode']
            salary1=request.POST['salary1']
            salary2=request.POST['salary2']
            applybefore=request.POST['applybefore']
            location=request.POST['location']
            qualification=request.POST['qualification']
            jobdescription=request.POST['jobDescription']
            skill=request.POST['skill']
            # if(request.POST['skill']){
            #     skill =request.POST['skill']
            # }
           
            jobpost=userpost.objects.create(userid=request.user,jobdiscription=jobdescription,jobtitle=jobtitle,vacancies=vacancies,experience=experience,jobmode=jobmode,minsalary=salary1,maxsalary=salary2,applybefor=applybefore,qualification=qualification,skill=skill,location=location)
            jobpost.save()
            return redirect('/')
        return render(request,'postdashboard3.html')
    return redirect('/userlogin')

def updatejob(request,id):
    if request.user.is_authenticated:
        up=userpost.objects.get(id=id)
        if request.method=='POST':
            
            jobtitle=request.POST['jobtitle']
            vacancies=request.POST['vacancies']
            experience=request.POST['experience']
            jobmode=request.POST['jobmode']
            salary1=request.POST['salary1']
            salary2=request.POST['salary2']
            applybefore=request.POST['applybefore']
            location=request.POST['location']
            qualification=request.POST['qualification']
            jobdescription=request.POST['jobDescription']
            skill=request.POST['skill']
            # if(request.POST['skill']){
            #     skill =request.POST['skill']
            # }
            userpost.objects.filter(id=id).update(jobdiscription=jobdescription,jobtitle=jobtitle,vacancies=vacancies,experience=experience,jobmode=jobmode,minsalary=salary1,maxsalary=salary2,applybefor=applybefore,qualification=qualification,skill=skill,location=location)
           
           
            return redirect('/')
    return render(request,'updatejob.html',{'data':up})

def postdashboard1(request):
    return render(request,'postdashboard1.html')
def postdashboard2(request):
    profile=clinteragister.objects.get(user=request.user)
    if request.method=='POST':
        companyname=request.POST['companyname']
        industry=request.POST['industry']
        location=request.POST['location']
        landlinephone=request.POST['landlinephone']
        companydescription=request.POST['companydescription']
        companywebsite=request.POST['companywebsite']
        orgType=request.POST['orgType']
        address=request.POST['address']
        cellphone=request.POST['cellphone']
        noofemployees=request.POST['noofemployees']
        
        img=request.FILES['img']
        
        try:
            clinteragister.objects.filter(user=request.user).update(type='clinte', companyname=companyname,industry=industry,orgtype=orgType,address=address,location=location,landlinephone=landlinephone,cellphone=cellphone,companywebsite=companywebsite,noofemployees=noofemployees,companydescription=companydescription,image=img)
            
            
           
        except clinteragister.DoesNotExist:
            pass        

    return render(request,'postdashboard2.html')
def postdashboard3(request):
    return render(request,'postdashboard3.html')
def postdashboard4(request):
    if request.user.is_authenticated:
        userpost1=userpost.objects.filter(userid=request.user)
       
        # if request.method=='POST':
        #      userdel=userpost.objects.get(id=id)
        #      userdel.delete()

    return render(request,'postdashboard4.html',{'userpo':userpost1,
                                                #  'data':userdel
                                                 })
def postdashboard5(request):
    return render(request,'postdashboard5.html')
def postdashboard6(request):
    if request.method=='POST':
        old=request.POST['old']
        new=request.POST['new']
        # conform=request.POST['conform']
        # if new==conform:
        try:
            u =User.objects.get(id=request.user.id)
            if u.check_password(old):
                u.set_password(new)
                u.save()
                alert =True
                return render(request,'postdashboard6.html',{'alert':alert})
            else:
                curntpassword =True
                return render(request,'postdashboard6.html',{'curntpassword':curntpassword})
        except:
            pass
            


    return render(request,'postdashboard6.html')
def delpost(request,id):
    return redirect('/postdashboard4/')
# def changepassword(request,token):
#     context ={}

#     try:
#         profile_obj=Profile.objects.filter(forget_password_token=token).first()
#         print(profile_obj)
#         if request.method=="POST":
#             new_password=request.POST['new']
#             confirm_password=request.POST['']
#         context={'user_id':profile_obj.user.id}

#     except Exception as e:
#         print(e)
#     return render(request,"changepass.html",context)

# import uuid
# def forgetpass(request):
#     try:
#         if request.method=='POST':
#             username=request.POST.get('username')
#             if not User.objects.filter(username=username).first():
#                 messages.success(request,'No User Found With This Username.')
#                 return redirect('/forgetpass/')
            # user_obj =User.objects.get(username=username)
            # token = str(uuid.uuid4())
            # profile_obj=Profile.objects.get(user=user_obj)
            # profile_obj.forget_password_token=token
            # profile_obj.save()
            # send_forget_password_mail(user_obj.email,token)
            # messages.success(request,'An Email Is Sent.')
            # return redirect('/forgetpass/')

    # except Exception as e:
    #     print(e)

    # return render(request,"password_reset_form.html")
    
def delete_post(request,id):
    data=userpost.objects.get(id=id)
    if request.method=='POST':
        data.delete()
        return redirect('/postdashboard4/')
    return render(request,'delete.html',{'data':data})