device_api_info = {
    "light": {
        "description": "Controls the light device, including turning it on/off, setting brightness, and changing color.",
        "methods": [
            {
                "name": "turn_on",
                "description": "Turn on the light.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the light device."
                    }
                ],
                "returns": "None"
            },
            {
                "name": "turn_off",
                "description": "Turn off the light.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the light device."
                    }
                ],
                "returns": "None"
            },
            {
                "name": "set_brightness",
                "description": "Set the brightness level of the light.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the light device."
                    },
                    {
                        "name": "brightness",
                        "type": "int",
                        "description": "The brightness level to set (0-100)."
                    }
                ],
                "returns": "None"
            },
            {
                "name": "set_color",
                "description": "Set the color of the light.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the light device."
                    },
                    {
                        "name": "color",
                        "type": "str",
                        "description": "The color to set (options: Warm White, Cool White, Orange)."
                    }
                ],
                "returns": "None"
            }
        ]
    },
    "air_conditioner": {
        "description": "Controls the air conditioner device, including turning it on/off, setting temperature, and adjusting mode.",
        "methods": [
            {
                "name": "turn_on",
                "description": "Turn on the air conditioner.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the air conditioner device."
                    }
                ],
                "returns": "None"
            },
            {
                "name": "turn_off",
                "description": "Turn off the air conditioner.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the air conditioner device."
                    }
                ],
                "returns": "None"
            },
            {
                "name": "set_temperature",
                "description": "Set the temperature of the air conditioner.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the air conditioner device."
                    },
                    {
                        "name": "temperature",
                        "type": "int",
                        "description": "The temperature value to set (15-30)."
                    }
                ],
                "returns": "None"
            },
            {
                "name": "set_mode",
                "description": "Set the mode of the air conditioner.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the air conditioner device."
                    },
                    {
                        "name": "mode",
                        "type": "str",
                        "description": "The mode to set (options: cooling, heating, fan)."
                    }
                ],
                "returns": "None"
            }
        ]
    },
    "television": {
        "description": "Controls the TV device, including turning it on/off, setting channel, and adjusting volume.",
        "methods": [
            {
                "name": "turn_on",
                "description": "Turn on the television.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the television device."
                    }
                ],
                "returns": "None"
            },
            {
                "name": "turn_off",
                "description": "Turn off the television.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the television device."
                    }
                ],
                "returns": "None"
            },
            {
                "name": "set_channel",
                "description": "Set the television channel.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the television device."
                    },
                    {
                        "name": "channel",
                        "type": "str",
                        "description": "The channel name to set (options: CCTV, Shanghai TV, Beijing TV, Jiangxi TV, Hunan TV, Zhejiang TV, Jiangsu TV)."
                    }
                ],
                "returns": "None"
            },
            {
                "name": "set_volume",
                "description": "Set the television volume.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the television device."
                    },
                    {
                        "name": "volume",
                        "type": "int",
                        "description": "The volume value to set (options: 0-100)."
                    }
                ],
                "returns": "None"
            }
        ]
    },
    "audio_player": {
        "description": "Controls the audio player device, including turning it on/off, adjusting volume, and playing music.",
        "methods": [
            {
                "name": "turn_on",
                "description": "Turn on the audio player.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the audio player device."
                    }
                ],
                "returns": "None"
            },
            {
                "name": "turn_off",
                "description": "Turn off the audio player.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the audio player device."
                    }
                ],
                "returns": "None"
            },
            {
                "name": "set_volume",
                "description": "Set the volume of the audio player.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the audio player device."
                    },
                    {
                        "name": "volume",
                        "type": "int",
                        "description": "The volume value to set (0-100)."
                    }
                ],
                "returns": "None"
            },
            {
                "name": "play_music",
                "description": "Play music on the audio player.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the audio player device."
                    },
                    {
                        "name": "song",
                        "type": "str",
                        "description": "The title of the song to play (options: 晴天, 稻香, 我记得, 程艾影, 干杯, 我怀念的, 知我, 上里与手抄卷)."
                    }
                ],
                "returns": "None"
            }
        ]
    },
    "curtain": {
        "description": "Controls the curtain device, including opening/closing it and setting its position.",
        "methods": [
            {
                "name": "open",
                "description": "Open the curtain.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the curtain device."
                    }
                ],
                "returns": "None"
            },
            {
                "name": "close",
                "description": "Close the curtain.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the curtain device."
                    }
                ],
                "returns": "None"
            },
            {
                "name": "set_position",
                "description": "Set the position of the curtain.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the curtain device."
                    },
                    {
                        "name": "position",
                        "type": "int",
                        "description": "The position value to set (options: 0-100, 0: fully closed, 100: fully open)."
                    }
                ],
                "returns": "None"
            }
        ]
    },
    "window": {
        "description": "Controls the window device, including opening/closing it and setting its position.",
        "methods": [
            {
                "name": "open",
                "description": "Open the window.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the window device."
                    }
                ],
                "returns": "None"
            },
            {
                "name": "close",
                "description": "Close the window.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the window device."
                    }
                ],
                "returns": "None"
            },
            {
                "name": "set_position",
                "description": "Set the position of the window.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the window device."
                    },
                    {
                        "name": "position",
                        "type": "int",
                        "description": "The position value to set (options: 0-100, 0: fully closed, 100: fully open)."
                    }
                ],
                "returns": "None"
            }
        ]
    },
    "air_purifier": {
        "description": "Controls the air_purifier device, including turning it on/off, setting purification level.",
        "methods": [
            {
                "name": "turn_on",
                "description": "Turn on the air_purifier.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the air_purifier device."
                    }
                ],
                "returns": "None"
            },
            {
                "name": "turn_off",
                "description": "Turn off the air_purifier.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the air_purifier device."
                    }
                ],
                "returns": "None"
            },
            {
                "name": "set_level",
                "description": "Set the purification level of the air_purifier.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the air_purifier device."
                    },
                    {
                        "name": "level",
                        "type": "str",
                        "description": "The purification level to set (options: low, medium, high, auto)."
                    }
                ],
                "returns": "None"
            },
        ]
    },
    "humidifier": {
        "description": "Controls the humidifier device, including turning it on/off, setting humidity level.",
        "methods": [
            {
                "name": "turn_on",
                "description": "Turn on the humidifier.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the humidifier device."
                    }
                ],
                "returns": "None"
            },
            {
                "name": "turn_off",
                "description": "Turn off the humidifier.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the humidifier device."
                    }
                ],
                "returns": "None"
            },
            {
                "name": "set_level",
                "description": "Set the humidify level of the humidifier.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the humidifier device."
                    },
                    {
                        "name": "level",
                        "type": "int",
                        "description": "The humidify level to set (20-80)."
                    }
                ],
                "returns": "None"
            },
        ]
    },
    "range_hood": {
        "description": "Controls the range_hood device, including turning it on/off, setting speed.",
        "methods": [
            {
                "name": "turn_on",
                "description": "Turn on the range_hood.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the range_hood device."
                    }
                ],
                "returns": "None"
            },
            {
                "name": "turn_off",
                "description": "Turn off the range_hood.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the range_hood device."
                    }
                ],
                "returns": "None"
            },
            {
                "name": "set_speed",
                "description": "Set the speed of the range_hood.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the range_hood device."
                    },
                    {
                        "name": "speed",
                        "type": "str",
                        "description": "The speed to set (options: low, medium, high)."
                    }
                ],
                "returns": "None"
            },
        ]
    },
    "ventilation_fan": {
        "description": "Controls the ventilation_fan device, including turning it on/off, setting speed.",
        "methods": [
            {
                "name": "turn_on",
                "description": "Turn on the ventilation_fan.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the ventilation_fan device."
                    }
                ],
                "returns": "None"
            },
            {
                "name": "turn_off",
                "description": "Turn off the ventilation_fan.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the ventilation_fan device."
                    }
                ],
                "returns": "None"
            },
            {
                "name": "set_speed",
                "description": "Set the speed of the ventilation_fan.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the ventilation_fan device."
                    },
                    {
                        "name": "speed",
                        "type": "str",
                        "description": "The speed to set (options: low, medium, high)."
                    }
                ],
                "returns": "None"
            },
        ]
    },
    "heater": {
        "description": "Controls the heater device, including turning it on/off, setting temperature level.",
        "methods": [
            {
                "name": "turn_on",
                "description": "Turn on the heater.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the heater device."
                    }
                ],
                "returns": "None"
            },
            {
                "name": "turn_off",
                "description": "Turn off the heater.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the heater device."
                    }
                ],
                "returns": "None"
            },
            {
                "name": "set_level",
                "description": "Set the temparature level of the heater.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the heater device."
                    },
                    {
                        "name": "level",
                        "type": "str",
                        "description": "The temperature level to set (options: low, medium, high)."
                    }
                ],
                "returns": "None"
            },
        ]
    },
}

