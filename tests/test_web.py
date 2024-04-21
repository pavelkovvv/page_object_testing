import pytest
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from selenium.webdriver import Chrome


@pytest.fixture
def browser():
    """Создание фикстуры, предоставляющей экземпляр браузера."""

    driver = Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_basic_duckduckgo_search(browser):
    """Тестовая функция."""

    PHRASE: str = 'barcelona'

    # Поиск фразы
    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()
    search_page.search(PHRASE)

    # Проверка, что результаты появились
    result_page = DuckDuckGoResultPage(browser)

    assert result_page.search_results_count() > 0
    assert result_page.phrase_result_count(PHRASE) > 0
    assert result_page.search_input_value() == PHRASE


def test_basic_duckduckgo_search_2(browser):
    """Тестовая функция."""

    PHRASE_2: str = 'madrid'

    # Поиск фразы
    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()
    search_page.search(PHRASE_2)

    # Проверка, что результаты появились
    result_page = DuckDuckGoResultPage(browser)

    assert result_page.search_results_count() > 0
    assert result_page.phrase_result_count(PHRASE_2) > 0
    assert result_page.search_input_value() == PHRASE_2
