#coding:utf-8
#function_md5

import requests,hashlib,sys
def function_md5(line,url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    }

    lis = line.split(' ')
    uri,cms,md5 = lis[0],lis[1],lis[2]
    url = url+uri

    r = requests.get(url=url, headers=headers, allow_redirects=False)

    if r.status_code == 200:
        rfile = r.content
        mb5 = hashlib.md5(rfile).hexdigest()

        if mb5 == md5:
            sys.stdout.write('CMS: %s , URI: %s , Finger MD5: %s\n' % (cms, uri, md5))


