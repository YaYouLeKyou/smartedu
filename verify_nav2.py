import re

with open('handbook.html', 'r', encoding='utf-8', errors='replace') as f:
    hb = f.read()

style_start = hb.find('<style>')
style_end = hb.find('</style>', style_start)
inline_css = hb[style_start:style_end]

print("=== Remaining inline nav/hamburger CSS ===")
for pattern in [r'\.hamburger\s*\{[^}]+\}', r'\.nav-links\s*\{[^}]+\}', r'\.nav-links\.active\s*\{[^}]+\}', r'\.nav-links\s*a\s*\{[^}]+\}']:
    for m in re.finditer(pattern, inline_css, re.DOTALL):
        rule = m.group(0)
        print(f"  {rule[:200]}")

# Check style.css has what we need
with open('style.css', 'r', encoding='utf-8', errors='replace') as f:
    css = f.read()

print("\n=== style.css nav/hamburger ===")
hamburger = re.search(r'\.hamburger\s*\{[^}]+\}', css)
if hamburger:
    print(f"  .hamburger: {hamburger.group(0)[:100]}")

hamburger_mq = re.search(r'@media[^{]*\{[^}]*\.hamburger\s*\{[^}]+\}', css, re.DOTALL)
if hamburger_mq:
    print(f"  .hamburger in media query: {hamburger_mq.group(0)[:200]}")

nav_links = re.search(r'\.nav-links\s*\{[^}]+\}', css)
if nav_links:
    print(f"  .nav-links: {nav_links.group(0)[:150]}")

# Check media queries
media_nav = re.findall(r'@media[^{]*\{[^}]*\.nav-links[^}]+\}', css, re.DOTALL)
print(f"\n  @media blocks with .nav-links: {len(media_nav)}")
for block in media_nav:
    nav_rule = re.search(r'\.nav-links\s*\{[^}]+\}', block)
    active_rule = re.search(r'\.nav-links\.active\s*\{[^}]+\}', block)
    ham_rule = re.search(r'\.hamburger\s*\{[^}]+\}', block)
    print(f"    nav: {nav_rule.group(0)[:80] if nav_rule else 'N/A'}")
    print(f"    active: {active_rule.group(0)[:80] if active_rule else 'N/A'}")
    print(f"    hamburger: {ham_rule.group(0)[:80] if ham_rule else 'N/A'}")
