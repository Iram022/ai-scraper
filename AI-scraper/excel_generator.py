import pandas as pd
from openpyxl.chart import BarChart, Reference
import os

def generate_excel(data, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    df = pd.DataFrame(data)
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Results')
        ws = writer.book['Results']

        # Only add chart if price column exists
        if 'price' in df.columns and 'title' in df.columns:
            chart = BarChart()
            chart.title = "Price Comparison"
            chart.y_axis.title = 'Price'
            chart.x_axis.title = 'Product'

            data_ref = Reference(ws, min_col=2, min_row=1, max_row=len(df)+1)
            cats = Reference(ws, min_col=1, min_row=2, max_row=len(df)+1)

            chart.add_data(data_ref, titles_from_data=True)
            chart.set_categories(cats)
            ws.add_chart(chart, "E5")
