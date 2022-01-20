import time
import string
import os
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

YLHSignIn = 'https://www.youlikehits.com/login.php'
twitterSignIn = 'https://twitter.com/i/flow/login'
YLHTwitter = 'https://www.youlikehits.com/twitter2.php'

# Importing Settings
settingU = json.load(open('twitter.json'))
jtopy = json.dumps(settingU)
setting = json.loads(jtopy)

# Starting Chromedriver
print('Starting...')
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "normal"
chrome_options = Options()
if setting["headlessmode"]:
	chrome_options.add_argument("--headless")
chrome_options.add_argument("--mute-audio")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options, desired_capabilities=caps)
os.system('clear')

# Sign in to Twitter
driver.get(twitterSignIn)
time.sleep(7)
driver.implicitly_wait(1)
driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input').send_keys(setting["twitterUsername"])
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label').send_keys(setting["twitterPassword"])
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div').click()
time.sleep(3)
#input('Press Enter After You Have Entered Code And Logged In')

# Sign in to YLH
driver.get(YLHSignIn)
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(setting["YLHUsername"])
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(setting["YLHPassword"])
driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/center/form/table/tbody/tr[3]/td/span/input').click()
if setting["headlessmode"] == False:
	input('Press Enter to Confirm Successful Login')

# Get Current Points
driver.get(YLHTwitter)
driver.implicitly_wait(3)
startpointss = driver.find_element(By.XPATH, '//*[@id="currentpoints"]').text
startpoints = int(startpointss.replace(',', ''))

# Twitter Loop
def ylhtwitter():
	driver.get(YLHTwitter)
	followbuttons = []
	confirmbuttons = []
	allbuttons = driver.find_elements(By.CLASS_NAME, 'followbutton')
	YLHTwitterPage = driver.current_window_handle
	for button in allbuttons:
		if button.text == 'Follow':
			followbuttons.append(button)
			if len(followbuttons) > 6:
				break
			continue
		if button.text == 'Confirm':
			confirmbuttons.append(button)
			if len(followbuttons) > 6:
				break
			continue

	loops = 0
	for button in followbuttons:
		driver.switch_to.window(YLHTwitterPage)
		try:
			button.click()
		except:
			loops += 1
			continue
		time.sleep(3)
		for handle in driver.window_handles:
			if handle != YLHTwitterPage:
				followPage = handle
		complete = 0
		fails = 0
		# Follow

		# Wait for the stupid redirect
		while complete != 1:
			try:
				action = webdriver.common.action_chains.ActionChains(driver)
				driver.switch_to.window(followPage)
				try:
					driver.find_element(By.XPATH, '//*[@id="autoclick"]/b').click()
				except:
					time.sleep(5)
				time.sleep(3)
				driver.implicitly_wait(1.5)
				twitterfollowbtn = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div')
				action.click_and_hold(twitterfollowbtn).perform()
				time.sleep(0.2)
				action.release().perform()
				time.sleep(2)
				complete = 1
			except:
				fails += 1
				if fails > 10:
					complete = 1
				pass
		# Confirm
		driver.close()
		driver.switch_to.window(YLHTwitterPage)
		try:
			confirmbuttons[loops].click()
		except:
			pass
		time.sleep(5)
		loops += 1


for i in range(1):
	ylhtwitter()

driver.implicitly_wait(3)
endpointss = driver.find_element(By.XPATH, '//*[@id="currentpoints"]').text
endpoints = int(endpointss.replace(',', ''))
earnedpoints = endpoints - startpoints
os.system('clear')
print(f'Finished\n{earnedpoints} Points Earned')
driver.quit()
