from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
from datetime import datetime
from typing import Optional
from fastapi import HTTPException

def createSnapshot(
    magic: int,  # Corresponds to 'set' in the snapshot table
    account: int,
    user: str,
    current_time: str, # Corresponds to 'current
    totalProfit: float,
    openProfit: Optional[float] = 0.0,
    drawdown: Optional[float] = 0.0
) -> dict:
    try:
        # Define the transport with the URL of your GraphQL endpoint
        transport = RequestsHTTPTransport(url='http://localhost:8321/v1/graphql')
        client = Client(transport=transport, fetch_schema_from_transport=True)

        # Get the current timestamp
        # = current_time.isoformat()

        # Check if the user and account exist
        check_existence_query = gql('''
        query CheckUserAndAccount($user: String!, $account: Int!) {
            users(where: {username: {_eq: $user}}) {
                username
            }
            accounts(where: {login: {_eq: $account}}) {
                login
            }
        }
        ''')

        existence_vars = {
            'user': user,
            'account': account
        }

        existence_response = client.execute(check_existence_query, variable_values=existence_vars)
        user_exists = len(existence_response['users']) > 0
        account_exists = len(existence_response['accounts']) > 0

        if not user_exists or not account_exists:
            raise HTTPException(status_code=404, detail="User or Account does not exist")

        # Define your mutation query for snapshot
        mutation = gql('''
        mutation CreateSnapshot(
            $time: timestamptz!,
            $set: Int!,
            $account: Int!,
            $user: String!,
            $totalProfit: float8!,
            $openProfit: float8!,
            $drawdown: float8!
        ) {
            insert_snapshots_one(object: {
                time: $time,
                set: $set,
                account: $account,
                user: $user,
                totalProfit: $totalProfit,
                openProfit: $openProfit,
                drawdown: $drawdown
            }) {
                time
                set
                account
                user
                totalProfit
                openProfit
                drawdown
            }
        }
        ''')

        # Define variables to be used in the mutation
        variables = {
            'time': current_time,
            'set': magic,  # Mapping 'set_id' to 'set'
            'account': account,
            'user': user,
            'totalProfit': totalProfit,
            'openProfit': openProfit,
            'drawdown': drawdown
        }

        # Execute the mutation
        response = client.execute(mutation, variable_values=variables)
        snapshot_data = response['insert_snapshots_one']
        return {
            'snapshot': snapshot_data
        }

    except HTTPException as http_ex:
        # Handle specific HTTP exceptions
        raise http_ex
    except Exception as e:
        # Handle other exceptions
        raise HTTPException(status_code=500, detail=f"Error executing GraphQL mutation: {str(e)}")

#createSnapshot(1932, 7451935, "breton123", str(datetime.now()), 600, 200, -230)