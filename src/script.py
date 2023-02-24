#!/usr/bin/python3
import logging
import os
import subprocess
import time
start_time = time.time()

import undetected_chromedriver as uc

from config import verificationImg, dataFolder

sleepTime = 4
url = "https://nowsecure.nl/#relax"
url = "https://www.zara.com/de/de/jacke-aus-kunstleder-p08281450.html?v1=222756772"
VERSION_MAIN = 110

logging.basicConfig(level=10)
logging.getLogger("parso").setLevel(100)
# o = uc.ChromeOptions()
# o.arguments.extend(["--no-sandbox", "--disable-setuid-sandbox"])  # these are needed to run chrome as root
driver = uc.Chrome(advanced_elements=True, version_main=VERSION_MAIN)
driver.get(url)
logging.getLogger().info(f'sleeping {sleepTime} seconds to give site a chance to load')
time.sleep(sleepTime)  # this is only for the timing of the screenshot
logging.getLogger().setLevel(20)
driver.save_screenshot(verificationImg)
subprocess.run(["catimg", verificationImg])
logging.getLogger().info(f'screenshot saved to {verificationImg}')
sourcePage = driver.page_source
logging.getLogger().info(f'source page saved to {dataFolder}')
# input("press a key to quit")
exit()
logging.getLogger().info("--- %s seconds ---" % (time.time() - start_time))

