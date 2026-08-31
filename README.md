# crm-quality-auditor

Audits a CRM contact export for data quality issues, then uses an LLM to summarise
and prioritise the findings into a report a business owner can act on.

## Why

Marketing and CRM teams run campaigns on databases nobody audits. Most quality
problems are detectable with deterministic rules. The hard part is turning several
hundred raw findings into something a business owner will actually read and act on.

This tool separates the two concerns: rules find the problems, the LLM explains and
ranks them. The LLM never decides whether something is an anomaly.

## How it works

1. Reads a CRM contact export (CSV)
2. Deterministic checks: duplicates, invalid email format, missing required fields,
   inconsistent formatting, implausible values
3. LLM layer: groups the findings, ranks them by business impact, writes a readable
   summary
4. Outputs a Markdown report

## Status

v1 in progress. Target delivery: 30 September 2026.

## Usage

Not yet available.

## Stack

Python, Anthropic API. Test data generated synthetically with Faker, so no real
customer data is ever used.

## Author

Marvin Petris, marketing automation and process engineering.
