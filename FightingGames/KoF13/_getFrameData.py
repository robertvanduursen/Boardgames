import urllib.request,sys,os
import operator,os,re,sys,inspect # default imports
import xml.etree.cElementTree as ET
from Fighters import *

currentPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
print(currentPath)

def getCharData(character):
	result = False
	url = r'http://wiki.shoryuken.com'
	print("fetching", url+character)
	try:
		f = urllib.request.urlopen(url+character)
		result = f.read()
		'''
		result = str(f.read())

		pages = []
		for x in result.split('<a'):
			link = x.split('>')[0].split('href=')[-1][1:-1]
			if '.html' in link and 'class_' in link:
				print(link)
				pages.append(link)
		'''
		print('done with', character)
	except:
		print(character,'didnt work for some reason')

	if result:
		folder = currentPath+'/data/'+character
		if not os.path.exists(folder): os.makedirs(folder)
		with open(folder+'/frameData.html','wb') as F: F.write(result)

for char in characters.values(): getCharData(char)




text = """
<table cellpadding="2" style="width:842px">

<tbody><tr>
<td><a href="/The_King_of_Fighters_XIII/Kyo" title="The King of Fighters XIII/Kyo"><img alt="KOFXIII-Kyo select face.png" src="/images/f/fa/KOFXIII-Kyo_select_face.png" width="42" height="115"></a><a href="/The_King_of_Fighters_XIII/Benimaru" title="The King of Fighters XIII/Benimaru"><img alt="KOFXIII-Benimaru select face.png" src="/images/7/70/KOFXIII-Benimaru_select_face.png" width="42" height="115"></a><a href="/The_King_of_Fighters_XIII/Daimon" title="The King of Fighters XIII/Daimon"><img alt="KOFXIII-Daimon select face.png" src="/images/8/80/KOFXIII-Daimon_select_face.png" width="42" height="115"></a>
</td>
<td><a href="/The_King_of_Fighters_XIII/Terry" title="The King of Fighters XIII/Terry"><img alt="KOFXIII-Terry select face.png" src="/images/2/2d/KOFXIII-Terry_select_face.png" width="42" height="115"></a><a href="/The_King_of_Fighters_XIII/Andy" title="The King of Fighters XIII/Andy"><img alt="KOFXIII-Andy select face.png" src="/images/2/28/KOFXIII-Andy_select_face.png" width="42" height="115"></a><a href="/The_King_of_Fighters_XIII/Joe" title="The King of Fighters XIII/Joe"><img alt="KOFXIII-Joe select face.png" src="/images/2/21/KOFXIII-Joe_select_face.png" width="42" height="115"></a>
</td>
<td><a href="/The_King_of_Fighters_XIII/Billy" title="The King of Fighters XIII/Billy"><img alt="KOFXIII-Billy select face.png" src="/images/4/42/KOFXIII-Billy_select_face.png" width="42" height="115"></a><a href="/The_King_of_Fighters_XIII/Ash" title="The King of Fighters XIII/Ash"><img alt="KOFXIII-Ash select face.png" src="/images/6/6d/KOFXIII-Ash_select_face.png" width="42" height="115"></a><a href="/The_King_of_Fighters_XIII/Saiki" title="The King of Fighters XIII/Saiki"><img alt="KOFXIII-Saiki select face.png" src="/images/3/37/KOFXIII-Saiki_select_face.png" width="42" height="115"></a>
</td>
<td><a href="/The_King_of_Fighters_XIII/EX_Iori" title="The King of Fighters XIII/EX Iori"><img alt="KOFXIII-EX Iori select face.png" src="/images/9/9d/KOFXIII-EX_Iori_select_face.png" width="42" height="115"></a><a href="/The_King_of_Fighters_XIII/EX_Kyo" title="The King of Fighters XIII/EX Kyo"><img alt="KOFXIII-EX Kyo select face.png" src="/images/c/c1/KOFXIII-EX_Kyo_select_face.png" width="42" height="115"></a><a href="/The_King_of_Fighters_XIII/Mr._Karate" title="The King of Fighters XIII/Mr. Karate"><img alt="KOFXIII-Mr. Karate select face.png" src="/images/3/31/KOFXIII-Mr._Karate_select_face.png" width="42" height="115"></a>
</td>
<td><a href="/The_King_of_Fighters_XIII/Ryo" title="The King of Fighters XIII/Ryo"><img alt="KOFXIII-Ryo select face.png" src="/images/2/23/KOFXIII-Ryo_select_face.png" width="42" height="115"></a><a href="/The_King_of_Fighters_XIII/Robert" title="The King of Fighters XIII/Robert"><img alt="KOFXIII-Robert select face.png" src="/images/b/bb/KOFXIII-Robert_select_face.png" width="42" height="115"></a><a href="/The_King_of_Fighters_XIII/Takuma" title="The King of Fighters XIII/Takuma"><img alt="KOFXIII-Takuma select face.png" src="/images/e/e7/KOFXIII-Takuma_select_face.png" width="42" height="115"></a>
</td>
<td><a href="/The_King_of_Fighters_XIII/Iori" title="The King of Fighters XIII/Iori"><img alt="KOFXIII-Iori select face.png" src="/images/7/75/KOFXIII-Iori_select_face.png" width="42" height="115"></a><a href="/The_King_of_Fighters_XIII/Mature" title="The King of Fighters XIII/Mature"><img alt="KOFXIII-Mature select face.png" src="/images/3/31/KOFXIII-Mature_select_face.png" width="42" height="115"></a><a href="/The_King_of_Fighters_XIII/Vice" title="The King of Fighters XIII/Vice"><img alt="KOFXIII-Vice select face.png" src="/images/b/b8/KOFXIII-Vice_select_face.png" width="42" height="115"></a>
</td>
<td><a href="/The_King_of_Fighters_XIII/Saiki_(Boss)" title="The King of Fighters XIII/Saiki (Boss)"><img alt="KOFXIII-Boss Saiki select face.png" src="/images/a/a2/KOFXIII-Boss_Saiki_select_face.png" width="42" height="115"></a>
</td></tr>
<tr>
<td><a href="/The_King_of_Fighters_XIII/Elisabeth" title="The King of Fighters XIII/Elisabeth"><img alt="KOFXIII-Elisabeth select face.png" src="/images/6/6b/KOFXIII-Elisabeth_select_face.png" width="42" height="115"></a><a href="/The_King_of_Fighters_XIII/Duo_Lon" title="The King of Fighters XIII/Duo Lon"><img alt="KOFXIII-Duo Lon select face.png" src="/images/3/37/KOFXIII-Duo_Lon_select_face.png" width="42" height="115"></a><a href="/The_King_of_Fighters_XIII/Shen" title="The King of Fighters XIII/Shen"><img alt="KOFXIII-Shen select face.png" src="/images/1/10/KOFXIII-Shen_select_face.png" width="42" height="115"></a>
</td>
<td><a href="/The_King_of_Fighters_XIII/Kim" title="The King of Fighters XIII/Kim"><img alt="KOFXIII-Kim select face.png" src="/images/1/11/KOFXIII-Kim_select_face.png" width="42" height="115"></a><a href="/The_King_of_Fighters_XIII/Hwa_Jai" title="The King of Fighters XIII/Hwa Jai"><img alt="KOFXIII-Hwa Jai select face.png" src="/images/3/3c/KOFXIII-Hwa_Jai_select_face.png" width="42" height="115"></a><a href="/The_King_of_Fighters_XIII/Raiden" title="The King of Fighters XIII/Raiden"><img alt="KOFXIII-Raiden select face.png" src="/images/e/eb/KOFXIII-Raiden_select_face.png" width="42" height="115"></a>
</td>
<td><a href="/The_King_of_Fighters_XIII/Mai" title="The King of Fighters XIII/Mai"><img alt="KOFXIII-Mai select face.png" src="/images/3/33/KOFXIII-Mai_select_face.png" width="42" height="115"></a><a href="/The_King_of_Fighters_XIII/King" title="The King of Fighters XIII/King"><img alt="KOFXIII-King select face.png" src="/images/8/89/KOFXIII-King_select_face.png" width="42" height="115"></a><a href="/The_King_of_Fighters_XIII/Yuri" title="The King of Fighters XIII/Yuri"><img alt="KOFXIII-Yuri select face.png" src="/images/d/d4/KOFXIII-Yuri_select_face.png" width="42" height="115"></a>
</td>
<td><a href="/The_King_of_Fighters_XIII/K%27" title="The King of Fighters XIII/K'"><img alt="KOFXIII-K' select face.png" src="/images/e/ef/KOFXIII-K%27_select_face.png" width="42" height="115"></a><a href="/The_King_of_Fighters_XIII/Kula" title="The King of Fighters XIII/Kula"><img alt="KOFXIII-Kula select face.png" src="/images/2/2b/KOFXIII-Kula_select_face.png" width="42" height="115"></a><a href="/The_King_of_Fighters_XIII/Maxima" title="The King of Fighters XIII/Maxima"><img alt="KOFXIII-Maxima select face.png" src="/images/a/a4/KOFXIII-Maxima_select_face.png" width="42" height="115"></a>
</td>
<td><a href="/The_King_of_Fighters_XIII/Athena" title="The King of Fighters XIII/Athena"><img alt="KOFXIII-Athena select face.png" src="/images/1/17/KOFXIII-Athena_select_face.png" width="42" height="115"></a><a href="/The_King_of_Fighters_XIII/Kensou" title="The King of Fighters XIII/Kensou"><img alt="KOFXIII-Kensou select face.png" src="/images/a/a8/KOFXIII-Kensou_select_face.png" width="42" height="115"></a><a href="/The_King_of_Fighters_XIII/Chin" title="The King of Fighters XIII/Chin"><img alt="KOFXIII-Chin select face.png" src="/images/1/1b/KOFXIII-Chin_select_face.png" width="42" height="115"></a>
</td>
<td><a href="/The_King_of_Fighters_XIII/Ralf" title="The King of Fighters XIII/Ralf"><img alt="KOFXIII-Ralf select face.png" src="/images/4/4c/KOFXIII-Ralf_select_face.png" width="42" height="115"></a><a href="/The_King_of_Fighters_XIII/Clark" title="The King of Fighters XIII/Clark"><img alt="KOFXIII-Clark select face.png" src="/images/e/e6/KOFXIII-Clark_select_face.png" width="42" height="115"></a><a href="/The_King_of_Fighters_XIII/Leona" title="The King of Fighters XIII/Leona"><img alt="KOFXIII-Leona select face.png" src="/images/c/c2/KOFXIII-Leona_select_face.png" width="42" height="115"></a>
</td>
<td><a href="/The_King_of_Fighters_XIII/Dark_Ash" title="The King of Fighters XIII/Dark Ash"><img alt="KOFXIII-Dark Ash select face.png" src="/images/d/d7/KOFXIII-Dark_Ash_select_face.png" width="42" height="115"></a>
</td></tr></tbody></table>
"""

# import re
# for idx, x in enumerate(re.findall(r'<a href=("/The_King_of_Fighters_XIII/(.*?)"?) title="The King of Fighters XIII/(.*?)">', text)):
#     # print(idx, x)
#     print("'%s' : %s," % (x[2],x[0]))