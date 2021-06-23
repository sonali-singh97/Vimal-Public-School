from django.db import models
from teacher.models import Teacher

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
    createdBy = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    createdAt = models.DateTimeField()

    def __str__(self):
        return self.full_name

class SubjectResult(models.Model):
    subject_id = models.ForeignKey(Class_Subject, on_delete=models.PROTECT)
    class_id = models.ForeignKey(Students_Class, on_delete=models.DO_NOTHING)
    sutdent_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    total_marks = models.PositiveSmallIntegerField()
    obtained_marks = models.PositiveSmallIntegerField()
    isPresent = models.BooleanField(null=False)
    createdBy = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    createdAt = models.DateTimeField()
