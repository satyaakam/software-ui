from utils.params import Params
from utils.units import Units

class InPacket():

    def __init__(self) -> None:
        self.data={'sequence_count': 0,
                   'packet_version': 0,
                   'packet_type': 0,
                   'mode_value': 0,
                   'control_state': 0,
                   'battery_status': 0,
                   'reserved': 0,
                   'respiratory_rate_set': 0,
                   'respiratory_rate_measured': 0,
                   'tidal_volume_set': 0,
                   'tidal_volume_measured': 0,
                   'ie_ratio_set': 0,
                   'ie_ratio_measured': 0,
                   'peep_value_measured': 0,
                   'peak_pressure_measured': 0,
                   'plateau_value_measurement': 0,
                   'pressure_set': 0,
                   'pressure_measured': 0,
                   'flow_measured': 0,
                   'volume_in_measured': 0,
                   'volume_out_measured': 0,
                   'volume_rate_measured': 0,
                   'high_pressure_limit_set': 0,
                   'low_pressure_limit_set': 0,
                   'high_volume_limit_set': 0,
                   'low_volume_limit_set': 0,
                   'high_respiratory_rate_limit_set': 0,
                   'low_respiratory_rate_limit_set': 0,
                   'alarm_bits': 0,
                   'crc': 0,
                   'run_state': 0
                   }

    # byteData must have already been checked for proper length and crc
    def from_bytes(self, byteData: bytes) -> None:
        self.data['sequence_count']=int.from_bytes(byteData[0:2], byteorder='little')
        self.data['packet_version']=byteData[2]
<<<<<<< HEAD
        self.data['packet_type']=byteData[3]        
        self.data['mode_value']=byteData[4]
        self.data['control_state']=byteData[5] & 0x1F
        self.data['run_state'] = byteData[5] & (1 << 7)
        self.data['battery_charge'] = byteData[6] & (1 << 7)
        self.data['battery_level'] = byteData[6] & 0x7F
        self.data['reserved'] = byteData[7]
        self.data['respiratory_rate_set']=int.from_bytes(byteData[8:10], byteorder='little')
        self.data['respiratory_rate_measured']=int.from_bytes(byteData[10:12], byteorder='little')
        self.data['tidal_volume_set']=int.from_bytes(byteData[12:14], byteorder='little', signed=True)
        self.data['tidal_volume_measured']=int.from_bytes(byteData[14:16], byteorder='little', signed=True)
        self.data['ie_ratio_set']=int.from_bytes(byteData[16:18], byteorder='little')
        self.data['ie_ratio_measured']=int.from_bytes(byteData[18:20], byteorder='little')
        self.data['peep_value_measured']=int.from_bytes(byteData[20:22], byteorder='little', signed=True)
        self.data['peak_pressure_measured']=int.from_bytes(byteData[22:24], byteorder='little', signed=True)
        self.data['plateau_value_measured']=int.from_bytes(byteData[24:26], byteorder='little', signed=True)
        self.data['pressure_set']=int.from_bytes(byteData[26:28], byteorder='little', signed=True)
        self.data['pressure_measured']=int.from_bytes(byteData[28:30], byteorder='little', signed=True)
        self.data['flow_measured']=int.from_bytes(byteData[30:32], byteorder='little', signed=True)
        self.data['volume_in_measured']=int.from_bytes(byteData[32:34], byteorder='little', signed=True)
        self.data['volume_out_measured']=int.from_bytes(byteData[34:36], byteorder='little', signed=True)
        self.data['volume_rate_measured']=int.from_bytes(byteData[36:38], byteorder='little', signed=True)
        self.data['high_pressure_limit_set']=int.from_bytes(byteData[38:40], byteorder='little', signed=True)
        self.data['low_pressure_limit_set']=int.from_bytes(byteData[40:42], byteorder='little', signed=True)
        self.data['high_volume_limit_set']=int.from_bytes(byteData[42:44], byteorder='little', signed=True)
        self.data['low_volume_limit_set']=int.from_bytes(byteData[44:46], byteorder='little', signed=True)
        self.data['high_respiratory_rate_limit_set']=int.from_bytes(byteData[46:48], byteorder='little', signed=True)
        self.data['low_respiratory_rate_limit_set']=int.from_bytes(byteData[48:50], byteorder='little', signed=True)
        
        self.data['alarm_bits']=int.from_bytes(byteData[50:52], byteorder='little')
        self.data['crc']=int.from_bytes(byteData[52:], byteorder='little')
