from playwright.sync_api import sync_playwright

def search_amazon(product, max_results=10):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.amazon.in/")
        page.fill("input[name='field-keywords']", product)
        page.press("input[name='field-keywords']", "Enter")
        page.wait_for_selector("div.s-main-slot", timeout=10000)

        items = page.query_selector_all("div.s-main-slot > div[data-component-type='s-search-result']")

        results = []
        for item in items:
            title_el = item.query_selector("h2 span")
            price_whole = item.query_selector("span.a-price > span.a-offscreen")
            link_el = item.query_selector("h2 a")

            if title_el and price_whole and link_el:
                try:
                    title = title_el.inner_text().strip()
                    price = price_whole.inner_text().replace("₹", "").replace(",", "").strip()
                    price = int(float(price))  # Clean numeric format
                    link = "https://www.amazon.in" + link_el.get_attribute("href").strip()
                    results.append({
                        "title": title,
                        "price": price,
                        "link": link
                    })
                except:
                    continue  # Skip any parsing errors

            if len(results) >= max_results:
                break

        browser.close()
        return results
