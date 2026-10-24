# Research record template — [short result name]

> This is a reusable template, not an evidence record. Delete instructions and fill missing fields only from verifiable sources.

**Record ID:** [stable ID]  
**Author and contributors:** [names/roles]  
**Research area:** [e.g. QEC / SAT / CHC]  
**Scope:** [exact code/benchmarks/dataset identifiers]  
**First reported:** [YYYY-MM-DD]  
**Last verified:** [YYYY-MM-DD]  
**Status:** [merged author PR / maintainer-adopted finding / independently reproduced observation / open author claim / negative or retracted result]  
**Primary source:** [canonical public GitHub issue or PR URL]  
**Evidence:** [public certificate/checker URL, or state that it is not publicly available]

## 1. Problem and significance
Define the *particular* problem and what would change if the result is correct. Avoid generic importance claims.

## 2. Precise claim
State exactly what was established, including the studied range, model assumptions and whether it is a finite computation or mathematical theorem.

## 3. Input and method
Record source dataset release and hash (if known), code commit, environment/dependencies, command to replay, time/space limits and tie-break rules where applicable. Do not invent missing information.

## 4. Checks and controls
Document independent checker, positive checks, corrupted negative controls, baselines, ablations and out-of-distribution controls where relevant. List failures, timeouts and exceptions.

## 5. External review
Link the **public original review or maintainer comment**, not a screenshot of private Gmail. Quote private correspondence only with explicit permission and in context.

## 6. Real-world effect
State specifically which file, rows, record, verdict or code behavior changed, and who authored the merged change. If nothing has been adopted, mark this as pending.

## 7. Limits and next tests
List unsupported broader claims, novelty/prior-art gaps, missing external acceptance and the test needed to change status.

## 8. History
| Date | Event | Primary-source link |
| --- | --- | --- |
| YYYY-MM-DD | Original report | [link] |
| YYYY-MM-DD | Reviewer response / checker | [link] |
| YYYY-MM-DD | Accepted/closed/pending | [link] |

---

**Disclosure rule:** Publish only cleared public evidence. Keep private source engines, patent-sensitive material and emails in a private archive. The project homepage should display the accepted summary and link here, then on to the canonical public discussion.
