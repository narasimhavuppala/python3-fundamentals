#pip3 install datetim
from datetime import datetime

tm=datetime.today()
#print(datetime.today())
#print(datetime.now().isoformat())
#print('test'.capitalize())

print(tm.isoweekday())
print(tm.weekday())
print(tm.__str__())