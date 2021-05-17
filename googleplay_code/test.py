from datetime import datetime

s = "APRIL 2 2021"


d = datetime.strptime(s, '%B %d %Y')
print(d.strftime('%Y-%m-%d'))
