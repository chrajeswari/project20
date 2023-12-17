from django.db import models

# Create your models here.
class Dept(models.Model):
    dname=models.CharField(max_length=100)
    deptno=models.IntegerField(primary_key=True)
    
    def _str_(self):
        return self.dname

class Emp(models.Model): 
    deptno=models.OneToOneField(Dept,on_delete=models.CASCADE)
    empno=models.IntegerField()
    ename=models.CharField(max_length=100,primary_key=True)
    def _str_(self):
        return str(self.empno)
    
class Bonus(models.Model):
    ename=models.OneToOneField(Emp,on_delete=models.CASCADE)
    job=models.CharField(max_length=100)
    sal=models.IntegerField()
    def _str_(self):
        return self.job
    

class Salgrade(models.Model):
    sal=models.CharField(max_length=100)
    losal=models.IntegerField() 
    hisal=models.IntegerField()

    def _str_(self):
        return str(self.sal)