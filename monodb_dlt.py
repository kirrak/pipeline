import logging
from pymongo import MongoClient

# Configure logging
logging.basicConfig(filename='script_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# MongoDB connection details
mongo_uri = "mongodb+srv://test998972:hEV5s7MnF32fs8kT@cluster0.moqw88r.mongodb.net/"  # Update with your actual connection string
mongo_cluster_name = 'cluster0'
mongo_db_names = ['psl2_db', 'psl_db']

# Extract username and password from the connection string (replace with your actual username and password)
mongo_username = "test998972"
mongo_password = "hEV5s7MnF32fs8kT"

try:
    # Construct the MongoDB connection string with username and password
    mongo_uri_with_auth = f"mongodb+srv://{mongo_username}:{mongo_password}@{mongo_cluster_name}.mongodb.net/"

    # Connect to MongoDB
    client = MongoClient(mongo_uri_with_auth)

    # Log connection success
    logging.info('Connected to MongoDB.')

    # Get the list of available databases
    available_dbs = client.list_database_names()

    # Check and delete each specified database
    for db_name in mongo_db_names:
        if db_name in available_dbs:
            # Exclude system databases (admin, config, local)
            client.drop_database(db_name)
            logging.info(f"Database '{db_name}' dropped successfully.")
        else:
            logging.warning(f"Database '{db_name}' does not exist.")
except Exception as e:
    logging.error(f"An error occurred: {str(e)}")
finally:
    # Close the MongoDB connection
    if 'client' in locals() and client is not None:
        client.close()
        logging.info('Closed MongoDB connection.')
