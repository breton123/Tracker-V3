from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
from datetime import datetime
from fastapi import HTTPException

def createUser(magic: int, name: str, strategy: str, profit: float, trades: int, maxDrawdown: float, profitFactor: float, returnOnDrawdown: float, account: int, user: str) -> dict:
    try:
        # Define the transport with the URL of your GraphQL endpoint
        transport = RequestsHTTPTransport(url='http://localhost:8321/v1/graphql')
        client = Client(transport=transport, fetch_schema_from_transport=True)

        # Get the current timestamp
        current_time = datetime.utcnow().isoformat()

        # Check if the user and account exist
        check_existence_query = gql('''
        query CheckUserAndAccount($user: String!, $account: Int!) {
            users(where: {username: {_eq: $user}}) {
                username
            }
            accounts(where: {login: {_eq: $account}}) {
                login
            }
        }
        ''')

        existence_vars = {
            'user': user,
            'account': account
        }

        existence_response = client.execute(check_existence_query, variable_values=existence_vars)
        user_exists = len(existence_response['users']) > 0
        account_exists = len(existence_response['accounts']) > 0

        if not user_exists or not account_exists:
            raise Exception("User or Account does not exist")

        # Define your mutation query
        mutation = gql('''
        mutation CreateSetAndAddTask(
            $magic: Int!,
            $name: String!,
            $strategy: String!,
            $profit: float8!,
            $trades: Int!,
            $maxDrawdown: float8!,
            $profitFactor: float8!,
            $returnOnDrawdown: float8!,
            $account: Int!,
            $user: String!,
            $time: timestamptz!,
            $task: String!
        ) {
            insert_sets_one(object: {
                magic: $magic,
                name: $name,
                strategy: $strategy,
                profit: $profit,
                trades: $trades,
                maxDrawdown: $maxDrawdown,
                profitFactor: $profitFactor,
                returnOnDrawdown: $returnOnDrawdown,
                account: $account,
                user: $user
            }) {
                magic
                name
                strategy
                profit
                trades
                maxDrawdown
                profitFactor
                returnOnDrawdown
                created_at
                updated_at
            }

            insert_tasks_one(object: {
                time: $time,
                user: $user,
                account: $account,
                magic: $magic,
                task: $task
            }) {
                time
                user
                account
                magic
                task
            }
        }
        ''')

        # Define variables to be used in the mutation
        variables = {
            'magic': magic,
            'name': name,
            'strategy': strategy,
            'profit': profit,
            'trades': trades,
            'maxDrawdown': maxDrawdown,
            'profitFactor': profitFactor,
            'returnOnDrawdown': returnOnDrawdown,
            'account': account,
            'user': user,
            'time': current_time,
            'task': 'Create Set'
        }

        # Execute the mutation
        response = client.execute(mutation, variable_values=variables)
        set_data = response['insert_sets_one']
        return {
            'set': set_data,
            'task': response['insert_tasks_one']
        }

    except Exception as e:
        raise Exception(f"Error executing GraphQL mutation: {e}")

