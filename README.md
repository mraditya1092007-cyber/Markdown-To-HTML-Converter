# Markdown To HTML Converter

A simple Python project that converts Markdown files into HTML using Python and the Markdown library.

## Features

- Convert Markdown files into HTML
- Save generated HTML output to a file
- Beginner-friendly Python project
- Error handling for missing files
- Clean and simple implementation

## Requirements

- Python 3
- Markdown Library

## Installation

```bash
pip install markdown
```

## Usage

1. Create an `input.md` file.
2. Run the Python script.
3. HTML output will be generated and saved as `output.html`.

## Example

### Input (input.md)

```md
# Aditya Portfolio

## Skills

- Python
- HTML
- Tkinter

**Created by Aditya**
```

### Output (output.html)

```html
<h1>Aditya Portfolio</h1>
<h2>Skills</h2>
<ul>
<li>Python</li>
<li>HTML</li>
<li>Tkinter</li>
</ul>
<p><strong>Created by Aditya</strong></p>
```

## Project Structure

```text
Markdown-To-HTML-Converter/
│
├── markdown_to_html.py
├── input.md
├── output.html
└── README.md
```

## Author

Aditya

## License

This project is created for educational and learning purposes.
