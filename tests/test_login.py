from playwright.sync_api import Page, expect


def test_login_with_valid_credential(page: Page):

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    expect(page).to_have_title("OrangeHRM")

    page.get_by_placeholder("username").fill("Admin")

    page.get_by_placeholder("Password").fill("admin123")

    page.get_by_role("button" , name="Login").click()

    expect(page.locator("h6")).to_have_text("Dashboard")

    page.wait_for_timeout(5000)




def test_login_with_invalid_username(page: Page):

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  

    page.get_by_placeholder("username").fill("wrongadmin")

    page.get_by_placeholder("Password").fill("admin123")

    page.get_by_role("button", name="Login").click()

    expect(page.locator("p.oxd-alert-content-text")).to_have_text("Invalid credentials")

    page.wait_for_timeout(5000)




def test_login_with_invalid_password(page: Page):

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") 

    page.get_by_placeholder("username").fill("Admin")

    page.get_by_placeholder("Password").fill("wrongpassword")  

    page.get_by_role("button", name="Login").click() 

    expect(page.locator("p.oxd-alert-content-text")).to_have_text("Invalid credentials")

    page.wait_for_timeout(5000)


def test_login_with_blank_username_password(page: Page):

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") 

    page.get_by_placeholder("username").fill("")

    page.get_by_placeholder("Password").fill("")

    page.get_by_role("button",name="Login").click()

##<span data-v-7b563373="" data-v-957b4417="" class="oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message">Required</span>


    error_messsage=page.locator("span.oxd-input-field-error-message")
    expect(error_messsage).to_have_count(2)
    expect(error_messsage.nth(0)).to_have_text("Required")
    expect(error_messsage.nth(1)).to_have_text("Required")

    page.wait_for_timeout(5000)
    

