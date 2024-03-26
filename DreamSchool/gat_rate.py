import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.common.exceptions import NoSuchElementException


currency_dict = {
    "GBP": "英镑",
    "HKD": "港币",
    "USD": "美元",
    "CHF": "瑞士法郎",
    "DEM": "德国马克",
    "FRF": "法国法郎",
    "SGD": "新加坡元",
    "SEK": "瑞典克朗",
    "DKK": "丹麦克朗",
    "NOK": "挪威克朗",
    "JPY": "日元",
    "CAD": "加拿大元",
    "AUD": "澳大利亚元",
    "EUR": "欧元",
    "MOP": "澳门元",
    "PHP": "菲律宾比索",
    "THB": "泰国铢",
    "NZD": "新西兰元",
    "KRW": "韩元",
    "RUB": "卢布",
    "MYR": "林吉特",
    "TWD": "新台币",
    "ESP": "西班牙比塞塔",
    "ITL": "意大利里拉",
    "NLG": "荷兰盾",
    "BEF": "比利时法郎",
    "FIM": "芬兰马克",
    "INR": "印度卢比",
    "IDR": "印尼卢比",
    "BRL": "巴西里亚尔",
    "AED": "阿联酋迪拉姆",
    "ZAR": "南非兰特",
    "SAR": "沙特里亚尔",
    "TRY": "土耳其里拉"
}



def fetch_exchange_rate(date, currency_code):
    # 初始化Selenium WebDriver
    driver = webdriver.Chrome()
    driver.get("https://www.boc.cn/sourcedb/whpj/")

    try:
        # 等待页面加载完成
        time.sleep(2)

        date_s_input = driver.find_element(By.NAME, "erectDate")
        date_s_input.clear()
        date_s_input.send_keys(date)
    
        date_e_input = driver.find_element(By.NAME, "nothing")
        date_e_input.clear()
        date_e_input.send_keys(date)

        # 输入货币代码
        currency_select = Select(driver.find_element(By.NAME, "pjname"))

        if currency_code in currency_dict:
            currency_name = currency_dict[currency_code]
            currency_select.select_by_value(currency_name)
        else:
            print ("输入的货币种类未知，请确认是否正确。")
            return None


        search_button = driver.find_element(By.XPATH, "//*[@id='historysearchform']/div/table/tbody/tr/td[7]/input")
        search_button.click()
       
        # time.sleep(5)

        # 获取现汇卖出价

        elements = driver.find_elements(By.XPATH,"/html/body/div/div[4]/table/tbody/tr/td[4]")
        # exchange_rate = driver.find_element(By.XPATH,"/html/body/div/div[4]/table/tbody/tr/td[4]")
        # 遍历元素列表，打印每个元素的文本内容
        if elements == None:
            print("未找到相关数据，请确认输入的日期和货币代码是否正确。")
            return None
        exchange_rates = []
        for element in elements:
            exchange_rates.append(element.text)

        # 将结果写入result.txt文件
        with open("result.txt", "w") as f:
            f.write(f"Date: {date}\n")
            f.write(f"Currency: {currency_code}\n")
            f.write(f"Exchange Rate: {exchange_rates}\n")

        return exchange_rates
    
    except NoSuchElementException:
        print("未找到相关数据，请确认输入的日期和货币代码是否正确。")
        return None
    

    finally:
        # 关闭浏览器
        driver.quit()

if __name__ == "__main__":
    # date_currency = input("请输入日期和货币类型（例如：20230112 USD）: ")
    # date, currency_code = date_currency.split()

    date = "20230524"
    currency_code = "USD"

    exchange_rate = fetch_exchange_rate(date, currency_code)
    if exchange_rate:
        print(f"现汇卖出价为: {exchange_rate[0]}")

