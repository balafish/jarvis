# **PHASE 1 MASTER EXECUTION PLAN**

Jarvis Hire – Vietnam-First Outcome-Based Hiring Engine

---

# **1\. PURPOSE OF THIS DOCUMENT**

This document defines **how Phase 1 is executed end-to-end**.

It covers:

* GTM (how demand is generated)  
* Ops (how hiring is delivered)  
* Engineering (how system runs)  
* Finance (how money flows)  
* KPI (how success is measured)

---

# **2\. PHASE 1 OBJECTIVE**

Build and validate a **repeatable hiring-to-cash system in Vietnam**.

The system must reliably:

* generate employer demand  
* convert demand into verified hires  
* convert hires into collected revenue  
* maintain controlled operational risk

---

# **3\. SUCCESS CRITERIA (PHASE 1 IS SUCCESSFUL IF)**

* 10–30 verified paid hires completed  
* 5–10 active employers with repeat behavior  
* Stable hire → verification → invoice → cash cycle  
* ≥45–55% gross margin trend  
* Payment leakage controlled and measurable  
* System operates without breakdown under real load

---

# **4\. TEAM STRUCTURE & OWNERSHIP**

![][image1]

### **Ownership Principle**

* **Nam owns revenue generation and system execution**  
  * GTM (Sales, Marketing)  
  * Product & Engineering  
  * Hiring conversion performance  
* **Kim owns delivery, financial control, and risk management**  
  * Operations execution  
  * Hire verification  
  * Invoice & payment collection

### **Core Rule**

* If it affects **getting the hire → Nam owns**  
* If it affects **getting the money → Kim owns**

---

## **5\. TEAM BUILDING STRATEGY (INTERNS & FRESHERS)**

### **5.1 Objective**

# Build a low-cost, scalable execution team to support:

* # candidate sourcing

* # employer outreach

* # pipeline management

# Goal:  Increase hiring volume without significantly increasing fixed cost.

# 

### **5.2 Hiring Approach**

# Phase 1 prioritizes:

* # interns

* # fresh graduates

# Roles:

* # Sales Intern (employer outreach, follow-up)

* # Marketing Intern (FB groups, content posting, lead gen)

* # Ops Intern (candidate sourcing, pipeline updates)

### **5.3 Why Intern/Fresher Model**

* # Lower cost → extends runway

* # High activity capacity → supports volume model

* # Flexible scaling (add/remove quickly)

* # Suitable for repetitive, process-driven tasks

### **5.4 Role of Execution Lead (Nam)**

* # Define workflow and scripts

* # Monitor output quality

* # Control conversion performance

* # Prevent pipeline chaos

# **Interns execute** **Lead controls system**

### **5.5 Scaling Rule**

# Increase headcount ONLY when:

* # ≥3–4 hires/month achieved

* # funnel conversion is measurable

* # workload exceeds current team capacity

### **5.6 Risk & Control**

# Main risks:

* # low quality output

* # inconsistent execution

* # high churn

# Control mechanisms:

* # strict SOPs

* # simple task structure

* # daily/weekly tracking

* # performance-based continuation

### **5.7 Success Condition**

# Intern/fresher model is successful if:

* # supports 4–6 hires/month without breakdown

* # maintains ≥70% candidate quality

* # does not significantly increase cost per hire

# ---

# **6\. CORE END-TO-END FLOW**

## **6.1 Business Flow**

Employer demand → Job posted → Candidates sourced → Interview → Hire → Day 30 verification → Invoice → Payment

## **6.2 Critical Rule**

A hire is ONLY valid when:

* Candidate is actively working  
* Day 30 employment confirmed  
* Verification evidence collected

---

# **7\. GTM (DEMAND GENERATION SYSTEM)**

## **7.1 Channels**

* Facebook groups (primary)  
* Referrals (primary)  
* Direct outbound (target employers)

## **7.2 Funnel State Machine**

