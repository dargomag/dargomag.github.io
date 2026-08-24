import os, re, sys

head = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>__TITLE__ — Физика</title>
    <style>
        body { font-family: Georgia,'Times New Roman',serif; font-size: 18px; line-height: 1.7; color: #222; background: #fafafa; margin: 0; padding: 20px; }
        .container { max-width: 800px; margin: 0 auto; background: #fff; padding: 30px 40px; border-radius: 4px; box-shadow: 0 0 10px rgba(0,0,0,0.05); }
        h1,h2,h3,h4 { font-family: 'Helvetica Neue',Arial,sans-serif; color: #111; }
        h1 { font-size: 28px; margin-top: 0; }
        h2 { font-size: 22px; }
        h3 { font-size: 19px; }
        h4 { font-size: 17px; }
        blockquote { border-left: 3px solid #ccc; margin: 20px 0; padding: 10px 20px; background: #f9f9f9; font-style: italic; }
        a { color: #336699; }
        hr { border: none; border-top: 1px solid #ddd; margin: 30px 0; }
        img { max-width: 100%; height: auto; }
        ol { padding-left: 25px; }
        li { margin: 5px 0; }
    </style>
    <script>
    MathJax = {
        tex: {
            inlineMath: [['$', '$'], ['\\(', '\\)']],
            displayMath: [['$$', '$$'], ['\\[', '\\]']]
        },
        svg: { fontCache: 'global' }
    };
    </script>
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js" async></script>
</head>
<body><div class="container">
"""
tail = "</div></body></html>"

files = [
    ("00_Введение_Физика_и_познание_мира.md", "physics/00.html", "Введение. Физика и познание мира"),
    ("01_Механика_§1_Что_такое_механика.md", "physics/01.html", "§1. Что такое механика"),
    ("01_Механика_§2_Классическая_механика_Ньютона.md", "physics/02.html", "§2. Классическая механика Ньютона"),
    ("02_Кинематика_§3_Движение_точки_и_тела.md", "physics/03.html", "§3. Движение точки и тела"),
    ("02_Кинематика_§4_Положение_точки_в_пространстве.md", "physics/04.html", "§4. Положение точки в пространстве"),
    ("02_Кинематика_§5_Способы_описания_движения.md", "physics/05.html", "§5. Способы описания движения"),
    ("02_Кинематика_§6_Перемещение.md", "physics/06.html", "§6. Перемещение"),
]

def line_to_html(line):
    t = line.strip()
    if not t:
        return ("", False)
    if t.startswith("#### "):
        return (f"<h4>{t[5:]}</h4>", False)
    if t.startswith("### "):
        return (f"<h3>{t[4:]}</h3>", False)
    if t.startswith("## "):
        return (f"<h2>{t[3:]}</h2>", False)
    if t.startswith("# "):
        return (f"<h1>{t[2:]}</h1>", False)
    if re.match(r'^\*{3,}$', t) or re.match(r'^-{3,}$', t):
        return ("<hr>", False)
    if t.startswith("> "):
        bt = t[2:]
        bt = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', bt)
        bt = re.sub(r'\*(.+?)\*', r'<i>\1</i>', bt)
        return (f"<blockquote>{bt}</blockquote>", False)
    m = re.match(r'^\d+\.\s+(.+)', t)
    if m:
        li = m.group(1)
        li = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', li)
        li = re.sub(r'\*(.+?)\*', r'<i>\1</i>', li)
        return (f"<li>{li}</li>", True)
    
    p = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    p = re.sub(r'\*(.+?)\*', r'<i>\1</i>', p)
    p = re.sub(r'!\[(.+?)\]\((.+?)\)', r'<img src="\2" alt="\1">', p)
    p = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', p)
    return (f"<p>{p}</p>", False)

for src, out, title in files:
    with open(src, 'r', encoding='utf-8') as f:
        md = f.read()
    
    # Replace display math \[ ... \] with $$ ... $$
    md = re.sub(r'\\\[\s*\n', '$$', md)
    md = re.sub(r'\n\s*\\\]', '$$', md)
    md = re.sub(r'\\\[', '$$', md)
    md = re.sub(r'\\\]', '$$', md)
    
    # Replace inline math \( ... \) with $ ... $
    md = re.sub(r'\\\(', '$', md)
    md = re.sub(r'\\\)', '$', md)
    
    lines = md.split('\n')
    html_parts = []
    in_list = False
    
    for line in lines:
        result, is_list_item = line_to_html(line)
        if is_list_item and not in_list:
            html_parts.append("<ol>")
            in_list = True
        elif not is_list_item and in_list and result:
            html_parts.append("</ol>")
            in_list = False
        if result:
            html_parts.append(result)
    
    if in_list:
        html_parts.append("</ol>")
    
    body = '\n'.join(html_parts)
    full_html = head.replace('__TITLE__', title) + body + tail
    
    with open(out, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"Created {out}")

print("All done!")