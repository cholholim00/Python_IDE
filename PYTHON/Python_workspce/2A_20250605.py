def test1():
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    
    url = "https://www.naver.com/"
    html_obj = urlopen(url)
    # html_obj.read()
    bs_obj = BeautifulSoup(html_obj.read(),"html.parser")
    # print(bs_obj)
    
    li_list = bs_obj.select("#shortcutArea > ul > li")
    print(len(li_list))
    
# test1()


# pip install pyautogui
def test2():
    """마우스 자동화.
    """
    import pyautogui
    
    # pyautogui.write("Hello World")
    
    # 화면 크기 출력
    # print(pyautogui.size())
    
    # 마우스 위치 출력
    # print(pyautogui.position())
    
    # 마우스 이동
    # pyautogui.moveTo(200,200)
    # pyautogui.moveTo(200, 200, 2)
    
    # 마우스 드래그
    # pyautogui.dragTo(200, 200, 2)
    
    # 마우스 클릭
    # pyautogui.click()
    # pyautogui.click(button="right")
    # pyautogui.doubleClick()
    # pyautogui.click(clicks=3)
    pyautogui.click(clicks=3, interval=0.1)
    
# test2()


def test3():
    """키보드 자동화.
    """
    import pyautogui
    import pyperclip
    
    
    # pyautogui.write("Hello")
    
    # Ctrl + c
    # pyautogui.keyDown('Ctrl')
    # pyautogui.press('c')
    # pyautogui.keyUp('ctrl')
    
    # Ctrl + v
    # pyautogui.keyDown('ctrl')
    # pyautogui.press('v')
    # pyautogui.keyUp('ctrl')
    
    # 키를 여러 번 입력
    # pyautogui.press(['left','left','left'])
    # pyautogui.press('enter', presses=1, interval=3)
    
    # HotKey
    # pyautogui.hotkey('ctrl','c')
    pyperclip.copy("홍길동")
    pyautogui.hotkey('ctrl','v')
    pyperclip.copy("asdf1234")
    pyautogui.hotkey('ctrl','v')

# test3()


def test4():
    """메세지박스.
    """
    import pyautogui as pg
    
    # 경고창
    # pg.alert("일어나세요!", title="무제", button="ok")
    
    # 확인창
    # value = pg.confirm("오늘 다이어트할래?", title="점심", buttons=["ok","no"])
    # print(value)
    
    # 패스워드창
    # value = pg.password("비밀번호를 입력하세요", title="비밀번호", default="입력하세요", mask="*")
    # print(value)
    
    # 입력창
    dan = pg.prompt("출력할 단을 입력하세요!", title="구구단", default="5")
    try:
        dan = int(dan)
        for i in range(1,10):
            print(f"{dan} x {i} = {dan*i}")
    except ValueError as e:
        print(e)
   
# test4()


# pip install selenium
# pip install webdriver_manager
def basic_setting(url):
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    # 크롬 드라이버 자동 업데이트
    from webdriver_manager.chrome import ChromeDriverManager  
    
    # 브라우저 생성 후 꺼짐
    service = Service(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    
    # 브라우저 꺼짐 방지
    options = Options()
    options.add_experimental_option("detach", True)
    service = Service(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    
    # 원하는 주소로 이동
    # url = "https://www.naver.com"
    browser.get(url)
    
    # 브라우저 종료
    # browser.quit()
    return browser

# basic_setting()

def test5():
    from selenium.webdriver.common.by import By
    
    url = "https://www.naver.com"
    browser = basic_setting(url)
    browser.implicitly_wait(10)
    #shortcutArea > ul > li:nth-child(1)        
    li_list = browser.find_elements(By.CSS_SELECTOR, "#shortcutArea > ul > li")
    for li in li_list:
        #shortcutArea > ul > li:nth-child(1) > a > span.service_name
        print(li.find_element(By.CSS_SELECTOR, "a > span.service_name").text)
    
test5()







