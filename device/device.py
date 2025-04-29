import pymysql

class Light:
    def __init__(self):
        self.client = pymysql.connect(
            host='localhost',
            user='root',
            password='123456a',
            database='smart_home',
            cursorclass=pymysql.cursors.DictCursor
        )
    """
    灯光设备 API
    """
    def turn_on(self, device_id):
        """
        Turn on the light
        :param device_id: device ID
        """
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM light WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE light SET power='on' WHERE device_id=%s", (device_id,)
            )
        self.client.commit()
        print(f"[Light {device_id}] 灯光已打开")

    def turn_off(self, device_id):
        """
        Turn off the light.
        :param device_id: device ID
        """
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM light WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE light SET power='off' WHERE device_id=%s", (device_id,)
            )
        self.client.commit()
        print(f"[Light {device_id}] 灯光已关闭")

    def set_brightness(self, device_id, brightness):
        """
        Set brightness level(options: 0-100, 0: darkest, 100: brightest)
        :param device_id: device ID
        :param brightness: brightness level (0-100)
        """
        if not (0 <= brightness <= 100):
            raise ValueError(f"亮度值无效：{brightness}。必须在 0 到 100 之间。")
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM light WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE light SET brightness=%s WHERE device_id=%s", (brightness, device_id)
            )
        self.client.commit()
        print(f"[Light {device_id}] 灯光亮度设置为 {brightness}")

    def set_color(self, device_id, color):
        """
        Set light color (options: Warm White, Cool White, Orange)
        :param device_id: device ID
        :param color: color (options: Warm White, Cool White, Orange)
        """
        valid_colors = ["Warm White", "Cool White", "Orange"]
        if color not in valid_colors:
            raise ValueError(f"不支持的颜色：{color}，可选值为: {', '.join(valid_colors)}")
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM light WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE light SET color=%s WHERE device_id=%s", (color, device_id)
            )
        self.client.commit()
        print(f"[Light {device_id}] 灯光颜色设置为 {color}")

class AirConditioner:
    def __init__(self):
        self.client = pymysql.connect(
            host='localhost',
            user='root',
            password='123456a',
            database='smart_home',
            cursorclass=pymysql.cursors.DictCursor
        )
    """
    空调设备 API
    """
    def turn_on(self, device_id):
        """
        Turn on the air conditioner.
        :param device_id: device ID
        """
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM air_conditioner WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE air_conditioner SET power='on' WHERE device_id=%s", (device_id,)
            )
        self.client.commit()
        print(f"[AirConditioner {device_id}] 空调已打开")

    def turn_off(self, device_id):
        """
        Turn off the air conditioner.
        :param device_id: device ID
        """
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM air_conditioner WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE air_conditioner SET power='off' WHERE device_id=%s", (device_id,)
            )
        self.client.commit()
        print(f"[AirConditioner {device_id}] 空调已关闭")

    def set_temperature(self, device_id, temperature):
        """
        Set the air conditioner temperature.
        :param device_id: device ID
        :param temperature: Temperature value (e.g. 26)
        """
        if not (15 <= temperature <= 30):
            raise ValueError(f"温度值无效：{temperature}。必须在 15 到 30 之间。")
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM air_conditioner WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE air_conditioner SET temperature=%s WHERE device_id=%s", (temperature, device_id)
            )
        self.client.commit()
        print(f"[AirConditioner {device_id}] 空调温度设置为 {temperature}°C")

    def set_mode(self, device_id, mode):
        """
        Set mode (options: cooling, heating, fan)
        :param device_id: device ID
        :param mode: mode type (options: cooling, heating, fan)
        """
        valid_modes = ["cooling", "heating", "fan"]
        if mode not in valid_modes:
            raise ValueError(f"不支持的模式：{mode}，可选值为: {', '.join(valid_modes)}")
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM air_conditioner WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE air_conditioner SET mode=%s WHERE device_id=%s", (mode, device_id)
            )
        self.client.commit()
        print(f"[AirConditioner {device_id}] 空调模式设置为 {mode}")

