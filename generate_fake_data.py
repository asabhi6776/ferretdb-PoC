from pymongo import MongoClient
from faker import Faker
import random

# Initialize the Faker library
fake = Faker()

# MongoDB connection details
username = 'ferret'
password = 'ferret321'
database_name = 'ferretdb'

# Create the MongoDB connection string
connection_string = f'mongodb://{username}:{password}@172.16.0.32:27017/{database_name}?authMechanism=PLAIN'

# Connect to MongoDB
client = MongoClient(connection_string)
db = client[database_name]
collection = db['dummy_data_collection']

# Generate dummy data
def generate_dummy_data(n):
    data = []
    for _ in range(n):
        person = {
            'name': fake.name(),
            'address': fake.address(),
            'email': fake.email(),
            'age': random.randint(18, 90),
            'phone_number': fake.phone_number(),
            'job': fake.job(),
            'company': fake.company()
        }
        data.append(person)
    return data

# Insert dummy data into MongoDB
def insert_dummy_data(data):
    collection.insert_many(data)

if __name__ == "__main__":
    # Number of dummy records to generate
    num_records = 10000

    # Generate and insert the data
    dummy_data = generate_dummy_data(num_records)
    insert_dummy_data(dummy_data)

    print(f"Inserted {num_records} records into the dummy_data_collection.")
