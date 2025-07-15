This project uses **Playwright Python** to simulate browser actions that mimic MCP (Model Context Protocol) commands like:

## Core Actions Implemented

| Action               | Playwright Equivalent                          |
|----------------------|------------------------------------------------|
| `browser_navigate`   | `page.goto(url)`                               |
| `browser_type`       | `page.fill(selector, text)`                    |
| `browser_click`      | `page.click(selector)`                         |
| `browser_wait`       | `page.wait_for_timeout(ms)` or `page.wait_for_selector()` |
| `browser_scroll`     | `page.evaluate("window.scrollBy(...)")`        |
| `browser_snapshot`   | `page.content()`                               |
| `browser_tab_new`    | `context.new_page()`                           |


## Error Handling Techniques

| Scenario            | Handling Method                                      |
|---------------------|------------------------------------------------------|
| Page load delay     | `page.wait_for_selector()` for content to appear     |
| Popup/alerts        | `page.on('dialog', lambda dialog: dialog.dismiss())` |
| Missing elements    | Wrapped actions in `try/except` with fallback logs   |
| CAPTCHA             | Logged + skipped page with retry logic (optional)    |

---

## Dynamic Content Handling

- Used `page.evaluate()` to scroll for lazy-loaded data
- Inserted `wait_for_timeout()` or selector waits after each major interaction
- Extracted page HTML only after confirming visibility of result blocks

---

## 🚀 Example Sequence

```python
page.goto("https://www.amazon.in")
page.fill("input[name='field-keywords']", "smartphones under ₹30,000")
page.press("input[name='field-keywords']", "Enter")
page.wait_for_selector(".s-result-item")
content = page.content()