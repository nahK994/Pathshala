from utils.userModel import *

class Student(User):
    phone = models.CharField()

    class Meta:
        db_table = 'students'
