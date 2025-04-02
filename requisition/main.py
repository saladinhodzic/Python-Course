# Requisition Project using Python
from datetime import datetime
date = str(datetime.now().date())
month = date.split("-")[1]
day = date.split("-")[2]

pattern = f"PRM-{day}{month}-ODR290"
print(pattern)