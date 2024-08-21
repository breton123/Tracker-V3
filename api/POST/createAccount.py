# graphql_client.py
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

def createAccount(login: str, password: str, server: str, deposit: int, user: str, name: str, terminalFilePath: str) -> dict:
    try:
        # Define the transport with the URL of your GraphQL endpoint
        transport = RequestsHTTPTransport(url='http://localhost:8321/v1/graphql')
        client = Client(transport=transport, fetch_schema_from_transport=True)

        # Define your mutation query
        mutation = gql('''
        mutation InsertAccount($login: Int!, $password: String!, $server: String!, $deposit: Int!, $user: String!, $name: String!, $enabled: Boolean!, $terminalFilePath: String!) {
            insert_accounts_one(object: {login: $login, password: $password, server: $server, deposit: $deposit, user: $user, name: $name, enabled: $enabled terminalFilePath: $terminalFilePath}) {
                login
                password
                server
                deposit
                user
                name
                enabled
                terminalFilePath
            }
        }
        ''')

        # Define variables to be used in the mutation
        variables = {
            "login": login,
            "password": password,
            "server": server,
            "deposit": deposit,
            "user": user,
            "name": name,
            "enabled": False,
            "terminalFilePath": terminalFilePath
            # or whatever default value you want
        }

        # Execute the mutation
        response = client.execute(mutation, variable_values=variables)
        return response["insert_accounts_one"]

    except Exception as e:
        raise Exception(f"Error executing GraphQL mutation: {e}")