class Television:
    def __init__(self):
        self.client = pymysql.connect(
            host='localhost',
            user='root',
            password='123456a',
            database='smart_home',
            cursorclass=pymysql.cursors.DictCursor
        )
    """
    电视设备 API
    """
    def turn_on(self, device_id):
        """
         Turn on the television.
        :param device_id: device ID
        """
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM television WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE television SET power='on' WHERE device_id=%s", (device_id,)
            )
        self.client.commit()
        print(f"[TV {device_id}] 电视已打开")

    def turn_off(self, device_id):
        """
         Turn off the television.
        :param device_id: device ID
        """
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM television WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE television SET power='off' WHERE device_id=%s", (device_id,)
            )
        self.client.commit()
        print(f"[TV {device_id}] 电视已关闭")

    def set_channel(self, device_id, channel):
        """
        Set channel (options: CCTV, Shanghai TV, Beijing TV, Jiangxi TV, Hunan TV, Zhejiang TV, Jiangsu TV)
        :param device_id: device ID
        :param channel: Channel (options: CCTV, Shanghai TV, Beijing TV, Jiangxi TV, Hunan TV, Zhejiang TV, Jiangsu TV)
        """
        valid_channels = ["CCTV", "Shanghai TV", "Beijing TV", "Jiangxi TV", "Hunan TV", "Zhejiang TV", "Jiangsu TV"]
        if channel not in valid_channels:
            raise ValueError(f"不支持的频道：{channel}，可选值为: {', '.join(valid_channels)}")
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM television WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE television SET channel=%s WHERE device_id=%s", (channel, device_id)
            )
        self.client.commit()
        print(f"[TV {device_id}] 电视频道设置为 {channel}")

    def set_volume(self, device_id, volume):
        """
        Set the TV volume.
        :param device_id: device ID
        :param volume: volume value (options: 0-100)
        """
        if not (0 <= volume <= 100):
            raise ValueError(f"音量值无效：{volume}。必须在 0 到 100 之间。")
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM television WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE television SET volume=%s WHERE device_id=%s", (volume, device_id)
            )
        self.client.commit()
        print(f"[TV {device_id}] 电视音量设置为 {volume}")

class AudioPlayer:
    def __init__(self):
        self.client = pymysql.connect(
            host='localhost',
            user='root',
            password='123456a',
            database='smart_home',
            cursorclass=pymysql.cursors.DictCursor
        )
    """
    音响设备 API
    """
    def turn_on(self, device_id):
        """
        Turn on the audio_player.
        :param device_id: device ID
        """
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM audio_player WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE audio_player SET power='on' WHERE device_id=%s", (device_id,)
            )
        self.client.commit()
        print(f"[AudioPlayer {device_id}] 音响已打开")

    def turn_off(self, device_id):
        """
        Turn off the audio_player.
        :param device_id: device ID
        """
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM audio_player WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE audio_player SET power='off' WHERE device_id=%s", (device_id,)
            )
        self.client.commit()
        print(f"[AudioPlayer {device_id}] 音响已关闭")
        
    def set_volume(self, device_id, volume):
        """
        Set the audio_player volume.
        :param device_id: device ID
        :param volume: volume value (0-100)
        """
        if not (0 <= volume <= 100):
            raise ValueError(f"音量值无效：{volume}。必须在 0 到 100 之间。")
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM audio_player WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE audio_player SET volume=%s WHERE device_id=%s", (volume, device_id)
            )
        self.client.commit()
        print(f"[AudioPlayer {device_id}] 音响音量设置为 {volume}")

    def play_music(self, device_id, song):
        """
        Play music(options: 晴天, 稻香, 我记得, 程艾影, 干杯, 我怀念的, 知我, 上里与手抄卷).
        :param device_id: device ID
        :param song: song title
        """
        valid_songs = ["晴天", "稻香", "我记得", "程艾影", "干杯", "我怀念的", "知我", "上里与手抄卷"]
        if song not in valid_songs:
            raise ValueError(f"不支持的歌曲：{song}，可选值为: {', '.join(valid_songs)}")
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM audio_player WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE audio_player SET music=%s WHERE device_id=%s", (song, device_id)
            )
        self.client.commit()
        print(f"[AudioPlayer {device_id}] 正在播放歌曲: {song}")

class Curtain:
    def __init__(self):
        self.client = pymysql.connect(
            host='localhost',
            user='root',
            password='123456a',
            database='smart_home',
            cursorclass=pymysql.cursors.DictCursor
        )
    """
    窗帘设备 API
    """
    def open(self, device_id):
        """
        Open the curtain.
        :param device_id: device ID
        """
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM curtain WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE curtain SET position=100 WHERE device_id=%s", (device_id,)
            )
        self.client.commit()
        print(f"[Curtain {device_id}] 窗帘已打开")

    def close(self, device_id):
        """
        Close the curtain.
        :param device_id: device ID
        """
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM curtain WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE curtain SET position=0 WHERE device_id=%s", (device_id,)
            )
        self.client.commit()
        print(f"[Curtain {device_id}] 窗帘已关闭")

    def set_position(self, device_id, position):
        """
        Set curtain position.
        :param device_id: device ID
        :param position: position value (options: 0-100, 0: fully closed, 100: fully open)
        """
        if not (0 <= position <= 100):
            raise ValueError(f"位置值无效：{position}。必须在 0 到 100 之间。")
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM curtain WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE curtain SET position=%s WHERE device_id=%s", (position, device_id,)
            )
        self.client.commit()
        print(f"[Curtain {device_id}] 窗帘位置设置为 {position}%")

