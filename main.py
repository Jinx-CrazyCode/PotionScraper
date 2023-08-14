import lib.scraper as s
from colorama import Fore
import os

os.system("cls")
os.system("title POTION-SCRAPER")
s.Banners.banner()
s.Banners.menu()
choice = int(input(f"[{Fore.LIGHTGREEN_EX}POTION{Fore.RESET}-{Fore.GREEN}SCRAPER{Fore.RESET}]$ "))
if choice == 1:
    s.Scraper.Link()
elif choice == 2:
    s.Scraper.image()