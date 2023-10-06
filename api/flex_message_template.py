def get_flex_message_content(user_name):
    return {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover",
                "action": {
                "type": "uri",
                "uri": "http://linecorp.com/"
                }
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": user_name +"  您好",
                    "weight": "bold",
                    "size": "xl"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "lg",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "訂單編號",
                            "color": "#aaaaaa",
                            "size": "md",
                            "flex": 1
                        },
                        {
                            "type": "text",
                            "text": "123456789",
                            "color": "#666666",
                            "size": "md",
                            "flex": 2
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "金額",
                            "color": "#aaaaaa",
                            "size": "md",
                            "flex": 1
                        },
                        {
                            "type": "text",
                            "text": "99",
                            "color": "#666666",
                            "size": "md",
                            "flex": 2
                        }
                        ]
                    }
                    ]
                }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                {
                    "type": "button",
                    "style": "primary",
                    "height": "sm",
                    "action": {
                    "type": "uri",
                    "label": "點我付款",
                    "uri": "https://linecorp.com"
                    }
                },
                {
                    "type": "button",
                    "style": "secondary",
                    "height": "sm",
                    "action": {
                    "type": "uri",
                    "label": "查詢付款狀態",
                    "uri": "https://linecorp.com"
                    }
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "margin": "sm"
                }
                ],
                "flex": 0
                }
            }