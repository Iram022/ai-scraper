from ai_parser import parse_query
from mcp_automation import search_amazon
from excel_generator import generate_excel
import os

os.makedirs("Outputs", exist_ok=True)

user_query = input("📝 Enter your query: ")
parsed = parse_query(user_query)

if parsed.get("intent") == "product_search":
    product = parsed["category"] + " under " + str(parsed["filters"].get("price_limit", ""))
    print(f"🔍 Searching for: {product}...")
    results = search_amazon(product)

    print("💬 Scraped Results:")
    for item in results:
        print(item)

    if not results:
        print("⚠️ No results found. Using dummy data for demo.")
        results = [
            {"title": "Demo Laptop 1", "price": 49999, "link": "https://amazon.in/demo1"},
            {"title": "Demo Laptop 2", "price": 48999, "link": "https://amazon.in/demo2"},
            {"title": "Demo Laptop 3", "price": 47999, "link": "https://amazon.in/demo3"},
        ]

    generate_excel(results, "Outputs/laptop_comparison.xlsx")
    print("✅ Excel generated at: Outputs/laptop_comparison.xlsx")

