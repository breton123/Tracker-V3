from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


def getAccounts(user):
     transport = RequestsHTTPTransport(url='http://localhost:8321/v1/graphql', use_json=True)
     client = Client(transport=transport, fetch_schema_from_transport=True)
     query = gql('''
     query {
     accounts(where: {user: {_eq: "'''+user+'''"}}) {
     enabled
     login
     name
     server
     terminalFilePath
     user
     password
     deposit
     }
}
     ''')

     # Execute the query
     result = client.execute(query)

     return result