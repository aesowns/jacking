import sys
import subprocess
import importlib
R = "\033[0;31m"
G = "\033[0;32m"
Y = "\033[0;33m"
M = "\033[0;35m"
W = "\033[0m"
libraries = {
    "requests": "requests",
    "mechanize": "mechanize",
    "names": "names",
    "render": "render",
    "user_agent": "user_agent",
    "telethon": "telethon",
    "python-cfonts": "cfonts",
    "pyfiglet": "pyfiglet",
    "colorama": "colorama",
    "rich": "rich",
    "uuid": "uuid",
    "bs4": "bs4",
    "pysocks": "socks",
    "pycryptodome": "Crypto"
}
def aesowns(xxx):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", xxx])
        print(f"{G}Installed {xxx} {W}")
    except Exception as e:
        print(f"{Y}Failed to install {xxx}. Error: {str(e)}{W}")
try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    print(f"{G}pip upgraded to the latest version{W}")
except Exception as e:
    print(f"{Y}Failed to upgrade pip. Error: {str(e)}{W}")
for deep_lulli, deep_chxt in libraries.items():
    try:
        importlib.import_module(deep_chxt)
        print(f"{G}{deep_lulli} is already installed{W}")
    except ImportError:
        print(f"{R}{deep_lulli} not installed. Installing{W}")
        try:
            aesowns(deep_lulli)
        except:
            pass