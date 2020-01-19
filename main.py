import requests,openpyxl,datetime,time
from bs4 import BeautifulSoup
from selenium import webdriver
while True :
    ch=input('Save as a file or not (Y or N) :')
    if ch == 'Y' or ch == 'N' :
        break
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
res=requests.get('http://jwc.scu.edu.cn/',headers=headers)
res.encoding='utf-8'
bs=BeautifulSoup(res.text,'html.parser')
t1=bs.find('div',class_='list-ll-b')
t2=t1.find_all('li',class_='list-llb-list')
res=[]
if ch == 'Y':
    wb=openpyxl.Workbook()
    sheet=wb.active
    sheet.title='教务处通知'
    sheet['A1']='级别'
    sheet['B1']='通知'
    sheet['C1']='时间'
    sheet['D1']='地址'
    i=2
    a='C'
for row in t2 :
    namet=row.find('span',class_='list-llb-text').text
    datet=row.find('em',class_='fr list-date-a').text
    url=row.find('a')['href']
    print('级别：学校\n通知名称：{}\n时间：{}\n链接：{}'.format(namet,datet[1:11],url))
    print('-'*100)
    if ch=='Y' :
        sheet.append(['学校', namet, datet[1:11], url])
        sheet[a+str(i)].hyperlink = url
        i += 1

#sheet.append([])
#i += 1

#res=requests.get('http://cs.scu.edu.cn/',headers=headers)
#res.encoding='utf-8'
#bs=BeautifulSoup(res.text,'html.parser')
#print('{}'.format(bs))
#t1=bs.find('div',class_='inform_box fl')
#print('{}'.format(t1))
#t2=t1.find_all('li')
#for row in t2 :
#    namet=row.find('a').text
#    datet=row.find('span',class_='fr')
#    url=row.find('a')['href']
#    sheet.append(['计院',namet,datet,url])
#    sheet[a + str(i)].hyperlink = url
#    i += 1

#res=requests.get('http://cs.scu.edu.cn/index/xytz.htm')
#res.encoding='utf-8'
#bs=BeautifulSoup(res.text,'html.parser')
#print('{}'.format(bs))

#option = webdriver.ChromeOptions()
#option.add_argument('headless')
#driver=webdriver.Chrome(options=option)
#driver.get('http://cs.scu.edu.cn/')
#time.sleep(5)
#t1=driver.find_element_by_css_selector('inform_box fl').find_element_by_css_selector('inform').find_elements_by_class_name('li')
#for t in t1 :
#    time=t.find_element_by_css_selector('fr').text
#    name=t.find_element_by_css_selector('a').text
#    url=t.find_element_by_name('a')['href']
#    print('{} {} {}'.format(time ,name,url))
if ch == 'Y' :
    now_time = datetime.datetime.now().strftime('%Y-%m-%d')
    wb.save(now_time+'_四川大学教务处通知.xls')
print('Process access.')