from selenium import webdriver
import logging
from selenium.webdriver.chrome.options import Options
import time

try :
    #chromedriver元件路徑
    chromedriver = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe" 
    chrome_options = Options()
    #argument參考：http://www.assertselenium.com/java/list-of-chrome-driver-command-line-arguments/
    chrome_options.add_argument("--start-maximized")
    driver=webdriver.Chrome(executable_path=chromedriver,chrome_options=chrome_options)
    #要截圖的網站
    #driver.get('http://140.112.10.204/WebGL/DaLinPu_A/App/index.html?scene=Production_3DMP&')
    driver.get('http://127.0.0.1:8000/static/A/App/index.html?scene=Production_2_WebGL&cX=-130.6234&cY=-2.2128&cZ=3.7635&upX=0.0000&upY=0.0000&upZ=1.0000&tX=-120.1952&tY=-8.3249&tZ=3.3499')
    time.sleep(35)
    driver.save_screenshot(time.strftime('C:/02_D/13_python_code/test/%Y_%m_%d_%H_%M_%S')+'.png')
    driver.get('http://127.0.0.1:8000/static/A/App/index.html?scene=Production_2_WebGL&cX=-132.2630&cY=-7.7320&cZ=3.8907&upX=0.0000&upY=0.0000&upZ=1.0000&tX=-120.1952&tY=-8.3249&tZ=3.3499')
    time.sleep(20)
    driver.save_screenshot(time.strftime('C:/02_D/13_python_code/test/%Y_%m_%d_%H_%M_%S')+'.png')
    driver.get('http://127.0.0.1:8000/static/A/App/index.html?scene=Production_2_WebGL&cX=-120.4278&cY=-20.1698&cZ=5.7835&upX=0.0000&upY=0.0000&upZ=1.0000&tX=-120.1952&tY=-8.3249&tZ=3.3499')
    time.sleep(20)
    driver.save_screenshot(time.strftime('C:/02_D/13_python_code/test/%Y_%m_%d_%H_%M_%S')+'.png')
    driver.get('http://127.0.0.1:8000/static/A/App/index.html?scene=Production_2_WebGL&cX=-115.0743&cY=-19.1521&cZ=5.0310&upX=0.0000&upY=0.0000&upZ=1.0000&tX=-120.1952&tY=-8.3249&tZ=3.3499')
    time.sleep(20)
    driver.save_screenshot(time.strftime('C:/02_D/13_python_code/test/%Y_%m_%d_%H_%M_%S')+'.png')

except Exception as e:
    logging.basicConfig(filename='logging.txt')
    logging.warning(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    logging.warning(e)#"element is not exist");
finally:
    driver.close()