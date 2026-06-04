import markdown

INPUT_FILE = "input.md"
OUTPUT_FILE = "output.html"

try:
    with open(INPUT_FILE, "r", encoding="utf-8") as md_file:
        markdown_text = md_file.read()

    html_content = markdown.markdown(markdown_text)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

    print("Conversion Successful!")
    print("HTML saved as output.html")

except FileNotFoundError:
    print(f"Error: '{INPUT_FILE}' not found.")

except Exception as error:
    print(f"Error: {error}"
