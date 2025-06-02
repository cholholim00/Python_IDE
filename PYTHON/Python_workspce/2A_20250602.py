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
    
    for index in range(1,2):
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
            p_name = p_name.strip()
            p_price = p_price.replace("Price","")
            p_price = p_price.strip()
            p_sale_price = p_sale_price.strip()
            print(f"[{index}] {p_price} | {p_sale_price}")
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
        writer.writerow(["제품명", "정가", "할인가"])

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
test4()
