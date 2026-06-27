## **OPS SOP**

## **Jarvis Hire** 

---

# **1\) Purpose & Scope**

This document defines **operational execution rules** for running the hiring system in Phase 1\.

It covers:

* Job execution flow  
* Candidate handling process  
* Verification process  
* Invoice & payment processing  
* Operational enforcement rules

---

# **2\) Operating Ownership Model (Execution Layer)**

### **Rule:**

Ops executes all workflows. Execution Lead has override authority.

| Area | Responsible | Accountable |
| :---- | :---- | :---- |
| Job intake | Ops | Ops Lead |
| Sourcing | Ops / Recruiter | Ops Lead |
| Interview coordination | Ops | Ops Lead |
| Offer tracking | Ops | Ops Lead |
| Verification | Ops | Ops Lead |
| Invoice issuance | Finance | Finance Lead |
| Payment enforcement | Finance | Execution Lead |
| Escalations | Ops Lead | Execution Lead |

### **Default Rule:**

If ownership is unclear → Ops Lead owns it.

---

# **3\) System States (Core Data Model)**

## **3.1 Job States**

Each job must be in exactly ONE state:

* Active  
* Paused  
* Frozen  
* Closed  
* Archived

---

## **3.2 Candidate Lifecycle (per job)**

Applied → Interview → Offer → Offer Accepted → Hired

Rules:

* No skipping stages  
* Any backward movement requires reason code  
* One active state per candidate per job

---

# **4\) End-to-End Execution Flow**

## **Step 1: Job Intake**

* Validate job request using intake checklist  
* Apply intake gate rules  
* Approve / Pause / Reject  
* Assign job owner

**Done when:**

* Job state \= Active  
* Owner assigned  
* Intake checklist completed

---

## **Step 2: Sourcing & Shortlist**

* Source candidates only for Active jobs  
* Prepare shortlist (3–5 candidates)  
* Send to employer with notes

**Done when:**

* Shortlist delivered  
* CV \+ notes attached  
* Timestamp logged

---

## **Step 3: Interview Coordination**

* Schedule interviews  
* Track employer response  
* Escalate delays

**Done when:**

* Interview confirmed  
* No pending communication gaps

---

## **Step 4: Offer & Hire Tracking**

* Track candidate progression  
* Validate employer confirmation  
* Record hire event with evidence

**Done when:**

* Hire status logged with proof

---

## **Step 5: Verification (Critical Gate)**

A hire is only valid if:

* Day 30 employment confirmation OR  
* Strong proof signals (attendance / payroll / employer validation)

Then:

* Start Day 30 verification cycle

**Done when:**

* Day 30 confirmation completed

---

## **Step 6: Invoice & Payment**

* Invoice issued ONLY after verification  
* Collect payment proof  
* Reconcile within 24h

**Done when:**

* Payment confirmed  
* System updated

---

## **Step 7: Closure**

* Close job  
* Assign reason code  
* Log final outcome

**Done when:**

* Job state \= Closed  
* Reason logged

---

# **5\) SLA (Operational Speed Rules)**

## **Shortlist SLA**

* Target: 48 hours after job becomes Active

## **Interview SLA**

* Employer response required within 48 hours

## **Stalled Work Rules**

* 7 days no progress → flagged  
* 14 days no progress → closed

---

# **6\) Core Operating Rules**

## **6.1 Intake Gate (Hard Filter)**

A job is accepted only if:

* Salary defined  
* Hiring urgency ≤ 30 days  
* Active intent confirmed  
* Within target vertical  
* Employer responsive

Else:  
 → Reject or pause immediately

---

## **6.2 Pipeline Hygiene**

* No progress for 7 days → flagged  
* No progress for 14 days → closed  
* Every closure must include reason code

---

## **6.3 Verification Rule**

* No hire without Day 30 confirmation  
* No verification → no invoice

---

## **6.4 Payment Rule**

* No payment → restrict delivery activity  
* Overdue → pipeline freeze  
* Repeat delay → escalation \+ review

---

# **7\) Enforcement System**

## **Intake Enforcement**

* Missing data → return to employer  
* Failed gate → reject/pause

## **Execution Enforcement**

* Employer delay → pause job  
* Repeated delay → escalate

## **Payment Enforcement**

* Day 3 overdue → warning  
* Day 7 overdue → freeze delivery  
* Day 14 overdue → full freeze  
* Day 30 overdue → blacklist review

---

# **8\) Escalation Path**

Ops → Ops Lead → Execution Lead

Escalation triggers:

* revenue risk  
* stalled critical job  
* payment issues  
* rule override requests

Execution Lead required approval for:

* rule overrides  
* reactivation of frozen accounts  
* blacklist reversal

---

# **9\) Weekly Operating Cadence**

## **Monday**

* Intake review  
* Pipeline health check  
* SLA risk review

## **Wednesday**

* Stalled roles review  
* Verification queue review

## **Friday**

* Payment reconciliation  
* Closure summary  
* Enforcement report

---

# **10\) Required System Logs**

Must be recorded for every job:

* Intake decision log  
* Follow-up log  
* Interview log  
* Verification proof  
* Invoice & payment record  
* Closure reason code  
* Enforcement actions  
* Exception logs

---

# **11\) Exception Handling Rule**

Any exception must include:

* Approver  
* Reason  
* Time limit  
* Follow-up action

### **Rule:**

No log \= invalid exception

