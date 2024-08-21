# graphql_client.py
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

def removeAccount(login: int, username: str) -> dict:
     try:
          # Define the transport with the URL of your GraphQL endpoint
          transport = RequestsHTTPTransport(url='http://localhost:8321/v1/graphql')
          client = Client(transport=transport, fetch_schema_from_transport=True)

          # Define your mutation query for deleting an account
          mutation = gql('''
          mutation DeleteAccount($login: Int!, $username: String!) {
               delete_accounts(where: {login: {_eq: $login}, user: {_eq: $username}}) {
                    returning {
                    login
                    }
               }
          }
          ''')

          # Define variables to be used in the mutation
          variables = {
               'login': login,
               'username': username
          }

          # Execute the mutation
          response = client.execute(mutation, variable_values=variables)
          if len(response["delete_accounts"]["returning"]) > 0:
               return response["delete_accounts"]["returning"][0]
          else:
               return {"login": 9999, "username": "Account Doesnt Exist"}

     except Exception as e:
          raise Exception(f"Error executing GraphQL mutation: {e}")
