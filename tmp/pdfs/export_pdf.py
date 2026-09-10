from pathlib import Path
from playwright.sync_api import sync_playwright
import fitz

root = Path('/Users/iva/Modelling_of_Biological_Systems_Group_11')
with sync_playwright() as p:
    print('Launching converter', flush=True)
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto((root / 'tmp/pdfs/analysis.html').as_uri(), wait_until='networkidle')
    print('Notebook loaded', flush=True)
    page.wait_for_function("typeof MathJax !== 'undefined' && MathJax.Hub && MathJax.Hub.isReady", timeout=60000)
    page.evaluate("() => new Promise(resolve => MathJax.Hub.Queue(() => resolve(true)))")
    print('Equations rendered', flush=True)
    page.add_style_tag(content='''
        @page { size: A4; }
        body { padding: 0 !important; }
        .jp-Notebook { padding: 0 !important; }
        .jp-InputPrompt, .jp-OutputPrompt { min-width: 42px !important; }
        pre { white-space: pre-wrap !important; overflow-wrap: anywhere !important; }
        .jp-Cell { break-inside: auto !important; }
        .jp-OutputArea-output img { max-width: 100% !important; height: auto !important; }
        .jp-OutputArea-child { break-inside: avoid; }
        h1, h2, h3 { break-after: avoid; }
    ''')
    page.pdf(path=str(root / 'output/pdf/analysis.pdf'), format='A4',
             print_background=True, margin={'top':'14mm','bottom':'14mm','left':'10mm','right':'10mm'})
    browser.close()

doc = fitz.open(root / 'output/pdf/analysis.pdf')
print(f'Created {len(doc)} pages')
for i, page in enumerate(doc):
    page.get_pixmap(matrix=fitz.Matrix(0.9, 0.9)).save(root / f'tmp/pdfs/page-{i+1}.png')
    print(i+1, len(page.get_text()), 'text characters')
