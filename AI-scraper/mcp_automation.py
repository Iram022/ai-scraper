from playwright.sync_api import sync_playwright

def search_amazon(product):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.amazon.in/")
        page.fill("input[name='field-keywords']", product)
        page.press("input[name='field-keywords']", "Enter")
        page.wait_for_timeout(3000)
        content = page.content()
        browser.close()
        return content
