import requests,re
from difflib import get_close_matches as caris
a=requests.get("https://api.kawalcorona.com/").text
namanegara=re.findall('"Country_Region":"(.*?)"',a)
ask=raw_input("Country : ")
cari="".join(caris(ask,namanegara,n=1,cutoff=0))


pat= r'{"OBJECTID":.*?,"Country_Region":"'+cari+'","Last_Update":.*?,"Lat":.*?,"Long_":.*?,"Confirmed":(.*?),"Deaths":(.*?),"Recovered":(.*?),"Active":(.*?)}}'
b=re.search(pat,a)
print ("\n\n======={} Status=======").format(cari)
print ("""Infected : {}
Died : {}
Recovered : {}
Active : {}
""".format(b.group(1),b.group(2),b.group(3),b.group(4)))
