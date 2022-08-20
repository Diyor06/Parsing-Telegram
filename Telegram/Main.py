# Kutubxonalar | Libraries
# pip install colorama
# pip install beautifulsoup
# pip install lxml
# pip install requests

from bs4 import BeautifulSoup
import requests
from colorama import Fore, Back, Style, init
import sys
from colorama import init, AnsiToWin32
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream

username = input('Usernameni Kiriting:>> ')

site = requests.get(f'https://t.me/{username}')

htmldom = BeautifulSoup(site.text, 'lxml')

title = htmldom.find('span',{'dir':'auto'})
username = htmldom.find('div',class_='tgme_page_extra')
bio = htmldom.find('div',class_='tgme_page_description')
rasm = htmldom.find('img',class_='tgme_page_photo_image')


print(Fore.GREEN + 'Foydalanuvchi:',Fore.RED + f"{ title.text.strip()}",'\n', file=stream,)
print(Fore.GREEN + 'Username:',Fore.RED + f"{ username.text.strip()}",'\n', file=stream,)
print(Fore.GREEN + 'Tarjimayi Hol:',Fore.RED + f"{ bio.text.strip()}",'\n', file=stream,)
print(Fore.GREEN + 'Hozirdagi Rasm:',Fore.YELLOW + f"{ rasm.get('src')}",'\n', file=stream,)
