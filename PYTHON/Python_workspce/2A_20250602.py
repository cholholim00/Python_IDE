# jolse 토너/미스트 제품의 1페이지를 크롤링하여 제품명, 정가, 할인가 출력
def test1():
    from urllib.request import urlopen
    from bs4 import BeautifulSoup

    # 크롤링 대상 URL
    url = "https://www.jolse.com/category/toners-mists/1019/"
    # HTML 요청 및 응답 받기
    html = urlopen(url)
    bs_obj = BeautifulSoup(html,"html.parser")
    # print(bs_obj)

    # CSS 선택자로 제품 리스트 추출
    li_list = bs_obj.select("#contents > div.xans-element-.xans-product.xans-product-normalpackage > div.xans-element-.xans-product.xans-product-listnormal.ec-base-product > ul > li")
    for index, li in enumerate(li_list):
        # 제품명 추출
        p_name = li.select_one("div.description > strong > a > span:nth-child(2)").text
        # 정가 추출
        p_price = li.select_one("div.description > ul > li:nth-child(1)").text
        # 할인가 추출
        p_sale_price = li.select_one("div.description > ul > li:nth-child(2)").text
        print(f"[{index}]: {p_name}")
        print(f"[{index}] {p_price} | {p_sale_price}")
# test1()


# jolse 제품의 11~13페이지 크롤링 및 랜덤 지연 출력
def test2():
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    import random
    import time

    # 11~13페이지의 제품 목록 페이지를 순회하며 크롤링 수행
    for index in range(11,14):
        # 해당 페이지 번호를 포함한 URL 생성
        url = f"https://www.jolse.com/category/toners-mists/1019/?page={index}"
        # URL 요청 및 HTML 응답 수신
        html = urlopen(url)
        # HTML 문서를 파싱하여 bs_obj 객체 생성
        bs_obj = BeautifulSoup(html,"html.parser")
        # 크롤링 차단 방지를 위한 랜덤한 대기 시간 설정 (5~10초)
        second = random.randint(5,10)
        # 제품 목록에 해당하는 li 요소들을 선택
        li_list = bs_obj.select("#contents > div.xans-element-.xans-product.xans-product-normalpackage > div.xans-element-.xans-product.xans-product-listnormal.ec-base-product > ul > li")
        # 현재 페이지 번호, 대기 시간, 제품 수 출력
        print(f"***** {index}page : {second}초, {len(li_list)}건 *****")
        # 설정된 초만큼 대기
        time.sleep(second)
        for index, li in enumerate(li_list):
            # 제품명 추출
            p_name = li.select_one("div.description > strong > a > span:nth-child(2)").text
            # 정가 추출
            p_price = li.select_one("div.description > ul > li:nth-child(1)").text
            # 할인가 추출
            p_sale_price = li.select_one("div.description > ul > li:nth-child(2)").text
# test2()


# 제품정보를 수집하고 csv로 저장 (페이지 1~2)
def test3():
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    import random
    import time
    import csv
    # 결과 저장용 리스트 초기화
    prod_list = []
    # 페이지 1~2를 대상으로 제품 정보를 수집
    # 페이지 블록 번호
    block = 0
    for index in range(1,3):
        url = f"https://www.jolse.com/category/toners-mists/1019/?page={index}"
        html = urlopen(url)
        bs_obj = BeautifulSoup(html,"html.parser")
        second = random.randint(5,10)
        li_list = bs_obj.select("#contents > div.xans-element-.xans-product.xans-product-normalpackage > div.xans-element-.xans-product.xans-product-listnormal.ec-base-product > ul > li")
        print(f"***** {index}page : {second}초, {len(li_list)}건 *****")
        time.sleep(second)
        block += 1
        for index, li in enumerate(li_list):
            # 제품명 추출 및 양쪽 공백 제거
            p_name = li.select_one("div.description > strong > a > span:nth-child(2)").text
            # 정가 추출 후 'Price' 텍스트 제거 및 공백 제거
            p_price = li.select_one("div.description > ul > li:nth-child(1)").text
            p_price = p_price.replace("Price","")
            p_price = p_price.strip()
            # 할인가 추출 및 공백 제거
            p_sale_price = li.select_one("div.description > ul > li:nth-child(2)").text
            p_name = p_name.strip()
            p_sale_price = p_sale_price.strip()
            # 제품 정보를 리스트에 저장 (페이지 블록 번호 활용한 번호 포함)
            prod_list.append([block*40 + index+1, p_name, p_price, p_sale_price])
            print(f"[{index}] {p_price} | {p_sale_price}")

    # 수집된 데이터를 CSV 파일로 저장
    # 결과를 csv 파일로 저장
    header = ["번호", "제품명", "정가", "할인가"]
    with open("jolse_toners_mists.csv2", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        for item in prod_list:
            writer.writerow(item)

            print(">>> 프로그램이 종료되었습니다! <<<")
# test3()

# jolse 제품 정보를 csv로 저장 (1페이지)
def test4():
    import csv
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    import random
    import time

    # 제품 정보를 CSV로 저장 (1페이지 대상)
    with open("jolse_toners_mists.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["번호","제품명", "정가", "할인가"])

        for index in range(1, 2):
            url = f"https://www.jolse.com/category/toners-mists/1019/?page={index}"
            html = urlopen(url)
            bs_obj = BeautifulSoup(html, "html.parser")
            second = random.randint(5, 10)
            li_list = bs_obj.select("#contents > div.xans-element-.xans-product.xans-product-normalpackage > div.xans-element-.xans-product.xans-product-listnormal.ec-base-product > ul > li")
            print(f"***** {index}page : {second}초, {len(li_list)}건 *****")
            time.sleep(second)

            for li in li_list:
                # 제품명 추출
                p_name = li.select_one("div.description > strong > a > span:nth-child(2)").text
                # 정가 추출 및 'Price' 텍스트 제거
                p_price = li.select_one("div.description > ul > li:nth-child(1)").text.replace("Price", "")
                # 할인가 추출
                p_sale_price = li.select_one("div.description > ul > li:nth-child(2)").text
                writer.writerow([p_name, p_price, p_sale_price])
                print(f"{p_name} | {p_price} | {p_sale_price}")
# test4()

# 교촌치킨 메뉴 정보를 크롤링하여 csv로 저장
def test5():
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    import csv

    url = "https://www.kyochon.com/menu/chicken.asp"
    html = urlopen(url)
    bs_obj = BeautifulSoup(html, "html.parser")

    #tabCont01 > ul > li:nth-child(1)
    li_list = bs_obj.select("#tabCont01 > ul > li")
    # print(len(li_list))
    prod_list = []
    for index, li in enumerate(li_list):
        # 메뉴 이름 / 설명 / 가격을 HTML 요소에서 추출
        p_name = li.select_one("a > dl > dt").text
        p_info = li.select_one("a > dl > dd").text
        p_price = li.select_one("a > p.money > strong").text
        # 추출한 메뉴 정보를 리스트에 저장
        prod_list.append([p_name, p_info, p_price])

    # CSV 파일을 열고 헤더와 메뉴 정보 저장
    header = ["[번호],메뉴이름],[설명],[가격]"]
    # 크롤링한 데이터를 CSV로 저장
    with open("kyochon_chicken.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="|", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        for item in prod_list:
            writer.writerow(item)
    # 저장 완료 메시지 출력
    print("메뉴 내용을 저장하였습니다.")
test5()