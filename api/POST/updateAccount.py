# graphql_client.py
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

def updateAccount(login: int, user: str, password: str, name: str, server: str, deposit: int, enabled: bool) -> dict:
     try:
          # Define the transport with the URL of your GraphQL endpoint
          transport = RequestsHTTPTransport(url='http://localhost:8321/v1/graphql')
          client = Client(transport=transport, fetch_schema_from_transport=True)

          # Define your mutation query for updating an account
          mutation = gql('''
          mutation UpdateAccount($login: Int!, $user: String!, $password: String, $name: String, $server: String, $deposit: Int, $enabled: Boolean) {
               update_accounts(where: {login: {_eq: $login}, user: {_eq: $user}}, _set: {password: $password, name: $name, server: $server, deposit: $deposit, enabled: $enabled}) {
                    returning {
                    login
                    user
                    password
                    name
                    server
                    deposit
                    enabled
                    }
               }
          }
          ''')

          # Define variables to be used in the mutation
          variables = {
               'login': login,
               'user': user,
               'password': password,
               'name': name,
               'server': server,
               'deposit': deposit,
               'enabled': enabled
          }

          # Execute the mutation
          response = client.execute(mutation, variable_values=variables)
          return response['update_accounts']['returning'][0]

     except Exception as e:
          raise Exception(f"Error executing GraphQL mutation: {e}")
