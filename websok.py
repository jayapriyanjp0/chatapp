import asyncio
import websockets

# This function handles a single client connection
async def handle_client(websocket):
    print("New client connected")

    # Send welcome message to the client
    await websocket.send("Welcome to the WebSocket server!")
    print(dir(websocket))

    try:
        # Listen for incoming messages
        async for message in websocket:
            print(f"Received: {message}")
            # Echo back
            await websocket.send(f"Server received: {message}")

    except websockets.exceptions.ConnectionClosedOK:
        print("Client disconnected normally.")
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        print("Client disconnected")

# Main function to start the server
async def main():
    # Create WebSocket server on port 8080
    async with websockets.serve(handle_client, "localhost", 8080):
        print("WebSocket server is running on ws://localhost:8080")
        await asyncio.Future()  # keep the server running forever

# Run the server
if __name__ == "__main__":
    asyncio.run(main())
