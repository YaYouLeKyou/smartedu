import re

filepath = 'D:/Temp/kilo/smartedu/handbook.html'
with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Fix the broken Instagram/Contact structure
old_broken = '''            <a href="https://www.instagram.com/smart.edu.ai/" target="_blank" rel="noopener noreferrer" class="project-link" style="margin-left:12px;background:linear-gradient(135deg,#e4405f,#c13584);">
            <a href="https://portefolio-2026.vercel.app/" target="_blank" rel="noopener noreferrer" class="project-link" style="margin-left:12px;background:linear-gradient(135deg,#1a1a2e,#16213e);">
                <i class="fas fa-envelope" aria-hidden="true"></i> Contact the Developer
            </a>
                <i class="fab fa-instagram" aria-hidden="true"></i> Follow on Instagram
            </a>'''

new_correct = '''            <a href="https://www.instagram.com/smart.edu.ai/" target="_blank" rel="noopener noreferrer" class="project-link" style="margin-left:12px;background:linear-gradient(135deg,#e4405f,#c13584);">
                <i class="fab fa-instagram" aria-hidden="true"></i> Follow on Instagram
            </a>
            <a href="https://portefolio-2026.vercel.app/" target="_blank" rel="noopener noreferrer" class="project-link" style="margin-left:12px;background:linear-gradient(135deg,#1a1a2e,#16213e);">
                <i class="fas fa-envelope" aria-hidden="true"></i> Contact the Developer
            </a>'''

if old_broken in content:
    content = content.replace(old_broken, new_correct)
    print("Fixed Instagram/Contact structure")
else:
    print("Pattern not found")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
    final = f.read()

# Check the section
idx = final.find('Explore the Project')
if idx >= 0:
    section = final[idx:idx+500]
    print(section)