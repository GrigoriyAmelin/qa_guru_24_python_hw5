import os

from selene import browser as br, by, be, have
from selenium.webdriver.support.expected_conditions import element_to_be_selected


def test_practice_form_filling_up():
    br.open('/automation-practice-form')
    br.driver.execute_script("$('#fixedban').remove()")
    br.driver.execute_script("$('footer').remove()")

    # Проверка открытия требуемой страницы
    br.element(".practice-form-wrapper").element('.text-center').should(have.text('Practice Form'))

    # Ввод основных данных пользователя
    br.element('#firstName').type('Mirko')
    br.element('#lastName').type('Stojanovic')
    br.element('#userEmail').type('mirko-stojanovic@srbijavoz.rs')
    br.element(by.text("Male")).click().should(be.enabled)
    br.element('#userNumber').type('+0682826586')

    # Установка даты в календаре
    br.element("#dateOfBirthInput").click()
    br.element('.react-datepicker__month-select').element(by.text('October')).click()
    br.element('.react-datepicker__year-select').element(by.text('1979')).click()
    br.element('.react-datepicker__month').element('.react-datepicker__day--008').click()

    # Выбор предмета
    br.element('#subjectsInput').send_keys('e')
    br.element(by.text('English')).click()
    br.element('#subjectsInput').send_keys('erc')
    br.element(by.text('Commerce')).click()
    br.element('#subjectsInput').send_keys('a')
    br.element(by.text('Arts')).click()

    # Выбор хобби
    br.element(by.text('Reading')).click()
    br.element('#hobbies-checkbox-2').should(be.enabled)

    # Загрузка файла
    dirname: str = os.path.dirname(os.path.abspath(__file__))
    abspath = os.path.join(dirname, 'resources', '111.png')
    br.element("#uploadPicture").send_keys(abspath)



