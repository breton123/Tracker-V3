from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

def checkLogin(email, username, password):
    # Define the transport and client
    transport = RequestsHTTPTransport(url='http://localhost:8321/v1/graphql', use_json=True)
    client = Client(transport=transport, fetch_schema_from_transport=True)

    # Define the query with placeholders for parameters
    query = gql('''
    query CheckUser($email: String!, $username: String!, $password: String!) {
        users(where: {
            _or: [
                {email: {_eq: $email}},
                {username: {_eq: $username}}
            ],
            password: {_eq: $password}
        }) {
            email
            type
            username
        }
    }
    ''')

    # Define the variables to pass into the query
    variables = {
        'email': email,
        'username': username,
        'password': password
    }

    try:
        # Execute the query with the variables
        result = client.execute(query, variable_values=variables)
        print(result)
        return result["users"][0]
    except Exception as e:
        #print(f"An error occurred: {e}")
        return None

