#coding:utf-8

#author:aedoo
#github:https://github.com/aedoo

import threading,Queue
import argparse,json
import time

from lib import function_md5
from lib import function_file
from lib import function_kv

class ACMSDiscovery(threading.Thread):

    def __init__(self,queue_md5,queue_file,queue_kv,url):
        threading.Thread.__init__(self)
        self.queue_md5 = queue_md5
        self.queue_file = queue_file
        self.queue_kv = queue_kv
        self.url = url

    def run(self):

        url = self.url

        while True:

            if not self.queue_md5.empty():        #MD5指纹校验
                try:

                    line_md5 = self.queue_md5.get(timeout=0.5)
                    function_md5.function_md5(line=line_md5,url=url)

                except Exception:
                    continue


            elif not self.queue_file.empty():     #存在文件校验
                try:

                    line_file = self.queue_file.get(timeout=0.5)
                    function_file.function_file(line=line_file, url=url)

                except Exception:
                    continue

            elif not self.queue_kv.empty():       #JSON格式数据校验
                try:
                    ajson = self.queue_kv.get(timeout=0.5)
                    function_kv.function_kv(ajson,url)

                except Exception:
                    continue

            else:
                break


def main():
    logo_file = open('logo/logo.txt','r')
    logo = logo_file.read()
    logo_file.close()

    md5_file = open('data/md5.txt','r')
    md5s = md5_file.readlines()
    md5_file.close()

    file_file = open('data/file.txt','r')
    files = file_file.readlines()
    file_file.close()

    kv_file = open('data/data.txt','r')
    kvs = json.load(kv_file)
    kv_file.close()


    print logo
    print 'github: https://github.com/aedoo'

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', dest='url', type=str, default="http://www.discuz.net", help='url like http://www.discuz.net')
    parser.add_argument('-t', dest='thread_number', type=int, default=100, help='Setting the number of threads, default=100')
    args = parser.parse_args()

    print ''

    parser.print_help()

    print ''

    try:

        thread_number = args.thread_number
        url = str(args.url)        #记录输入URL
        threads = []

        queue_md5 = Queue.Queue()   #放置MD5指纹的队列
        for md5 in md5s:
            md5 = md5.strip()
            queue_md5.put(str(md5))

        queue_file = Queue.Queue()  #放置存在文件指纹的队列
        for file in files:
            file = file.strip()
            queue_file.put(str(file))

        queue_kv = Queue.Queue()
        for kv in kvs:
            queue_kv.put(kv)

        for i in xrange(thread_number):
            threads.append(ACMSDiscovery(queue_md5,queue_file,queue_kv,url))

        for t in threads:
            t.start()
        for t in threads:
            t.join()

    except Exception:
        parser.print_help()


if __name__ == '__main__':

    time_start = time.time()
    main()
    time_all = time.time()-time_start
    print '\nAll Finish. Use %ss' % time_all