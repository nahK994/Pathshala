from utils.userModel import *

class Admin(User):
    phone = models.CharField()
    bio = models.TextField(default='')

    class Meta:
        db_table = 'admins'