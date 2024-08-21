from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

def doesTradeExist(magic: int, account: int, user: str, id: int) -> bool:
    try:
        # Define the transport with the URL of your GraphQL endpoint
        transport = RequestsHTTPTransport(url='http://localhost:8321/v1/graphql')
        client = Client(transport=transport, fetch_schema_from_transport=True)

        # Define your query for checking if the set exists
        query = gql('''
        query CheckTradeExistence($magic: Int!, $account: Int!, $user: String!, $id: Int!) {
            trades(where: {set: {_eq: $magic}, account: {_eq: $account}, user: {_eq: $user}, id: {_eq: $id}}) {
                id
            }
        }
        ''')

        # Define variables to be used in the query
        variables = {
            'magic': magic,
            'account': account,
            'user': user,
            'id': id
        }

        # Execute the query
        response = client.execute(query, variable_values=variables)
        return len(response['trades']) > 0

    except Exception as e:
        raise Exception(f"Error executing GraphQL query: {e}")
