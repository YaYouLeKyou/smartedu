import re

# 1. Add dropdown CSS to style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add dropdown styles after .nav-links a:hover
dropdown_css = '''
/* Dropdown menu */
.nav-links li {
    position: relative;
}

.nav-links .dropdown-menu {
    display: none;
    position: absolute;
    top: 100%;
    left: 0;
    background: white;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    padding: 8px 0;
    min-width: 180px;
    z-index: 1001;
}

.nav-links li:hover .dropdown-menu,
.nav-links li:focus-within .dropdown-menu {
    display: block;
    animation: slideDown 0.2s ease;
}

.nav-links .dropdown-menu li {
    margin: 0;
}

.nav-links .dropdown-menu a {
    display: block;
    padding: 10px 16px;
    color: #333;
    white-space: nowrap;
}

.nav-links .dropdown-menu a:hover {
    background: #f5f5f5;
    color: #ff8c42;
}

/* Dropdown arrow indicator */
.nav-links .has-dropdown > a {
    padding-right: 24px;
    position: relative;
}

.nav-links .has-dropdown > a::after {
    content: '';
    position: absolute;
    right: 8px;
    top: 50%;
    transform: translateY(-50%);
    border: 5px solid transparent;
    border-top-color: white;
    transition: transform 0.2s ease;
}

.nav-links li:hover .has-dropdown > a::after,
.nav-links li:focus-within .has-dropdown > a::after {
    transform: translateY(-50%) rotate(180deg);
}

/* Mobile dropdown adjustments */
@media (max-width: 600px) {
    .nav-links .dropdown-menu {
        position: static;
        box-shadow: none;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 0;
        padding: 0;
        border-top: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .nav-links .dropdown-menu a {
        color: rgba(255, 255, 255, 0.9);
        padding: 10px 16px 10px 32px;
    }
    
    .nav-links .dropdown-menu a:hover {
        background: rgba(255, 255, 255, 0.1);
        color: #ffd23f;
    }
}

'''

# Insert after .nav-links a:hover
insert_after = '.nav-links a:hover {\n    color: #333;\n}'
if insert_after in css:
    css = css.replace(insert_after, insert_after + dropdown_css)
    print("Added dropdown CSS")
else:
    print("Could not find insertion point")

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update handbook.html navbar
with open('handbook.html', 'r', encoding='utf-8') as f:
    hb = f.read()

# Replace the nav-links with dropdown structure
old_nav = '''            <ul class="nav-links">
                <li><a href="index.html">Home</a></li>
                <li><a href="handbook.html" class="active" aria-current="page">Handbook</a></li>
                <li><a href="handbook-foundations.html">Foundations</a></li>
                <li><a href="handbook-teaching.html">Teaching</a></li>
                <li><a href="handbook-ethics.html">Ethics</a></li>
                <li><a href="handbook-language.html">Language</a></li>
                <li><a href="handbook-creative.html">Creative</a></li>
                <li><a href="handbook-professional.html">Professional</a></li>
                <li><a href="france.html">France</a></li>
                <li><a href="turkey.html">Turkey</a></li>
            </ul>'''

new_nav = '''            <ul class="nav-links">
                <li><a href="index.html">Home</a></li>
                <li><a href="handbook.html" class="active" aria-current="page">Handbook</a></li>
                <li><a href="handbook-foundations.html">Foundations</a></li>
                <li><a href="handbook-teaching.html">Teaching</a></li>
                <li><a href="handbook-ethics.html">Ethics</a></li>
                <li><a href="handbook-language.html">Language</a></li>
                <li><a href="handbook-creative.html">Creative</a></li>
                <li><a href="handbook-professional.html">Professional</a></li>
                <li class="has-dropdown">
                    <a href="#" aria-haspopup="true" aria-expanded="false">Mobilité</a>
                    <ul class="dropdown-menu" role="menu">
                        <li role="none"><a href="france.html" role="menuitem">France</a></li>
                        <li role="none"><a href="turkey.html" role="menuitem">Turkey</a></li>
                    </ul>
                </li>
            </ul>'''

if old_nav in hb:
    hb = hb.replace(old_nav, new_nav)
    print("Updated navbar with Mobilité dropdown")
else:
    print("Could not find old navbar")

# 3. Fix Contact button margin
hb = hb.replace(
    'style="margin-left:24px;background:linear-gradient(135deg,#1a1a2e,#16213e);"',
    'style="margin-left:32px;background:linear-gradient(135deg,#1a1a2e,#16213e);"'
)
print("Updated Contact button margin")

with open('handbook.html', 'w', encoding='utf-8') as f:
    f.write(hb)

print("Done!")