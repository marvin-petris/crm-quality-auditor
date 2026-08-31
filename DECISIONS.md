# Decisions

Engineering decisions log. One entry per decision: what was decided, why, and what
was rejected. Written before the code, updated when a decision changes.

---

## 2026-08-31 | Python, not N8N or JavaScript

**Decision.** Build v1 in Python, despite having no prior Python experience.

**Why.** The purpose of this project is to demonstrate that I write code. Building it
in N8N would produce more evidence that I am a no-code automation practitioner, which
is the opposite of the intent. Python is also the language of the roles targeted, so
the learning cost is an investment rather than an overhead.

**Rejected.** A JavaScript or N8N v1 followed by a Python rewrite in v2. Faster to
ship, but the rewrite would waste the effort and the v1 artefact would send the wrong
signal.

---

## 2026-08-31 | Deterministic detection first, LLM second

**Decision.** All anomaly detection is done by explicit rules. The LLM only groups,
ranks and summarises what the rules already found.

**Why.** Anomaly detection must be reproducible and auditable. An LLM asked to find
data quality issues gives different answers on the same input and cannot be trusted
to be exhaustive. Rules are testable; judgement about business impact is where the
LLM adds value.

**Rejected.** Passing the raw export to the LLM and asking it to identify problems.
Simpler to build, unreliable, and unsellable in a professional context.

---

## 2026-08-31 | Minimal v1 scope

**Decision.** v1 is: CSV input, rule-based checks, one LLM call for synthesis,
Markdown report output. Nothing else.

**Why.** Every additional unfamiliar component multiplies the risk of shipping
nothing by the deadline. A small tool that runs beats an ambitious one that does not
exist.

**Explicitly out of scope for v1.** Database storage, Supabase, Langfuse
observability, multi-model routing, Docker packaging, web interface, vector search.
These are v2 candidates once v1 is delivered.

---

## 2026-08-31 | Synthetic test data only

**Decision.** Test data is generated with Faker plus a corruption script that injects
known anomalies.

**Why.** No real customer data can be used, for obvious confidentiality reasons.
Generating the corruption also means the expected findings are known in advance,
which makes the detection rules testable.
