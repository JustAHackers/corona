import requests,re,os
os.system("clear")
from difflib import get_close_matches as caris
a=requests.get("https://api.kawalcorona.com/").text
namanegara=re.findall('"Country_Region":"(.*?)"',a)

while True:
	ask=raw_input("Country : ")
	cari="".join(caris(ask,namanegara,n=1,cutoff=0))
	a=requests.get("https://api.kawalcorona.com/").text
	pat= r'{"OBJECTID":.*?,"Country_Region":"'+cari+'","Last_Update":.*?,"Lat":.*?,"Long_":.*?,"Confirmed":(.*?),"Deaths":(.*?),"Recovered":(.*?),"Active":(.*?)}}'
	b=re.search(pat,a)
	print ("\x1b[1;35m\n======={} Status=======").format(cari)
	print ("""\x1b[1;33mInfected : {}
\x1b[1;31mDied : {}
\x1b[1;32mRecovered : {}
\x1b[1;36mActive : {}\x1b[1;39m
""".format(b.group(1),b.group(2),b.group(3),b.group(4)))
	if cari.lower() == "indonesia":
		while True:
			aska=raw_input("\n\x1b[1;36mTampilkan Provinsi? (\x1b[1;32my\x1b[1;36m/\x1b[1;31mn\x1b[1;36m) : ").lower()
			if aska == "y":
				a=requests.get("https://api.kawalcorona.com/indonesia/provinsi/").text
				pat = re.findall(r'"Provinsi":"(.*?)","Kasus_Posi":(.*?),"Kasus_Semb":(.*?),"Kasus_Meni":(.*?)}}',a)
				for i in pat:
					print ("\n\x1b[1;35m========== "+i[0]+" ===========")
					print ("\x1b[1;33mTerinfeksi : "+str(i[1]))
					print ("\x1b[1;32mSembuh     : "+str(i[2]))
					print ("\x1b[1;31mMati       : "+str(i[3])+"\x1b[1;39m")
				print("\n\n");break
