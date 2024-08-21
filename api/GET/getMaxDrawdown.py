from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

def getMaxDrawdown(user: str, account: int, magic: int):
    # Create a transport instance for the GraphQL server
    transport = RequestsHTTPTransport(url='http://localhost:8321/v1/graphql', use_json=True)
    # Create a GraphQL client using the transport
    client = Client(transport=transport, fetch_schema_from_transport=True)

    # Define the query with placeholders for variables
    query = gql('''
    query ($user: String!, $account: Int!, $magic: Int!) {
        sets(where: {user: {_eq: $user}, account: {_eq: $account}, magic: {_eq: $magic}}) {
            maxDrawdown
        }
    }
    ''')

    # Define the variables for the query
    variables = {
        'user': user,
        'magic': magic,
        'account': account
    }

    # Execute the query with the variables
    result = client.execute(query, variable_values=variables)

    return result

