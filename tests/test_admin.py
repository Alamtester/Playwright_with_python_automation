from playwright.async_api import Page,expect
from pages.admin_page import AdminPage
from pages.login_page import LoginPage
from utils.test_data_reader import TestDataReader

login_data = TestDataReader.read_json("login_data.json")


async def test_create_admin(page: Page):
    admin = AdminPage(page)
    login = LoginPage(page)
    login_credentials = login_data["valid_credentials"]

    await login.navigate()
    await login.enter_username(login_credentials["username"])
    await login.enter_password(login_credentials["password"])
    await login.click_login_btn()

    await expect(admin.admin_menu).to_be_visible()
    #print("Admin menu visible on UI")

    await admin.admin_click()
    #print("Clicked the Admin menu")

    await expect(admin.admin_header).to_have_text("AdminUser Management")

    await admin.create_admin()

    await admin.click_user_role_field("Admin")

    await admin.employee_name_field_enter("Charles Carter")

    await admin.employee_name_field_autosugesstion()

    await admin.click_status("Enabled")

    await admin.enter_username()

    await admin.enter_password()

    await admin.enter_confirm_password()

    await admin.click_save_btn()

async def test_validate_required_error_message(page: Page):
    admin = AdminPage(page)
    login = LoginPage(page)
       
    await login.navigate()
    await login.login("Admin","admin123") 

    await admin.admin_click()
        
    await expect(admin.admin_header).to_have_text("AdminUser Management")
    
    await admin.create_admin()

    await admin.click_save_btn()

    await expect(admin.required_error_messsage.nth(0)).to_have_text("Required")
    await expect(admin.required_error_messsage.nth(1)).to_have_text("Required")
    await expect(admin.required_error_messsage.nth(2)).to_have_text("Required")
    await expect(admin.required_error_messsage.nth(3)).to_have_text("Required")
    await expect(admin.required_error_messsage.nth(4)).to_have_text("Required")
    await expect(admin.required_error_messsage.nth(5)).to_have_text("Passwords do not match")



    

    

