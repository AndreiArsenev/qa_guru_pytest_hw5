import os
from selene import browser, be, have


def test_fill_form():
    browser.element('#firstName').type("Andrei")
    browser.element('#lastName').type("Arseniev")
    browser.element('#userEmail').type("Andrei@gmail.com")
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('#userNumber').type("9113845400")
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="8"]').should(be.visible).click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1988"]').should(be.visible).click()
    browser.element('.react-datepicker__day--020').click()
    browser.element('#subjectsInput').type("English").press_enter()
    browser.element('label[for ="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('file.txt'))
    browser.element('#currentAddress').type('My address')
    browser.element('#state').click().element('#react-select-3-option-0').click()
    browser.element('#city').click().element('#react-select-4-option-0').click()
    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    browser.all('.table-responsive td:nth-child(2)').should(have.texts(

        'Andrei Arseniev',
        'Andrei@gmail.com',
        'Male',
        '9113845400',
        '20 September,1988',
        'English',
        'Sports',
        'file.txt',
        'My address',
        'NCR Delhi'
    ))