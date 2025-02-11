import datetime
x = datetime.date.today()
q = x - datetime.timedelta(days=1)
w = x + datetime.timedelta(days=1)
print(q.strftime("%A"), x.strftime("%A"), w.strftime("%A"))