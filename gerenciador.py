import markdown
from weasyprint import HTML

# Converte Markdown para HTML
with open('manual do lider.md', 'r', encoding='utf-8') as md_file:
    markdown_text = md_file.read()
    html_text = markdown.markdown(markdown_text)

# Converte HTML para PDF
HTML(string=html_text).write_pdf('manual do lider.pdf')
