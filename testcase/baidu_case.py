import unittest
from driver.page import Page


class TestLogin(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

    @classmethod
    def setUpClass(cls):
        cls.homepage = Page(pagefile="homepage", browser_type='chrome').get("https://www.baidu.com")
        cls.journalismpage = Page(page=cls.homepage, pagefile="journalismpage")

    @classmethod
    def tearDownClass(cls):
        cls.homepage.close()

    def tearDown(self):
        self.homepage.screen_shot()

    def test01(self):
        self.homepage.page_el("journalism_by_xpath").click()
        # self.journalism_page.page_el("girl_by_xpath").click()
        # self.journalismpage.page_el("baidu_new_by_xpath").click()
        # self.journalismpage.page_el("baidubotton_by_xpath").click()


if __name__ == '__main__':
    unittest.main()
