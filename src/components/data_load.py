from sqlalchemy import MetaData, Table, Column, String, Integer, Float, JSON, text
from sqlalchemy import inspect
from src.config import get_db_engine, get_session


def create_table_if_not_exists(engine, table_name):
    """Create table in MySQL if not exists."""
    metadata = MetaData()
    sales_data_table = Table(table_name, metadata,
                             Column('OrderId', String(255), primary_key=True),
                             Column('OrderItemId', Float),
                             Column('QuantityOrdered', Integer),
                             Column('ItemPrice', Float),
                             Column('PromotionDiscount', JSON),
                             Column('batch_id', Integer),
                             Column('total_sales', Float),
                             Column('region', String(1)),
                             Column('net_sale', Float)
                             )

    # Use inspect to check if table exists
    inspector = inspect(engine)
    if not inspector.has_table(table_name):
        sales_data_table.create(engine)
        print(f"Table {table_name} created.")
    else:
        print(f"Table {table_name} already exists.")


def load_data_to_db(df, table_name='sales_data'):
    """Load DataFrame into MySQL, replace if table exists."""
    engine = get_db_engine()

    if engine:
        # Create table if it doesn't exist
        create_table_if_not_exists(engine, table_name)

        # Insert data into the table
        try:
            # Create session
            session = get_session()

            print(df.head())
            # Insert data row by row (or use bulk insert if needed)
            for _, row in df.iterrows():

                query = text(f""" INSERT INTO {table_name} (OrderId, OrderItemId, QuantityOrdered, ItemPrice, 
                                    PromotionDiscount, batch_id, total_sales, region, net_sale)
                                    VALUES ('{row['OrderId']}', {row['OrderItemId']}, {row['QuantityOrdered']}, {row['ItemPrice']}, 
                                    '{row['PromotionDiscount']}', {row['batch_id']}, {row['total_sales']}, '{row['region']}', {row['net_sale']})
                                """)
                print("Executing query:", query)  # Log the query
                # Execute the query with the row values
                session.execute(query, {
                    'OrderId': row['OrderId'],
                    'OrderItemId': row['OrderItemId'],
                    'QuantityOrdered': row['QuantityOrdered'],
                    'ItemPrice': row['ItemPrice'],
                    'PromotionDiscount': row['PromotionDiscount'],
                    'batch_id': row['batch_id'],
                    'total_sales': row['total_sales'],
                    'region': row['region'],
                    'net_sale': row['net_sale']
                })
            # Commit changes
            session.commit()
            print(f"Data loaded into {table_name}.")

        except Exception as e:
            print(f"Error loading data: {e}")
            session.rollback()
        finally:
            session.close()
