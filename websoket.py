import websockets as ws
import asyncio 
print(ws)
async def echo(websocket, path):
        print(path,websocket)
        ws.onopen()
        print(f"Client connected from path: {path}")
        try:
            async for message in websocket:
                print(f"Received from client: {message}")
                # Echo the received message back to the client
                await websocket.send(f"Server received: {message}")
        except ws.exceptions.ConnectionClosedOK:
            print("Client disconnected gracefully.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            print("Connection handler finished.")
async def main():
    async with ws.serve(echo,"localhost",3000):
       print("WebSocket server started on ws://localhost:8765")
       await asyncio.Future() 
if __name__=="__main__":
    asyncio.run(main())
