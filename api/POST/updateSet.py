from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
from typing import Optional
from fastapi import HTTPException

def updateSet(
    magic: int,
    account: int,
    user: str,
    name: Optional[str] = None,
    strategy: Optional[str] = None,
    profit: Optional[float] = None,
    trades: Optional[int] = None,
    maxDrawdown: Optional[float] = None,
    profitFactor: Optional[float] = None,
    returnOnDrawdown: Optional[float] = None,
    openEquity: Optional[float] = None,
    openDrawdown: Optional[float] = None,
    minLotSize: Optional[float] = None,
    maxLotSize: Optional[float] = None,
    avgLotSize: Optional[float] = None,
    wins: Optional[int] = None,
    losses: Optional[int] = None,
    winRate: Optional[int] = None,
    minTradeTime: Optional[str] = None,
    maxTradeTime: Optional[str] = None,
    avgTradeTime: Optional[str] = None
) -> dict:
    try:
        # Define the transport with the URL of your GraphQL endpoint
        transport = RequestsHTTPTransport(url='http://localhost:8321/v1/graphql')
        client = Client(transport=transport, fetch_schema_from_transport=True)

        # Check if the set with the provided magic, account, and user exists
        check_existence_query = gql('''
        query CheckSetExists($magic: Int!, $account: Int!, $user: String!) {
            sets(where: {magic: {_eq: $magic}, account: {_eq: $account}, user: {_eq: $user}}) {
                magic
                account
                user
            }
        }
        ''')

        existence_vars = {
            'magic': magic,
            'account': account,
            'user': user
        }

        existence_response = client.execute(check_existence_query, variable_values=existence_vars)
        set_exists = len(existence_response['sets']) > 0

        if not set_exists:
            raise HTTPException(status_code=404, detail="Set with the provided identifiers does not exist")

        # Define your update mutation query
        mutation = gql('''
        mutation UpdateSet(
            $magic: Int!,
            $account: Int!,
            $user: String!,
            $name: String,
            $strategy: String,
            $profit: float8,
            $trades: Int,
            $maxDrawdown: float8,
            $profitFactor: float8,
            $returnOnDrawdown: float8,
            $openEquity: float8,
            $openDrawdown: float8,
            $minLotSize: float8,
            $maxLotSize: float8,
            $avgLotSize: float8,
            $wins: Int,
            $losses: Int,
            $winRate: Int,
            $minTradeTime: String,
            $maxTradeTime: String,
            $avgTradeTime: String
        ) {
            update_sets(
                where: {magic: {_eq: $magic}, account: {_eq: $account}, user: {_eq: $user}},
                _set: {
                    name: $name,
                    strategy: $strategy,
                    profit: $profit,
                    trades: $trades,
                    maxDrawdown: $maxDrawdown,
                    profitFactor: $profitFactor,
                    returnOnDrawdown: $returnOnDrawdown,
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
                }
            ) {
                returning {
                    magic
                    account
                    user
                    name
                    strategy
                    profit
                    trades
                    maxDrawdown
                    profitFactor
                    returnOnDrawdown
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
                    created_at
                    updated_at
                }
            }
        }
        ''')

        # Define variables to be used in the mutation
        variables = {
            'magic': magic,
            'account': account,
            'user': user,
            'name': name,
            'strategy': strategy,
            'profit': profit,
            'trades': trades,
            'maxDrawdown': maxDrawdown,
            'profitFactor': profitFactor,
            'returnOnDrawdown': returnOnDrawdown,
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

        # Remove keys with None values
        variables = {k: v for k, v in variables.items() if v is not None}

        # Execute the mutation
        response = client.execute(mutation, variable_values=variables)
        updated_set = response['update_sets']['returning'][0]
        return {
            'set': updated_set
        }

    except HTTPException as http_ex:
        # Handle specific HTTP exceptions
        raise http_ex
    except Exception as e:
        # Handle other exceptions
        raise HTTPException(status_code=500, detail=f"Error executing GraphQL mutation: {str(e)}")

# Example call to the function
print(updateSet(
    magic=1798,
    account=7451935,
    user='breton123',
    name='Updated Again',  # If you want to update the name
    strategy='Updated Strategy',
    profit=43.5,
    trades=2,
    maxDrawdown=0.0,
    profitFactor=0.0,
    returnOnDrawdown=0.0,
    openEquity=0.0,
    openDrawdown=0.0,
    minLotSize=0.31,
    maxLotSize=0.31,
    avgLotSize=0.31,
    wins=2,
    losses=0,
    winRate=100,
    minTradeTime='01:05:08',
    maxTradeTime='05:32:12',
    avgTradeTime='03:18:40'
))
