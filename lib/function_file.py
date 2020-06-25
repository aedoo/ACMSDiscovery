#coding:utf-8
#function_file

import requests,sys
def function_file(line,url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    }

    lis = line.split(' ')
    uri,cms = lis[0],lis[1]
    url = url+uri

    r = requests.get(url=url, headers=headers, allow_redirects=False)

    if r.status_code == 200:
        sys.stdout.write('CMS: %s , Finger URI: %s\n' % (cms, uri))