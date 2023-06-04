# This is a sample Python script.
import requests
import multiprocessing
from class_db import class_db
from class_main import class_main
import threading
from time import sleep
import base64

main = class_main()
db = class_db()


def freeproxy():
    while True:
        proxy1 = main.getproxie_FreeProxy()
        res = main.proxies_checker(proxy1)
        ip = proxy1["http"].replace("http://", '')
        if res:
            print("type:freeproxy", proxy1, "Working")
            db.add_working_ip(ip, proxy1, res["response_time"])
        else:
            print("type:freeproxy", proxy1, "Not Working")
        sleep(2)


def proxyscan():
    while True:
        proxy1 = main.getproxie_proxyscan()
        res = main.proxies_checker(proxy1)
        ip = proxy1["http"].replace("http://", '')
        if res:
            print("type:proxyscan", proxy1, "Working")
            db.add_working_ip(ip, proxy1, res["response_time"])
        else:
            print("type:proxyscan", proxy1, "Not Working")
        sleep(2)


def free_proxy_list():
    while True:
        ips = main.get_proxies_free_proxy_list()
        for ip in ips:
            proxy1 = ip["proxy"]
            ip = ip["ip"]
            res = main.proxies_checker(proxy1)
            if res:
                print("type:free_proxy_list", proxy1, "Working")
                db.add_working_ip(ip, proxy1, res["response_time"])
            else:
                print("type:free_proxy_list", proxy1, "Not Working")
            sleep(1)

        sleep(60 * 60)


def sslproxies():
    while True:
        ips = main.get_proxies_sslproxies()
        for ip in ips:
            proxy1 = ip["proxy"]
            ip = ip["ip"]
            res = main.proxies_checker(proxy1)
            if res:
                print("type:sslproxies", proxy1, "Working")
                db.add_working_ip(ip, proxy1, res["response_time"])
            else:
                print("type:sslproxies", proxy1, "Not Working")
            sleep(1)

        sleep(60 * 60)


def us_proxy():
    while True:
        ips = main.get_proxies_us_proxy()
        for ip in ips:
            proxy1 = ip["proxy"]
            ip = ip["ip"]
            res = main.proxies_checker(proxy1)
            if res:
                print("type:us_proxy", proxy1, "Working")
                db.add_working_ip(ip, proxy1, res["response_time"])
            else:
                print("type:us_proxy", proxy1, "Not Working")
            sleep(1)

        sleep(60 * 60)


def proxyscrape():
    while True:
        ips = main.get_proxies_proxyscrape()
        for ip in ips:
            proxy1 = ip["proxy"]
            ip = ip["ip"]
            res = main.proxies_checker(proxy1)
            if res:
                print("type:proxyscrape", proxy1, "Working")
                db.add_working_ip(ip, proxy1, res["response_time"])
            else:
                print("type:proxyscrape", proxy1, "Not Working")
            sleep(1)

        sleep(60 * 60)


# pip install free-proxy


def geonode():
    while True:
        ips = main.get_proxies_geonode()
        for ip in ips:
            proxy1 = ip["proxy"]
            ip = ip["ip"]
            res = main.proxies_checker(proxy1)
            if res:
                print("type:geonode", proxy1, "Working")
                db.add_working_ip(ip, proxy1, res["response_time"])
            else:
                print("type:geonode", proxy1, "Not Working")
            sleep(2)
        sleep(60 * 60)


def proxy_cz():
    while True:
        ips = main.get_proxies_proxy_cz()
        for ip in ips:
            proxy1 = ip["proxy"]
            ip = ip["ip"]
            res = main.proxies_checker(proxy1)
            if res:
                print("type:proxy_cz", proxy1, "Working")
                db.add_working_ip(ip, proxy1, res["response_time"])
            else:
                print("type:proxy_cz", proxy1, "Not Working")
            sleep(1)

        sleep(60 * 60)


# get_proxies_git_jetkai

def git_jetkai():
    while True:
        ips = main.get_proxies_git_jetkai()
        for ip in ips:
            proxy1 = ip["proxy"]
            ip = ip["ip"]
            res = main.proxies_checker(proxy1)
            if res:
                print("type:git_jetkai", proxy1, "Working")
                db.add_working_ip(ip, proxy1, res["response_time"])
            else:
                print("type:git_jetkai", proxy1, "Not Working")
            sleep(1)

        sleep(60 * 10)


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def run():
    multiprocessing.Process(target=git_jetkai).start()
    multiprocessing.Process(target=proxyscrape).start()
    multiprocessing.Process(target=proxy_cz()).start()


def run2():
    for i in range(0, 10):
        multiprocessing.Process(target=freeproxy).start()
        multiprocessing.Process(target=proxyscan).start()


def run3():
    multiprocessing.Process(target=free_proxy_list).start()
    multiprocessing.Process(target=sslproxies).start()
    multiprocessing.Process(target=us_proxy).start()
    multiprocessing.Process(target=geonode).start()


if __name__ == '__main__':
    multiprocessing.Process(target=run).start()
    multiprocessing.Process(target=run2()).start()
    multiprocessing.Process(target=run3()).start()