Target → Contacted → Engaged → Meeting → Pilot Job → Active Job → Closed/Lost

## **7.3 Conversion Rules**

* No sourcing without validated employer demand  
* Written agreement required before candidate delivery  
* High-risk employers require scoring approval  
* Pipeline inactivity → pause/close rule

## **7.4 Weekly GTM Discipline**

Every week must improve:

* Contact → meeting rate  
* Meeting → active job rate  
* Active job → hire rate

---

# **8\. OPERATIONS SYSTEM (DELIVERY ENGINE)**

## **8.1 Job Lifecycle**

Active → Paused → Closed → Archived

## **8.2 Candidate Pipeline**

Applied → Interview → Offer → Offer Accepted → Hired → Rejected

## **8.3 SLA Targets**

* Shortlist delivery: ≤48 hours  
* Interview setup: ≤5 days  
* Time-to-hire: ≤35 days (Phase 1 target)

## **8.4 Operating Rules**

* No sourcing without active job approval  
* No job inactivity \>14 days  
* No hire without verification proof  
* No invoice without Day 30 confirmation

## **8.5 Verification System**

Hire is confirmed only with:

* HR confirmation OR payroll OR attendance proof  
* Day 30 stability confirmation

---

# **9\. ENGINEERING SYSTEM (PLATFORM RULES)**

## **9.1 Frontend Strategy**

* Use existing job board template (fast launch)  
* Candidate flow:  
  * Job listing  
  * Job detail  
  * Apply flow  
* Employer flow (custom):  
  * Job posting  
  * Candidate pipeline  
  * Hire tracking  
* Admin:  
  * verification  
  * invoice  
  * payment tracking

## **9.2 Backend Strategy**

Core owned systems:

* Job lifecycle engine  
* Candidate pipeline engine  
* Hire verification system  
* Invoice trigger system  
* Payment tracking system

## **9.3 AI Layer (Strict Rule)**

AI is advisory only:

* CV suggestion  
* Matching score  
* Screening summary

AI cannot:

* change state  
* approve hires  
* trigger invoices

## **9.4 Event System** 

All actions generate events:

* JobPosted  
* CandidateSubmitted  
* HireMarked  
* HireVerified  
* InvoiceIssued  
* PaymentReceived

Rule:  
All KPIs come from event log (no manual reporting)

---

# **10\. FINANCE SYSTEM**

## **10.1 Revenue Model**

* Success fee only: 15–20% first-month salary OR 2-month equivalent  
* No upfront employer fees  
* Revenue only after verified hire

## **10.2 Cash Flow Reality**

* Hire → Day 30 verification → invoice → payment  
* Cash delay: \~45 days per hire cycle

## **10.3 Unit Economics**

* Revenue per hire: \~$1,500 average  
* Break-even: 4–5 hires/month  
* Strong performance: 5–6+ hires/month

## **10.4 Cost Discipline**

Scale cost only if:

* ≥2 successful hires achieved  
* conversion funnel is stable  
* candidate quality ≥70%

---

# **11\. KPI SYSTEM (SUCCESS MEASUREMENT)**

## **11.1 North Star Metric**

Successful Paid Hires (Monthly)

## **11.2 Core Metrics**

* Hire conversion rate  
* Time-to-hire (≤35 days)  
* Qualified candidate ratio (≥70%)  
* Invoice collection rate (≥80–90%)  
* Revenue leakage rate  
* Repeat employer rate

## **11.3 Operational Health**

* Pipeline hygiene (≥90%)  
* Stale job rate (\<10%)  
* SLA compliance rate

## **11.4 System Integrity**

* Event accuracy (≤1% mismatch)  
* State consistency (100% valid transitions)

---

# **12\. RISK & FAILURE HANDLING**

## **12.1 Invoice Failure**

* retry up to 3 times  
* fallback → manual queue

## **12.2 Hire Reversal**

* emit HireReversed event  
* move to Conditional Review  
* block invoice

## **12.3 Payment Issues**