device_api_store = [
  {
    "id": "1",
    "description": "Turn on the light.",
    "api": "light.turn_on",
    "args_num": 1
  },
  {
    "id": "2",
    "description": "Turn off the light.",
    "api": "light.turn_off",
    "args_num": 1
  },
  {
    "id": "3",
    "description": "Set the brightness level of the light.",
    "api": "light.set_brightness",
    "args_num": 2
  },
  {
    "id": "4",
    "description": "Set the color of the light.",
    "api": "light.set_color",
    "args_num": 2
  },
  {
    "id": "5",
    "description": "Turn on the air conditioner.",
    "api": "air_conditioner.turn_on",
    "args_num": 1
  },
  {
    "id": "6",
    "description": "Turn off the air conditioner.",
    "api": "air_conditioner.turn_off",
    "args_num": 1
  },
  {
    "id": "7",
    "description": "Set the temperature of the air conditioner.",
    "api": "air_conditioner.set_temperature",
    "args_num": 2
  },
  {
    "id": "8",
    "description": "Set the mode of the air conditioner.",
    "api": "air_conditioner.set_mode",
    "args_num": 2
  },
  {
    "id": "9",
    "description": "Turn on the television.",
    "api": "television.turn_on",
    "args_num": 1
  },
  {
    "id": "10",
    "description": "Turn off the television.",
    "api": "television.turn_off",
    "args_num": 1
  },
  {
    "id": "11",
    "description": "Set the television channel.",
    "api": "television.set_channel",
    "args_num": 2
  },
  {
    "id": "12",
    "description": "Set the television volume.",
    "api": "television.set_volume",
    "args_num": 2
  },
  {
    "id": "13",
    "description": "Turn on the audio player.",
    "api": "audio_player.turn_on",
    "args_num": 1
  },
  {
    "id": "14",
    "description": "Turn off the audio player.",
    "api": "audio_player.turn_off",
    "args_num": 1
  },
  {
    "id": "15",
    "description": "Set the volume of the audio player.",
    "api": "audio_player.set_volume",
    "args_num": 2
  },
  {
    "id": "16",
    "description": "Play music on the audio player.",
    "api": "audio_player.play_music",
    "args_num": 2
  },
  {
    "id": "17",
    "description": "Open the curtain.",
    "api": "curtain.open",
    "args_num": 1
  },
  {
    "id": "18",
    "description": "Close the curtain.",
    "api": "curtain.close",
    "args_num": 1
  },
  {
    "id": "19",
    "description": "Set the position of the curtain.",
    "api": "curtain.set_position",
    "args_num": 2
  },
  {
    "id": "20",
    "description": "Open the window.",
    "api": "window.open",
    "args_num": 1
  },
  {
    "id": "21",
    "description": "Close the window.",
    "api": "window.close",
    "args_num": 1
  },
  {
    "id": "22",
    "description": "Set the position of the window.",
    "api": "window.set_position",
    "args_num": 2
  },
  {
    "id": "23",
    "description": "Turn on the air purifier.",
    "api": "air_purifier.turn_on",
    "args_num": 1
  },
  {
    "id": "24",
    "description": "Turn off the air purifier.",
    "api": "air_purifier.turn_off",
    "args_num": 1
  },
  {
    "id": "25",
    "description": "Set the purification level of the air purifier.",
    "api": "air_purifier.set_level",
    "args_num": 2
  },
  {
    "id": "26",
    "description": "Turn on the humidifier.",
    "api": "humidifier.turn_on",
    "args_num": 1
  },
  {
    "id": "27",
    "description": "Turn off the humidifier.",
    "api": "humidifier.turn_off",
    "args_num": 1
  },
  {
    "id": "28",
    "description": "Set the humidify level of the humidifier.",
    "api": "humidifier.set_level",
    "args_num": 2
  },
  {
    "id": "29",
    "description": "Turn on the range hood.",
    "api": "range_hood.turn_on",
    "args_num": 1
  },
  {
    "id": "30",
    "description": "Turn off the range hood.",
    "api": "range_hood.turn_off",
    "args_num": 1
  },
  {
    "id": "31",
    "description": "Set the speed of the range hood.",
    "api": "range_hood.set_speed",
    "args_num": 2
  },
  {
    "id": "32",
    "description": "Turn on the ventilation fan.",
    "api": "ventilation_fan.turn_on",
    "args_num": 1
  },
  {
    "id": "33",
    "description": "Turn off the ventilation fan.",
    "api": "ventilation_fan.turn_off",
    "args_num": 1
  },
  {
    "id": "34",
    "description": "Set the speed of the ventilation fan.",
    "api": "ventilation_fan.set_speed",
    "args_num": 2
  },
  {
    "id": "35",
    "description": "Turn on the heater.",
    "api": "heater.turn_on",
    "args_num": 1
  },
  {
    "id": "36",
    "description": "Turn off the heater.",
    "api": "heater.turn_off",
    "args_num": 1
  },
  {
    "id": "37",
    "description": "Set the temperature level of the heater.",
    "api": "heater.set_level",
    "args_num": 2
  }
]