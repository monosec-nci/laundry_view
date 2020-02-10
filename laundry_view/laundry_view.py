#"http://api.laundryview.com/room/?api_key=8c31a4878805ea4fe690e48fddbfffe1&method=getAppliances&location=186779"
import requests
from bs4 import BeautifulSoup

def main():
    ret = requests.get("http://api.laundryview.com/room/?api_key=8c31a4878805ea4fe690e48fddbfffe1&method=getAppliances&location=186779")
    f = open("api.xml", "w")
    f.write(ret.text)
    f.close()
    infile = open("api.xml","r")
    contents = infile.read()
    soup = BeautifulSoup(contents,'lxml')
    stat = soup.find_all('status')
    names = soup.find_all('appliance_type')
    time = soup.find_all('time_remaining')
    for i in range(len(stat)):
        print(names[i].get_text(),":",stat[i].get_text(), "\nTime:", time[i].get_text(),"\n")

if __name__ == "__main__":
    main()
