import time
from selenium import webdriver
from selenium.webdriver.common.by import By


from faker import Faker
import random


fake = Faker('ru_RU')
        

driver = webdriver.Chrome() 
driver.get('http://127.0.0.1:5000')
time.sleep(1)
element = driver.find_element(By.XPATH,  "//a[contains(text(), 'Регистрация')]")

time.sleep(1)
element.click()

name=f'{fake.first_name()} {fake.last_name()}'
password=random.choice("!@#$%^&*")+fake.first_name()+str(random.randint(0,10000000))
email=fake.email()

element = driver.find_element("name", "username")
element.send_keys(name)
element = driver.find_element("name", "password")
element.send_keys(password)
element = driver.find_element("name", "email")
element.send_keys(email)

print(name)
print(password)
print(email)

element = driver.find_element(By.XPATH, "//button[@type='submit']")
element.click()

time.sleep(3)
element = driver.find_element("name", "username")
element.send_keys(name)
element = driver.find_element("name", "password")
element.send_keys(password)

element = driver.find_element(By.XPATH, "//button[@type='submit']")
element.click()

a=input('отзыв? ')

element = driver.find_element("name", "text")
text=fake.paragraph(nb_sentences=1)
print(text)
element.send_keys(text)
time.sleep(1)
element = driver.find_element(By.XPATH, "//button[@type='submit']")
element.click()
#element = driver.find_element(By.XPATH, "//button[@type='submit']")

