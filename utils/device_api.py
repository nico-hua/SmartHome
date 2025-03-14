# utils/device_api.py

class Light:
    """
    灯光设备 API
    """
    def set_brightness(self, brightness):
        """
        设置灯光亮度。
        :param brightness: 亮度值 (0-100)
        """
        print(f"[Light] 灯光亮度设置为 {brightness}")

    def set_color(self, color):
        """
        设置灯光颜色。
        :param color: 颜色值 (例如 "red", "blue")
        """
        print(f"[Light] 灯光颜色设置为 {color}")

    def turn_on(self):
        """打开灯光"""
        print("[Light] 灯光已打开")

    def turn_off(self):
        """关闭灯光"""
        print("[Light] 灯光已关闭")


class AirConditioner:
    """
    空调设备 API
    """
    def set_temperature(self, temperature):
        """
        设置空调温度。
        :param temperature: 温度值 (例如 26)
        """
        print(f"[AirConditioner] 空调温度设置为 {temperature}°C")

    def set_mode(self, mode):
        """
        设置空调模式。
        :param mode: 模式值 (例如 "cool", "heat")
        """
        print(f"[AirConditioner] 空调模式设置为 {mode}")

    def turn_on(self):
        """打开空调"""
        print("[AirConditioner] 空调已打开")

    def turn_off(self):
        """关闭空调"""
        print("[AirConditioner] 空调已关闭")


class TV:
    """
    电视设备 API
    """
    def set_power(self, status):
        """
        设置电视电源状态。
        :param status: 电源状态 (True: 开, False: 关)
        """
        print(f"[TV] 电视电源设置为 {'开' if status else '关'}")

    def set_channel(self, channel):
        """
        设置电视频道。
        :param channel: 频道号 (例如 1, 2)
        """
        print(f"[TV] 电视频道设置为 {channel}")

    def set_volume(self, volume):
        """
        设置电视音量。
        :param volume: 音量值 (0-100)
        """
        print(f"[TV] 电视音量设置为 {volume}")


class Speaker:
    """
    音响设备 API
    """
    def set_volume(self, volume):
        """
        设置音响音量。
        :param volume: 音量值 (0-100)
        """
        print(f"[Speaker] 音响音量设置为 {volume}")

    def play_music(self, song):
        """
        播放音乐。
        :param song: 歌曲名称
        """
        print(f"[Speaker] 正在播放歌曲: {song}")

    def stop_music(self):
        """停止播放音乐"""
        print("[Speaker] 音乐已停止")


class Curtain:
    """
    窗帘设备 API
    """
    def open(self):
        """打开窗帘"""
        print("[Curtain] 窗帘已打开")

    def close(self):
        """关闭窗帘"""
        print("[Curtain] 窗帘已关闭")

    def set_position(self, position):
        """
        设置窗帘位置。
        :param position: 位置值 (0-100, 0: 完全关闭, 100: 完全打开)
        """
        print(f"[Curtain] 窗帘位置设置为 {position}%")


# 设备实例化（可以根据需要调整）
light = Light()
air_conditioner = AirConditioner()
tv = TV()
speaker = Speaker()
curtain = Curtain()