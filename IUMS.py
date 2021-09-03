# @todo Take over the world

from selenium import webdriver
PATH="C:\Program Files (x86)\chromedriver.exe"
######################################################################  IUMS E-Mail Update  ################################################################

## Search any item from a page
# import keys to hit enter or other things in a page
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
import os
import operator
# Import Python Packages
import smtplib, ssl
import filecmp
from getpass import getpass

directory='Grades'
if not os.path.exists(directory):
    os.makedirs(directory)
    f1 = open("Grades/Spring, 2020True.txt", "w")
    f2 = open("Grades/Spring, 2020False.txt", "w")
    # closing files
    f1.close()
    f2.close()

flag=True


# reading files
def read():
  global flag

  compare=filecmp.cmp('Grades/Spring, 2020True.txt', 'Grades/Spring, 2020False.txt')
  message=''

  if compare==False:
    global session
    # Create Email
    gmail_user = 'boi.yourbook@gmail.com'
    gmail_password = 'password'
    mail_from = gmail_user
    mail_to = 'nipun4338@gmail.com'
    mail_subject = 'IUMS Result Changed'
    flag1=operator.not_(flag)
    with open(f'Grades/{session}{flag}.txt', 'r') as f:
      message+=f.read()
      with open(f'Grades/{session}{flag1}.txt', 'w') as f3:
        f3.write(message)
        f3.close()
      mail_message = f'''IUMS Result Changed!\nLast Update:\n\n{message}'''
      # Sent Email
      context = ssl.create_default_context()
      with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(gmail_user, gmail_password)
        server.sendmail(mail_from, mail_to, mail_message)
        server.quit()
      f.close()
      print('Email Sent!')


def find_grade():
  global flag
  flag=operator.not_(flag)
  driver = webdriver.Chrome(PATH)
  driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
  driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
  driver.get("https://iums.aust.edu/ums-web/login/")

  global username
  global password

  # find the input box by name
  search1=driver.find_element_by_id('userName')

  # send the text to the box
  search1.send_keys(username)


  # find the input box by name
  search2=driver.find_element_by_id('password')

  # send the text to the box
  search2.send_keys(password)
  #print(search1.get_attribute("value"))
  #print(search2.get_attribute("value"))

  link=driver.find_element_by_css_selector('#login_btn')
  link.click()

  time.sleep(5)
  link=driver.find_element_by_link_text('Result')
  link.click()

  time.sleep(3)
  select=Select(driver.find_element_by_id('semester_id'))
  #select.select_by_value('11012020')
  global session

  select.select_by_visible_text(session)

  link=driver.find_element_by_css_selector('#leftDiv > div.panel-body.pan > form > div.form-actions.text-right.pal > button')
  link.click()
  time.sleep(3)

  semester=driver.find_element_by_css_selector('#rightDiv > div.panel.ng-scope > div.panel-heading.ng-binding')
  print(semester.text)
  print('')
  table=driver.find_element_by_css_selector('#rightDiv > div.panel.ng-scope > div.panel-body > div:nth-child(3) > table')
  grades=table.find_elements_by_class_name('ng-scope')
  with open(f'Grades/{session}{flag}.txt', 'w') as f:
    f.write('{:^8}'.format('Course'))
    f.write('{:^8}'.format('Credit'))
    f.write('{:^8}'.format('Grade'))
    f.write('{:^8}'.format('GPA'))
    f.write('{:^8}'.format('Title'))
    f.write('\n')
    for grade in grades:
      names=grade.find_elements_by_tag_name('td')
      x=''
      for index, name in enumerate(names):
        if index!=1 and index<5:
          f.write('{:^8}'.format(name.text))
        elif index==1:
          x=name.text
      f.write(x)
      f.write('\n')
    f.close()


if __name__=='__main__':
  global username
  global password
  global session
  username=input('Enter your IUMS username (EX: 180X0XXXX): ')
  password=input('Enter your IUMS password: ')
  session=input('Enter your session (EX: Spring, 2020): ')
  while True:
    find_grade()
    time_wait=10
    read()
    print(f'Wainting {time_wait} minutes...')
    time.sleep(600)
