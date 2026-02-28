import asyncio
import midas
import midas.frontend
import midas.event
import collections
import time
import random
from radon_ble import WavePlus



class RadonEvent(midas.frontend.EquipmentBase):

    def __init__(self, client):

        equip_name = "RadonBLE"

        default_common = midas.frontend.InitialEquipmentCommon()
        default_common.equip_type = midas.EQ_PERIODIC
        default_common.buffer_name = "SYSTEM"
        default_common.event_id = 10
        default_common.period_ms = 1000
        default_common.read_when = midas.RO_ALWAYS
        default_common.log_history = 1

        default_settings = collections.OrderedDict()

        super().__init__(client, equip_name, default_common, default_settings)
        self.odb_readback_dir = self.odb_settings_dir.replace("Settings", "Readback")
        names_dict = {
                    "HUMI":  ["Wilgotno (%)"],
                    "RADS":  ["Radon ST (Bq/m)"],
                    "RADL":  ["Radon LT (Bq/m)"],
                    "TEMP":  ["Temperatura (C)"],    
                    "PRES":  ["Cisnienie (hPa)"],
                    "CO_2":  ["CO2 (ppm)"],
                    "VOC_":  ["TVOC (ppb)"],
                }

        settings_dir = self.odb_settings_dir
        for bank, name_list in names_dict.items():
            self.client.odb_set(f"{settings_dir}/Names{bank}", name_list)


        self.device = WavePlus("F4:60:77:74:E2:F4")

        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    # ==========================================================
    # TYLKO JEDNA readout_func — na poziomie klasy
    # ==========================================================

    def readout_func(self):

        self.loop.run_until_complete(self.device.read_data())

        self.client.odb_set(self.odb_readback_dir, self.device.values)

        event = midas.event.Event()

        event.create_bank("HUMI", midas.TID_DOUBLE,
                          [float(self.device.values.get("Humidity", 0))])

        event.create_bank("RADS", midas.TID_DOUBLE,
                          [float(self.device.values.get("Radon ST", 0))])

        event.create_bank("RADL", midas.TID_DOUBLE,
                          [float(self.device.values.get("Radon LT", 0))])

        event.create_bank("TEMP", midas.TID_DOUBLE,
                          [float(self.device.values.get("Temperature", 0))])

        event.create_bank("PRES", midas.TID_DOUBLE,
                          [float(self.device.values.get("Pressure", 0))])

        event.create_bank("CO_2", midas.TID_DOUBLE,
                          [float(self.device.values.get("CO2", 0))])

        event.create_bank("VOC_", midas.TID_DOUBLE,
                          [float(self.device.values.get("VOC", 0))])

        return event

    #self.loop.run_until_complete(self.device.read_data())
    # zapis do 
    #self.client.odb_set(self.odb_readback_dir, self.device.values)


    #self.client.odb_set(self.odb_readback_dir, self.device.values)
    #self.client.odb_set(self.odb_readback_dir, self.device.values)

class RadonFrontend(midas.frontend.FrontendBase):

    def __init__(self):
        super().__init__("RadonBLEFrontend")
        self.add_equipment(RadonEvent(self.client))


if __name__ == "__main__":
    args = midas.frontend.parse_args()
    fe = RadonFrontend()

    try:
        fe.run() #w razie problemow wpisac help(midas.frontend.FrontendBase.run)
    except KeyboardInterrupt:
        print("Zatrzymano frontend")
    except Exception as e:
        print(f"Wystąpił błąd: {e}") 
        raise
