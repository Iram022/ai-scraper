### Example 1: "Find me smartphones under ₹30,000"

**Workflow:**

1. **LLM Parsing**
   - Intent: `product_search`
   - Platform: `Amazon`
   - Category: `smartphones`
   - Filters: `price_limit: ₹30,000`

2. **MCP Automation Flow**
   - `browser_navigate`: Go to https://www.amazon.in
   - `browser_type`: Type `"smartphones under ₹30,000"` into search bar
   - `browser_press_key`: Press Enter
   - `browser_wait`: Wait for result list
   - `browser_snapshot`: Capture HTML for parsing

3. **Scraping**
   - Parse top 10 results: Title, Price, Link
   - Handle missing prices gracefully

4. **Excel Report**
   - Add product title, price, and link
   - Generate bar chart showing prices

---

### Example 2: "Flights from Delhi to Dubai"

**Workflow:**

1. **LLM Parsing**
   - Intent: `flight_search`
   - Source: `Delhi`
   - Destination: `Dubai`
   - Platform: `Skyscanner`

2. **MCP Automation Flow**
   - Navigate to travel site
   - Autofill "From", "To", and Dates
   - Click "Search"
   - Wait for AJAX-loaded results

3. **Scraping**
   - Extract airline, price, flight duration

4. **Excel Report**
   - Show airline vs price chart
   - Include filterable table

---

### Example 3: "Compare AirPods on Amazon and Flipkart"

**Workflow:**

1. **LLM Parsing**
   - Intent: `price_compare`
   - Product: `AirPods`
   - Platforms: `Amazon`, `Flipkart`

2. **MCP Flow**
   - Open both platforms
   - Search for AirPods
   - Extract top 5 results from each

3. **Aggregation**
   - Normalize prices
   - Match titles by keywords

4. **Excel Report**
   - Sheet 1: Amazon
   - Sheet 2: Flipkart
   - Sheet 3: Price Comparison