import pytest
from playwright.async_api import Page,expect
from pages.login_page import LoginPage
from pages.dashboard_page import Dashboard_page
from utils.test_data_reader import TestDataReader

login_data = TestDataReader.read_json("login_data.json")


@pytest.mark.parametrize("menu_name",["Admin","PIM","Leave","Time","Recruitment","My Info","Performance","Directory","Maintenance","Buzz"])

async def test_menu_item(page: Page,menu_name):

    login = LoginPage(page)
    dashboard = Dashboard_page(page)
    login_credentials = login_data["valid_credentials"]


    await login.navigate()
    await login.enter_username(login_credentials["username"])
    await login.enter_password(login_credentials["password"])
    await login.click_login_btn()

    await expect(dashboard.pim_menu).to_be_visible()
    menu = page.get_by_role("link",name=menu_name,exact=True)
    await expect(menu).to_be_visible()

    await dashboard.menu_click(menu_name)




