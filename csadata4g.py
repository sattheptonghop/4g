import os
import datetime
import csv
import time
import json
import re
import requests
import cv2
from PIL import Image
from pyzbar import pyzbar
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
# Tạo thư mục pic nếu nó chưa tồn tại
if not os.path.exists("pic"):
    os.makedirs("pic")

# 1 | setWindowSize | 500x1200 | 
driver.set_window_size(360, 720)
# 2 | open | https://4pn.me/#/register | 
driver.get("https://csadata4g.me/#/register")

iLoop = 0
oweb = re.search(r"(.*/#/)", driver.current_url).group(0)
driver.save_screenshot("pic/csadata4g" + str(iLoop) + "test.png")
while re.search(r"/#/(.*)",driver.current_url).group(1) != "dashboard":
	try:
		element = driver.find_element(By.CSS_SELECTOR, ".tbclose-btn")
		element.click()
		print('dong thong bao')
	except:
		pass
	# 4 | click | linkText=Đăng ký | 

	if re.search(r"/#/(.*)",driver.current_url).group(1) == "register":
		print("dang o trang dang ky")
		print(driver.current_url)

		try:
			#time.sleep(1)
			iemail = driver.find_element(By.CSS_SELECTOR, ".v2board-email-whitelist-enable > .form-control:nth-child(1)")
			ipass1 = driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control")
			ipass2 = driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(3) > .form-control")
			icode = driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > .form-control")
			if iemail.get_attribute("value"):
				print('sua lai email')
				try:
					oemail = iemail.get_attribute("value")
					iemail.clear()
					#iemail.send_keys(oemail.split("@")[0])
					iemail.send_keys(oemail)
					iemail.send_keys("1")
					#iemail.send_keys("@gmail.com")
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
					#iemail.send_keys("@gmail.com")
					ipass1.click()
					ipass1.send_keys("63668890")
					ipass2.click()
					ipass2.send_keys("63668890")
					icode.send_keys("FqNAr2Mo")
					print('nhập xong')
					print(iemail.get_attribute("value"))
					try:
						element = driver.find_element(By.CSS_SELECTOR, ".tbclose-btn")
						element.click()
						print('dong thong bao')
					except:
						pass
					driver.save_screenshot("pic/csadata4g" + str(iLoop) + "nhapxong.png")
				except Exception as e:
					print("loi khi nhap email, pass")
					print(e)
					pass
			
			driver.save_screenshot("pic/csadata4g" + str(iLoop) + "tandk.png")
			print('Bat dau an nut dang ky')
			try:
				try:
					element = driver.find_element(By.CSS_SELECTOR, "span:nth-child(1)")
					driver.execute_script("arguments[0].click();", element)
				except TimeoutException:
					print('Không tìm thấy button dang ky')
				except Exception as ex:
					print('Lỗi:', ex)

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
			time.sleep(10)
			print('Ket thuc an nut dang ky')
		#wait = WebDriverWait(driver, 10)
		#wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
		except Exception as e:
			print("khong co iemail")
			print(e)
			driver.save_screenshot("pic/csadata4g" + str(iLoop) + "kci.png")
			pass

	if iLoop == 3:
		break
	else:
		iLoop = iLoop + 1
	if re.search(r"/#/(.*)",driver.current_url).group(1) == "login":
		print('Trang dang nhap')
		try:
			lemail = driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control")
			lpass = driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(3) > .form-control")
			lemail.clear()
			lemail.send_keys(ticket)
			lemail.send_keys("@gmail.com")
			time.sleep(1)
			lpass.send_keys("63668890")
			time.sleep(1)
			blogin = driver.find_element(By.CSS_SELECTOR, ".btn")
			#blogin.click()
			driver.execute_script("arguments[0].click();", blogin)
		except Exception as e:
			print(e)
			
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
		driver.save_screenshot("pic/csadata4g" + str(iLoop) + "0clash.png")
		element = driver.find_element(By.CSS_SELECTOR, ".v2board-shortcuts-item:nth-child(2) > .description")
		actions = ActionChains(driver)
		actions.move_to_element(element).perform()
		driver.execute_script("arguments[0].click();", element)
		#element.click()
		time.sleep(3)
		#driver.execute_script("window.scrollTo(0,306)")
		element = driver.find_element(By.CSS_SELECTOR, ".subscribe-for-qrcode > div:nth-child(2)")
		actions = ActionChains(driver)
		actions.move_to_element(element).perform()
		driver.execute_script("arguments[0].click();", element)
		#element.click()
		time.sleep(3)
		
		# Đợi cho phần tử canvas xuất hiện
		canvas_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "canvas")))
		# Lưu hình ảnh của canvas
		driver.save_screenshot(f"pic/screenshot.png")
		crop_area = (canvas_element.location['x']*3, (canvas_element.location['y'] - canvas_element.size['height']/2 - 4)*3, (canvas_element.location['x'] + canvas_element.size['width'])*3, (canvas_element.location['y'] + canvas_element.size['height']/2 -4)*3)
		image = Image.open(f"pic/screenshot.png")
		image = image.crop(crop_area)
		image.save(f"pic/qrcode.png")
		# Giải mã QR code
		decoded_objects = pyzbar.decode(image)

		# Lấy nội dung từ QR code
		for obj in decoded_objects:
		    data = obj.data.decode("utf-8")
		    print("QR Code content:", data)
		#element = driver.find_element(By.LINK_TEXT, "Chuyển đến Clash For Android")
		#element = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".clash-for > div:nth-child(2)")))
		#url = element.get_attribute("href")
		url = data
		#print(url)
		result = "https://convert.v2ray-subscribe.workers.dev/?url=" + url
		#.split("url=")[1].split("&name=")[0]
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
		with open('csadata4g.txt', 'w', newline='') as file:
			writer = csv.writer(file)
			if countrow >= 11:
				print("số dòng hơn 12")
				for row in rows[1:]:
					writer.writerow(row)
			else:
				print("số dòng ít hơn 12")
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
print('Kết thúc chương trình')
driver.save_screenshot("pic/csadata4g10.png")
driver.close()
driver.quit()
