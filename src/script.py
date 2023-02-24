#!/usr/bin/python3
import logging
import os
import subprocess
import time
from datetime import datetime

import undetected_chromedriver as uc

from config import dataFolder, verificationImg, sourcePage

sleepTime = 5
url = "https://nowsecure.nl/#relax"
url = "https://www.zara.com/de/de/jacke-aus-kunstleder-p08281450.html?v1=222756772"
VERSION_MAIN = 110
WORKING_DIR = os.path.join()


def saveHtmlFile(destinationDir: str, htmlResponse):
    filename = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
    savePath = os.path.join(destinationDir, filename)

    with open(savePath, "w", encoding="utf-8") as file:
        try:
            file.write(htmlResponse.text)
        except AttributeError:
            # AttributeError: 'str' object has no attribute 'text'
            file.write(htmlResponse)


logging.basicConfig(level=10)
logging.getLogger("parso").setLevel(100)

# o = uc.ChromeOptions()
# o.arguments.extend(["--no-sandbox", "--disable-setuid-sandbox"])  # these are needed to run chrome as root
driver = uc.Chrome(advanced_elements=True, version_main=VERSION_MAIN)  # driver = uc.Chrome( version_main = 108 )
driver.get(url)

logging.getLogger().info(f'sleeping {sleepTime} seconds to give site a chance to load')
time.sleep(sleepTime)  # this is only for the timing of the screenshot
logging.getLogger().setLevel(20)
driver.save_screenshot("/data/nowsecure.png")
subprocess.run(["catimg", verificationImg])
logging.getLogger().info(f'screenshot saved to {verificationImg}')
saveHtmlFile(sourcePage, driver.page_source)
logging.getLogger().info(f'source page saved to {sourcePage}')
# input("press a key to quit")
exit()
