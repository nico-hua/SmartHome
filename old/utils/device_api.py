class Light:
    """
    灯光设备 API
    """
    def turn_on(self, device_id):
        """
        Turn on the light
        :param device_id: device ID
        """
        print(f"[Light {device_id}] 灯光已打开")

    def turn_off(self, device_id):
        """
        Turn off the light.
        :param device_id: device ID
        """
        print(f"[Light {device_id}] 灯光已关闭")
    
    def get_brightness(self, device_id):
        """
        Get current brightness level.
        :param device_id: device ID
        :return: current brightness level
        """
        print(f"[Light {device_id}] 获取灯光当前亮度")
        return 50

    def set_brightness(self, device_id, brightness):
        """
        Set the light brightness.
        :param device_id: device ID
        :param brightness: brightness level (0-100)
        """
        print(f"[Light {device_id}] 灯光亮度设置为 {brightness}")

    def set_color(self, device_id, color):
        """
        Set the light color
        :param device_id: device ID
        :param color: color (options: Warm White, Cool White, Red, Blue)
        """
        print(f"[Light {device_id}] 灯光颜色设置为 {color}")

class AirConditioner:
    """
    空调设备 API
    """
    def turn_on(self, device_id):
        """
        Turn on the air conditioner.
        :param device_id: device ID
        """
        print(f"[AirConditioner {device_id}] 空调已打开")

    def turn_off(self, device_id):
        """
        Turn off the air conditioner.
        :param device_id: device ID
        """
        print(f"[AirConditioner {device_id}] 空调已关闭")

    def get_temperature(self, device_id):
        """
        Get the current temperature of the air conditioner.
        :param device_id: device ID
        :return: current temperature value
        """
        print(f"[AirConditioner {device_id}] 获取空调当前温度")
        return 25

    def set_temperature(self, device_id, temperature):
        """
        Set the air conditioner temperature.
        :param device_id: device ID
        :param temperature: Temperature value (e.g. 26)
        """
        print(f"[AirConditioner {device_id}] 空调温度设置为 {temperature}°C")

    def set_mode(self, device_id, mode):
        """
        Set air conditioning mode.
        :param device_id: device ID
        :param mode: mode type (options: cooling, heating, fan)
        """
        print(f"[AirConditioner {device_id}] 空调模式设置为 {mode}")

class TV:
    """
    电视设备 API
    """
    def turn_on(self, device_id):
        """
        Turn on the TV.
        :param device_id: device ID
        """
        print(f"[TV {device_id}] 电视已打开")

    def turn_off(self, device_id):
        """
        Turn off the TV.
        :param device_id: device ID
        """
        print(f"[TV {device_id}] 电视已关闭")

    def set_channel(self, device_id, channel):
        """
        Set TV channels.
        :param device_id: device ID
        :param channel: Channel number (options: 1-10)
        """
        print(f"[TV {device_id}] 电视频道设置为 {channel}")

    def set_volume(self, device_id, volume):
        """
        Set the TV volume.
        :param device_id: device ID
        :param volume: volume value (options: 0-100)
        """
        print(f"[TV {device_id}] 电视音量设置为 {volume}")
    
    def get_volume(self, device_id):
        """
        Get the TV volume.
        :param device_id: device ID
        :return: current volume value
        """
        print(f"[TV {device_id}] 获取电视当前音量")


class AudioPlayer:
    """
    音响设备 API
    """
    def turn_on(self, device_id):
        """
        Turn on the audio_player.
        :param device_id: device ID
        """
        print(f"[AudioPlayer {device_id}] 音响已打开")

    def turn_off(self, device_id):
        """
        Turn off the audio_player.
        :param device_id: device ID
        """
        print(f"[AudioPlayer {device_id}] 音响已关闭")
    def set_volume(self, device_id, volume):
        """
        Set the audio_player volume.
        :param device_id: device ID
        :param volume: volume value (0-100)
        """
        print(f"[AudioPlayer {device_id}] 音响音量设置为 {volume}")

    def get_volume(self, device_id):
        """
        Get the audio_player volume.
        :param device_id: device ID
        :return: current volume value
        """
        print(f"[AudioPlayer {device_id}] 获取音响当前音量")
        return 50

    def play_music(self, device_id, song):
        """
        Play music.
        :param device_id: device ID
        :param song: song title
        """
        print(f"[AudioPlayer {device_id}] 正在播放歌曲: {song}")

    def stop_music(self, device_id):
        """
        Stop music.
        :param device_id: device ID
        """
        print(f"[AudioPlayer {device_id}] 音乐已停止")


class Curtain:
    """
    窗帘设备 API
    """
    def open(self, device_id):
        """
        Open the curtains.
        :param device_id: device ID
        """
        print(f"[Curtain {device_id}] 窗帘已打开")

    def close(self, device_id):
        """
        Close the curtains.
        :param device_id: device ID
        """
        print(f"[Curtain {device_id}] 窗帘已关闭")

    def set_position(self, device_id, position):
        """
        Set curtain position.
        :param device_id: device ID
        :param position: position value (options: 0-100, 0: fully closed, 100: fully open)
        """
        print(f"[Curtain {device_id}] 窗帘位置设置为 {position}%")
    
    def get_position(self, device_id):
        """
        Get the current curtain position.
        :param device_id: device ID
        :return: current position value
        """
        print(f"[Curtain {device_id}] 获取窗帘当前位置")
        return 50


# 设备实例化（可以根据需要调整）
light = Light()
air_conditioner = AirConditioner()
tv = TV()
audio_player = AudioPlayer()
curtain = Curtain()