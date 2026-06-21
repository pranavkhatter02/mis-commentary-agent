# MIS Commentary Agent

> AI-powered financial MIS commentary generator for CFOs, finance teams, and accounting firms.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Overview

The **MIS Commentary Agent** is an AI-enabled workflow that takes raw financial MIS data (P&L, variance reports, balance sheets) and generates board-ready, insightful commentary. Designed for Human-in-the-Loop (HITL) operations, it combines AI speed with accountant expertise to deliver consistent, explainable, and audit-ready financial narratives.

### What It Does

- Reads monthly P&L, variance reports, and key financial metrics
- Generates structured commentary with variance explanations, ratio analysis, and executive summaries
- Flags anomalies, trends, and areas requiring human review
- Outputs polished MIS reports ready for board meetings, bank presentations, and management reviews

---

## Product Definition

| Field | Value |
|---|---|
| **Product Name** | MIS Commentary Agent |
| **Buyer** | CFOs, Finance Managers, Accounting Firms, Shared Services Centers |
| **Problem Solved** | Manual MIS commentary is time-consuming, inconsistent, and delays reports |
| **Inputs** | P&L CSV/Excel, prior month comparison, budget vs actuals |
| **Outputs** | Structured financial commentary (executive summary, variance analysis, ratio insights, risk flags) |
| **Human Review Rule** | All outputs require finance professional review before distribution; agent flags items with >10% variance for priority review |

---

## Architecture

```
[Raw MIS Data] --> [AI Commentary Layer] --> [Human Review] --> [Final Report]
        |                    |                    |                |
    P&L CSV/            GPT/Claude/          Finance          Board/Management
    Excel Input         Perplexity API       Professional     Distribution
```

### Layers

1. **Data Ingestion Layer** - Upload P&L, variance, and budget data in CSV/Excel
2. **AI Commentary Layer** - LLM generates draft commentary using structured prompts
3. **Review Checklist Layer** - Built-in quality control with validation rules
4. **Human-in-the-Loop** - Finance team reviews, edits, and approves
5. **Output & Distribution** - Final MIS commentary delivered to stakeholders

---

## Repository Structure

```
mis-commentary-agent/
├── prompts/
│   ├── system-prompt.md       # Core AI instructions and rules
│   └── review-checklist.md    # Quality control checklist
├── examples/
│   ├── sample-input.csv       # Example MIS data input
│   └── sample-output.md       # Example generated commentary
├── docs/
│   └── use-cases.md           # Real-world use cases and scenarios
├── README.md                  # This file
├── LICENSE                    # MIT License
└── .env.example               # Environment configuration template
```

---

## Quick Start

### For Finance Teams (No-Code Route)

1. **Download** the `prompts/system-prompt.md` file
2. **Paste** the system prompt into ChatGPT, Claude, or Perplexity
3. **Upload** your monthly P&L CSV (see `examples/sample-input.csv` for format)
4. **Generate** draft commentary
5. **Review** against the `review-checklist.md`
6. **Approve** and distribute

### For Developers (API Route)

```bash
# Clone the repository
git clone https://github.com/pranavkhatter02/mis-commentary-agent.git
cd mis-commentary-agent

# Set up environment
cp .env.example .env
# Edit .env with your API keys

# Run the agent
colab run main.ipynb
```

---

## Sample Workflow

### Step 1: Prepare Your Data
Format your P&L data as a CSV with columns: `Account`, `Current Month`, `Prior Month`, `Budget`, `YTD Actual`, `YTD Budget`

### Step 2: Generate Commentary
Feed the data to the AI with the system prompt from `prompts/system-prompt.md`.

### Step 3: Quality Review
Use `prompts/review-checklist.md` to validate:
- All material variances (>10%) are explained
- Executive summary is under 150 words
- No numbers are misstated
- Action items are assigned

### Step 4: Finalize
Finance professional reviews, edits for company-specific context, and approves.

---

## Use Cases

| Industry | Application |
|---|---|
| **Manufacturing** | Monthly P&L commentary with raw material variance analysis |
| **Services** | Project profitability commentary for client management |
| **Trading/Retail** | Inventory and margin variance reporting |
| **Accounting Firms** | Client MIS commentary as a billable service |
| **Banking/NBFC** | Portfolio and NPA trend commentary for boards |

See `docs/use-cases.md` for detailed scenarios.[screenshot:3]

---

## Human-in-the-Loop (HITL) Rules

This agent is designed as a **copilot, not an autopilot**. Key HITL principles:

- **AI generates draft** commentary in 5-10 minutes
- **Human reviews** for accuracy, context, and tone (15-20 minutes)
- **Total time saved**: Hours of manual commentary writing per month
- **Quality**: Consistent format, comprehensive coverage, no data hallucinations

### What the AI Does Well
- Identifies all variances consistently
- Calculates ratios and trends
- Structures commentary logically
- Flags anomalies automatically

### What the Human Must Do
- Verify numbers against source data
- Add company-specific context
- Adjust tone for audience (board vs. management)
- Approve final report

---

## Getting Started for Your Business

### Phase 1: Service Model (Weeks 1-4)
- Set up the prompt templates from this repo
- Run MIS commentary for 1-3 pilot clients
- Use no-code tools: ChatGPT + Google Sheets + Power BI
- Price: \$500-1,500/month per client

### Phase 2: Productization (Months 2-4)
- Build a simple web front-end for data upload
- Integrate with LLM APIs
- Offer self-serve subscription at \$199/month
- Add reconciliation and close modules

### Phase 3: Platform (Months 5-12)
- Multi-tenant architecture
- API access for enterprise clients
- Expand to full finance ops suite (AP, AR, close, forecasting)

---

## ROI Calculator

| Metric | Manual Process | With Agent |
|---|---|---|
| Time per MIS report | 4-6 hours | 30-45 minutes |
| Reports per month | 1-2 | 4-6 |
| Cost per report | \$200-400 | \$20-40 |
| Savings | - | 80-90% |

---

## Technology Stack

| Layer | Tools |
|---|---|
| **AI Models** | ChatGPT, Claude, Perplexity |
| **Data** | CSV, Excel, Google Sheets |
| **Automation** | Zapier, Make, Power Automate |
| **Visualization** | Power BI, Tableau |
| **OCR** | Adobe Scan, Google Lens (for scanned reports) |
| **Hosting** | GitHub (open source), Vercel/Netlify (web app) |

---

## Contributing

Contributions are welcome! Please read `CONTRIBUTING.md` for guidelines on how to contribute prompt improvements, new use cases, or code enhancements.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Author

**Pranav Khatter** | Chartered Accountant | Finance & AI Enthusiast

- LinkedIn: [linkedin.com/in/pranavkhatter](https://www.linkedin.com/in/pranavkhatter/)
- Email: pranavkhatter02@gmail.com

---

## Roadmap

- [x] MIS Commentary Agent (core)
- [ ] Bank Reconciliation Agent
- [ ] Month-End Close Agent
- [ ] Accounts Payable Agent
- [ ] Finance Knowledge Agent (RAG-based)
- [ ] Web app with file upload and API integration
- [ ] Multi-tenant platform for accounting firms

---

*Built for finance professionals who want AI augmentation, not replacement.*


