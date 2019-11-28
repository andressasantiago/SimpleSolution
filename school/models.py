from django.db import models
from account.models import Profile


class Professor(models.Model):
    profile = models.OneToOneField(Profile,
                                   on_delete=models.PROTECT,
                                   primary_key=True)
    code = models.CharField(max_length=25, blank=True, auto_created=True)

    def __str__(self):
        return '{}-{}'.format(self.profile, self.code)


class Subject(models.Model):
    STARTER = 'STARTER'
    BASIC = 'BASIC'
    INTERMEDIATE = 'INTERMEDIATE'
    ADVANCED = 'ADVANCED'
    SUBJECT_TYPE_MAP = {
        STARTER: 'STARTER',
        BASIC: 'BASIC',
        INTERMEDIATE: 'INTERMEDIATE',
        ADVANCED: 'ADVANCED',
    }
    SUBJECT_TYPE_CHOICES = (
        (STARTER, SUBJECT_TYPE_MAP[STARTER]),
        (BASIC, SUBJECT_TYPE_MAP[BASIC]),
        (INTERMEDIATE, SUBJECT_TYPE_MAP[INTERMEDIATE]),
        (ADVANCED, SUBJECT_TYPE_MAP[ADVANCED]),
    )
    
    name = models.CharField(max_length=80, unique=True)
    code = models.CharField(max_length=25, unique=True, auto_created=True)
    subject_type = models.CharField(
        max_length=12,
        choices=SUBJECT_TYPE_CHOICES,
    )
    professors = models.ManyToManyField(Professor, blank=True)
    students = models.ManyToManyField('Student', blank=True)
    def __str__(self):
        return '{} {}'.format(self.name, self.code)

    def get_subject_type(self):
        return self.SUBJECT_TYPE_MAP[self.subject_type]


class Career(models.Model):
    name = models.CharField(max_length=80, unique=True)
    code = models.CharField(max_length=25, unique=True)
    subjects = models.ManyToManyField(Subject, blank=True)

    def __str__(self):
        return '{}, {}'.format(self.name, self.code)


class Student(models.Model):
    profile = models.OneToOneField(Profile,
                                   on_delete=models.PROTECT,
                                   primary_key=True)
    code = models.CharField(max_length=25, blank=False, auto_created=True)
    careers = models.ManyToManyField(Career, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.profile, self.code)


class Grade(models.Model):
    N_1 = '01'
    N_2 = '02'
    N_3 = '03'
    N_4 = '04'
    N_5 = '05'
    N_6 = '06'
    N_7 = '07'
    N_8 = '08'
    N_9 = '09'
    N_10 = '10'
    GRADES_MAP = {
        N_1: '1',
        N_2: '2',
        N_3: '3',
        N_4: '4',
        N_5: '5',
        N_6: '6',
        N_7: '7',
        N_8: '8',
        N_9: '9',
        N_10: '10',
    }
    GRADES_TURMA = (
        (N_1, GRADES_MAP[N_1]),
        (N_2, GRADES_MAP[N_2]),
        (N_3, GRADES_MAP[N_3]),
        (N_4, GRADES_MAP[N_4]),
        (N_5, GRADES_MAP[N_5]),
        (N_6, GRADES_MAP[N_6]),
        (N_7, GRADES_MAP[N_7]),
        (N_8, GRADES_MAP[N_8]),
        (N_9, GRADES_MAP[N_9]),
        (N_10, GRADES_MAP[N_10]),
    )

    grade_creator = models.ForeignKey(Profile, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    date = models.DateField(db_index=True, help_text='mm/dd/yy')
    created = models.DateTimeField(auto_now_add=True)
    grade = models.CharField(
        max_length=2,
        choices=GRADES_TURMA
    )

    def __str__(self):
        return self.GRADES_MAP[self.grade]


class Absences(models.Model):
    HALF_ABS = '.5'
    FULL_ABS = '01'
    ABSENCES_MAP = {
        HALF_ABS: '0.5',
        FULL_ABS: '1'
    }
    ABSENCES_CHOICES = (
        (HALF_ABS, ABSENCES_MAP[HALF_ABS]),
        (FULL_ABS, ABSENCES_MAP[FULL_ABS])
    )
    absence_creator = models.ForeignKey(Profile, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    date = models.DateField(db_index=True, help_text='mm/dd/yy')
    created = models.DateTimeField(auto_now_add=True)
    absence = models.CharField(
        max_length=2,
        choices=ABSENCES_CHOICES
    )

    def __str__(self):
        return self.ABSENCES_MAP[self.absence]