class Window:
    def __init__(self):
        self.client = pymysql.connect(
            host='localhost',
            user='root',
            password='123456a',
            database='smart_home',
            cursorclass=pymysql.cursors.DictCursor
        )
    """
    窗户设备 API
    """
    def open(self, device_id):
        """
        Open the window.
        :param device_id: device ID
        """
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM windows WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE windows SET position=100 WHERE device_id=%s", (device_id,)
            )
        self.client.commit()
        print(f"[Window {device_id}] 窗户已打开")

    def close(self, device_id):
        """
        Close the window.
        :param device_id: device ID
        """
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM windows WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE windows SET position=0 WHERE device_id=%s", (device_id,)
            )
        self.client.commit()
        print(f"[Window {device_id}] 窗户已关闭")

    def set_position(self, device_id, position):
        """
        Set window position.
        :param device_id: device ID
        :param position: position value (options: 0-100, 0: fully closed, 100: fully open)
        """
        if not (0 <= position <= 100):
            raise ValueError(f"位置值无效：{position}。必须在 0 到 100 之间。")
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM windows WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE windows SET position=%s WHERE device_id=%s", (position, device_id,)
            )
        self.client.commit()
        print(f"[Window {device_id}] 窗户位置设置为 {position}%")

class AirPurifier:
    def __init__(self):
        self.client = pymysql.connect(
            host='localhost',
            user='root',
            password='123456a',
            database='smart_home',
            cursorclass=pymysql.cursors.DictCursor
        )
    """
    空气净化器设备 API
    """
    def turn_on(self, device_id):
        """
        Turn on the air_purifier
        :param device_id: device ID
        """
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM air_purifier WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE air_purifier SET power='on' WHERE device_id=%s", (device_id,)
            )
        self.client.commit()
        print(f"[AirPurifier {device_id}] 空气净化器已打开")

    def turn_off(self, device_id):
        """
        Turn off the air_purifier.
        :param device_id: device ID
        """
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM air_purifier WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE air_purifier SET power='off' WHERE device_id=%s", (device_id,)
            )
        self.client.commit()
        print(f"[AirPurifier {device_id}] 空气净化器已关闭")

    def set_level(self, device_id, level):
        """
        Set the purification level (options: low, medium, high, auto)
        :param device_id: device ID
        :param level: purification level (options: low, medium, high, auto)
        """
        valid_levels = ["low", "medium", "high", "auto"]
        if level not in valid_levels:
            raise ValueError(f"不支持的级别：{level}，可选值为: {', '.join(valid_levels)}")
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM air_purifier WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE air_purifier SET level=%s WHERE device_id=%s", (level, device_id)
            )
        self.client.commit()
        print(f"[AirPurifier {device_id}] 空气净化器级别设置为 {level}")
            
class Humidifier:
    def __init__(self):
        self.client = pymysql.connect(
            host='localhost',
            user='root',
            password='123456a',
            database='smart_home',
            cursorclass=pymysql.cursors.DictCursor
        )
    """
    加湿器设备 API
    """
    def turn_on(self, device_id):
        """
        Turn on the humidifier
        :param device_id: device ID
        """
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM humidifier WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE humidifier SET power='on' WHERE device_id=%s", (device_id,)
            )
        self.client.commit()
        print(f"[Humidifier {device_id}] 加湿器已打开")

    def turn_off(self, device_id):
        """
        Turn off the humidifier.
        :param device_id: device ID
        """
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM humidifier WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE humidifier SET power='off' WHERE device_id=%s", (device_id,)
            )
        self.client.commit()
        print(f"[Humidifier {device_id}] 加湿器已关闭")

    def set_level(self, device_id, level):
        """
        Set the humidity level (options: 20-80)
        :param device_id: device ID
        :param level: humidity level (20-80)
        """
        if not (0 <= level <= 100):
            raise ValueError(f"湿度值无效：{level}。必须在 20 到 80 之间。")
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM humidifier WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE humidifier SET level=%s WHERE device_id=%s", (level, device_id)
            )
        self.client.commit()
        print(f"[Humidifier {device_id}] 加湿器湿度设置为 {level}")

