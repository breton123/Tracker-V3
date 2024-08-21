import asyncio
from scripts.tasksSocket import listen_to_server

def run_async_code():
     # Create a new event loop for this thread
     loop = asyncio.new_event_loop()
     asyncio.set_event_loop(loop)

     # Run the async function
     loop.run_until_complete(listen_to_server())

run_async_code()
