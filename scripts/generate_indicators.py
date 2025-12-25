#!/usr/bin/env python3
"""
generate_indicators.py

Generates an indicator register in Markdown format from a JSON configuration.

Usage:
    python generate_indicators.py [config.json] [output.md]
"""

import json
import sys
from pathlib import Path
from datetime import datetime


DEFAULT_INDICATORS = {
    "title": "AI Governance Indicator Register",
    "updated": datetime.now().strftime("%Y-%m-%d"),
    "indicators": [
        {
            "id": "I-01",
            "signal": "Frontier model capability announcements",
            "source": "Lab blogs, arXiv, press releases",
            "scenarios": ["All"],
            "type": "Leading",
            "frequency": "Weekly",
            "confidence": "High",
            "threshold": "Capability significantly exceeds scaling extrapolation"
        },
        {
            "id": "I-02", 
            "signal": "AI safety researcher departures/statements",
            "source": "Social media, press, Congressional testimony",
            "scenarios": ["Emergency Coordination"],
            "type": "Leading",
            "frequency": "Weekly",
            "confidence": "Medium",
            "threshold": "Multiple senior departures citing safety concerns"
        },
        {
            "id": "I-03",
            "signal": "International AI governance meetings",
            "source": "Government announcements, UN, OECD",
            "scenarios": ["Coordinated Caution"],
            "type": "Leading", 
            "frequency": "Monthly",
            "confidence": "High",
            "threshold": "Binding multilateral agreement announced"
        },
        {
            "id": "I-04",
            "signal": "US federal AI legislation progress",
            "source": "Congress.gov, press coverage",
            "scenarios": ["Coordinated Caution"],
            "type": "Confirming",
            "frequency": "Monthly",
            "confidence": "High",
            "threshold": "Comprehensive bill passes committee or floor"
        },
        {
            "id": "I-05",
            "signal": "EU AI Act enforcement actions",
            "source": "EU Commission, national regulators",
            "scenarios": ["Patchwork Progress"],
            "type": "Confirming",
            "frequency": "Monthly",
            "confidence": "High",
            "threshold": "First major fine or compliance order"
        },
        {
            "id": "I-06",
            "signal": "Major AI incident reports",
            "source": "Press, incident databases, regulatory filings",
            "scenarios": ["Emergency Coordination", "Fragmented Scramble"],
            "type": "Confirming",
            "frequency": "Continuous",
            "confidence": "High",
            "threshold": "Incident causing significant harm or near-miss"
        },
        {
            "id": "I-07",
            "signal": "Compute governance proposals",
            "source": "Executive orders, legislation, international agreements",
            "scenarios": ["Emergency Coordination"],
            "type": "Leading",
            "frequency": "Monthly",
            "confidence": "High",
            "threshold": "Mandatory compute reporting or licensing proposed"
        },
        {
            "id": "I-08",
            "signal": "AI labor displacement data",
            "source": "BLS, company announcements, industry surveys",
            "scenarios": ["All"],
            "type": "Lagging",
            "frequency": "Quarterly",
            "confidence": "Medium",
            "threshold": "Displacement rate exceeds historical automation trends"
        },
        {
            "id": "I-09",
            "signal": "Export control escalations",
            "source": "Commerce Dept, press, trade policy analysis",
            "scenarios": ["Fragmented Scramble"],
            "type": "Confirming",
            "frequency": "Monthly",
            "confidence": "High",
            "threshold": "Major new restrictions or retaliatory measures"
        },
        {
            "id": "I-10",
            "signal": "AI safety research funding",
            "source": "Grant announcements, budget documents",
            "scenarios": ["Coordinated Caution"],
            "type": "Leading",
            "frequency": "Quarterly",
            "confidence": "High",
            "threshold": ">50% YoY increase in government/philanthropic funding"
        }
    ]
}


