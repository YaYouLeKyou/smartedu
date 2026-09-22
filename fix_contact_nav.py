import re

filepath = 'D:/Temp/kilo/smartedu/handbook.html'
with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Remove all nav-links CSS from inline (style.css handles everything)
style_start = content.find('<style>')
style_end = content.find('</style>', style_start)
before_style = content[:style_start]
inline_css = content[style_start:style_end]
after_style = content[style_end:]

# Remove .nav-links related rules from inline CSS
inline_css = re.sub(r'\.nav-links\s*\{[^}]*\}', '', inline_css)
inline_css = re.sub(r'\.nav-links\s*\{[^}]*', '', inline_css)  # catch unclosed braces
# Clean extra blank lines
inline_css = re.sub(r'\n{3,}', '\n\n', inline_css)

content = before_style + inline_css + after_style

# Now fix the Explore the Project section
# Remove the old "Contacter le dev" button and add in English after Instagram
old_btn = '''<a href="https://portefolio-2026.vercel.app/" target="_blank" rel="noopener noreferrer" class="project-link" style="background:linear-gradient(135deg,#1a1a2e,#16213e);">
                <i class="fas fa-envelope" aria-hidden="true"></i> Contacter le dev
            </a>
            <section class="handbook-section"'''

new_btn = '''<section class="handbook-section"'''

if old_btn in content:
    content = content.replace(old_btn, new_btn)
    print("Removed old button")

# Add Contact Developer after Instagram link
instagram_link = '<a href="https://www.instagram.com/smart.edu.ai/" target="_blank" rel="noopener noreferrer" class="project-link" style="margin-left:12px;background:linear-gradient(135deg,#e4405f,#c13584);">'
contact_btn = '''<a href="https://portefolio-2026.vercel.app/" target="_blank" rel="noopener noreferrer" class="project-link" style="margin-left:12px;background:linear-gradient(135deg,#1a1a2e,#16213e);">
                <i class="fas fa-envelope" aria-hidden="true"></i> Contact the Developer
            </a>'''

if instagram_link in content:
    content = content.replace(instagram_link, instagram_link + '\n' + contact_btn)
    print("Added Contact button after Instagram")
else:
    print("Instagram link not found")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
    final = f.read()

print(f"\nContact button in English: {'Contact the Developer' in final}")
print(f"French text removed: {'Contacter le dev' not in final}")
print(f"Nav-links CSS removed: {'.nav-links {' not in final[final.find('<style>'):final.find('</style>')]}")
