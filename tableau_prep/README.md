[← Back to Tableau Module](../README.md)

---

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
```

---

## 📐 Data Transformation Steps & Operations

### Step 1: Structural Union & Schema Enforcement
- **Node:** `Union_MultiYear_Shipments`
- **Operation:** Combines `Shipments_2024.csv` and `Shipments_2025.csv`.
- **Validation:** Aligns mismatched column data types and generates the system field `[Table Name]` to track source lineage.

### Step 2: String Cleansing & Categorical Normalization
- **Node:** `Clean_Shipment_Attributes`
- **Transforms Applied:**
  - `OriginHub`: `UPPER(TRIM([OriginHub]))` to resolve casing anomalies (e.g., `"hub-north "` ➔ `"HUB-NORTH"`).
  - `DestinationHub`: `UPPER(TRIM([DestinationHub]))`.
  - `BilledAmount`: Converted string values to `Fixed Decimal(16,2)`. Replaced nulls with baseline default or flagged for manual finance review.

### Step 3: Contract Rate Join & Variance Engineering
- **Node:** `Join_Contracts_Master`
- **Join Type:** `Left Outer Join` (`Shipments` ⟕ `Contracts`) on `[CarrierID]`.
- **Calculated Fields Created:**
  ```tableau
  // Rate Variance Amount
  [Cost_Variance] = [BilledAmount] - [AgreedRate]

  // Data Quality Status Flag
  [DQ_Audit_Flag] = 
  IF ISNULL([BilledAmount]) THEN "CRITICAL: Missing Billing Data"
  ELSEIF [Cost_Variance] > 0 THEN "WARNING: Overbilled Contract Rate"
  ELSEIF ISNULL([AgreedRate]) THEN "ERROR: Unmapped Carrier Contract"
  ELSE "VALIDATED"
  END
  ```

---

## ⚡ Automated Pipeline Execution (CLI / Tableau Server Conductor)

To automate this workflow in a CI/CD or production environment, execute the flow using Tableau Prep Command Line Interface:

```bash
# Execute flow headlessly and output directly to Hyper Extract
tableau-prep-cli.bat -t "logistics_data_prep.tflx" -c "credentials.json"
```

---

## 📊 Data Quality & Output Schema Assertions

| Field Name | Target Type | Constraint / Quality Rule |
| :--- | :--- | :--- |
| `TrackingNumber` | `String` | Primary Key. Unique constraint verified. |
| `OriginHub` | `String` | Upper-case normalized. Must match Master Hub list. |
| `BilledAmount` | `Decimal` | Non-negative numeric value. |
| `Cost_Variance` | `Decimal` | Evaluated against `ContractsMaster.AgreedRate`. |
| `DQ_Audit_Flag` | `String` | Used as Row-Level Security and Dashboard Alert Filter. |

---

[← Back to Tableau Module](../README.md)
