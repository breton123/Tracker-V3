import asyncio
import base64
import os
import websockets
import json
from database.getAccount import getAccount
from scripts.getPreviousProfile import getPreviousProfile
from scripts.getProfileSets import getProfileSets
from scripts.getProfiles import getDataPath
from scripts.getProfiles import getProfiles
from scripts.loadSets import loadSets

user = "breton123"

async def listen_to_server():
    uri = "ws://127.0.0.1:8000/ws"
    username = "breton123"  # Replace with the actual username

    while True:
        try:
            async with websockets.connect(uri) as websocket:
                # Send the username as the first message
                await websocket.send(json.dumps({
                    "type": "connect",
                    "username": username,
                    "source": "controller"
                }))

                while True:
                    response_text = await websocket.recv()
                    response = json.loads(response_text)

                    if response.get("message") == "Set Data":
                        account = response.get("account")
                        terminalFilePath = getAccount(user, account)["terminalFilePath"]

                        if response.get("newData"):
                            terminalConfigPath = os.path.join(
                                getDataPath(terminalFilePath), "config", "common.ini"
                            )
                            profileLast = getPreviousProfile(terminalConfigPath)
                            profileSets = getProfileSets(terminalFilePath, profileLast)
                            profiles = getProfiles(terminalFilePath)
                            print(profileSets)
                            await websocket.send(json.dumps({
                                "message": "Set Data",
                                "username": username,
                                "source": "controller",
                                "previousProfile": profileLast,
                                "profiles": profiles,
                                "profileSets": profileSets
                            }))

                        else:
                            profiles = getProfiles(terminalFilePath)

                            if response.get("profile") in profiles:
                                profileLast = response.get("profile")
                                profileSets = getProfileSets(terminalFilePath, profileLast)
                            else:
                                profileLast = getPreviousProfile(terminalConfigPath)
                                profileSets = getProfileSets(terminalFilePath, profileLast)
                            await websocket.send(json.dumps({
                                "message": "Set Data",
                                "username": username,
                                "source": "controller",
                                "previousProfile": profileLast,
                                "profiles": profiles,
                                "profileSets": profileSets
                            }))
                    if response.get("type") == "upload":
                         files = response.get("files", [])
                         account = response.get("account")
                         profile = response.get("profile")
                         apiKey = response.get("apiKey")
                         expertName = response.get("expertName")
                         symbolSuffix = response.get("symbolSuffix")
                         terminalFilePath = getAccount(user, account)["terminalFilePath"]
                         loadSets(account, profile, terminalFilePath, files, apiKey, expertName, symbolSuffix, username)
                    else:
                         print(f"Received from server: {response}")

        except websockets.ConnectionClosedError as e:
            print(f"Connection closed: {e}. Reconnecting in 5 seconds...")
            await asyncio.sleep(5)  # Wait for 5 seconds before retrying

        except Exception as e:
            print(f"An error occurred: {e}. Reconnecting in 5 seconds...")
            await asyncio.sleep(5)  # Handle unexpected errors and retry
