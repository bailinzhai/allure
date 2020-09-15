import allure
from selenium import webdriver


class Test:
    def setup_class(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.baidu.com")
    @allure.step("第二布")
    def abc(self):
        print(121121)

    @allure.step("第一步")
    def test_01(self):
        self.abc()
        allure.attach(self.driver.get_screenshot_as_png(), "截图", allure.attachment_type.PNG)
        print("test_001--")
