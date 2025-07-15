from mcp_automation import search_amazon
html = search_amazon("smartphone under 30000")
print(html[:500])  # just preview
