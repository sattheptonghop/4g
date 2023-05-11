import os
import datetime
import csv
import time
import json
import re
import requests
from urllib.parse import urlparse
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
#from chromedriver_binary import chromedriver_binary_path

chrome_service = Service(ChromeDriverManager().install())
chrome_options = Options()
options = [
	"--headless",
	"--window-size=800,1200",
	"start-maximized",
	"disable-infobars",
	"--disable-gpu",
	"--ignore-certificate-errors",
	"--disable-extensions",
	"--no-sandbox",
	"--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

mobile_emulation = {
    "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
    "userAgent": "Mozilla/5.0 (Android 12; Mobile; LG-M255; rv:100.0) Gecko/100.0 Firefox/100.0Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Mobile Safari/537.36"
}
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
#driver = webdriver.Chrome(executable_path=chromedriver_binary_path, service=chrome_service, options=chrome_options)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# 1 | setWindowSize | 500x1200 | 
driver.set_window_size(360, 720)
# 2 | open | https://4pn.me/#/register | 
driver.get("https://4pn.me/#/register")

iLoop = 0
oweb = re.search(r"(.*/#/)", driver.current_url).group(0)
while re.search(r"/#/(.*)",driver.current_url).group(1) != "dashboard":
	try:
		element = driver.find_element(By.CSS_SELECTOR, ".tbclose-btn")
		element.click()
		print('dong thong bao')
	except:
		pass
	# 4 | click | linkText=Đăng ký | 
	if re.search(r"/#/(.*)",driver.current_url).group(1) == "login":
		print(driver.current_url)
		print('Thu chuyen toi trang dang ky')
		#driver.save_screenshot("pic/tltvpncom" + str(iLoop) + "tcttdk.png")
		try:
			#element = driver.find_element(By.LINK_TEXT, "Đăng ký")
			element = driver.find_element(By.XPATH, "//main[@id=\'main-container\']/div/div/div/div[2]/div/form/div[2]/p/a[2]")
			element.click()
			#driver.execute_script("arguments[0].click();", element)
			print('an dang ky')
		except Exception as e:
			#ko duoc
			#driver.close
			#driver.get("https://tnetz.pro/#/register")
			print('ko an duoc nut dang ky, thu chay bang link')
			print(e)
			pass
		time.sleep(1)
			
	if re.search(r"/#/(.*)",driver.current_url).group(1) == "register":
		print("dang o trang dang ky")
		print(driver.current_url)

		try:
			time.sleep(1)
			iemail = driver.find_element(By.CSS_SELECTOR, ".input-group > .form-control")
			ipass1 = driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control")
			ipass2 = driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(3) > .form-control")
			#iemail = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='input-group']/input[@class='form-control form-control-lg form-control-alt']")))
			#ipass1 = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='py-3']/div[2]/input[@class='form-control form-control-lg form-control-alt']")))
			#ipass2 = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//div[3]/input[@class='form-control form-control-lg form-control-alt']")))
			#driver.implicitly_wait(3)
			if iemail.get_attribute("value"):
				print('sua lai email')
				try:
					oemail = iemail.get_attribute("value")
					iemail.clear()
					iemail.send_keys(oemail.split("@")[0])
					iemail.send_keys("1")
					iemail.send_keys("@gmail.com")
					print(iemail.get_attribute("value"))
					#iemail.send_keys(oemail.split("@")[1])
				except Exception as e:
					print("loi khi sua email")
					print(e)
					pass
			else:
				try:
					print('Đăng ký và đăng nhập')
					ticket = driver.execute_script("return Math.random(). toString(36).substring(2,16)")
					iemail.click()
					iemail.send_keys(ticket)
					iemail.send_keys("@gmail.com")
					ipass1.click()
					ipass1.send_keys("63668890")
					ipass2.click()
					ipass2.send_keys("63668890")
					print('nhập xong')
					print(iemail.get_attribute("value"))
					try:
						element = driver.find_element(By.CSS_SELECTOR, ".tbclose-btn")
						element.click()
						print('dong thong bao')
					except:
						pass
					#driver.save_screenshot("pic/tltvpncom" + str(iLoop) + "nhapxong.png")
				except Exception as e:
					print("loi khi nhap email, pass")
					print(e)
					pass

			print("Bat dau an nut dong y dieu khoan")
			try:
				if driver.execute_script("return (document.querySelector(\"#signup-terms\").checked != true)"):
					element = driver.find_element(By.CSS_SELECTOR, "#signup-terms")
					driver.execute_script("arguments[0].click();", element)
					#element.send_keys(Keys.TAB)
					#element.send_keys(Keys.RETURN)
			except Exception as e:
				print(e)
				pass
			print("Ket thuc an nut dong y dieu khoan")
			
			#driver.save_screenshot("pic/tltvpncom" + str(iLoop) + "tandk.png")
			print('Bat dau an nut dang ky')
			try:
				##print("Bat dau Chuyển iframe")
				##print(driver.current_url)
				##try:
				##	print("Chuyển sang iframe")
				##	iframe = driver.find_element(By.XPATH, '//iframe[2]')
				##	driver.switch_to.frame(iframe)
				##except:
				##	print("Ko Chuyển sang iframe dc")
				##	pass
				try:
					driver.find_element(By.CSS_SELECTOR, ".btn-block").click()
				except TimeoutException:
					print('Không tìm thấy button có class là "btn-block"')
					try:
						driver.find_element(By.CSS_SELECTOR, ".fa-fw").click()
					except TimeoutException:
						print('Không tìm thấy button có class là ".fa-fw"')
					except Exception as ex:
						print('Lỗi:', ex)
				except Exception as ex:
					print('Lỗi:', ex)

				#driver.execute_script("arguments[0].click();", element)
				print('an nut dang ky pa1')
				print(driver.current_url)
			except Exception as e:
				#ko duoc
				print('ko an duoc nut dang ky')
				# Tìm tất cả các phần tử HTML có thể click được và in ra tên của chúng
				elements = driver.find_elements(By.XPATH, '//*[@onclick or @href]')
				for element in elements:
				    print(element.get_attribute('outerHTML'))
				pass
			print('Ket thuc an nut dang ky')
		#wait = WebDriverWait(driver, 10)
		#wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
		except Exception as e:
			print("khong co iemail")
			print(e)
			#driver.save_screenshot("pic/tltvpncom" + str(iLoop) + "kci.png")
			pass
		##print("Bat dau Chuyển lai iframe")
		##print(driver.current_url)
		##try:
		##	print("Chuyển lai iframe")
		##	driver.switch_to.default_content()
		##except:
		##	print("Ko Chuyển lai iframe dc")
		##	pass
		##print(driver.current_url)
	if iLoop == 3:
		break
	else:
		iLoop = iLoop + 1
if re.search(r"/#/(.*)",driver.current_url).group(1) == "dashboard":
	print('Trang quan tri dashboard')

	try:
		WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".tbclose-btn"))).click()
		#driver.find_element(By.CSS_SELECTOR, ".tbclose-btn").click()
	except Exception as e:
		print('ko co qc sau khi dang nhap')
		pass

	print('Lấy link clash')
	##chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
	##driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
	##driver.refresh()
	try:
		element = driver.find_element(By.CSS_SELECTOR, ".row:nth-child(1) .font-size-base")
		actions = ActionChains(driver)
		actions.move_to_element(element).perform()
		driver.execute_script("window.scrollTo(0,306)")
		driver.find_element(By.XPATH, "//main[@id=\'main-container\']/div/div[2]/div/div/div[2]/div/div[2]/a").click()
		#element = driver.find_element(By.LINK_TEXT, "Chuyển đến Clash For Android")
		element = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.LINK_TEXT, "Chuyển đến Clash For Android")))
		url = element.get_attribute("href")
		result = "https://convert.v2ray-subscribe.workers.dev/?url=" + url.split("url=")[1].split("&name=")[0]
		print("result=")
		print(result)
		
		# Mở tệp CSV để ghi dữ liệu
		today = datetime.datetime.now()
		with open('tltvpncom.txt', mode='r', newline='') as vpn_file:
			reader = csv.reader(vpn_file)
			rows = list(reader)
			countrow = len(rows)
			print("countrow=", countrow)

		# Ghi file mới với nội dung đã chỉnh sửa
		with open('tltvpncom.txt', 'w', newline='') as file:
			writer = csv.writer(file)
			if countrow >= 5:
				print("số dòng hơn 5")
				for row in rows[1:]:
					writer.writerow(row)
			else:
				print("số dòng ít hơn 5")
				for row in rows:
					writer.writerow(row)
			writer.writerow([result])
	except Exception as e:
		print(e)
		pass
	print('Xong Lấy link clash')
	try:
		print('Thử đăng xuất')
		# 20 | mouseOver | css=.fa-angle-down | 
		element = driver.find_element(By.CSS_SELECTOR, ".fa-angle-down")
		actions = ActionChains(driver)
		actions.move_to_element(element).perform()
		# ko tim thay
		#driver.find_element(By.LINK_TEXT, "Đăng xuất").click()
	except Exception as e:
		print('Thất bại đăng xuất')
		#print(e)
		pass


	
# Đóng trình duyệt web
driver.save_screenshot("pic/tltvpncom10.png")
driver.close()
driver.quit()
