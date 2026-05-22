# Skill #1 - Central Dashboard Updater

import json
from datetime import datetime

def load_context():
    try:
        with open('context.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def generate_dashboard():
    context = load_context()
    print("## COMMAND CENTER - Updated at", datetime.now().strftime("%Y-%m-%d %H:%M"))
    print("\n### EXECUTIVE PULSE")
    print(f"Saúde do Portfólio: {context.get('portfolio_health', 7.4)}/10 ↑")
    print("\n### COMPANY CARDS")
    for proj, data in context.get('projects', {}).items():
        print(f"**{proj.replace('_', ' ').title()}**: {data.get('status', 'Active')}")
        for metric in data.get('key_metrics', []):
            print(f"  - {metric}")
    print("\n### SYNERGIES")
    for syn in context.get('synergies', []):
        print(f"- {syn}")
    print("\n✅ Dashboard atualizado automaticamente via Skill #1")

if __name__ == "__main__":
    generate_dashboard()
