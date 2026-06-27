# **Product System \+ Build Scope \+ Delivery Gates**

---

## **1\. Document Purpose**

This document defines **what to build and how the product must behave** to support Phase 1 execution.

It focuses only on:

* Product scope (MVP)  
* Workflow design  
* System constraints  
* Delivery milestones and exit gates

---

## **2\. Product Objective (Execution Goal)**

Build a **minimum operational system** that reliably supports:

* Job intake → Candidate flow → Hire confirmation → Invoice → Payment tracking  
* Controlled manual-first operations with optional automation later  
* End-to-end traceability of every hire and revenue event

---

## **3\. Product Constraints (Hard Rules)**

* Manual-first execution is required for all critical workflows  
* AI features are limited to:  
  * CV suggestion  
  * Candidate matching assist (non-decisional)  
* Bank transfer \+ manual reconciliation is default payment model  
* Employer input is treated as a **signal**, not system truth  
* All sourcing must be demand-driven (no speculative sourcing)

---

## **4\. Core Users**

### **Employer**

* Post jobs  
* Review candidates  
* Confirm hires  
* Provide hiring signals (not system authority)

### **Candidate**

* Apply quickly via mobile-first flow  
* View active job listings  
* Trust verified job sources

### **Ops / Admin**

* Control verification process  
* Manage pipeline states  
* Trigger invoice and payment tracking  
* Enforce operational rules

---

## **5\. Core MVP Scope**

---

### **5.1 Data Model & Workflow Backbone (Must Have)**

Core entities:

* Job  
* Candidate  
* Hire  
* Invoice  
* Payment

---

### **Lifecycle Flow**

Candidate lifecycle:  
 Applied → Interview → Offer → Offer Accepted → Hired

Payment lifecycle:  
 Pending → Paid → Overdue → Disputed

---

Rules:

* All state changes must follow defined workflow transitions  
* No direct manual override of system state without logged reason  
* Each transition must be traceable

---

## **6\. Candidate Experience**

### **Must Have**

* Job listing page (mobile-first)  
* Job detail page  
* Fast apply (CV upload or simple form)  
* Application confirmation page

### **Should Have**

* Save job feature  
* Basic filters (location, salary, language)  
* Light CV improvement suggestions (AI assist only)

### **Out of Scope**

* Assessments or testing system  
* Advanced AI career recommendation engine

---

## **7\. Employer Experience**

### **Must Have**

* Job posting form:  
  * Title  
  * Location (Vietnam)  
  * Salary range  
  * Language requirement  
  * Job requirements  
* Candidate pipeline:  
   Applied → Interview → Offer → Offer Accepted → Hired  
* Hire confirmation action:  
  * Start date  
  * Salary confirmation

### **Should Have**

* Candidate notes/tags  
* Internal comments  
* AI match score \+ screening summary (assist only)

### **Out of Scope**

* Automated interview scheduling  
* Enterprise workflow builder

---

## **8\. Admin / Ops Console**

### **Must Have**

* View all jobs, candidates, hires  
* Manual verification workflow (proof-based)  
* Invoice trigger after verified hire  
* Payment tracking:  
   Pending / Paid / Overdue / Disputed

### **Should Have**

* Reminder templates for follow-ups  
* Daily export (CSV)

### **Out of Scope**

* ERP integration  
* Automated reconciliation system

---

## **9\. Trust & Verification Layer (Minimal)**

### **Must Have**

* Post-hire verification workflow  
* Review request after confirmation window  
* Rating \+ text review  
* Basic moderation queue

### **Should Have**

* Employer response to reviews

### **Out of Scope**

* Fraud detection AI  
* Benchmarking or analytics product

---

## **10\. System Architecture Rules**

### **10.1 Workflow Integrity**

* All changes must go through defined lifecycle transitions  
* No direct database state mutation from UI  
* Every state change must be logged and traceable

---

### **10.2 Revenue Flow Control**

Hire → Verification → Invoice → Payment must be strictly enforced

Rules:

* No verification → no invoice  
* No invoice → no payment tracking  
* No payment → system flags revenue risk

---

### **10.3 Event Tracking (Required)**

Every key action emits an event:

* JobPosted  
* CandidateSubmitted  
* CandidateStageChanged  
* HireMarked  
* HireVerified  
* InvoiceIssued  
* PaymentReceived

All events must include:

* timestamp  
* actor  
* idempotency key  
* payload

---

### **10.4 AI Guardrail**

AI is strictly:

* advisory only  
* cannot modify system state  
* cannot approve hires or invoices

Fallback:

* system must degrade to manual process if AI fails

---

## **11\. Product Milestones**

---

### **Milestone A (Weeks 1–8): Foundation**

Build:

* Candidate flow (apply system)  
* Employer job posting \+ pipeline  
* Admin verification \+ invoice \+ payment tracking  
* Basic event logging

Exit Gate:

* End-to-end flow works in production  
* First invoice successfully issued

---

### **Milestone B (Weeks 9–16): Controlled Pilot**

Build:

* Pipeline UX improvements  
* Reminder system (manual/templated)  
* Basic review system  
* AI assist (CV \+ matching)

Exit Gate:

* 3–5 successful paid hires  
* Stable invoice \+ payment cycle

---

### **Milestone C (Weeks 17–24): Stabilization**

Build:

* Conversion improvements  
* Reliability improvements  
* Ops efficiency tools  
* Dispute handling support

Exit Gate:

* 10–30 successful paid hires  
* Stable monthly operating cycle

---

### **Contingency (Weeks 25–32)**

Only fix:

* conversion issues  
* payment issues  
* system reliability issues

No new features allowed

---

## **12\. Month-by-Month Execution**

---

### **Month 1–2: Build Core System**

Focus:

* Core data model  
* Workflow engine  
* Minimal UI  
* Admin controls  
* Payment tracking logic  
* Event logging

Rule:  
 No non-essential features allowed

---

### **Month 3: Internal Dry Run**

* Full workflow simulation  
* Validate state transitions  
* Validate invoice \+ payment flow  
* Fix system gaps

---

### **Month 4: Controlled Pilot**

* Limited employer cohort  
* Manual sourcing \+ execution  
* Real invoice and payment cycles

---

### **Month 5–6: Stabilization**

* Improve conversion efficiency  
* Improve reliability  
* Strengthen ops execution  
* Prepare Phase 2 transition

---

## **13\. System Dependencies**

Product depends on:

### **Operations System**

* Intake rules  
* Verification SOP  
* Payment enforcement rules

### **GTM System**

* ICP definition  
* Demand mapping  
* Employer pipeline

### **Business Model**

* Pricing rules  
* Invoice trigger logic  
* Payment terms

---

## **14\. Key Risks & Mitigation**

### **Risk: Overbuilding features**

→ Strict MVP scope enforcement

### **Risk: Weak hire verification**

→ Proof-based verification system

### **Risk: Payment leakage**

→ Manual invoice \+ overdue enforcement early

---

## **15\. Product Guardrail**

If speed of first hire conflicts with system design:

Prioritize manual execution → log override → improve system later

