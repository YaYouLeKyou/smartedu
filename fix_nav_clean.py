import re

filepath = 'D:/Temp/kilo/smartedu/handbook.html'
with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Remove ALL .nav-links rules from inline CSS (style.css handles everything)
# Pattern: .nav-links { ... }  and  .nav-links { ... }  and  .nav-links.active { ... }
# Use regex to find and remove these blocks

# Find all .nav-links related rules in the inline CSS
style_start = content.find('<style>')
style_end = content.find('</style>', style_start)
before_style = content[:style_start]
inline_css = content[style_start:style_end]
after_style = content[style_end:]

# Remove .nav-links { ... } blocks (with possible !important)
inline_css_new = re.sub(r'\.nav-links\s*\{[^}]*\}', '', inline_css)
# Clean up extra blank lines
inline_css_new = re.sub(r'\n\s*\n\s*\n', '\n\n', inline_css_new)

content = before_style + inline_css_new + after_style

# Verify
if 'display: none !important' in inline_css_new:
    print("WARNING: nav-links display: none still in inline CSS")
else:
    print("OK: nav-links removed from inline CSS")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

# Final check
with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
    final = f.read()

style_start = final.find('<style>')
style_end = final.find('</style>', style_start)
inline_css = final[style_start:style_end]

print("\nRemaining inline CSS nav/hamburger rules:")
for pattern in [r'\.hamburger\s*\{[^}]+\}', r'\.nav-links\s*\{[^}]+\}', r'\.nav-links\.active\s*\{[^}]+\}']:
    for m in re.finditer(pattern, inline_css, re.DOTALL):
        print(f"  {m.group(0)[:200]}")
