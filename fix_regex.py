import re

filepath = 'D:/Temp/kilo/smartedu/handbook.html'
with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Find and fix the broken structure using regex
# The broken part is:
# <a href="...instagram...">\n<a href="...portefolio...">...</a>\n<i class="fab fa-instagram">...</i>\n</a>

old_pattern = re.compile(
    r'(<a href="https://www\.instagram\.com/smart\.edu\.ai/"[^>]*>)\n'
    r'(<a href="https://portefolio-2026\.vercel\.app/"[^>]*>.*?</a>)\n'
    r'(\s*<i class="fab fa-instagram"[^>]*>.*?</i>\s*)\n'
    r'(</a>)',
    re.DOTALL
)

def replace_broken(match):
    instagram_open = match.group(1)
    contact_link = match.group(2)
    instagram_content = match.group(3)
    closing = match.group(4)
    # Return properly structured: Instagram link complete, then Contact link
    return f'{instagram_open}\n{instagram_content}\n</a>\n{contact_link}'

new_content = old_pattern.sub(replace_broken, content)

if new_content != content:
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Fixed via regex")
else:
    print("Regex didn't match")

# Verify
with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
    final = f.read()

idx = final.find('instagram.com/smart.edu.ai')
print(final[idx:idx+400])