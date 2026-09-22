import re

filepath = 'D:/Temp/kilo/smartedu/handbook.html'
with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# The exact broken string we need to replace
old = '''            <a href="https://www.instagram.com/smart.edu.ai/" target="_blank" rel="noopener noreferrer" class="project-link" style="margin-left:12px;background:linear-gradient(135deg,#e4405f,#c13584);">
<a href="https://portefolio-2026.vercel.app/" target="_blank" rel="noopener noreferrer" class="project-link" style="margin-left:12px;background:linear-gradient(135deg,#1a1a2e,#16213e);">
                <i class="fas fa-envelope" aria-hidden="true"></i> Contact the Developer
            </a>
                <i class="fab fa-instagram" aria-hidden="true"></i> Follow on Instagram
            </a>'''

new = '''            <a href="https://www.instagram.com/smart.edu.ai/" target="_blank" rel="noopener noreferrer" class="project-link" style="margin-left:12px;background:linear-gradient(135deg,#e4405f,#c13584);">
                <i class="fab fa-instagram" aria-hidden="true"></i> Follow on Instagram
            </a>
            <a href="https://portefolio-2026.vercel.app/" target="_blank" rel="noopener noreferrer" class="project-link" style="margin-left:12px;background:linear-gradient(135deg,#1a1a2e,#16213e);">
                <i class="fas fa-envelope" aria-hidden="true"></i> Contact the Developer
            </a>'''

if old in content:
    content = content.replace(old, new)
    print("Fixed!")
else:
    print("Exact string not found, trying with flexible whitespace...")
    # Try with flexible whitespace
    old_flex = re.escape(old).replace(r'\ ', r'\s+').replace(r'\n', r'\s*')
    # Actually let's just find and replace the section
    idx = content.find('instagram.com/smart.edu.ai')
    if idx >= 0:
        # Find the section end
        section_end = content.find('</section>', idx)
        section = content[idx:section_end]
        print(f"Current section:\n{section}")
    else:
        print("Not found")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)