=======
        self.data['run_state'] = byteData[3] & (1 << 7)
        self.data['mode_value']= byteData[3] & 0x7F
        self.data['respiratory_rate_measured']=int.from_bytes(byteData[4:8], byteorder='little')
        self.data['respiratory_rate_set']=int.from_bytes(byteData[8:12], byteorder='little')
        self.data['tidal_volume_measured']=int.from_bytes(byteData[12:16], byteorder='little', signed=True)
        self.data['tidal_volume_set']=int.from_bytes(byteData[16:20], byteorder='little', signed=True)
        
        ie_measured_fixed = int.from_bytes(byteData[20:24], byteorder='little')
        ie_measured_fraction = self.ie_fixed_to_fraction(ie_measured_fixed)
        self.data['ie_ratio_measured'] = ie_measured_fraction

        ie_set_fixed = int.from_bytes(byteData[24:28], byteorder='little')
        ie_set_fraction = self.ie_fixed_to_fraction(ie_set_fixed)
        self.data['ie_ratio_set'] = ie_set_fraction

        self.data['peep_value_measured']=int.from_bytes(byteData[28:32], byteorder='little', signed=True)
        self.data['peak_pressure_measured']=int.from_bytes(byteData[32:36], byteorder='little', signed=True)
        self.data['plateau_value_measured']=int.from_bytes(byteData[36:40], byteorder='little', signed=True)
        self.data['pressure_measured']=int.from_bytes(byteData[40:44], byteorder='little', signed=True)
        self.data['flow_measured']=int.from_bytes(byteData[44:48], byteorder='little', signed=True)
        self.data['volume_in_measured']=int.from_bytes(byteData[48:52], byteorder='little', signed=True)
        self.data['volume_out_measured']=int.from_bytes(byteData[52:56], byteorder='little', signed=True)
        self.data['volume_rate_measured']=int.from_bytes(byteData[56:60], byteorder='little', signed=True)
        self.data['control_state']=byteData[60]
        self.data['battery_level']=byteData[61]
        self.data['reserved']=int.from_bytes(byteData[62:64], byteorder='little')
        self.data['alarm_bits']=int.from_bytes(byteData[64:68], byteorder='little')
        self.data['crc']=int.from_bytes(byteData[68:], byteorder='little')
>>>>>>> develop


    def to_params(self) -> Params:
        params = Params()
        params.run_state = self.data['run_state']
        params.seq_num = self.data['sequence_count']
        params.packet_version = self.data['packet_version']
        params.mode = self.data['mode_value']
        params.resp_rate_meas = self.data['respiratory_rate_measured']
        params.resp_rate_set = self.data['respiratory_rate_set']
        params.tv_meas = Units.ecu_to_ml(self.data['tidal_volume_measured'])
        params.tv_set = Units.ecu_to_ml(self.data['tidal_volume_set'])
        params.ie_ratio_meas = self.data['ie_ratio_measured']
        params.ie_ratio_set = self.data['ie_ratio_set']
        params.peep = Units.ecu_to_cmh2o(self.data['peep_value_measured'])
        params.ppeak = Units.ecu_to_cmh2o(self.data['peak_pressure_measured'])
        params.pplat = Units.ecu_to_cmh2o(self.data['plateau_value_measured'])
        params.pressure= Units.ecu_to_cmh2o(self.data['pressure_measured'])
        params.flow = Units.ecu_to_slm(self.data['flow_measured'])
        params.tv_insp = Units.ecu_to_ml(self.data['volume_in_measured'])
        params.tv_exp = Units.ecu_to_ml(self.data['volume_out_measured'])
        params.tv_rate = Units.ecu_to_ml(self.data['volume_rate_measured'])
        params.battery_level = self.data['battery_level']
        return params


    def ie_fixed_to_fraction(self, n: int) -> float:
        if n == 0:
            return 0

        if (n <= 128):
            i = 1.0
            e = (256 / float(n)) - 1
        else:
            i = (float(n) / 256) / (1 - float(n) / 256)
            e = 1.0
        
        if e == 0:
            return 0
        else:
            return i / e
       
    