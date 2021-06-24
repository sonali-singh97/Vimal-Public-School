from django.db import models

# Create your models here.
class Students_Class(models.Model):
    class_name = models.CharField(max_length=10)
    strength = models.IntegerField(default=0)
    class_teacher = models.CharField(max_length=15)
    tution_fees = models.IntegerField(default=0)

    def __str__(self):
        return self.class_name

class Class_Subject(models.Model):
    name = models.CharField(max_length=10)
    class_id = models.ForeignKey(Students_Class, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    

class Student(models.Model):
    student_id = models.IntegerField(default=0)
    full_name = models.CharField(max_length=20)
    student_class = models.ForeignKey(Students_Class, on_delete=models.PROTECT)
    section = models.CharField(max_length=1)
    session_start = models.DateField()
    session_end = models.DateField()
    dob = models.DateField()
    father_name = models.CharField(max_length=20)
    contact_number = models.IntegerField(default=0)
    address = models.CharField(max_length=50)
    attendence = models.IntegerField(default=0)
    createdBy = models.CharField(max_length=20)
    createdAt = models.DateTimeField()

# class Fees(models.Model):
#     title = models.CharField(max_length=50)
#     amount = models.IntegerField(default=0)
#     fee_type = models.CharField(max_length=50)
#     class_id = models.ForeignKey(Students_Class, on_delete=models.PROTECT)
#     due_date = models.DateField()
#     fine = models.IntegerField(default=0)

# class Student_Fee(models.Model):
#     fee = models.ForeignKey(Fees , on_delete=models.PROTECT)
#     student = models.ForeignKey(Student, on_delete=models.PROTECT)
#     # advance_pay = 
#     discount = models.IntegerField(default=0)
#     status = models.CharField(max_length=20)

# class Fee_Transaction(models.Model):
#     fee = models.ForeignKey(Fees , on_delete=models.PROTECT)
#     student = models.ForeignKey(Student, on_delete=models.PROTECT)
#     amount = models.IntegerField(default=0)
#     paid_date = models.DateField()

# class Advance_Payment(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.PROTECT)
#     amount = models.IntegerField(default=0)
#     months = models.IntegerField(default=0)

class Fee_Type(models.Model):
  fee_type = models.CharField(max_length=50)
  amount = models.IntegerField(default=0)

  def __str__(self):
    return self.fee_type

class Fee_Transaction(models.Model):
  fee_id = models.ForeignKey(Fee_Type, on_delete=models.PROTECT, default = 0)
  student_id = models.ForeignKey(Student, on_delete=models.PROTECT)
  amount = models.IntegerField(default=0)
  balance = models.IntegerField(default=0)
  discount = models.IntegerField(default=0)
  total = models.IntegerField(default=0)

class Payment(models.Model):
  fee_trans_id = models.ForeignKey(Fee_Transaction, on_delete=models.PROTECT)
  amount = models.IntegerField(default=0)
  date = models.DateTimeField()
  clear = models.BooleanField()
  fine = models.FloatField()

   