def transform_data(df, region):
    """Transform data according to business rules and add necessary columns."""
    # Remove hyphens from OrderId and keep it as a string (or you can convert it to BIGINT if required)
    df['OrderId'] = df['OrderId'].str.replace('-', '')

    # Add 'total_sales' column
    df['total_sales'] = df['QuantityOrdered'] * df['ItemPrice']

    # Add 'region' column
    df['region'] = region

    # Calculate 'net_sale'
    df['PromotionDiscount'] = df['PromotionDiscount'].apply(lambda x: float(eval(x).get("Amount", 0)))
    df['net_sale'] = df['total_sales'] - df['PromotionDiscount']

    # Remove duplicates based on 'OrderId'
    df.drop_duplicates(subset=['OrderId'], keep='first', inplace=True)

    # Exclude orders with non-positive net_sales
    df = df[df['net_sale'] > 0]

    return df
