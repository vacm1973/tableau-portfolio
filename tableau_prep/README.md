# 🛠️ Enterprise Data Preparation Pipeline | Tableau Prep Builder

> **Pipeline Version:** `v2.4.0`  
> **Source Systems:** Multi-year WMS CSV Extracts (`Shipments_2024`, `Shipments_2025`) & ERP Master Tables (`Carrier_Contracts`)  
> **Output Target:** Published Data Source (.hyper) to Tableau Cloud / Server  

---

## 📌 Architecture & ETL Design Overview

This data flow transforms dirty, multi-source operational shipment logs into an enterprise-ready published data source. It handles structural schema inconsistencies, string normalization, missing value imputation, variance flagging, and multi-table relationships.

```text
[Shipments_2024.csv] ──┐
                      ├──► [Union Step] ──► [Clean & Normalize] ──┐
[Shipments_2025.csv] ──┘                                         │
                                                                 ├──► [Left Join] ──► [Audit Step] ──► Output (.hyper)
[Carrier_Contracts.csv] ────────────────────► [Clean Master]   ──┘   (CarrierID)      (Cost Variance)
