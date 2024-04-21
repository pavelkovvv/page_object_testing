from selenium.webdriver.common.by import By


class DuckDuckGoResultPage:
    """
    Необходим для взаимодействия с результатами поиска на странице DuckDuckGo.
    """

    SEARCH_RESULTS: tuple = (By.CSS_SELECTOR, "li[data-layout='organic']")
    SEARCH_INPUT: tuple = (By.ID, 'search_form_input')

    @classmethod
    def PHRASE_RESULTS(cls, phrase):
        """
        Возвращает кортеж с информацией о методе поиска ссылок,
        содержащих пользовательский запрос - фразу или слово, которое задаёт
        пользователь в поисковой строке.
        """

        xpath = f"//li[@data-layout='organic']//a[contains(@href, '{phrase}')]"

        return (By.XPATH, xpath)

    def __init__(self, browser):
        self.browser = browser

    def search_results_count(self):
        """Находит все элементы результатов поиска на странице."""

        search_results = self.browser.find_elements(*self.SEARCH_RESULTS)

        return len(search_results)

    def phrase_result_count(self, phrase):
        """Находит все ссылки результатов поиска, содержащих пользовательский запрос."""

        phrase_results = self.browser.find_elements(*self.PHRASE_RESULTS(phrase))
        print(phrase_results)
        return len(phrase_results)

    def search_input_value(self):
        """Находит элемент поисковой строки на странице."""

        search_input = self.browser.find_element(*self.SEARCH_INPUT)

        return search_input.get_attribute('value')
