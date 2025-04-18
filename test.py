from utils.mysql_util import MySQLUtils
from device.deviceFullInfo import DeviceFullInfo
from device.deviceInfo import DeviceInfo
from device.lightStatus import LightStatus
from device.curtainStatus import CurtainStatus
from device.airconditionerStatus import AirConditionerStatus
from device.televisionStatus import TelevisionStatus
from device.audioplayerStatus import AudioPlayerStatus
from utils.convert_util import convert_room_info_to_json

if __name__ == "__main__":
    room_info = [
        {
            "living_room": [DeviceFullInfo(device_info=DeviceInfo(device_id='ac_living_room', device_type='air_conditioner', location='wall', description='This device can control the air conditioner switch in the living room, set the temperature and mode(options: cooling, heating, fan).', room='living_room'), device_status=AirConditionerStatus(device_id='ac_living_room', power='on', mode='cooling', temperature=23)), DeviceFullInfo(device_info=DeviceInfo(device_id='curtain_living_room', device_type='curtain', location='window', description='This device can control the opening and closing of the curtains in the living room and adjust their position(options: 0-100, 0: fully closed, 100: fully open).', room='living_room'), device_status=CurtainStatus(device_id='curtain_living_room', position=100)), DeviceFullInfo(device_info=DeviceInfo(device_id='light_living_room', device_type='light', location='center of ceiling', description='This device can control the switch of the living room lights and adjust the brightness and color of the living room lights(options: Warm White, Cool White, Orange).', room='living_room'), device_status=LightStatus(device_id='light_living_room', power='on', brightness=100, color='Cool White')), DeviceFullInfo(device_info=DeviceInfo(device_id='speaker_living_room', device_type='audio_player', location='both sides of the TV', description='This device can control the audio player in the living room to adjust the volume, play and stop music(options: 晴天, 稻香, 我记得, 程艾影, 干杯, 我怀念的, 知我, 上里与手抄卷).', room='living_room'), device_status=AudioPlayerStatus(device_id='speaker_living_room', power='on', volume=80, music='晴天')), DeviceFullInfo(device_info=DeviceInfo(device_id='tv_living_room', device_type='television', location='TV wall', description='This device can control the power switch, channel(options: CCTV, Shanghai TV, Beijing TV, Jiangxi TV, Hunan TV, Zhejiang TV, Jiangsu TV) and volume of the living room television.', room='living_room'), device_status=TelevisionStatus(device_id='tv_living_room', power='on', channel='Jiangxi TV', volume=40))]
        }
    ]
    print(convert_room_info_to_json(room_info))
