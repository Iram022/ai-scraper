from bs4 import BeautifulSoup

def parse_amazon_html(html):
    soup = BeautifulSoup(html, "html.parser")
    results = []
    for item in soup.select("[data-component-type='s-search-result']")[:10]:
        title = item.select_one("h2 a span")
        price = item.select_one(".a-price-whole")
        link = item.select_one("h2 a")
        if title and price and link:
            results.append({
                "title": title.text.strip(),
                "price": price.text.strip(),
                "link": "https://amazon.in" + link['href']
            })
    return results
