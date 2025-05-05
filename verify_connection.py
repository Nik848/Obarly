from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB setup
mongodb_uri = os.getenv('MONGODB_URI', 'mongodb+srv://nik84810:Niku_2004@obarly.xwq8r3k.mongodb.net/')
database_name = os.getenv('DATABASE_NAME', 'Inventory')

try:
    # Connect to MongoDB Atlas
    client = MongoClient(mongodb_uri)
    db = client[database_name]
    
    # Test connection
    print("Successfully connected to MongoDB Atlas!")
    
    # List all collections
    collections = db.list_collection_names()
    print("\nAvailable collections:")
    for collection in collections:
        count = db[collection].count_documents({})
        print(f"- {collection}: {count} documents")
    
    # Show sample data from Products collection
    print("\nSample Products:")
    products = db.Products.find().limit(3)
    for product in products:
        print(f"\nProduct Name: {product.get('product_name', 'N/A')}")
        print(f"Price: {product.get('default_price', 'N/A')}")
        print(f"Categories: {product.get('categories', 'N/A')}")
        print("---")
    
    # Close the connection
    client.close()
    
except Exception as e:
    print(f"Error connecting to MongoDB Atlas: {str(e)}") 