from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

def getAccount(user: str, login: int):
    # Create a transport instance for the GraphQL server
    transport = RequestsHTTPTransport(url='http://localhost:8321/v1/graphql', use_json=True)
    # Create a GraphQL client using the transport
    client = Client(transport=transport, fetch_schema_from_transport=True)

    # Define the query with placeholders for variables
    query = gql('''
    query ($user: String!, $login: Int!) {
        accounts(where: {user: {_eq: $user}, login: {_eq: $login}}) {
            login
            password
            name
            server
            deposit
            enabled
            user
            terminalFilePath

        }
    }
    ''')

    # Define the variables for the query
    variables = {
        'user': user,
        'login': login
    }

    # Execute the query with the variables
    result = client.execute(query, variable_values=variables)["accounts"][0]

    return result

