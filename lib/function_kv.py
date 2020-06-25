#coding:utf-8
#function_md5

import requests,hashlib,sys
def function_kv(ajson,url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }

    uri,select,cms,md5 = ajson['url'],ajson['re'],ajson['name'],ajson['md5']
    url = url + uri

    r = requests.get(url=url, headers=headers, allow_redirects=False)

    if r.status_code == 200:
        if md5:

            rfile = r.content
            mb5 = hashlib.md5(rfile).hexdigest()

            if mb5 == md5:
                sys.stdout.write('CMS: %s , JSON Finger & JSON uri: %s, Finger md5: %s\n' % (cms, uri,md5))

        elif select:

            html = r.content
            if (html.find(select) != -1):
                sys.stdout.write('CMS: %s , JSON Finger & JSON uri: %s, Finger re: %s\n' % (cms, uri, select))

#
# if __name__ == '__main__':
#
#     url = 'https://www.drupal.org'
#
#     ajson =     {
#         "url": "/README.txt",
#         "re": "Drupal",
#         "name": "Drupal",
#         "md5": ""
#     }
#
#     function_kv(ajson=ajson,url=url)
