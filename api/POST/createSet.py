from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
from datetime import datetime
from typing import Optional
from fastapi import HTTPException

def createSet(
    magic: int,
    name: str,
    strategy: str,
    profit: float,
    trades: int,
    maxDrawdown: float,
    profitFactor: float,
    returnOnDrawdown: float,
    account: int,
    user: str,
    openEquity: Optional[float] = 0,
    openDrawdown: Optional[float] = 0,
    minLotSize: Optional[float] = 0,
    maxLotSize: Optional[float] = 0,
    avgLotSize: Optional[float] = 0,
    wins: Optional[int] = 0,
    losses: Optional[int] = 0,
    winRate: Optional[int] = 0,
    minTradeTime: Optional[str] = '0',
    maxTradeTime: Optional[str] = '0',
    avgTradeTime: Optional[str] = '0'
) -> dict:
    try:
        # Define the transport with the URL of your GraphQL endpoint
        transport = RequestsHTTPTransport(url='http://localhost:8321/v1/graphql')
        client = Client(transport=transport, fetch_schema_from_transport=True)

        # Get the current timestamp
        current_time = datetime.utcnow().isoformat()

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

        # Define your mutation query
        mutation = gql('''
        mutation CreateSet(
            $magic: Int!,
            $name: String!,
            $strategy: String!,
            $profit: float8!,
            $trades: Int!,
            $maxDrawdown: float8!,
            $profitFactor: float8!,
            $returnOnDrawdown: float8!,
            $account: Int!,
            $user: String!,
            $openEquity: float8!,
            $openDrawdown: float8!,
            $minLotSize: float8!,
            $maxLotSize: float8!,
            $avgLotSize: float8!,
            $wins: Int!,
            $losses: Int!,
            $winRate: Int!,
            $minTradeTime: String!,
            $maxTradeTime: String!,
            $avgTradeTime: String!
        ) {
            insert_sets_one(object: {
                magic: $magic,
                name: $name,
                strategy: $strategy,
                profit: $profit,
                trades: $trades,
                maxDrawdown: $maxDrawdown,
                profitFactor: $profitFactor,
                returnOnDrawdown: $returnOnDrawdown,
                account: $account,
                user: $user,
                openEquity: $openEquity,
                openDrawdown: $openDrawdown,
                minLotSize: $minLotSize,
                maxLotSize: $maxLotSize,
                avgLotSize: $avgLotSize,
                wins: $wins,
                losses: $losses,
                winRate: $winRate,
                minTradeTime: $minTradeTime,
                maxTradeTime: $maxTradeTime,
                avgTradeTime: $avgTradeTime
            }) {
                magic
                name
                strategy
                profit
                trades
                maxDrawdown
                profitFactor
                returnOnDrawdown
                created_at
                updated_at
                account
                user
                openEquity
                openDrawdown
                minLotSize
                maxLotSize
                avgLotSize
                wins
                losses
                winRate
                minTradeTime
                maxTradeTime
                avgTradeTime
            }
        }
        ''')

        # Define variables to be used in the mutation
        variables = {
            'magic': magic,
            'name': name,
            'strategy': strategy,
            'profit': profit,
            'trades': trades,
            'maxDrawdown': maxDrawdown,
            'profitFactor': profitFactor,
            'returnOnDrawdown': returnOnDrawdown,
            'account': account,
            'user': user,
            'openEquity': openEquity,
            'openDrawdown': openDrawdown,
            'minLotSize': minLotSize,
            'maxLotSize': maxLotSize,
            'avgLotSize': avgLotSize,
            'wins': wins,
            'losses': losses,
            'winRate': winRate,
            'minTradeTime': minTradeTime,
            'maxTradeTime': maxTradeTime,
            'avgTradeTime': avgTradeTime
        }

        # Execute the mutation
        response = client.execute(mutation, variable_values=variables)
        set_data = response['insert_sets_one']
        return {
            'set': set_data
        }

    except HTTPException as http_ex:
        # Handle specific HTTP exceptions
        raise http_ex
    except Exception as e:
        # Handle other exceptions
        raise HTTPException(status_code=500, detail=f"Error executing GraphQL mutation: {str(e)}")
