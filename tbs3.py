from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from stem import Signal
from stem.control import Controller
import subprocess,os,random,string,time
for i in range (1000):
    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.socks", "127.0.0.1")
    profile.set_preference("network.proxy.socks_port", 9050)

    options = FirefoxOptions()
    options.add_argument("--headless")

    caps = DesiredCapabilities().FIREFOX
    caps["pageLoadStrategy"] = "eager"

    profile.update_preferences()
    torexe = subprocess.Popen(os.path.expandvars(r"C:\Users\Onebless\Desktop\tbs\Browser\TorBrowser\Tor\tor.exe"))
    time.sleep(1)
    driver = webdriver.Firefox(profile,options=options,capabilities=caps)
    try:
        driver.get('http://vote.mc256.net/1')
        time.sleep(5)
        namebox=driver.find_element(By.NAME,'mcname')
        namebox.send_keys(random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters))
        submit=driver.find_element(By.CLASS_NAME,'r3submit')
        driver.execute_script("arguments[0].click();", submit)
        try:
            submit.click()
        except:
            driver.get_screenshot_as_png('bruh.png')
            print('pass')
            pass
        time.sleep(20)
        print('go next '+str(i))
    except Exception as e:
        print(e, type(e))
        print('fail')
    finally:
        driver.quit()
        torexe.kill()