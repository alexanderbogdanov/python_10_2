from selene import browser, be, have


def test_find_selene_in_google(browser_config):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_unsuccessful_search_in_google(browser_config):

    browser.element('[name="q"]').should(be.blank).type('a;slslie%%%%000034j3k4jkjk').press_enter()
    browser.element('#botstuff').should(have.text('Претрага - a;slslie%%%%000034j3k4jkjk - не одговара ниједном документу.'))
