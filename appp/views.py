from django.db.models import Q
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import  auth,User
from django.contrib.auth import authenticate,login,logout
from datetime import date
# Create your views here.
def Index(request):
    placed=Placed_student.objects.order_by('-id')
    return render(request,'index.html',{"placed":placed})

def Description(request,pid):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    job=AddJob.objects.filter(id=pid)
    d={'job':job}
    return render(request,'description.html',d)

def Adminlogin(request):
    error=""
    if request.method=='POST':
        un=request.POST['uname']
        pw=request.POST['pwd']
        user=authenticate(username=un,password=pw)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d={"error":error}
    return render(request,'admin.html',d)

def Adminhome(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    return render(request,'adminhome.html')

def Userlogin(request):
    error=""
    if request.method == 'POST':
        e=request.POST['eml']
        p=request.POST['pwd']
        user=authenticate(username=e,password=p)
        if user:
            try:
                user1=S_user.objects.get(user=user)
                if user1.types == "student":
                    login(request,user)
                    error="no"
                else:
                    error="yes"
            except:
                error="yes"
        else:
            error="yes"
    d={'error':error}
    return render(request,'user.html',d)

def Recruiterlogin(request):
    error=""
    if request.method == 'POST':
        u=request.POST['user']
        p=request.POST['pwd']
        user=authenticate(username=u,password=p)
        if user:
            try:
                user1=Recruiter.objects.get(user=user)
                if user1.types == "recruiter" and user1.status != "pending":
                    if user1.status == "Reject":
                        error="out"
                    else:
                        login(request,user)
                        error="no"
                else:
                    error="not"
            except:
                error="yes"
        else:
            error="yes"
    d={'error':error}
    return render(request,'recruiter.html',d)

def Signup(request):
    error=""
    if request.method == 'POST':
        f=request.POST['fname']
        l=request.POST['lname']
        e=request.POST['email']
        c=request.POST['contact']
        g=request.POST['gender']
        p=request.POST['pwd']
        i=request.FILES['image']
        try:
            user=User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
            S_user.objects.create(user=user,mobile=c,gender=g,image=i,types="student")
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'signup.html',d)

def Sjl(request):
    job=AddJob.objects.all()
    d={'job':job}
    return render(request,'sjl.html',d)

def Userhome(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    user=request.user
    student=S_user.objects.get(user=user)
    error=""
    if request.method == 'POST':
        f=request.POST['fname']
        l=request.POST['lname']
        c=request.POST['contact']
        g=request.POST['gender']
        student.user.first_name=f
        student.user.last_name=l
        student.mobile=c
        student.gender=g
        try:
            student.save()
            student.user.save()
            error="no"
        except:
            error="yes"
    d={'rec':student,'error':error}
    return render(request,'userhome.html',d)

def Logout(request):
    logout(request)
    return redirect('index')

def Recsignup(request):
    error=""
    if request.method == 'POST':
        f=request.POST['fname']
        l=request.POST['lname']
        e=request.POST['email']
        c=request.POST['contact']
        g=request.POST['gender']
        p=request.POST['pwd']
        i=request.FILES['image']
        com=request.POST['company']
        try:
            user=User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
            Recruiter.objects.create(user=user,company=com,mobile=c,gender=g,image=i,types="recruiter",status="pending")
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'recsignup.html',d)

def Recruiterhome(request):
    if not request.user.is_authenticated:
        return redirect('recruiterlogin')
    user=request.user
    rec=Recruiter.objects.get(user=user)
    error=""
    if request.method == 'POST':
        f=request.POST['fname']
        l=request.POST['lname']
        c=request.POST['contact']
        g=request.POST['gender']
        rec.user.first_name=f
        rec.user.last_name=l
        rec.mobile=c
        rec.gender=g
        try:
            rec.save()
            rec.user.save()
            error="no"
        except:
            error="yes"
    d={'rec':rec,'error':error}
    return render(request,'recruiterhome.html',d)

