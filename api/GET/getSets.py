from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

def getSets(user: str, account: int):
    # Create a transport instance for the GraphQL server
    transport = RequestsHTTPTransport(url='http://localhost:8321/v1/graphql', use_json=True)
    # Create a GraphQL client using the transport
    client = Client(transport=transport, fetch_schema_from_transport=True)

    # Define the query with placeholders for variables
    query = gql('''
    query ($user: String!, $account: Int!) {
        sets(where: {user: {_eq: $user}, account: {_eq: $account}}) {
            magic
            name
            strategy
            profit
            maxDrawdown
            profitFactor
            returnOnDrawdown
            minLotSize
            maxLotSize
            avgLotSize
            wins
            losses
            winRate
            minTradeTime
            maxTradeTime
            avgTradeTime
            trades
            openEquity
            openDrawdown


        }
    }
    ''')

    # Define the variables for the query
    variables = {
        'user': user,
        'account': account
    }

    # Execute the query with the variables
    result = client.execute(query, variable_values=variables)

    return result

