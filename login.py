#!/usr/bin/python

from selenium import webdriver

#set server address, user_id and password here
URL = "http://10.120.120.22:8090"
USER = "admin"
PASS = "pass"

#To Do
#add support to change details from cmd

browser = webdriver.Firefox()
browser.get(URL)

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")
submit = browser.find_element_by_name("btnSubmit")

username.send_keys(USER)
password.send_keys(PASS)
submit.submit()

browser.close()