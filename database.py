from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["milk_mate"]

vendors = db["vendors"]
customers = db["customers"]
deliveries = db["deliveries"]
payments = db["payments"]
inventory = db["inventory"]

print("MilkMate MongoDB Connected Successfully!")