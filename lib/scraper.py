from colorama import Fore
from pystyle import *
import requests
from bs4 import *
import time


#BANNERS AND MENU
class Banners:
    def banner():
        print(Center.XCenter(f"""{Fore.LIGHTGREEN_EX}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠢⣀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠒⠔⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠤⠴⠒⠖⠖⠶⠢⠤⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠠⠖⢆⡀⠀⠀⣠⠔⣇⠲⣀⢀⠂⣀⠒⣊⢴⣹⠠⣄⠀⠀⠀⡠⢄
⠀⠀⠈⠂⠋⠀⠀⢸⠀⠀⠽⣷⣮⣷⢿⣮⣷⣽⡾⠏⠀⠀⡆⠀⠀⠁⠈
⠀⠀⠀⠀⠀⠀⠀⠸⡀⠀⣸⡧⡀⡤⣀⠠⣀⠠⣼⣟⢀⢠⠇⠀⠀⠀⠀
⡤⡀⠀⠀⠀⠀⠀⠀⠨⡇⢹⡕⠶⠶⠴⠶⠴⠶⣮⡏⢸⠁⠀⠀⠀⠀⠀
⠑⠁⠀⠀⠀⠀⢀⡠⠞⠁⠀⠙⠳⠾⠶⠷⠾⠞⠋⠀⠈⠳⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⠋⠀⣀⣤⣤⣤⣶⣶⣶⣶⣶⣦⣤⣤⣤⣀⠈⠓⡄⠀⠀
⠀⠀⠀⠀⠀⢸⠀⠘⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠂⡅⠀⠀    [Made by BabyDoll]
⠀⠀⠀⠀⠀⢸⠀⠀⠀⢀⣾⣿⣷⣶⣿⣿⣿⣿⣷⣾⣶⡾⢷⡆⡄⠀⠀             [POTION-SCRAPER]
⠀⠀⠀⠀⠀⢸⠀⠀⢀⣾⣿⣿⣿⣯⣿⣿⣿⠟⠉⠙⢿⣿⣿⡇⠇⠀⠀
⠀⠀⠀⠀⠀⢸⠀⠀⢸⣿⣿⣯⣿⣿⣿⣻⣧⡠⢤⢤⣬⣿⣿⡇⡃⠀⠀
⠀⠀⠀⠀⠀⢸⠀⠀⢾⣯⣽⡿⣽⣿⣟⣿⢿⣦⣥⣼⡿⣿⣹⡇⡃⠀⠀
⠀⠀⠀⠀⠀⢸⠀⠀⢯⡿⡏⠁⠀⢹⣟⡾⡿⣽⣻⣽⣻⢿⡽⡇⡅⠀⠀
⠀⠀⠀⠀⠀⢸⠀⠀⡟⡟⣷⣤⣤⣿⢫⣷⠛⣧⡟⣶⣿⣯⡟⡇⡆⠀⠀
⠀⠀⠀⠀⠀⢸⠀⠀⣽⡷⣍⢯⣝⢮⡽⢬⡛⣶⢹⣭⢆⡾⣹⠇⡆⠀⠀
⠀⠀⠀⠀⠀⢸⠀⠀⢾⡘⢿⠚⡌⢇⢏⢣⢃⠗⡛⡜⢎⡹⢏⡇⠆⠀⠀
⠀⠀⠀⠀⠀⢾⡀⠀⣞⢡⢎⠩⡘⠌⡌⢢⠉⡌⡙⠬⡆⠩⠌⣆⡃⠀⠀
⠀⠀⠀⠀⠀⠈⠋⠤⣈⢀⡂⠡⠌⠰⢈⠂⠌⡐⠁⢂⡐⣡⠼⠚⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠑⠒⠒⠒⠒⠒⠒⠛⠉⠉⠀⠀⠀⠀⠀⠀{Fore.RESET}"""))
        

    def menu():
        print(Center.XCenter(f"""{Fore.LIGHTGREEN_EX}
[1] Extract links from a site
[2] Extract images from a site{Fore.RESET}"""))
        



#CLASS Scraper
class Scraper:

    def Link():
        try:
            query = input("Enter the site where you want to extract the links: ")
            url = requests.get(query)
            soup = BeautifulSoup(url.content,"html.parser")
            for link in soup.find_all("a"):
                print(Fore.LIGHTBLACK_EX,link.get("href"),Fore.RESET)
                time.sleep(1)
        except:
            print(f"{Fore.RED}link not founds{Fore.RESET}")


    def image():
        try:
            query = input("Enter the site where you want to extract the links: ")
            url = requests.get(query)
            soup = BeautifulSoup(url.content,"html.parser")
            images = []
            img = soup.select("img")
            for image in img:
                 src = image.get('src')
                 alt = image.get('alt')
                 images.append({"src": src, "alt": alt})
            for image in images:
                print(Fore.LIGHTBLACK_EX,image,Fore.RESET)
                time.sleep(1)
        except:
            print(f"{Fore.RED}link not founds{Fore.RESET}")