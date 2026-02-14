import asyncio
from pywizlight import wizlight, PilotBuilder, discovery

async def main():
    # Set up the light with the IP address
    light = wizlight("192.168.1.2")
    
    print("Trying to turn ON...")
    await light.turn_on(PilotBuilder())
    await asyncio.sleep(1)
    
    print("Trying to turn OFF...")
    await light.turn_off()
    await asyncio.sleep(1)
    
    print("Trying to turn ON again...")
    await light.turn_on(PilotBuilder())
    
    # Get current state
    state = await light.updateState()
    print(f"Current state: {state.get_colortemp()}")

if __name__ == "__main__":
    asyncio.run(main())
