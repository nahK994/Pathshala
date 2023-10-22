import json


def inviteTeacher(ch, method, properties, body):
    data = json.loads(body.decode('ASCII'))
    print("react ==> ", data)
    print(f"Invite teacher {data}")