import pandas as pd
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

# Sample data
amazon_data = [
    {"title": "Laptop A", "price": 45000, "link": "https://amazon.in/laptop-a"},
    {"title": "Laptop B", "price": 48000, "link": "https://amazon.in/laptop-b"},
    {"title": "Laptop C", "price": 49000, "link": "https://amazon.in/laptop-c"},
]

flipkart_data = [
    {"title": "Laptop A", "price": 45500, "link": "https://flipkart.com/laptop-a"},
    {"title": "Laptop B", "price": 47000, "link": "https://flipkart.com/laptop-b"},
    {"title": "Laptop C", "price": 49500, "link": "https://flipkart.com/laptop-c"},
]

# Output filename
filename = "Outputs/laptop_comparison.xlsx"

# Create Excel file with sheets for Amazon and Flipkart
with pd.ExcelWriter(filename, engine='openpyxl') as writer:
    for site, data in [("Amazon", amazon_data), ("Flipkart", flipkart_data)]:
        df = pd.DataFrame(data)
        df.to_excel(writer, index=False, sheet_name=site)

        # Add a bar chart to each sheet
        ws = writer.book[site]
        chart = BarChart()
        chart.title = f"{site} Laptop Prices"
        chart.y_axis.title = "Price (INR)"
        chart.x_axis.title = "Laptops"

        # Data and category references
        data_ref = Reference(ws, min_col=2, min_row=1, max_row=len(df)+1)
        cats = Reference(ws, min_col=1, min_row=2, max_row=len(df)+1)
        chart.add_data(data_ref, titles_from_data=True)
        chart.set_categories(cats)
        ws.add_chart(chart, "E5")
