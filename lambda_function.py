import pandas as pd

def lambda_handler(event, context):
    d = {'col1': [1,2], 'col2': [3,4]}
    df = pd.DataFrame(data=d)
    print(df)
    print(('Done x1.1'))
    # This is a simple AWS Lambda function that returns a greeting message.
    #return {
    #    'statusCode': 200,
    #    'body': 'Hello from AWS Lambda!'
    #}