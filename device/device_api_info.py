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
                "description": "Turn off the TV.",
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
                "description": "Set the TV channel.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the TV device."
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
                "description": "Set the TV volume.",
                "parameters": [
                    {
                        "name": "device_id",
                        "type": "str",
                        "description": "The ID of the TV device."
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
    }
}