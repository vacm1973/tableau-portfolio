# 🛠️ Tableau Prep Workflow (`logistics_data_prep.tflx`)

This workflow demonstrates data cleaning, dataset unions, and relationships using Tableau Prep Builder:

1. **Dataset Union:** Combines monthly transactional logs (`Shipments_2024.csv` and `Shipments_2025.csv`) into a single unified stream.
2. **Data Cleansing:** Normalizes carrier text to uppercase, removes null tracking records, and handles missing weight/volume metrics.
3. **Multi-Table Relationships:** Joins cleaned shipments with `ContractsMaster` and `Calendar` datasets on `CarrierID` and `ShipmentDate`.
