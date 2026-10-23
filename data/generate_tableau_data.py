import csv
import os

# Ensure directory exists
os.makedirs("tableau_portfolio/data", exist_ok=True)

# 1. Carrier Contracts Master
contracts_data = [
    ["CarrierID", "CarrierName", "RouteID", "AgreedRate", "ServiceLevel", "SLA_MaxHours"],
    ["CARRIER-A", "Express Logistics", "RT-NORTH-SOUTH", 1200.00, "Premium", 24],
    ["CARRIER-B", "Global Freight Inc", "RT-WEST-EAST", 850.00, "Standard", 48],
    ["CARRIER-C", "Patagonian Transit", "RT-SOUTH-NORTH", 1500.00, "Express", 30],
]

with open("tableau_portfolio/data/Carrier_Contracts.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(contracts_data)

# 2. Shipments 2024 (Raw Logs with dirty formatting)
shipments_2024 = [
    ["TrackingNumber", "OriginHub", "DestinationHub", "CarrierID", "BilledAmount", "DispatchDate", "DeliveryStatus"],
    ["TRK-2024-001", "hub-north ", "HUB-SOUTH", "CARRIER-A", "1250.50", "2024-03-15 08:30:00", "DELIVERED"],
    ["TRK-2024-002", "HUB-WEST", "hub-east", "CARRIER-B", "850.00", "2024-03-16 10:15:00", "DELIVERED"],
    ["TRK-2024-003", "HUB-NORTH", "HUB-EAST", "CARRIER-A", "2100.00", "2024-04-01 14:00:00", "LATE"],
    ["TRK-2024-004", "HUB-SOUTH", "HUB-NORTH", "CARRIER-C", "", "2024-05-10 11:20:00", "IN_TRANSIT"],  # Null billing
    ["TRK-2024-005", "HUB-NORTH", "HUB-SOUTH", "CARRIER-A", "1200.00", "2024-06-12 09:00:00", "DELIVERED"],
]

with open("tableau_portfolio/data/Shipments_2024.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(shipments_2024)

# 3. Shipments 2025 (Raw Logs with schema variations)
shipments_2025 = [
    ["TrackingNumber", "OriginHub", "DestinationHub", "CarrierID", "BilledAmount", "DispatchDate", "DeliveryStatus"],
    ["TRK-2025-001", "HUB-NORTH", "HUB-SOUTH", "CARRIER-A", "1300.00", "2025-01-10 07:45:00", "DELIVERED"],
    ["TRK-2025-002", "HUB-WEST", "HUB-EAST", "CARRIER-B", "900.50", "2025-02-14 16:30:00", "DELIVERED"],
    ["TRK-2025-003", "HUB-SOUTH", "HUB-NORTH", "CARRIER-C", "1850.00", "2025-03-01 12:00:00", "CANCELLED"],
    ["TRK-2025-004", "hub-west", "HUB-EAST", "CARRIER-B", "850.00", "2025-03-15 13:10:00", "DELIVERED"],
]

with open("tableau_portfolio/data/Shipments_2025.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(shipments_2025)

print("Data generation complete. Datasets saved to tableau/data/")
