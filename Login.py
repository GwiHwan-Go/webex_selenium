# 모듈설명 
# 입력받은 웹엑스이메일과 비밀번호, 클래스이름으로 해당 수업 시작
# 원래는 웹버전으로 스트리밍을 시작해 모든과정의 전 자동화를 하려 하였으나, 웹엑스 스트리밍 웹버전의 크롤링이 불가하여 몇몇 작업을 수동으로 전환
# 웹크롤링을 위해 bs4 와 selenium을 이용
# python3 -m venv tutorial-env, source tutorial-env/bin/activate


import bs4
from urllib.parse import quote_plus #한국어 처리
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


def login(email,pwd, class_name):
    url = 'https://www.webex.com/ko/index.html'
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome('/Users/gwihwango/Desktop/python project/project/chromedriver',chrome_options=chrome_options)#chrome driver 의 경로

    driver.get(url)

    # password = input('Webex의 비밀번호를 입력해 주세요 : ')
    # useremail = 'ie1914@naver.com'
    # userpassword = 'Sangin62'
    useremail = email
    userpassword = pwd

    login_menu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wbx-header"]/nav/div/div/ul/li[7]/div/a')))
    login_menu.click()
    login_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ' //*[@id="wbx-header"]/nav/div/div/ul/li[7]/div/div/div/ul/li[1]/div/a/div[1]')))
    login_option.click()

    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sign-in"]/div[1]/div/form/div[1]/div/div[1]/input')))
    username.send_keys(useremail)
    username_click = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sign-in"]/div[1]/div/form/div[2]/div/button')))
    username_click.click()

    password_ = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sign-in"]/div[1]/div/form/div[2]/div/div/input')))
    password_.send_keys(userpassword)
    password_click = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sign-in"]/div[1]/div/form/div[3]/div/button')))
    password_click.click()

    # meeting_option = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main_content"]/div/div[1]/div[1]/div[1]/div/div[2]/div/a/div/button[2]')))
    # builder = ActionChains(driver)
    # builder.click(meeting_option).send_keys(Keys.DOWN).send_keys(Keys.DOWN).send_keys(Keys.RETURN)
    # builder.perform()

    # class_name = input('시작하실 수업명을 정확히 기재해주세요. : ')
    # class_name = '문제해결과 알고리즘'

    class_list = driver.find_elements_by_xpath('//*[@id="main_content"]/div/div[1]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[1]/div[1]/a')

    if len(class_list)>1 :
        meeting_list = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main_content"]/div/div[1]/div[2]/div/div/div[2]/a')))
        meeting_list.click()
        driver.implicitly_wait(3)
        all_name = driver.find_elements_by_xpath('//*[@id="main_content"]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/div/div[3]/div[1]/div[1]/a')

        for i in range(len(all_name)) :
            # print(all_name[i].text)
            if all_name[i].text[:-1] == class_name :
                print(all_name[i].text)
                xpath_='//*[@id="main_content"]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/'
                nameidx = 'div[{}]'.format(i+1)
                xpath_tail = '/div[4]/span/button'
                meeting_start = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_+nameidx+xpath_tail)))
                meeting_start.click()

    else : #수업이 하나밖에 없을때
        meeting_start = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main_content"]/div/div[1]/div[2]/div/div/div/div[1]/div/div[4]/span/button')))
        meeting_start.click()


if __name__ == '__main__':
    login('ie1914@naver.com','Sangin62','문제해결과 알고리즘')