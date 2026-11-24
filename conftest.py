import pytest
from playwright.async_api import async_playwright

@pytest.fixture
async def page():
    print("Page fixture is running")

    async with async_playwright() as p:
      browser = await p.chromium.launch(headless=False)

      page = await browser.new_page()

      yield page

      await browser.close()