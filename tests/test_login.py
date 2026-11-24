from playwright.async_api import  Page, expect
from pages.login_page import LoginPage


async def test_login_with_valid_credentials(page: Page):
     login_page = LoginPage(page)

     await login_page.navigate()

     await  expect(page).to_have_title("OrangeHRM")

     await login_page.login("Admin", "admin123")

     await expect(page.locator(".oxd-topbar-header-breadcrumb-module")).to_have_text("Dashboard")


async def test_login_with_invalid_username(page: Page):

    login_page = LoginPage(page)  
    await login_page.navigate()
    await login_page.login("wrongusername","admin123")
    await expect(login_page.error_message).to_have_text("Invalid credentials")


async def test_login_with_invalid_password(page: Page):
    login_page = LoginPage(page)
    await login_page.navigate()
    await login_page.login("Admin","wrongpassword")
    await expect(login_page.error_message).to_have_text("Invalid credentials")


async def test_login_with_empty_username_password(page: Page):
    login_page = LoginPage(page)
    await login_page.navigate()

    await login_page.login("","")
    await expect(login_page.required_field_error_message.nth(0)).to_have_text("Required")
    await expect(login_page.required_field_error_message.nth(1)).to_have_text("Required")




