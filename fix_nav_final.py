import re

filepath = 'D:/Temp/kilo/smartedu/handbook.html'
with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Current problematic structure:
# .hamburger { ... }  (no display - OK, relies on style.css)
# .nav-links { display: none; ... }  (BAD - always hidden)
# .nav-links.active { display: flex !important; }  (BAD - not in media query)
# .nav-links a { ... }  (BAD - mobile only, outside media query)
# @media (max-width: 600px) { .nav-links { top: 58px; ... } }  (mobile only)

# Fix: Move .nav-links { display: none; } inside the @media block
# And ensure .nav-links is visible on desktop

# Step 1: Remove .nav-links { display: none; ... } from outside media query
# This block is between ".nav-links {" and the next "}" after it
old_nav = '''.nav-links {
            display: none;
            flex-direction: column;
            gap: 12px;
            background: linear-gradient(135deg, #ff8c42, #ffd23f);
            position: absolute;
            top: 62px;
            left: 15px;
            right: 15px;
            border-radius: 10px;
            padding: 15px 20px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
            z-index: 998;
        }'''

new_nav = ''  # Remove this entirely from inline CSS (style.css handles desktop/mobile)

if old_nav in content:
    content = content.replace(old_nav, new_nav)
    print("Removed .nav-links from inline CSS (style.css handles it)")
else:
    print("Could not find .nav-links block, trying regex...")
    # Use regex to find and remove
    pattern = re.compile(r'\.nav-links\s*\{[^}]*display:\s*none[^}]*\}', content, re.DOTALL)
    match = pattern.search(content)
    if match:
        content = content.replace(match.group(0), '')
        print("Removed via regex")

# Step 2: Remove .nav-links.active from inline CSS (style.css handles it too)
old_active = '''.nav-links.active {
            display: flex !important;
            animation: slideDown 0.3s ease;
        }'''

new_active = ''

if old_active in content:
    content = content.replace(old_active, new_active)
    print("Removed .nav-links.active from inline CSS")
else:
    print("Could not find .nav-links.active")

# Step 3: Remove .nav-links a from inline CSS (mobile only)
old_nav_a = '''.nav-links a {
            padding: 4px 0;
            font-size: 1rem;
        }'''

if old_nav_a in content:
    content = content.replace(old_nav_a, '')
    print("Removed .nav-links a from inline CSS")

# Step 4: Wrap mobile-specific rules in @media query
# Find the existing @media block and add nav-links rules there
old_media = '''@media (max-width: 600px) {
            .handbook-hero h1 {
                font-size: 1.8rem;
            }
            .chapter-grid {
                grid-template-columns: 1fr;
            }'''

# Check if the media block exists
if old_media in content:
    # Add nav-links: display: none; inside the media query (it's the first rule)
    new_media = '''@media (max-width: 600px) {
            .nav-links {
                display: none !important;
            }
            .handbook-hero h1 {
                font-size: 1.8rem;
            }
            .chapter-grid {
                grid-template-columns: 1fr;
            }'''
    content = content.replace(old_media, new_media)
    print("Added .nav-links display: none to media query")

# Write back
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("\nDone! Navbar should now work correctly.")
print("Desktop: nav visible, hamburger hidden (style.css)")
print("Mobile: hamburger visible, nav hidden until clicked")
