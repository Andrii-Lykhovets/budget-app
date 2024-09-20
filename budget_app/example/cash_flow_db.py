import mysql.connector
from pprint import pprint

DB_CONFIG = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': '',
        'database': 'cash_flow',
    }


def get_all_transaction_records():
    """
    1. DB config must be known (/)
    2. Connect to DB
        import mysql.connector (/)
    3. Initiate cursor
    4. use cursor to execute MySQL queries
    5. Close DB connection !!!  (/)
    """

    all_transactions = []
    query = """
    SELECT id, income, expenditure, date_time, description, company_id
      FROM transaction;
    """

    connection = mysql.connector.connect(**DB_CONFIG)
    
    with connection.cursor(dictionary=True) as cursor:
        cursor.execute(query)
        all_transactions = cursor.fetchall()
    
    connection.close()
    return all_transactions


def insert_new_transaction_record(data_transaction):
    cnx = mysql.connector.connect(**DB_CONFIG)
    cursor = cnx.cursor()

    add_transaction = ("INSERT INTO transaction "
                       "(income, expenditure, description, date_time, company_id) "
                       "VALUES (%(income)s, %(expenditure)s, %(description)s, %(date_time)s, %(company_id)s)")

    cursor.execute(add_transaction, data_transaction)

    cnx.commit()

    cursor.close()
    cnx.close()


if __name__ == '__main__':
    get_all_transaction_records()
    # insert_new_transaction_record()
