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
        Open the curtains.
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
        Close the curtains.
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

# 设备实例化（可以根据需要调整）
light = Light()
air_conditioner = AirConditioner()
television = Television()
audio_player = AudioPlayer()
curtain = Curtain()