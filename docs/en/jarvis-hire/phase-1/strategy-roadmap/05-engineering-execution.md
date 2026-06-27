# **Dev Team Plan \+ Architecture \+ Delivery Plan**

## **1\) Mission (Engineering Scope Only)**

Deliver a stable MVP that supports the **core revenue execution loop**:

Job Intake → Candidate → Hire → Verification (Day 30\) → Invoice → Payment

Engineering focus:

* Ensure **end-to-end system reliability**  
* Ensure **no revenue leakage due to system failure**  
* Support **manual-first execution with system tracking**  
* Enable controlled AI assistance (non-blocking)

---

## **2\) Engineering Principles (Hard Rules)**

* Revenue path \> features  
* Manual execution always allowed as fallback  
* No system state without event logging  
* AI is advisory only (never writes state)  
* Every critical action must be traceable via events

---

## **3\) System Architecture Overview** 

### **3.1 Frontend Strategy (Fast Delivery / Template-First)**

\- Use purchased UI theme: [Superio Job Board](https://preview.themeforest.net/item/superio-job-board-react-nextjs-template/full_screen_preview/42719363) as base for candidate-facing flows.

Goal: ship usable UI fast, not perfect UI.

#### **Candidate Side (Template-Based Funnel Only)**

Use existing job board template:

* Job listing  
* Job detail  
* Apply flow (CV upload / form)  
* Application confirmation

Rules:

* No candidate dashboard  
* No profile system  
* No retention features  
* No personalization layer in Phase 1

👉 Purpose: pure acquisition \+ application funnel

---

#### **Employer Side**

Build only workflow-critical UI:

* Job posting  
* Job list (Active / Paused / Closed)  
* Candidate pipeline board:  
   Applied → Interview → Offer → Offer Accepted → Hired  
* Hire action (mark as hired)  
* Basic candidate notes

Rules:

* No analytics dashboard  
* No BI/reporting layer  
* No advanced AI UI dependency in core flow

👉 Purpose: control hiring decisions \+ pipeline execution

---

#### **Admin Console (Internal Control System)**

Must-have operational control:

* Verification (Day 30 hire validation)  
* Invoice control (issue / track / override)  
* Payment tracking:  
   Pending → Paid → Overdue → Disputed  
* Job \+ candidate monitoring  
* Manual override \+ audit logs

👉 Purpose: revenue protection \+ system integrity

---

#### **AI UI Hooks (Minimal, Non-Critical)**

Embedded only at decision assist points:

* CV suggestion (apply flow)  
* Matching score (employer pipeline)

Rules:

* AI output \= advisory only  
* No automatic state changes  
* Always requires human confirmation

---

## **4\) Core Domain Model (System of Record)**

### **JobState**

Draft → Active → Paused → Closed → Archived

### **CandidateState**

Applied → Interview → Offer → Accepted → Hired → Rejected

### **HireState**

PendingVerification → VerifiedDay30 → ConditionalReview → Finalized

### **InvoiceState**

NotReady → Ready → Issued → Overdue → Paid → Disputed

### **PaymentState**

Pending → Paid → Overdue → Disputed

---

## **5\) Event-Driven System (Critical Backbone)**

All business actions emit immutable events.

### **Core Events (Minimum)**

* JobPosted  
* CandidateApplied  
* CandidateStageUpdated  
* HireMarked  
* HireVerifiedDay30  
* InvoiceIssued  
* PaymentReceived  
* PaymentOverdue  
* HireReversed

Rules:

* append-only event store  
* idempotent processing  
* no direct DB state mutation without events  
* all KPIs derived from events

---

## **6\) AI Integration Rules (Strict)**

AI is:

* advisory only  
* non-authoritative

Allowed:

* CV suggestion  
* match scoring  
* screening summary

Not allowed:

* hiring decisions  
* invoice triggers  
* state changes

AI logs must include:

* input hash  
* output hash  
* model version

Fallback:

full manual workflow always available

---

### **7\) Failure Handling & Recovery**

#### **7.1 Invoice Failure**

* System retries invoice issuance up to **3 times (exponential backoff)**  
* If still failed → move to **Manual Invoice Queue**  
* Ops must resolve within SLA  
* All retries must be logged as events

#### **7.2 Hire Reversal**

* Emit `HireReversed` event  
* Move Hire state → `ConditionalFailureReview`  
* Block invoice generation until resolution  
* Finance cannot proceed until review is closed  
* All reversals require reason code \+ evidence

#### **7.3 Duplicate Event Handling**

* All events must use `idempotency_key`  
* Duplicate events are ignored (no state mutation)  
* System must guarantee **exactly-once business effect (logically)**

#### **7.4 Payment Issues**

* If payment not received by Net 15 → set `PaymentState = Overdue`  
* After dispute or inconsistency → set `PaymentState = Disputed`  
* Trigger reconciliation task (Finance \+ Ops)  
* Invoice remains frozen until resolved

---

## **8\) System Scale Assumptions**

* 300–1,000 events/day  
* 20–60 employer users  
* 10–25 internal users  
* 40–60 active jobs

---

## **9\) Delivery Phases**

### **Phase 1: Build (Month 1–2)**

Core delivery:

* Candidate flow (apply)  
* Employer workflow (post → pipeline → hire)  
* Admin verification \+ invoice \+ payment tracking  
* Event system

Backend:

* domain models  
* API contracts  
* event store  
* AI service layer v1

Frontend:

* template integration  
* minimal workflows  
* admin dashboards

---

### **Phase 2: Pilot (Month 3–4)**

Focus:

* conversion fixes  
* workflow stabilization  
* reporting accuracy

Add:

* reminders system  
* KPI dashboard APIs  
* audit improvements

---

### **Phase 3: Stabilization (Month 5–6)**

Focus:

* reliability  
* operational efficiency  
* dispute handling

Add:

* review system  
* bulk admin tools  
* system hardening

---

## **10\) Quality Gates**

### **Gate A — Build Complete**

* end-to-end flow works  
* first hire → invoice → payment successful  
* event tracking fully active

### **Gate B — Pilot Stable**

* \<1% event mismatch  
* no duplicate state transitions  
* ops can run without engineers

### **Gate C — Stable Engine**

* ≤1 Sev-1/month  
* AI failure ≤3%  
* manual override ≤5%

---

## **11\) Architecture Boundaries**

* Candidate FE → template-based UI  
* Employer/Admin FE → workflow system  
* Core backend → owned services  
* AI layer → isolated service

---

## **12\) Weekly Execution Rhythm**

* Monday: engineering delivery \+ blockers  
* Wednesday: ops feedback \+ conversion issues  
* Friday: system health \+ incidents \+ KPI tracking

