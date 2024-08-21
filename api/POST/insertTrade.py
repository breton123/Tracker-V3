from datetime import datetime
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
from fastapi import HTTPException

def insertTrade(trade_data):
    try:
        # Define the transport with the URL of your GraphQL endpoint
        transport = RequestsHTTPTransport(url='http://localhost:8321/v1/graphql')
        client = Client(transport=transport, fetch_schema_from_transport=True)

        # Define the mutation query
        mutation = gql('''
        mutation InsertTrade(
            $id: Int!,
            $entryTime: String!,
            $exitTime: String!,
            $holdTime: String!,
            $symbol: String!,
            $direction: String!,
            $profit: float8!,
            $volume: float8!,
            $account: Int!,
            $user: String!,
            $set: Int!,
            $entryPrice: float8!,
            $exitPrice: float8!
        ) {
            insert_trades_one(object: {
                id: $id,
                entryTime: $entryTime,
                exitTime: $exitTime,
                holdTime: $holdTime,
                symbol: $symbol,
                direction: $direction,
                profit: $profit,
                volume: $volume,
                account: $account,
                user: $user,
                set: $set,
                entryPrice: $entryPrice,
                exitPrice: $exitPrice
            }) {
                id
                entryTime
                exitTime
                holdTime
                symbol
                direction
                profit
                volume
                account
                user
                set
                entryPrice
                exitPrice
            }
        }
        ''')

        # Prepare variables for the mutation
        variables = {
            'id': int(trade_data['id']),
            'entryTime': str(trade_data['entryTime']),
            'exitTime': str(trade_data['exitTime']),
            'entryPrice': float(trade_data['entryPrice']),
            'exitPrice': float(trade_data['exitPrice']),
            'holdTime': str(trade_data['holdTime']),  # Hold time should be in a string format that matches the DB's time format
            'symbol': str(trade_data['symbol']),
            'direction': str(trade_data['direction']),  # Assuming 'orderType' is 'direction'
            'profit': float(trade_data['profit']),
            'volume': float(trade_data['volume']),
            'account': int(trade_data['account']),  # Assuming 'account' is provided directly
            'user': str(trade_data['user']),  # The user is now provided directly in the trade_data
            'set': int(trade_data['set']),  # Assuming 'set' is provided directly
        }

        # Execute the mutation
        response = client.execute(mutation, variable_values=variables)
        return response['insert_trades_one']

    except HTTPException as http_ex:
        raise http_ex
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error executing GraphQL mutation: {str(e)}")
