from flask import Flask, jsonify
from src.components.data_ignestion import read_data
import pandas as pd
from src.components.data_transformation import transform_data
from src.components.data_load import load_data_to_db
from src.api.analysis_data.get_sales_data import (
    get_total_record_count,
    get_total_sales_by_region,
    get_avg_sales_per_transaction,
    check_no_duplicate_order_ids
)

app = Flask(__name__)

@app.route('/process_data', methods=['POST'])
def process_data():
    # Step 1: Ingest Data
    df_region_a = read_data("order_region_a.csv")
    df_region_b = read_data("order_region_b.csv")

    # Step 2: Transform Data
    df_region_a = transform_data(df_region_a, region='A')
    df_region_b = transform_data(df_region_b, region='B')

    # Step 3: Combine Data and Load to Database
    combined_df = pd.concat([df_region_a, df_region_b], ignore_index=True)
    print(combined_df.head())


    print(combined_df.shape)

    load_data_to_db(combined_df.iloc[:2])

    # Step 4: Run Analysis
    results = {
        "total_records": get_total_record_count(),
        "total_sales_by_region": get_total_sales_by_region(),
        "average_sales_per_transaction": get_avg_sales_per_transaction(),
        "no_duplicate_order_ids": check_no_duplicate_order_ids()
    }

    # Return JSON response
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
