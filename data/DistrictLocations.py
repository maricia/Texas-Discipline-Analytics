import csv

# Data for the districts with postal codes
districts_data = [
    {"DISTNAME": "PROSPER ISD", "Latitude": 33.2383, "Longitude": -96.7909, "PostalCode": "75078"},
    {"DISTNAME": "COMAL ISD", "Latitude": 29.6455, "Longitude": -98.2236, "PostalCode": "78130"},
    {"DISTNAME": "KILLEEN ISD", "Latitude": 31.1171, "Longitude": -97.7278, "PostalCode": "76543"},
    {"DISTNAME": "NORTHSIDE ISD", "Latitude": 29.4873, "Longitude": -98.6265, "PostalCode": "78238"},
    {"DISTNAME": "GRAND PRAIRIE ISD", "Latitude": 32.7388, "Longitude": -97.0031, "PostalCode": "75052"},
    {"DISTNAME": "ALDINE ISD", "Latitude": 29.9329, "Longitude": -95.3798, "PostalCode": "77039"},
    {"DISTNAME": "MIDLAND ISD", "Latitude": 32.0005, "Longitude": -102.0774, "PostalCode": "79706"},
    {"DISTNAME": "ALVIN ISD", "Latitude": 29.4238, "Longitude": -95.2441, "PostalCode": "77511"},
    {"DISTNAME": "NORTHWEST ISD", "Latitude": 33.0267, "Longitude": -97.3176, "PostalCode": "76247"},
    {"DISTNAME": "AMARILLO ISD", "Latitude": 35.1992, "Longitude": -101.8453, "PostalCode": "79107"},
    {"DISTNAME": "PHARR-SAN JUAN-ALAMO ISD", "Latitude": 26.1948, "Longitude": -98.1836, "PostalCode": "78577"},
    {"DISTNAME": "CYPRESS-FAIRBANKS ISD", "Latitude": 29.9691, "Longitude": -95.6972, "PostalCode": "77429"},
    {"DISTNAME": "DENTON ISD", "Latitude": 33.2148, "Longitude": -97.1331, "PostalCode": "76201"},
    {"DISTNAME": "IRVING ISD", "Latitude": 32.8196, "Longitude": -96.9454, "PostalCode": "75060"},
    {"DISTNAME": "KIPP TEXAS PUBLIC SCHOOLS", "Latitude": 29.6901, "Longitude": -95.5215, "PostalCode": "77021"},
    {"DISTNAME": "ECTOR COUNTY ISD", "Latitude": 31.8506, "Longitude": -102.3744, "PostalCode": "79761"},
    {"DISTNAME": "KELLER ISD", "Latitude": 32.9232, "Longitude": -97.2350, "PostalCode": "76244"},
    {"DISTNAME": "EDINBURG CISD", "Latitude": 26.3017, "Longitude": -98.1633, "PostalCode": "78539"},
    {"DISTNAME": "SPRING BRANCH ISD", "Latitude": 29.8406, "Longitude": -98.4105, "PostalCode": "77080"},
    {"DISTNAME": "MANSFIELD ISD", "Latitude": 32.5635, "Longitude": -97.1420, "PostalCode": "76063"},
    {"DISTNAME": "HOUSTON ISD", "Latitude": 29.7604, "Longitude": -95.3698, "PostalCode": "77002"},
    {"DISTNAME": "LAMAR CISD", "Latitude": 29.5822, "Longitude": -95.7608, "PostalCode": "77469"},
    {"DISTNAME": "YSLETA ISD", "Latitude": 31.7253, "Longitude": -106.3306, "PostalCode": "79907"},
    {"DISTNAME": "CORPUS CHRISTI ISD", "Latitude": 27.8006, "Longitude": -97.3964, "PostalCode": "78401"},
    {"DISTNAME": "SPRING ISD", "Latitude": 30.0799, "Longitude": -95.4172, "PostalCode": "77090"},
    {"DISTNAME": "BROWNSVILLE ISD", "Latitude": 25.9017, "Longitude": -97.4975, "PostalCode": "78520"}
]

# Define the CSV file name
csv_file = 'districts_coordinates_with_postal_codes.csv'

# Write data to CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["DISTNAME", "Latitude", "Longitude", "PostalCode"])
    writer.writeheader()
    writer.writerows(districts_data)

print(f"CSV file '{csv_file}' has been created with the district coordinates and postal codes.")
