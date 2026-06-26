import asyncio
from bleak import BleakScanner

# 1. Define a helper function to do the scanning
async def main():
    print("Scanning... please wait 5 seconds...")
    
    # 2. Ask the computer to find nearby devices
    devices = await BleakScanner.discover()
    
    # 3. Loop through every device found and print it
    for d in devices:
        print(f"Device Found: {d.name} -> Address: {d.address}")

# 4. Start the program
asyncio.run(main())