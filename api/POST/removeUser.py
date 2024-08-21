# graphql_client.py
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

def removeUser(username: str) -> dict:
     try:
          # Define the transport with the URL of your GraphQL endpoint
          transport = RequestsHTTPTransport(url='http://localhost:8321/v1/graphql')
          client = Client(transport=transport, fetch_schema_from_transport=True)

          # Define your mutation query for deleting a user
          mutation = gql('''
          mutation DeleteUser($username: String!) {
          delete_users(where: {username: {_eq: $username}}) {
               returning {
                    username
               }
          }
          }

          ''')

          # Define variables to be used in the mutation
          variables = {
               'username': username,
          }

          response = client.execute(mutation, variable_values=variables)
          return variables
     except Exception as e:
          raise Exception(f"Error executing GraphQL mutation: {e}")
