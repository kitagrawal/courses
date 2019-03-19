import time
from datetime import datetime as dt

host_tmp = "hosts"
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
#website = input("enter the URL")
#website_list.append(website)
website_list = ["www.facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,20):
        print("working hours")
        with open(hosts_path,'r+') as f:
            content = f.read()
            for website in website_list:
                if website in content: pass;
                else: f.write(redirect+" "+website+"\n");

    else:
        with open(hosts_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours")
    time.sleep(300)
