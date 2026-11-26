from playwright.async_api import  Page, expect
from pages.login_page import LoginPage
from utils.test_data_reader import TestDataReader

test_data = TestDataReader.read_json("login_data.json")
text_validation = TestDataReader.read_json("expected_result.json")


async def test_login_with_valid_credentials(page: Page):

     login_page = LoginPage(page)

     credentials = test_data["valid_credentials"]
     text_validate = text_validation["page_title"]
     text_validate = text_validation["dashboard_text"]

     await login_page.navigate()

     await  expect(page).to_have_title(text_validation["page_title"]["login_title"])

     await login_page.enter_username(credentials["username"])
     await login_page.enter_password(credentials["password"])
     await login_page.click_login_btn()

     await expect(login_page.dashboard_text).to_have_text(text_validate["header"])


async def test_login_with_invalid_username(page: Page):

    login_page = LoginPage(page) 
    credentials = test_data["invalid_username"]
    text_validate = text_validation["login_errors"] 


    await login_page.navigate()
    await login_page.enter_username(credentials["username"])
    await login_page.enter_password(credentials["password"])
    await login_page.click_login_btn()
    
    await expect(login_page.error_message).to_have_text(text_validate["invalid_credentials"])


async def test_login_with_invalid_password(page: Page):
    login_page = LoginPage(page)
    credentials = test_data["invalid_password"]
    text_validate = text_validation["login_errors"]


    await login_page.navigate()
    await login_page.enter_username(credentials["username"])
    await login_page.enter_password(credentials["password"])
    await login_page.click_login_btn()

    await expect(login_page.error_message).to_have_text(text_validate["invalid_credentials"])


async def test_login_with_empty_username_password(page: Page):
    login_page = LoginPage(page)
    credentials = test_data["empty_credentials"]
    text_validate = text_validation["login_errors"]


    await login_page.navigate()

    await login_page.enter_username(credentials["username"])
    await login_page.enter_password(credentials["password"])
    await login_page.click_login_btn()

    await expect(login_page.required_field_error_message.nth(0)).to_have_text(text_validate["required_field"])
    await expect(login_page.required_field_error_message.nth(1)).to_have_text(text_validate["required_field"])




