from datetime import datetime
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from dateutil import parser

def getSnapshotsWithMagic(magic: int, account: int, user: str):
    # Create a transport instance for the GraphQL server
    transport = RequestsHTTPTransport(url='http://localhost:8321/v1/graphql', use_json=True)
    # Create a GraphQL client using the transport
    client = Client(transport=transport, fetch_schema_from_transport=True)

    # Define the query with placeholders for variables
    query = gql('''
    query ($set: Int!, $account: Int!, $user: String!) {
        snapshots(where: {set: {_eq: $set}, account: {_eq: $account}, user: {_eq: $user}}) {
            time
            set
            account
            user
            totalProfit
            openProfit
            drawdown
        }
    }
    ''')

    # Define the variables for the query
    variables = {
        'set': magic,
        'account': account,
        'user': user
    }

    # Execute the query with the variables
    try:
        result = client.execute(query, variable_values=variables)
        return result
    except Exception as e:
        # Handle exceptions, e.g., connection errors or query issues
        raise Exception(f"Error executing GraphQL query: {str(e)}")

def getSnapshots(account: int, user: str):
    # Create a transport instance for the GraphQL server
    transport = RequestsHTTPTransport(url='http://localhost:8321/v1/graphql', use_json=True)
    # Create a GraphQL client using the transport
    client = Client(transport=transport, fetch_schema_from_transport=True)

    # Define the query with placeholders for variables
    query = gql('''
    query ($account: Int!, $user: String!) {
        snapshots(where: {account: {_eq: $account}, user: {_eq: $user}}) {
            time
            set
            account
            user
            totalProfit
            openProfit
            drawdown
        }
    }
    ''')


    # Define the variables for the query
    variables = {
        'account': account,
        'user': user
    }

    # Execute the query with the variables
    try:
        result = client.execute(query, variable_values=variables)
        return result
    except Exception as e:
        # Handle exceptions, e.g., connection errors or query issues
        raise Exception(f"Error executing GraphQL query: {str(e)}")

def getSnapshotsGraph(account: int, user: str):
     # Create a transport instance for the GraphQL server
     transport = RequestsHTTPTransport(url='http://localhost:8321/v1/graphql', use_json=True)
     # Create a GraphQL client using the transport
     client = Client(transport=transport, fetch_schema_from_transport=True)

     # Define the query with placeholders for variables
     query = gql('''
     query ($account: Int!, $user: String!) {
          snapshots(where: {account: {_eq: $account}, user: {_eq: $user}}) {
               time
               set
               account
               user
               totalProfit
               openProfit
               drawdown
          }
     }
     ''')


     # Define the variables for the query
     variables = {
          'account': account,
          'user': user
     }


     # Execute the query with the variables
     try:
          result = client.execute(query, variable_values=variables)
          drawdownGraph = {}
          equityGraph = {}
          magics = []
          for snapshot in result["snapshots"]:
               time = snapshot["time"]
               time = parser.isoparse(time)
               time = time.strftime('%Y-%m-%d %H:%M:%S')
               drawdown = snapshot["drawdown"]
               equity = snapshot["totalProfit"] + snapshot["openProfit"]
               magic = str(snapshot["set"])
               if magic not in magics:
                    magics.append(magic)
               try:
                    drawdownGraph[time][str(magic)] = drawdown
                    equityGraph[time][str(magic)] = equity
               except:
                    drawdownTemp = {
                         "time": time,
                         str(magic): drawdown
                    }
                    equityTemp = {
                         "time": time,
                         str(magic): equity
                    }
                    drawdownGraph[time] = drawdownTemp
                    equityGraph[time] = equityTemp

          drawdownData = []
          equityData = []
          for key in drawdownGraph:
               drawdownData.append(drawdownGraph[key])
          for key in equityGraph:
               equityData.append(equityGraph[key])

          return drawdownData, equityData, magics
     except Exception as e:
          # Handle exceptions, e.g., connection errors or query issues
          raise Exception(f"Error executing GraphQL query: {str(e)}")

getSnapshotsGraph(7451935, "breton123")