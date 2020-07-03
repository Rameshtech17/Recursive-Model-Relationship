from django.db import models


class School(models.Model):
    Principal = 'Principal'
    Teacher = 'Teacher'
    Student = 'Student'


    EMPLOYEE_TYPES = (
        (Principal, 'Principal'),
        (Teacher, 'Teacher'),
        (Student, 'Student'),
    )

    role = models.CharField(max_length=25, choices=EMPLOYEE_TYPES)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    manager = models.ForeignKey('self', null=True, related_name='employee',on_delete=models.SET_NULL)

    def __str__(self):
        return "{} : {} {}".format(self.role, self.first_name, self.last_name)

    def __repr__(self):
        return self.__str__()