* mark Disputed  
* trigger reconciliation task  
* freeze pipeline if overdue

## **12.4 Duplicate Events**

* deduplicate via idempotency key  
* no double state transitions allowed

---

# **13\. EXECUTION DISCIPLINE RULES**

* No sourcing without validated demand  
* No hire without Day 30 proof  
* No invoice without verification  
* No automation before system stability  
* Revenue protection \> feature development

---

# **14\. WEEKLY EXECUTION LOOP**

Every week review:

### **GTM**

* funnel conversion rates  
* channel performance

### **Ops**

* SLA performance  
* stalled jobs  
* verification queue

### **Finance**

* revenue at risk  
* overdue payments  
* cash flow status

### **Engineering**

* system reliability  
* event correctness  
* workflow failures

---

# **15\. PHASE 1 EXIT CRITERIA**

Phase 1 is complete when:

* 10–30 verified paid hires achieved  
* repeat employer behavior proven  
* cash collection is stable  
* system runs without structural breakdown  
* conversion \+ margin trends are improving

---

# **16\. CORE PRINCIPLE**

This is NOT a job board.

This is a **controlled execution system that converts hiring demand into verified revenue.**

[image1]: <data:image/png;base64,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061btwMtA/e7nYcQQlKGvW+EEBIsUp8ucjWMr7fnE0JIykgF83FJRfN3ex4hhJCyg9/RRL3K34QjJAVGjhx58IQJE06kSlefPn2UHaPi9fLLLzewyxYhpGzY11WYVdnq1XHjxh1nn29CUkIK1m179+5VFJWKnn/++b522SKElI033njDc21R4dD48eOX2eebkJSggaOCEA0cIalDAxde0cCRwKGBo4IQDRwhqUMDF17RwJHAoYGjghANHCGpQwMXXtHAkcChgaOCEA0cIalDAxde0cCRwKGBo4IQDRwhqUMDF17RwJHAoYGjghANHCGpQwMXXtHAkcChgaOCEA0cIalDAxde0cCRwKGBo4IQDRwhqUMDF17RwJHAoYGjghANHCGpQwMXXtHAkcChgaOCEA0cIalDAxde0cCRwAnSwK1duzbu88qVK9X27ds9+ZLVL7/8Evd51qxZatq0aWrnzp2evEFoxIgRasmSJZ54otq1a5davHix+vrrrz3zEtX69evVXXfd5YlnmmjgCEmdIA3cqlWr4j6jPsZ09erVnryJauvWrU567ty56v333/fkCVJr1qzR+21kvtNPP/3kyZvpooEjgROkgTv33HPVAw884HyW1av58+d78iWrE0880UkfdNBBev2IYWrnTVYdOnRw0vg+qVSoqHCwb3Xq1NHTyy67zJPnj/Tll1+W+ftNnz7dEytv0cARkjqp1De2DjnkELV7926dPvjgg1Xnzp11g/CAAw7w5E1Et912m9MYrV+/vq6XmjdvrqebN2/25A9CZ5xxhqpRo4beZ6hx48Y6fuCBB3ryZrpo4EjgBG3gZJXq8ccf15+RhoFDL1xOTo668MIL1RNPPKHnLV26VL388svq8ssvV7fffrtuUV177bVqyJAhnvVCt9xyi/rxxx91ukGDBqqwsNCTB/Nvvvlmde+99+rtIfbII49o44SeOny+7rrrnPz9+/d30oijRYl9vvHGG7Vxw/d56aWXVKdOndT111/v2Z7RmDFjPDEIBq5mzZrOZ6wbvYWPPfaYys/PV5deeqmO5+XlqT/96U9q9OjRTt6vvvpKH69YLOYYOOyXme9ODxo0SF188cXqueeeUz///LM6/vjj9fw+ffp49gl69NFHPbFURQNHSOqUh4E76aST1GmnnaZjqBdQ3yLdo0cP9cwzz+i6Y+zYsSoajeo6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>