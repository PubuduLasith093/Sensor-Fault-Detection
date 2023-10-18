from sensor.configuration.mogo_db_connection import MongoDBClient

if __name__ == '__main__':
    mongodb_client = MongoDBClient()
    print('pubudu')
    print(mongodb_client.database.list_collection_names())