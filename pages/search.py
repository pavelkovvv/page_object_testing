from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DuckDuckGoSearchPage:
    """Реализация взаимодействия с веб-страницей поиска на DuckDuckGo."""

    URL: str = 'https://www.duckduckgo.com/'
    SEARCH_INPUT: tuple = (By.ID, 'searchbox_input')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        """Загрузка страницы поиска DuckDuckGo."""

        self.browser.get(self.URL)

    def search(self, phrase):
        """Метод, для выполнения поискового запроса."""

        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
