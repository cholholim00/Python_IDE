def basic_setting(url):
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    # 크롬 드라이버 자동 업데이트
    from webdriver_manager.chrome import ChromeDriverManager  
    
    # 브라우저 생성 후 꺼짐
    # service = Service(executable_path=ChromeDriverManager().install())
    # browser = webdriver.Chrome(service=service)
    
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


# def test1():
#     import pyperclip
#     import pyautogui
#     import time
#     from selenium.webdriver.common.by import By
    
#     url = "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/"
#     browser = basic_setting(url)
#     browser.implicitly_wait(10)
    
    
#     #id
#     time.sleep(2)
#     browser.find_element(By.CSS_SELECTOR,'#id').click()
#     pyperclip.copy('evas91')
#     pyautogui.hotkey('ctrl','v')
    
#     #pw
#     time.sleep(2)
#     browser.find_element(By.CSS_SELECTOR, '#pw').click()
#     pyperclip.copy('나의비밀번호')
#     passwd = pyautogui.password("비밀번호를 입력하세요", title="비밀번호", default="입력하세요", mask='*')
#     pyperclip.copy(passwd)
#     pyautogui.hotkey('ctrl','v')
    
#     # 로그인 버튼
#     time.sleep(2)
#     button = browser.find_element(By.CSS_SELECTOR,'#log\.login')
#     button.click()

# test1()


def test2():
    """다음 사이트에 로그인 하고, 5초 후에 로그아웃 하기
    """
    import pyperclip
    import pyautogui
    import time
    from selenium.webdriver.common.by import By
    
    # 다음 로그인 페이지 URL 설정
    url = "https://accounts.kakao.com/login/?continue=https%3A%2F%2Fwww.daum.net#login"
    # selenium 크롬 브라우저 실행 및 URL 열기
    browser = basic_setting(url)
    # 요소 로딩을 위한 암시적 대기 설정
    browser.implicitly_wait(10)

    # 로그인 ID 입력 과정 시작
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR,'#loginId--1').click()
    time.sleep(1)
    pyperclip.copy("evas91@daum.net")
    # pyautogui.hotkey('ctrl','v')
    # ctrl 키 누르기
    pyautogui.keyDown('ctrl')
    # v 키 누르기 (붙여넣기)
    pyautogui.press('v')
    # ctrl 키 떼기
    pyautogui.keyUp('ctrl')

    # 비밀번호 입력 과정 시작
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, '#password--2').click()
    passwd = pyautogui.password("비밀번호를 입력하세요", title="비밀번호", default="입력하세요", mask='*')
    pyperclip.copy(passwd)
    # pyautogui.hotkey('ctrl','v')
    # ctrl 키 누르기
    pyautogui.keyDown('ctrl')
    # v 키 누르기 (붙여넣기)
    pyautogui.press('v')
    # ctrl 키 떼기
    pyautogui.keyUp('ctrl')

    # 로그인 버튼 클릭
    #mainContent > div > div.login_kakaomail > form > div.confirm_btn > button.btn_g.highlight.submit
    time.sleep(2)
    button = browser.find_element(By.CSS_SELECTOR,'#mainContent > div > div.login_kakaomail > form > div.confirm_btn > button.btn_g.highlight.submit')
    button.click()

# test2()


def test3():
    # 필요한 모듈 임포트: 클립보드 조작, 키보드 자동화, 시간 지연, CSV 파일 저장, 셀레니움 요소 제어
    import pyperclip
    import pyautogui
    import time
    import csv
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys

    # 네이버 쇼핑 메인 페이지
    url = "https://shopping.naver.com/ns/home"
    # selenium 브라우저 실행
    browser = basic_setting(url)
    # 요소 로딩을 위한 암시적 대기 설정
    browser.implicitly_wait(10)

    # 창을 최대화하여 모든 요소가 보이도록 설정
    browser.maximize_window()
    time.sleep(10)

    # 검색창에 커서 이동
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, '#gnb-gnb > div._gnb_header_area_nfFfz > div > div._gnbContent_gnb_content_JUwjU > div._gnbSearch_gnb_search_ULxKx > form > div > div > div > div > input').click()

    # 검색창에 검색어 붙여넣기
    time.sleep(1)
    pyperclip.copy('오메가3 고려은단')
    pyautogui.hotkey('ctrl','v')

    # 검색버튼 클릭하기
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR,'#gnb-gnb > div._gnb_header_area_nfFfz > div > div._gnbContent_gnb_content_JUwjU > div._gnbSearch_gnb_search_ULxKx > form > div > div > div > div > button._searchInput_button_search_wu9xq._nlog_click').click()

    # 스크롤창의 높이 비교를 통해 페이지 끝까지 스크롤
    before = browser.execute_script("return window.scrollY")

    while True:
        browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
        time.sleep(2)
        after = browser.execute_script("return window.scrollY")
        if before == after:
            break
        before = after


    # 상품 목록 추출
    item_list = browser.find_elements(By.CSS_SELECTOR,"#composite-card-list > div > ul.compositeCardList_product_list__Ih4JR > li")
    prod_list = []
    print(f"item_list:{len(item_list)}")
    for index, item in enumerate(item_list):
        # 상점명 추출 시도
        try:
            p_shop = item.find_element(By.CSS_SELECTOR,"div.productCardMallLink_product_card_mall_link__H7GC2.productCardMallLink_view_type_grid2__ou5fk > a > span").text
        except Exception as e:
            # 요소가 없을 경우 예외 처리 및 빈 문자열 할당
            print(f"Exception[p_shop]: {e}")
            p_shop = ""

        # 제품명 추출 시도
        try:
            p_name = item.find_element(By.CSS_SELECTOR,"strong").text
        except Exception as e:
            # 요소가 없을 경우 예외 처리 및 빈 문자열 할당
            print(f"Exception[p_name]: {e}")
            p_name = ""

        # 가격 추출 시도
        try:
             p_price = item.find_element(By.CSS_SELECTOR,"div.basicProductCardInformation_wrap_price__largu > div > div > div.priceTag_wrap_content__fTsdA > div > span > span.priceTag_number__1QW0R").text
        except Exception as e:
            # 요소가 없을 경우 예외 처리 및 빈 문자열 할당
            print(f"Exception[p_price]: {e}")
            p_price = ""

        prod_list.append([index+1, p_shop, p_name, p_price])

    # 결과를 CSV 파일로 저장
    header = ["번호","상점이름","제품명","가격"]
    with open("naver_shopping.csv","w",encoding="utf8",newline="") as f:
        writer = csv.writer(f,delimiter=",",quotechar='"',quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(header)
        for item in prod_list:
            # 추출된 정보를 파일에 기록
            writer.writerow(item)

    print("파일에 저장되었습니다!")

test3()

