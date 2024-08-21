from datetime import datetime
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
from fastapi import HTTPException

def removeSet(magic: int, account: int, user: str) -> dict:
    try:
        # Define the transport with the URL of your GraphQL endpoint
        transport = RequestsHTTPTransport(url='http://localhost:8321/v1/graphql')
        client = Client(transport=transport, fetch_schema_from_transport=True)

        # Define your mutation query
        mutation = gql('''
        mutation DeleteSetAndAddTask(
            $magic: Int!,
            $account: Int!,
            $user: String!,
            $task: String!
        ) {
            # Delete the set
            delete_sets(where: {magic: {_eq: $magic}, account: {_eq: $account}, user: {_eq: $user}}) {
                returning {
                    magic
                    name
                    strategy
                    profit
                    trades
                    maxDrawdown
                    profitFactor
                    returnOnDrawdown
                    updated_at
                }
            }

            # Insert a new task
            insert_tasks_one(object: {
                user: $user,
                account: $account,
                magic: $magic,
                task: $task,
                completed: false
            }) {
                id
                user
                account
                magic
                task
                completed
                created_at
            }
        }
        ''')

        # Define variables to be used in the mutation
        variables = {
            'magic': magic,
            'account': account,
            'user': user,
            'task': "removeSet"  # Default task description
        }

        # Execute the mutation
        response = client.execute(mutation, variable_values=variables)

        # Check if the set was deleted successfully and get the new task
        deleted_set = response.get('delete_sets', {}).get('returning', [{}])[0]
        new_task = response.get('insert_tasks_one', {})

        return {
            'deleted_set': deleted_set,
            'new_task': new_task
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error executing GraphQL mutation: {e}")
