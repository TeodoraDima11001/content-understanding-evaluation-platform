# Content Understanding & Evaluation Platform

## Overview

This project simulates a production-style Data Science system inspired by Spotify’s Content Platform team.

It focuses on evaluating and improving how large-scale content systems classify, annotate, and understand content (music, podcasts, audiobooks) using a combination of:

- SQL-based data modeling
- dbt transformation pipelines
- Annotation quality evaluation (human + LLM)
- Statistical experimentation
- Decision-making under uncertainty

---

## Problem Statement

Modern content platforms must ensure:

- Content is correctly classified across complex taxonomies
- Human and LLM-generated annotations are reliable
- Metadata quality is consistent across segments
- Product decisions are based on statistically valid evidence

This project simulates that environment end-to-end.

---

## System Architecture

The system follows a full data → decision pipeline:
Data Ingestion (SQL Layer) ↓ Data Modeling (dbt) ↓ Annotation Layer (Human + LLM labels) ↓ Evaluation Layer (Python) ↓ Experimentation Layer (Statistical Testing) ↓ Decision Layer (Ship / No-Ship logic)
---

## Key Components

### 1. SQL Layer (`sql/schema`)
Defines the core warehouse tables:

- `dim_user`
- `dim_content`
- `fact_content_events`

Represents the source of truth for user-content interactions.

---

### 2. dbt Layer (`dbt/models`)
Transforms raw data into analytics-ready datasets.

Includes:
- staging models
- intermediate transformations
- final metrics marts

Ensures reproducible and testable data pipelines.

---

### 3. Evaluation Layer (`src/evaluation`)

#### Annotation Quality
Measures agreement between human labels and system annotations:
- Accuracy
- Disagreement rate
- Segment-level performance

#### LLM Evaluation
Evaluates LLM-generated annotations:
- False positive / false negative rates
- Calibration gap (confidence vs correctness)
- Confusion summary metrics

#### Statistical Testing
Supports decision-making using:
- Bootstrap confidence intervals
- T-tests
- Effect size calculations

---

### 4. Decision Intelligence Layer

Converts metrics into product decisions:

- SHIP
- SHIP_WITH_RISK
- DO_NOT_SHIP
- NEEDS_FURTHER_ANALYSIS

It introduces risk-aware decision-making rather than relying on raw accuracy.

---

## Key Design Principles

### 1. Real-world ambiguity
Content classification is treated as:
- noisy
- multi-label
- context-dependent

---

### 2. Segment-aware evaluation
Performance is measured across:
- content type
- user groups
- annotation confidence levels

---

### 3. Statistical rigor
All comparisons use:
- uncertainty estimation
- hypothesis testing
- effect size measurement

---

### 4. Decision over metrics
The system prioritizes:

> “What should we do?”  
over  
> “Which model has higher accuracy?”

---

## Technologies Used

- Python (pandas, numpy, scipy)
- SQL (warehouse modeling)
- dbt (data transformations)
- Statistical inference methods

---

## What This Project Demonstrates

This project shows ability to:

- Design production-style data systems
- Build evaluation frameworks for ML + annotation systems
- Apply statistical reasoning to product decisions
- Work with SQL + analytics pipelines
- Translate metrics into business decisions
- Think like a Data Scientist II in a content platform environment

---

## How This Maps to Spotify

This project mirrors Spotify Content Platform challenges:

- Content taxonomy design
- Annotation quality control
- LLM evaluation pipelines
- Metric reliability across large-scale systems
- Data-driven product decision-making

---

## Final Summary

This is not a model-building project.

It is a **content understanding system simulation**, covering the full lifecycle:

👉 Data → Evaluation → Experimentation → Decision
