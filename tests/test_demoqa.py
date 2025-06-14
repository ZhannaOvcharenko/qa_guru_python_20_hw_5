import os
import pytest
from selene import browser, have, be

@pytest.fixture(scope="function", autouse=True)
def browser_settings():
    browser.config.base_url = "https://demoqa.com"
    browser.config.window_width = 1920
    browser.config_height = 1080
    yield
    browser.quit()


def test_submit_form():
    # открытие формы
    browser.open("/automation-practice-form")

    # заполнение формы
    browser.element('#firstName').type('Test')
    browser.element('#lastName').type('Testov')
    browser.element('#userEmail').type('test.testov@gmail.com')
    browser.element('[for=gender-radio-2]').click()
    browser.element('#userNumber').type('9839583958')

    # выбор даты рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="6"').click() # июль
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1996"').click()  # 1996
    browser.element('.react-datepicker__day--009').click()  # день 1

    # заполнение формы subjects
    browser.element('#subjectsInput').type('Computer Science').press_enter()

    # выбор хобби
    browser.element('[for=hobbies-checkbox-1]').click() # Sports

    # загрузка картинки
    browser.element('#uploadPicture').send_keys(os.path.abspath('demoqa.jpg'))

    # заполнение адреса
    browser.element('#currentAddress').type('St. Petersburg, Lomanosovskaya street')

    # выбор State and City
    browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()
    browser.element('#react-select-4-input').type('Agra').press_enter()

    # отправка формы
    browser.element('#submit').click()

    # проверка данных
    browser.element('.table').should(have.text('Test Testov'))
    browser.element('.table').should(have.text('test.testov@gmail.com'))
    browser.element('.table').should(have.text('Female'))
    browser.element('.table').should(have.text('9839583958'))
    browser.element('.table').should(have.text('09 July,1996'))
    browser.element('.table').should(have.text('Computer Science'))
    browser.element('.table').should(have.text('Sports'))
    browser.element('.table').should(have.text('St. Petersburg, Lomanosovskaya street'))
    browser.element('.table').should(have.text('Uttar Pradesh Agra'))