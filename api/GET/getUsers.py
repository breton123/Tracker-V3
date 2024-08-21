from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


def getUsers():
     transport = RequestsHTTPTransport(url='http://localhost:8321/v1/graphql', use_json=True)
     client = Client(transport=transport, fetch_schema_from_transport=True)
     query = gql('''
     query {
          users {
          username
          email
          type
          }
     }
     ''')

     # Execute the query
     result = client.execute(query)

     return result