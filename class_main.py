import requests
import pymongo
from datetime import datetime
from time import sleep
from fp.fp import FreeProxy
from bs4 import BeautifulSoup
import base64


class class_main:
    def __init__(self):
        print("class main created")

    def __del__(self):
        print("class  main destructed")

    def proxies_checker(self, proxy, r=0):
        try:
            res = requests.get(
                'http://httpbin.org/ip',
                proxies=proxy,
                timeout=10
            )
            if res.status_code == "200" or res.status_code == 200: return {"response_time": res.elapsed.total_seconds()}
        except Exception as e:
            print(e)
            if r == 1: return False
            return self.proxies_checker(proxy, r=1)

    def getproxie_proxyscan(self):
        r = requests.get('https://www.proxyscan.io/api/proxy?type=https').json()
        ip = r[0]['Ip']
        port = r[0]['Port']

        if not r[0]['Failed']:
            http_proxy = f"http://{ip}:{port}"
            https_proxy = f"https://{ip}:{port}"
            proxyDict = {
                "http": http_proxy,
                "https": https_proxy
            }
            return proxyDict
        else:
            return self.getproxie_proxyscan()

    def getproxie_FreeProxy(self):
        proxy = FreeProxy(timeout=4, rand=True).get()
        if proxy:
            return {
                'http': proxy,
                'https': proxy.replace("http", "https")
            }
        return self.getproxie_FreeProxy()

    def get_proxies_free_proxy_list(self):
        url = "https://free-proxy-list.net/"
        res = requests.get(url).text
        soup = BeautifulSoup(res, "html.parser")
        ips = soup.find("textarea", {"class": 'form-control'})
        ips = ips.text.strip().split("\n")
        ips.remove(ips[0])
        ips.remove(ips[0])
        ips.remove(ips[0])
        ip_array = []
        for ip in ips:
            if ip:
                obj = {}
                obj["ip"] = ip
                obj["proxy"] = {
                    'http': f"http://{ip}",
                    'https': f"https://{ip}"
                }
                ip_array.append(obj)
        return ip_array

    def get_proxies_sslproxies(self):
        url = "https://sslproxies.org/"
        res = requests.get(url).text
        soup = BeautifulSoup(res, "html.parser")
        ips = soup.find("textarea", {"class": 'form-control'})
        ips = ips.text.strip().split("\n")
        ips.remove(ips[0])
        ips.remove(ips[0])
        ips.remove(ips[0])
        ip_array = []
        for ip in ips:
            if ip:
                obj = {}
                obj["ip"] = ip
                obj["proxy"] = {
                    'http': f"http://{ip}",
                    'https': f"https://{ip}"
                }
                ip_array.append(obj)
        return ip_array

    def get_proxies_us_proxy(self):
        url = "https://us-proxy.org/"
        res = requests.get(url).text
        soup = BeautifulSoup(res, "html.parser")
        ips = soup.find("textarea", {"class": 'form-control'})
        ips = ips.text.strip().split("\n")
        ips.remove(ips[0])
        ips.remove(ips[0])
        ips.remove(ips[0])
        ip_array = []
        for ip in ips:
            if ip:
                obj = {}
                obj["ip"] = ip
                obj["proxy"] = {
                    'http': f"http://{ip}",
                    'https': f"https://{ip}"
                }
                ip_array.append(obj)
        return ip_array

    def get_proxies_geonode(self):
        url = "https://proxylist.geonode.com/api/proxy-list?limit=50&page=1&sort_by=lastChecked&sort_type=desc&speed=medium&protocols=http%2Chttps&anonymityLevel=elite&anonymityLevel=anonymous"
        ip_array = []
        try:
            res = requests.get(url).json()
            for i in res["data"]:
                ip = f"{i['ip']}:{i['port']}"
                obj["ip"] = ip
                obj["proxy"] = {
                    'http': f"http://{ip}",
                    'https': f"https://{ip}"
                }
                ip_array.append(obj)
        except:
            pass

        return ip_array

    def get_proxies_proxyscrape(self):
        url = "https://api.proxyscrape.com/v2/?request=getproxies&amp;protocol=http&amp;timeout=3000&amp;country=all&amp;ssl=yes&amp;anonymity=all&amp;simplified=true"
        ip_array = []
        try:
            res = requests.get(url).text
            # print(res)
            # print("lenght is ", len(res.split("\n")))
            for i in res.split("\n"):
                ip = i
                # print(ip)
                obj = {}
                obj["ip"] = ip
                obj["proxy"] = {
                    'http': f"http://{ip}",
                    'https': f"https://{ip}"
                }
                proxy = obj["proxy"]
                ip_array.append(obj)
        except:
            pass
        return ip_array

    def get_proxies_proxy_cz(self):
        url = "http://free-proxy.cz/en/proxylist/country/all/https/uptime/all"
        ip_array = []

        res = requests.get(url).text
        soup = BeautifulSoup(res, "html.parser")
        table = soup.find("table", {"id": "proxy_list"})
        tbody = table.find("tbody")
        # print(len(tbody.findAll("tr")))
        for row in tbody.findAll("tr"):
            # print(row)
            try:
                td = row.find("td", {"class": 'left'})
                port = row.find("span", {"class": 'fport'}).text

                ip = td.find("script")
                raw_ip = str(ip).split('"')[3]
                ip = None
                if "." in raw_ip:
                    ip = raw_ip.split("//")[1]
                else:
                    ip = base64.b64decode(raw_ip).decode('utf-8')
                # print(f"{ip}:{port}")
                if ip:
                    proxy = {
                        'http': f"http://{ip}",
                        'https': f"https://{ip}"
                    }
                    obj = {}
                    obj["ip"] = ip
                    obj["proxy"] = proxy
                    ip_array.append(obj)
            except AttributeError:
                print("error")

        return ip_array

    def get_proxies_git_jetkai(self):
        ip_array = []
        url = "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/json/proxies-http%2Bhttps.json"
        req = requests.get(url).json()
        ips = req["http"]
        for ip in ips:
            # print(ip)
            proxy = {
                'http': f"http://{ip}",
                'https': f"https://{ip}"
            }
            obj = {}
            obj["proxy"] = proxy
            obj["ip"] = ip
            ip_array.append(obj)

        return ip_array
