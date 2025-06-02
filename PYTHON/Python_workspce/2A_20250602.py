def test1():
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    
    url = "https://www.jolse.com/category/toners-mists/1019/"
    html = urlopen(url)
    bs_obj = BeautifulSoup(html,"html.parser")
    # print(bs_obj)
    
    li_list = bs_obj.select("#contents > div.xans-element-.xans-product.xans-product-normalpackage > div.xans-element-.xans-product.xans-product-listnormal.ec-base-product > ul > li")
    for index, li in enumerate(li_list):
        p_name = li.select_one("div.description > strong > a > span:nth-child(2)").text
        p_price = li.select_one("div.description > ul > li:nth-child(1)").text
        p_sale_price = li.select_one("div.description > ul > li:nth-child(2)").text
        print(f"[{index}]: {p_name}")
        print(f"[{index}] {p_price} | {p_sale_price}")
# test1()


def test2():
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    import random
    import time
    
    for index in range(11,14):
        url = f"https://www.jolse.com/category/toners-mists/1019/?page={index}"
        html = urlopen(url)
        bs_obj = BeautifulSoup(html,"html.parser")
        second = random.randint(5,10)
        li_list = bs_obj.select("#contents > div.xans-element-.xans-product.xans-product-normalpackage > div.xans-element-.xans-product.xans-product-listnormal.ec-base-product > ul > li")
        print(f"***** {index}page : {second}초, {len(li_list)}건 *****")
        time.sleep(second)
        for index, li in enumerate(li_list):
            p_name = li.select_one("div.description > strong > a > span:nth-child(2)").text
            p_price = li.select_one("div.description > ul > li:nth-child(1)").text
            p_sale_price = li.select_one("div.description > ul > li:nth-child(2)").text
# test2()


def test3():
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    import random
    import time
    import csv
    prod_list = []
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
            p_name = li.select_one("div.description > strong > a > span:nth-child(2)").text
            p_price = li.select_one("div.description > ul > li:nth-child(1)").text
            p_sale_price = li.select_one("div.description > ul > li:nth-child(2)").text
            p_name = p_name.strip()
            p_price = p_price.replace("Price","")
            p_price = p_price.strip()
            p_sale_price = p_sale_price.strip()
            prod_list.append([block*40 + index+1, p_name, p_price, p_sale_price])
            print(f"[{index}] {p_price} | {p_sale_price}")

        header = ["번호", "제품명", "정가", "할인가"]
        with open("jolse_toners_mists.csv2", "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(header)
            for item in prod_list:
                writer.writerow(item)

                print(">>> 프로그램이 종료되었습니다! <<<")
# test3()

# 제품명 정가 할인가 csv 파일로 만들기
def test4():
    import csv
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    import random
    import time

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
                p_name = li.select_one("div.description > strong > a > span:nth-child(2)").text
                p_price = li.select_one("div.description > ul > li:nth-child(1)").text.replace("Price", "")
                p_sale_price = li.select_one("div.description > ul > li:nth-child(2)").text
                writer.writerow([p_name, p_price, p_sale_price])
                print(f"{p_name} | {p_price} | {p_sale_price}")
# test4()

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
        #tabCont01 > ul > li:nth-child(1) > a > dl > dt
        p_name = li.select_one("a > dl > dt").text
        #tabCont01 > ul > li:nth-child(1) > a > dl > dd
        p_info = li.select_one("a > dl > dd").text
        #tabCont01 > ul > li:nth-child(1) > a > p.money > strong
        p_price = li.select_one("a > p.money > strong").text
        prod_list.append([p_name, p_info, p_price])

    header = ["[번호],메뉴이름],[설명],[가격]"]
    with open("kyochon_chicken.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="|", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        for item in prod_list:
            writer.writerow(item)
    print("메뉴 내용을 저장하였습니다.")
test5()