class RangeHood:
    def __init__(self):
        self.client = pymysql.connect(
            host='localhost',
            user='root',
            password='123456a',
            database='smart_home',
            cursorclass=pymysql.cursors.DictCursor
        )
    """
    抽油烟机设备 API
    """
    def turn_on(self, device_id):
        """
        Turn on the range_hood
        :param device_id: device ID
        """
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM range_hood WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE range_hood SET power='on' WHERE device_id=%s", (device_id,)
            )
        self.client.commit()
        print(f"[RangeHood {device_id}] 抽油烟机已打开")

    def turn_off(self, device_id):
        """
        Turn off the range_hood.
        :param device_id: device ID
        """
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM range_hood WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE range_hood SET power='off' WHERE device_id=%s", (device_id,)
            )
        self.client.commit()
        print(f"[RangeHood {device_id}] 抽油烟机已关闭")

    def set_speed(self, device_id, speed):
        """
        Set the speed (options: low, medium, high)
        :param device_id: device ID
        :param speed: speed (options: low, medium, high)
        """
        valid_speeds = ["low", "medium", "high"]
        if speed not in valid_speeds:
            raise ValueError(f"不支持的速度：{speed}，可选值为: {', '.join(valid_speeds)}")
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM range_hood WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE range_hood SET speed=%s WHERE device_id=%s", (speed, device_id)
            )
        self.client.commit()
        print(f"[RangeHood {device_id}] 抽油烟机速度设置为 {speed}")

class VentilationFan:
    def __init__(self):
        self.client = pymysql.connect(
            host='localhost',
            user='root',
            password='123456a',
            database='smart_home',
            cursorclass=pymysql.cursors.DictCursor
        )
    """
    通风风扇设备 API
    """
    def turn_on(self, device_id):
        """
        Turn on the ventilation_fan
        :param device_id: device ID
        """
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM ventilation_fan WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE ventilation_fan SET power='on' WHERE device_id=%s", (device_id,)
            )
        self.client.commit()
        print(f"[VentilationFan {device_id}] 通风风扇已打开")

    def turn_off(self, device_id):
        """
        Turn off the ventilation_fan.
        :param device_id: device ID
        """
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM ventilation_fan WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE ventilation_fan SET power='off' WHERE device_id=%s", (device_id,)
            )
        self.client.commit()
        print(f"[VentilationFan {device_id}] 通风风扇已关闭")

    def set_speed(self, device_id, speed):
        """
        Set the speed (options: low, medium, high)
        :param device_id: device ID
        :param speed: speed (options: low, medium, high)
        """
        valid_speeds = ["low", "medium", "high"]
        if speed not in valid_speeds:
            raise ValueError(f"不支持的速度：{speed}，可选值为: {', '.join(valid_speeds)}")
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM ventilation_fan WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE ventilation_fan SET speed=%s WHERE device_id=%s", (speed, device_id)
            )
        self.client.commit()
        print(f"[VentilationFan {device_id}] 通风风扇速度设置为 {speed}")

class Heater:
    def __init__(self):
        self.client = pymysql.connect(
            host='localhost',
            user='root',
            password='123456a',
            database='smart_home',
            cursorclass=pymysql.cursors.DictCursor
        )
    """
    加热器设备 API
    """
    def turn_on(self, device_id):
        """
        Turn on the heater
        :param device_id: device ID
        """
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM heater WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE heater SET power='on' WHERE device_id=%s", (device_id,)
            )
        self.client.commit()
        print(f"[Heater {device_id}] 加热器已打开")

    def turn_off(self, device_id):
        """
        Turn off the heater.
        :param device_id: device ID
        """
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM heater WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE heater SET power='off' WHERE device_id=%s", (device_id,)
            )
        self.client.commit()
        print(f"[Heater {device_id}] 加热器已关闭")

    def set_level(self, device_id, level):
        """
        Set temperature level (options: low, medium, high)
        :param device_id: device ID
        :param level: temperature level (options: low, medium, high)
        """
        valid_levels = ["low", "medium", "high"]
        if level not in valid_levels:
            raise ValueError(f"不支持的速度：{level}，可选值为: {', '.join(valid_levels)}")
        with self.client.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM heater WHERE device_id=%s", (device_id,))
            count = cursor.fetchone()['COUNT(*)']
            if count == 0:
                raise ValueError(f"设备ID不存在：{device_id}")
            cursor.execute(
                "UPDATE heater SET level=%s WHERE device_id=%s", (level, device_id)
            )
        self.client.commit()
        print(f"[Heater {device_id}] 加热器温度级别设置为 {level}")






# 设备实例化（可以根据需要调整）
light = Light()
air_conditioner = AirConditioner()
television = Television()
audio_player = AudioPlayer()
curtain = Curtain()
window = Window()
air_purifier = AirPurifier()
humidifier = Humidifier()
range_hood = RangeHood()
ventilation_fan = VentilationFan()
heater = Heater()