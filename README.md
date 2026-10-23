# 📊 Tableau & Tableau Prep Enterprise Analytics Portfolio

> **`Tableau Desktop` | `Tableau Prep Builder` | `LOD Calculations` | `Dynamic RLS` | `Multi-Source Relationships`**

A comprehensive end-to-end Tableau BI solution demonstrating multi-dataset prep workflows, Level of Detail (LOD) calculations, dynamic Row-Level Security (RLS), and interactive dashboard architecture.

---

## 🗂️ Navigation & Key Contents

| Directory / File | Description | Link |
| :--- | :--- | :--- |
| 📁 **`tableau_prep/`** | Data union, transformation, and relationship flows in Tableau Prep. | [View Prep Workflow](./tableau_prep/) |
| 📄 **`lod_metrics.tableau`** | FIXED, INCLUDE, and EXCLUDE Level of Detail (LOD) expressions. | [View LOD Metrics](./calculations/lod_metrics.tableau) |
| 📄 **`complex_calculations.tableau`** | Table calculations, running totals, and YoY variance logic. | [View Calculations](./calculations/complex_calculations.tableau) |
| 📄 **`user_filters_rls.tableau`** | Dynamic Row-Level Security using `USERNAME()` and groups. | [View Security Rules](./security/user_filters_rls.tableau) |

---

## 🏗️ Technical Highlights

### 1. Tableau Prep ETL & Unions (`/tableau_prep`)
- Unified multi-year shipment files using Tableau Prep Union nodes.
- Created relationships between operational transactions, carrier master contracts, and time dimensions.

### 2. Advanced Level of Detail (LOD) Expressions (`/calculations`)
- Implemented **FIXED LODs** to evaluate total regional spend independently of dashboard slicers.
- Utilized **INCLUDE & EXCLUDE LODs** for granular baseline vs. actual performance metrics.

### 3. Dynamic Security & Governance (`/security`)
- Established server-side Row-Level Security restricting distribution center access based on Tableau Cloud user identity (`USERNAME()`) and active Directory Groups (`ISMEMBEROF`).

---

**Victor Andres Costa Molina**

Senior Data Engineer | BI & Data Architecture

[GitHub Profile](https://github.com/vacm1973)
