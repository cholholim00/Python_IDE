def test1():
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    
    url = "https://www.naver.com/"
    # NAVER 홈페이지 HTML 소스 요청
    html_obj = urlopen(url)
    # HTML 문서를 파싱하여 bs_obj로 저장
    bs_obj = BeautifulSoup(html_obj.read(),"html.parser")
    # 네이버 바로가기 영역의 li 항목들을 CSS 선택자로 추출
    li_list = bs_obj.select("#shortcutArea > ul > li")
    # li 요소의 개수 출력
    print(len(li_list))

# test1()


# pip install pyautogui
def test2():
    """pyautogui를 활용한 마우스 자동화 예제.
    """
    import pyautogui

    # pyautogui.write("Hello World")
    # 텍스트 입력 테스트

    # 화면 크기 출력
    # print(pyautogui.size())
    # 화면 해상도 정보 테스트

    # 마우스 위치 출력
    # print(pyautogui.position())
    # 현재 마우스 커서 위치 확인 테스트

    # 마우스 이동
    # pyautogui.moveTo(200,200)
    # pyautogui.moveTo(200, 200, 2)
    # 마우스 커서 지정 위치로 이동 테스트

    # 마우스 드래그
    # pyautogui.dragTo(200, 200, 2)
    # 마우스 드래그 동작 테스트

    # 마우스 클릭
    # pyautogui.click()
    # pyautogui.click(button="right")
    # pyautogui.doubleClick()
    # pyautogui.click(clicks=3)
    # 마우스를 3번 빠르게 클릭 (0.1초 간격)
    pyautogui.click(clicks=3, interval=0.1)

# test2()


def test3():
    """pyautogui 및 pyperclip을 사용한 키보드 자동화.
    """
    import pyautogui
    import pyperclip


    # pyautogui.write("Hello")
    # 텍스트 입력 테스트

    # Ctrl + c
    # pyautogui.keyDown('Ctrl')
    # pyautogui.press('c')
    # pyautogui.keyUp('ctrl')
    # 복사 단축키 테스트

    # Ctrl + v
    # pyautogui.keyDown('ctrl')
    # pyautogui.press('v')
    # pyautogui.keyUp('ctrl')
    # 붙여넣기 단축키 테스트

    # 키를 여러 번 입력
    # pyautogui.press(['left','left','left'])
    # pyautogui.press('enter', presses=1, interval=3)
    # 방향키 및 엔터키 입력 테스트

    # HotKey
    # pyautogui.hotkey('ctrl','c')
    # 클립보드에 문자열 저장
    pyperclip.copy("홍길동")
    # Ctrl + V 입력을 자동 수행
    pyautogui.hotkey('ctrl','v')
    pyperclip.copy("asdf1234")
    pyautogui.hotkey('ctrl','v')

# test3()


def test4():
    """메세지 박스 활용 예제 (pyautogui).
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

    # 사용자에게 구구단 단 수 입력 요청
    dan = pg.prompt("출력할 단을 입력하세요!", title="구구단", default="5")
    try:
        # 입력값을 정수로 변환 후 구구단 출력
        dan = int(dan)
        for i in range(1,10):
            print(f"{dan} x {i} = {dan*i}")
    except ValueError as e:
        # 정수가 아닌 값 입력 시 예외 처리
        print(e)

# test4()


# pip install selenium
# pip install webdriver_manager
def basic_setting(url):
    # 필요한 selenium 관련 모듈 불러오기
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    # 크롬 드라이버 자동 설치 및 실행
    from webdriver_manager.chrome import ChromeDriverManager

    # 브라우저 생성 후 꺼짐
    service = Service(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)

    # 브라우저 꺼짐 방지 옵션 적용
    options = Options()
    options.add_experimental_option("detach", True)
    service = Service(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)

    # 해당 URL 페이지 열기
    browser.get(url)

    # 브라우저 객체 반환
    return browser

# basic_setting()

def test5():
    """네이버 바로가기 영역에서 서비스 이름 추출 (selenium 활용).
    """
    from selenium.webdriver.common.by import By

    url = "https://www.naver.com"
    browser = basic_setting(url)
    # 요소 로딩 대기 설정
    browser.implicitly_wait(10)
    # 바로가기 항목 전체 선택
    li_list = browser.find_elements(By.CSS_SELECTOR, "#shortcutArea > ul > li")
    for li in li_list:
        # 각 li 요소 내 서비스 이름(span.service_name) 출력
        print(li.find_element(By.CSS_SELECTOR, "a > span.service_name").text)

test5()
