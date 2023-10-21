from utils.userModel import *

class Teacher(User):
    phone = models.CharField()
    headline = models.CharFields()
    bio = models.TextField(default='')

    class Meta:
        db_table = 'teachers'