def Viewuser(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    data=S_user.objects.all()
    d={'data':data}
    return render(request,'viewuser.html',d)

def Deleteuser(request,sid):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    student=User.objects.get(id=sid)
    student.delete()
    return redirect('viewuser')

def Deleterecruiter(request,pid):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    recruiter=User.objects.get(id=pid)
    recruiter.delete()
    return redirect('allrecruiter')

def Deletejob(request,pid):
    if not request.user.is_authenticated:
        return redirect('recruiterlogin')
    job=AddJob.objects.get(id=pid)
    job.delete()
    return redirect('joblist')


def Recruiterpending(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    rec=Recruiter.objects.filter(status="pending")
    return render(request,'recpending.html',{"rec":rec})

def Recruiteraccepted(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    rec=Recruiter.objects.filter(status='Accept')
    return render(request,'recaccepted.html',{"rec":rec})

def Recruiterrejected(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    rec=Recruiter.objects.filter(status='Reject')
    return render(request,'recrejected.html',{"rec":rec})

def Allrecruiter(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    al=Recruiter.objects.all()
    return render(request,'allrecruiter.html',{"al":al})

def Changestatus(request,rid):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    error=""
    recruiter=Recruiter.objects.get(id=rid)
    if request.method == 'POST':
        s=request.POST['status']
        recruiter.status=s
        try:
            recruiter.save()
            error="no"
        except:
            error="yes"
    d={"recruiter":recruiter,"error":error}
    return render(request,'changestatus.html',d)

def Cpadmin(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    error=""
    v=User.objects.get(id=request.user.id)
    if request.method=='POST':
        c=request.POST['cpwd']
        n=request.POST['npwd']
        try:
            u=User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d={"error":error,"v":v}
    return render(request,"cpadmin.html",d)

def Cpuser(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    error=""
    v=User.objects.get(id=request.user.id)
    if request.method=='POST':
        c=request.POST['cpwd']
        n=request.POST['npwd']
        try:
            u=User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d={"error":error,"v":v}
    return render(request,"cpuser.html",d)

def Cprecruiter(request):
    if not request.user.is_authenticated:
        return redirect('recruiterlogin')
    error=""
    v=User.objects.get(id=request.user.id)
    if request.method=='POST':
        c=request.POST['cpwd']
        n=request.POST['npwd']
        try:
            u=User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d={"error":error,"v":v}
    return render(request,"cprecruiter.html",d)

def Addjob(request):
    if not request.user.is_authenticated:
        return redirect('recruiterlogin')
    error=""
    if request.method == 'POST':
        t=request.POST['title']
        s=request.POST['sdate']
        e=request.POST['edate']
        x=request.POST['exp']
        sa=request.POST['salary']
        l=request.POST['location']
        lo=request.FILES['logo']
        sk=request.POST['skill']
        de=request.POST['des']
        user=request.user
        r=Recruiter.objects.get(user=user)
        try:
            AddJob.objects.create(recruiter=r,title=t,start_date=s,end_date=e,experience=x,salary=sa,Location=l,image=lo,skills=sk,description=de,creationdate=date.today())
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'addjob.html',d)

def Joblist(request):
    if not request.user.is_authenticated:
        return redirect('recruiterlogin')
    user=request.user
    r=Recruiter.objects.get(user=user) 
    jl=AddJob.objects.filter(recruiter=r)
    d={"jl":jl}
    return render(request,'joblist.html',d)

def SJoblist(request):
    job=AddJob.objects.all()
    d={"job":job}
    return render(request,'sjoblist.html',d)

def Editjobdetail(request,pid):
    if not request.user.is_authenticated:
        return redirect('recruiterlogin')
    error=""
    job=AddJob.objects.get(id=pid)
    if request.method == 'POST':
        t=request.POST['title']
        s=request.POST['sdate']
        e=request.POST['edate']
        x=request.POST['exp']
        sa=request.POST['salary']
        l=request.POST['location']
        sk=request.POST['skill']
        de=request.POST['des']
        job.title=t
        job.salary=sa
        job.experience=x
        job.Location=l
        job.skills=sk
        job.description=de
        try:
            job.save()
            error="no"
        except:
            error="yes"
        if s:
            try:
                job.start_date=sd
                job.save()
            except:
                pass
        else:
            pass
        if e:
            try:
                job.start_date=e
                job.save()
            except:
                pass
        else:
            pass
    d={'error':error,"job":job}
    return render(request,'editjobdetail.html',d)

def Changelogo(request,rid):
    if not request.user.is_authenticated:
        return redirect('recruiterlogin')
    error=""
    job=AddJob.objects.get(id=rid)
    if request.method == 'POST':
        i=request.FILES['logo']
        job.image=i
        try:
            job.save()
            error="no"
        except:
            error="yes"
    d={"error":error,"job":job}
    return render(request,'changelogo.html',d)

def Crlogo(request,pid):
    if not request.user.is_authenticated:
        return redirect('recruiterlogin')
    error=""
    rec=Recruiter.objects.get(id=pid)
    if request.method == 'POST':
        i=request.FILES['logo']
        rec.image=i
        try:
            rec.save()
            error="no"
        except:
            error="yes"
    d={"error":error,"rec":rec}
    return render(request,'crlogo.html',d)

def Culogo(request,pid):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    error=""
    student=S_user.objects.get(id=pid)
    if request.method == 'POST':
        i=request.FILES['logo']
        student.image=i
        try:
            student.save()
            error="no"
        except:
            error="yes"
    d={"error":error,"rec":student}
    return render(request,'culogo.html',d)  