def generate_markdown(config: dict) -> str:
    """Generate Markdown indicator register."""
    
    lines = []
    
    # Header
    lines.append(f"# {config['title']}\n")
    lines.append(f"**Last Updated:** {config['updated']}\n")
    
    # Summary table
    lines.append("## Indicator Summary\n")
    lines.append("| ID | Signal | Scenarios | Type | Frequency |")
    lines.append("|----|--------|-----------|------|-----------|")
    
    for ind in config["indicators"]:
        scenarios = ", ".join(ind["scenarios"])
        lines.append(f"| {ind['id']} | {ind['signal']} | {scenarios} | {ind['type']} | {ind['frequency']} |")
    
    lines.append("")
    
    # Detailed indicators
    lines.append("## Detailed Indicators\n")
    
    for ind in config["indicators"]:
        lines.append(f"### {ind['id']}: {ind['signal']}\n")
        lines.append(f"| Attribute | Details |")
        lines.append(f"|-----------|---------|")
        lines.append(f"| **Source** | {ind['source']} |")
        lines.append(f"| **Linked Scenarios** | {', '.join(ind['scenarios'])} |")
        lines.append(f"| **Indicator Type** | {ind['type']} |")
        lines.append(f"| **Threshold** | {ind['threshold']} |")
        lines.append(f"| **Confidence** | {ind['confidence']} |")
        lines.append(f"| **Update Frequency** | {ind['frequency']} |")
        lines.append("")
    
    # Monitoring schedule
    lines.append("## Monitoring Schedule\n")
    
    weekly = [i for i in config["indicators"] if i["frequency"] == "Weekly"]
    monthly = [i for i in config["indicators"] if i["frequency"] == "Monthly"]
    quarterly = [i for i in config["indicators"] if i["frequency"] == "Quarterly"]
    continuous = [i for i in config["indicators"] if i["frequency"] == "Continuous"]
    
    lines.append("| Frequency | Indicators |")
    lines.append("|-----------|------------|")
    if continuous:
        lines.append(f"| Continuous | {', '.join(i['id'] for i in continuous)} |")
    if weekly:
        lines.append(f"| Weekly | {', '.join(i['id'] for i in weekly)} |")
    if monthly:
        lines.append(f"| Monthly | {', '.join(i['id'] for i in monthly)} |")
    if quarterly:
        lines.append(f"| Quarterly | {', '.join(i['id'] for i in quarterly)} |")
    
    lines.append("")
    
    # By type
    lines.append("## Indicators by Type\n")
    
    leading = [i for i in config["indicators"] if i["type"] == "Leading"]
    confirming = [i for i in config["indicators"] if i["type"] == "Confirming"]
    lagging = [i for i in config["indicators"] if i["type"] == "Lagging"]
    
    lines.append("| Type | Purpose | Indicators |")
    lines.append("|------|---------|------------|")
    lines.append(f"| Leading | Early warning signals | {', '.join(i['id'] for i in leading)} |")
    lines.append(f"| Confirming | Validates shift occurring | {', '.join(i['id'] for i in confirming)} |")
    lines.append(f"| Lagging | Confirms after the fact | {', '.join(i['id'] for i in lagging)} |")
    
    lines.append("")
    lines.append("---")
    lines.append("*Generated by generate_indicators.py*")
    
    return "\n".join(lines)


def main():
    # Load config
    if len(sys.argv) > 1 and Path(sys.argv[1]).exists():
        with open(sys.argv[1]) as f:
            config = json.load(f)
    else:
        config = DEFAULT_INDICATORS
        # Write default config for reference
        config_path = Path(__file__).parent / "indicators_config.json"
        with open(config_path, "w") as f:
            json.dump(DEFAULT_INDICATORS, f, indent=2, default=str)
    
    # Generate markdown
    output = generate_markdown(config)
    
    # Write or print
    if len(sys.argv) > 2:
        with open(sys.argv[2], "w") as f:
            f.write(output)
        print(f"Indicator register written to {sys.argv[2]}")
    else:
        print(output)


if __name__ == "__main__":
    main()
