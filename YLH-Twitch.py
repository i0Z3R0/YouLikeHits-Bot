import time
import string
import os
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

YLHSignIn = 'https://www.youlikehits.com/login.php'
twitchSignIn = 'https://www.twitch.tv/login'
YLHTwitch = 'https://www.youlikehits.com/twitch.php'

# Importing Settings
settingU = json.load(open('settings.json'))
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

# Sign in to Twitch
driver.get(twitchSignIn)
driver.implicitly_wait(1)
driver.find_element(By.XPATH, '//*[@id="login-username"]').send_keys(setting["twitchUsername"])
driver.find_element(By.XPATH, '//*[@id="password-input"]').send_keys(setting["twitchPassword"])
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[3]/button/div/div').click()
time.sleep(3)
try:
	driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div/div/div/div[3]/div[3]/button').click()
except:
	if setting["headlessmode"]:
		print('Possible Captcha Detected, Restart Program Please')
#input('Press Enter After You Have Entered Code And Logged In')
twitchcode = input("Twitch Email Code: ")
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div/div/div/div[3]/div[2]/div/div[1]/div/input').send_keys(twitchcode)
time.sleep(5)

# Sign in to YLH
driver.get(YLHSignIn)
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(setting["YLHUsername"])
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(setting["YLHPassword"])
driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/center/form/table/tbody/tr[3]/td/span/input').click()
if setting["headlessmode"] == False:
	input('Press Enter to Confirm Successful Login')

# Get Current Points
driver.get(YLHTwitch)
driver.implicitly_wait(3)
startpointss = driver.find_element(By.XPATH, '//*[@id="currentpoints"]').text
startpoints = int(startpointss.replace(',', ''))

# Twitch Loop
def ylhtwitch():
	driver.get(YLHTwitch)
	followbuttons = []
	confirmbuttons = []
	allbuttons = driver.find_elements(By.CLASS_NAME, 'followbutton')
	YLHTwitchPage = driver.current_window_handle
	for button in allbuttons:
		if button.text == 'Follow':
			followbuttons.append(button)
			continue
		if button.text == 'Confirm':
			confirmbuttons.append(button)
			continue

	loops = 0
	for button in followbuttons:
		driver.switch_to.window(YLHTwitchPage)
		try:
			button.click()
		except:
			loops += 1
			continue
		time.sleep(3)
		for handle in driver.window_handles:
			if handle != YLHTwitchPage:
				followPage = handle
		complete = 0
		fails = 0
		# Follow
		while complete != 1:
			try:
				action = webdriver.common.action_chains.ActionChains(driver)
				driver.switch_to.window(followPage)
				time.sleep(5)
				try:
					# Time Machine
					if "time machine" in driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div/div/div[2]/p').text.lower()
				except:
					pass
				driver.implicitly_wait(1.5)
				twitchfollowbtn = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div/div/div/button')
				action.click_and_hold(twitchfollowbtn).perform()
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
		driver.switch_to.window(YLHTwitchPage)
		try:
			confirmbuttons[loops].click()
		except:
			pass
		time.sleep(5)
		loops += 1


ylhtwitch()

driver.implicitly_wait(3)
endpointss = int(driver.find_element(By.XPATH, '//*[@id="currentpoints"]').text)
endpoints = int(endpointss.replace(',', ''))
earnedpoints = endpoints - startpoints
os.system('clear')
print(f'Finished\n{earnedpoints} Earned')
