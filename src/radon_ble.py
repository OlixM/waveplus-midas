import asyncio
from bleak import BleakClient
WAVEPLUS_MAC = "F4:60:77:74:E2:F4"
CHAR_UUID = "b42e2a68-ade7-11e4-89d3-123b93f75cba"

class WavePlus:
    def __init__(self, mac):
        self.mac = mac
        self.values = {
            "Humidity": 0.0,
            "Radon ST": 0,
            "Radon LT": 0,
            "Temperature": 0.0,
            "Pressure": 0.0,
            "CO2": 0,
            "VOC": 0,
        }
    async def read_data(self):
        async with BleakClient(self.mac) as client:
            data = await client.read_gatt_char(CHAR_UUID)
            self.parse_wave_plus(data)

    def parse_wave_plus(self, data: bytearray):
        self.values["Humidity"] = data[1] / 2
        self.values["Radon ST"] = int.from_bytes(data[4:6], "little")
        self.values["Radon LT"] = int.from_bytes(data[6:8], "little")
        self.values["Temperature"] = int.from_bytes(data[8:10], "little") / 100
        self.values["Pressure"] = int.from_bytes(data[10:12], "little") / 50
        self.values["CO2"] = int.from_bytes(data[12:14], "little")
        self.values["VOC"] = int.from_bytes(data[14:16], "little")

    def printowanie(self): # do sprawdzenia, czy dane są poprawnie parsowane
        for key, value in self.values.items():
            print(f"{key}: {value}")
async def main():
    Aktualny = WavePlus(WAVEPLUS_MAC)
    await Aktualny.read_data()
    Aktualny.printowanie()

asyncio.run(main())
