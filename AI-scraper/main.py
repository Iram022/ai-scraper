from ai_parser import parse_query
from mcp_automation import search_amazon
from scraper import parse_amazon_html
from excel_generator import generate_excel

user_query = input("📝 Enter your query: ")
parsed = parse_query(user_query)

if parsed.get("intent") == "product_search":
    product = parsed["category"] + " under " + str(parsed["filters"].get("price_limit", ""))
    html = search_amazon(product)
    results = parse_amazon_html(html)
    generate_excel(results, "outputs/amazon_products.xlsx")
    print("✅ Excel generated: amazon_products.xlsx")
