import os
import re

base_dir = r"C:\Users\ishan\Documents\Projects\Awesome-Direct-Preference-Optimization"
assets_dir = os.path.join(base_dir, "assets")
if not os.path.exists(assets_dir):
    os.makedirs(assets_dir)

svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 200" width="100%">
    <defs>
        <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:#4facfe;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#00f2fe;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="800" height="200" fill="url(#grad)" rx="15" ry="15" />
    <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-family="Arial, sans-serif" font-size="40" font-weight="bold" fill="white">
        Awesome Direct Preference Optimization
        <animate attributeName="opacity" values="0.5;1;0.5" dur="3s" repeatCount="indefinite"/>
    </text>
    <circle cx="100" cy="100" r="20" fill="white" opacity="0.3">
        <animate attributeName="cy" values="100;50;100" dur="2s" repeatCount="indefinite"/>
    </circle>
    <circle cx="700" cy="100" r="20" fill="white" opacity="0.3">
        <animate attributeName="cy" values="100;150;100" dur="2.5s" repeatCount="indefinite"/>
    </circle>
</svg>"""

with open(os.path.join(assets_dir, "banner.svg"), "w", encoding="utf-8") as f:
    f.write(svg_content)

readme_path = os.path.join(base_dir, "README.md")
with open(readme_path, "r", encoding="utf-8") as f:
    readme = f.read()

# Add emojis to headings if not present
heading_replacements = {
    "# Awesome-Direct-Preference-Optimization": "# 🚀 Awesome-Direct-Preference-Optimization",
    "## Direct Preference Optimization": "## 🎯 Direct Preference Optimization",
    "## 1. The Macro Chronological Evolution": "## 🕰️ 1. The Macro Chronological Evolution",
    "## 2. Core Algorithmic & Objective Variants": "## 🧮 2. Core Algorithmic & Objective Variants",
    "## 3. Training Training Pipelines & Data Ingestion Modalities": "## ⚙️ 3. Training Training Pipelines & Data Ingestion Modalities",
    "## 4. Production Engineering Challenges & Mitigations": "## 🛡️ 4. Production Engineering Challenges & Mitigations",
    "## 5. Frontier Real-World AI Applications": "## 🌍 5. Frontier Real-World AI Applications",
    "## References": "## 📚 References",
}

for old, new in heading_replacements.items():
    if old in readme and new not in readme:
        readme = readme.replace(old, new)

# Add banner
banner_tag = '<p align="center">\n  <img src="assets/banner.svg" alt="Banner" width="100%">\n</p>\n'
if "assets/banner.svg" not in readme:
    readme = readme.replace("# 🚀 Awesome-Direct-Preference-Optimization", "# 🚀 Awesome-Direct-Preference-Optimization\n\n" + banner_tag)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme)
