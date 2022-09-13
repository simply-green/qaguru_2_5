import os.path
from selene.support.shared import browser,config
from selene import be, have
import pytest


@pytest.fixture(scope='function', autouse=True)
def configure_enviroment():
    #Подготавливаем окружение
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.hold_browser_open
    browser.open('https://demoqa.com/automation-practice-form')

def test_filling_form(configure_enviroment):
    #Заполнение формы
    browser.element('#firstName').should(be.blank).type('Aleksandr')
    browser.element('#lastName').should(be.blank).type('Aleksandrov')
    browser.element('#userEmail').type('demoqa@demoqa.com')
    browser.element('#gender-radio-1').double_click()
    browser.element('#userNumber').type('9999999999')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').type('1991')
    browser.element('.react-datepicker__month-select').type('October')
    browser.element('[aria-label="Choose Monday, October 7th, 1991"]').click()
    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath(r'C:\Users\Aleks\PycharmProjects\qaguru_2_5\image\cat.jpg'))
    browser.element('#currentAddress').type('Earth')
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Karnal').press_enter()
    browser.element('#submit').click()

    #Проверки
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('#closeLargeModal').should(have.text('Close'))
    browser.element('#closeLargeModal').click()
    browser.element('#firstName').should(be.blank)
    browser.element('#lastName').should(be.blank)
    browser.element('#userEmail').should(be.blank)
    





