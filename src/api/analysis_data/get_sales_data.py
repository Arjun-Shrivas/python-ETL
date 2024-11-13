from sqlalchemy import text
from src.config import get_session

def get_total_record_count():
    """
    Get the total number of records in the sales_data table.
    """
    session = get_session()
    try:
        # Wrap the query in text() to avoid the ArgumentError
        result = session.execute(text("SELECT COUNT(*) FROM sales_data"))
        return result.scalar()  # Extract the scalar value from the result
    except Exception as e:
        print(f"Error getting total record count: {e}")
        return None
    finally:
        session.close()

def get_total_sales_by_region():
    """
    Get the total sales by region.
    """
    session = get_session()
    try:
        # Wrap the query in text() to avoid the ArgumentError
        result = session.execute(text("SELECT region, SUM(total_sales) FROM sales_data GROUP BY region")).all()
        return {region: sales for region, sales in result}
    except Exception as e:
        print(f"Error getting total sales by region: {e}")
        return None
    finally:
        session.close()

def get_avg_sales_per_transaction():
    """
    Get the average sales amount per transaction.
    """
    session = get_session()
    try:
        # Wrap the query in text() to avoid the ArgumentError
        result = session.execute(text("SELECT AVG(total_sales) FROM sales_data"))
        return result.scalar()  # Extract the scalar value (average)
    except Exception as e:
        print(f"Error getting average sales per transaction: {e}")
        return None
    finally:
        session.close()

def check_no_duplicate_order_ids():
    """
    Check if there are any duplicate OrderIds in the sales_data table.
    """
    session = get_session()
    try:
        # Wrap the query in text() to avoid the ArgumentError
        duplicate_count = session.execute(text("SELECT COUNT(OrderId) - COUNT(DISTINCT OrderId) FROM sales_data")).scalar()
        return duplicate_count == 0  # Returns True if no duplicates, False if duplicates exist
    except Exception as e:
        print(f"Error checking for duplicate OrderIds: {e}")
        return None
    finally:
        session.close()
