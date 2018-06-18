import io
import zipfile
import requests
import os
import sys
import shutil
from bs4 import BeautifulSoup

s = requests.Session()
hw_sum = 0

def change_filename():
    global hw_sum
    path = './hw_repo'
    files = os.listdir(path)
    for name in files:
        newname = name[:name.find('_')].replace(' ','')
        print(newname)
        os.rename('./hw_repo/'+name, './hw_repo/'+newname)
    hw_sum = len(files)

def download_assignment(dic):
    global hw_sum
    url = dic['url'] + '&action=downloadall'
    file_name = dic['name']

    if os.path.exists('./'+file_name+'.zip'):
        print('File already exist!')
    else:
        r = s.get(url)
        with open('./'+file_name+'.zip', 'wb') as f:
            f.write(r.content)
        zip_ref = zipfile.ZipFile(file_name+'.zip', 'r')
        zip_ref.extractall('hw_repo')
        zip_ref.close()
        change_filename()
        if os.path.exists('./'+file_name+'.zip'):
            os.remove('./'+file_name+'.zip')
    print('download completed')
    print(hw_sum,'students submited the homework')

def print_all_assignment(url):
    res = s.post(url)
    soup = BeautifulSoup(res.text, 'html.parser').find('div', attrs={'role':'main'})
    lst = []
    for i in soup.find_all('li', attrs={'class':"activity assign modtype_assign "}):
        dic = {}
        dic['name'] = i.find('a').text
        dic['url'] = i.find('a').get('href')
        lst.append(dic)

    for index,item in enumerate(lst):
        print(index,item['name'])
        print()
    
    download_assignment(lst[int(input('Please input homework number : '))])


def print_all_course(usr, pwd):
    url = 'https://moodle.ncnu.edu.tw/login/index.php'
    payload = {}
    payload['username'] = usr
    payload['password'] = pwd
    res = s.post(url, data=payload, allow_redirects=True)
    soup = BeautifulSoup(res.text, 'html.parser')
    #print(soup.prettify())
    lst = []
    for i in soup.find_all('div',attrs = {'class':['coursebox clearfix odd first','coursebox clearfix even','coursebox clearfix odd']}):
        if usr in i.text:
            dic = {}
            dic['name'] =i.find('a').text
            dic['url'] = i.find('a').get('href')
            #print(i.find('a').text,i.find('a').get('href'))
            lst.append(dic)

    for index,item in enumerate(lst):
        print(index,item['name'])
        print()

    print_all_assignment(lst[int(input('Please input class number : '))]['url'])


def login():
    #print('user_id: ',end='')
    usr = ''
    #print('user_password: ',end='')
    pwd = ''

    if not usr or not pwd:
        print("Please fill in your username and password (line:85,87)")
        return
    print_all_course(usr, pwd)


if __name__ == '__main__':
    if os.path.isdir('./hw_repo'):
        shutil.rmtree('./hw_repo')
    login()
