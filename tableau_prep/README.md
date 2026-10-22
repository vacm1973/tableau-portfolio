# 🛠️ Tableau Prep Workflow (`logistics_data_prep.tflx`)

This workflow demonstrates data cleansing, dataset unions, and relationships in Tableau Prep Builder using local multi-source datasets:

1. **Dataset Union:** Merges historical shipment records from [`/tableau/data/Shipments_2024.csv`](../data/Shipments_2024.csv) and [`/tableau/data/Shipments_2025.csv`](../data/Shipments_2025.csv) into a unified transaction stream.
2. **Data Cleansing:** Standardizes hub text formatting (`UPPER`), handles missing billing values, and flags tracking anomalies.
3. **Data Relationship / Join:** Joins unified shipments with [`/tableau/data/Carrier_Contracts.csv`](../data/Carrier_Contracts.csv) on `CarrierID` to prepare contract variance metrics for Tableau Desktop.

[← Back to Tableau Module](../README.md)
