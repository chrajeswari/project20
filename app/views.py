from django.shortcuts import render

# Create your views here.
from app.models import *

def display_dept(request):
    QLDO=Dept.objects.all()
    d={'dept':QLDO}
    return render(request,'display_dept.html',d)

def display_emp(request):
    QLEO=Emp.objects.all()
    d={'emp':QLEO}
    return render(request,'display_emp.html',d)

def display_bonus(request):
    QLBO=Bonus.objects.all()
    d={'bonus':QLBO}
    return render(request,'display_bonus.html',d)

def display_sal(request):
    QLSO=Salgrade.objects.all()
    d={'salary':QLSO}
    return render(request,'display_sal.html',d)



def insert_dept(request):
    dn=input('enter dname')
    dno=int(input('enter deptno'))
    NDO=Dept.objects.get_or_create(dname=dn,deptno=dno)[0]
    NDO.save()

    QLDO=Dept.objects.all()
    d={'dept':QLDO}
    return render(request,'display_dept.html',d)

def insert_emp(request):
    dno=int(input('enter deptno'))
    eno=int(input('enter empno'))
    en=input('enter ename')
    DO=Dept.objects.get(deptno=dno)

    NEO=Emp.objects.get_or_create(deptno=DO,empno=eno,ename=en)[0]
    NEO.save()

    QLEO=Emp.objects.all()
    d={'emp':QLEO}
    return render(request,'display_emp.html',d)

def insert_bonus(request):
    en=input('Enter Ename : ')
    j=input('Enter job : ')
    s=int(input('Enter Salary : '))
    EO=Emp.objects.get(ename=en)
    NBO=Bonus.objects.get_or_create(ename=EO,job=j,sal=s)[0]
    NBO.save()

    QLBO=Bonus.objects.all()
    d={'bonus':QLBO}
    return render(request,'display_bonus.html',d)
    
def insert_salgrade(request):
    # p_k=int(input('Enter Previous Pk Value : '))
    g=input('Enter Grade : ') 
    hs=int(input('Enter High salray : '))
    ls=int(input('Enter Low salary : '))

    # BO=Bonus.objects.get(pk=p_k)
    NSO=Salgrade.objects.get_or_create(grade=g,losal=ls,hisal=hs)[0]
    NSO.save()

    QLSO=Salgrade.objects.all()
    d={'salary':QLSO}
    return render(request,'display_sal.html',d)

    



