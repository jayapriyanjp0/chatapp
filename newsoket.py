import asyncio
import websockets

connected_users = set()

async def handle_client(websocket):
    print("New user connected")
    connected_users.add(websocket)

    # Send welcome message to the new user
    await websocket.send("Welcome! You are connected to the chat server.")

    try:
        async for message in websocket:
            print(f"Received: {message}")

            # Broadcast to all connected clients
            for user in connected_users:
                if user != websocket:
                    await user.send(message)

    except websockets.exceptions.ConnectionClosedOK:
        print("Client disconnected normally.")
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        connected_users.remove(websocket)
        print("Client removed.")

async def main():
    async with websockets.serve(handle_client, "0.0.0.0", 8080):
        print("WebSocket server running on ws://localhost:8080")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
