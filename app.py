from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import uuid
import json
from graph.graph import graph
from utils.log_util import Logger

app = FastAPI()

logger = Logger()

DEFAULT_ROOM_NAMES = ["客厅", "主卧", "次卧", "厨房", "卫生间"]

html = """
<!DOCTYPE html>
<html>
<head>
    <title>智能家居AI助手</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        :root {
            --primary-color: #4361ee;
            --secondary-color: #3f37c9;
            --accent-color: #4895ef;
            --light-color: #f8f9fa;
            --dark-color: #212529;
            --success-color: #4cc9f0;
            --warning-color: #f72585;
            --border-radius: 12px;
            --box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            --transition: all 0.3s ease;
        }
        
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        
        body {
            font-family: 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            height: 100vh;
            display: flex;
            flex-direction: column;
            color: var(--dark-color);
        }
        
        .container {
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            width: 100%;
            height: 100%;
            display: flex;
            flex-direction: column;
        }
        
        header {
            text-align: center;
            margin-bottom: 20px;
            position: relative;
        }
        
        h1 {
            color: var(--primary-color);
            font-size: 2.2rem;
            margin-bottom: 10px;
            font-weight: 600;
            background: linear-gradient(to right, #4361ee, #3a0ca3);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .subtitle {
            color: #6c757d;
            font-size: 0.9rem;
        }
        
        .room-selector {
            display: flex;
            align-items: center;
            background: white;
            padding: 12px 15px;
            border-radius: var(--border-radius);
            margin-bottom: 15px;
            box-shadow: var(--box-shadow);
        }
        
        .room-selector label {
            margin-right: 10px;
            font-weight: 600;
            color: var(--primary-color);
            white-space: nowrap;
        }
        
        select {
            flex: 1;
            padding: 10px 15px;
            border: 2px solid #e9ecef;
            border-radius: 8px;
            font-size: 1rem;
            background-color: white;
            transition: var(--transition);
            cursor: pointer;
        }
        
        select:focus {
            outline: none;
            border-color: var(--accent-color);
            box-shadow: 0 0 0 3px rgba(72, 149, 239, 0.2);
        }
        
        #chat {
            flex: 1;
            overflow-y: auto;
            background: white;
            border-radius: var(--border-radius);
            padding: 20px;
            margin-bottom: 15px;
            box-shadow: var(--box-shadow);
            scroll-behavior: smooth;
        }
        
        .message-container {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        
        .message {
            max-width: 80%;
            padding: 12px 16px;
            border-radius: 18px;
            line-height: 1.5;
            word-wrap: break-word;
            position: relative;
            animation: fadeIn 0.3s ease-out;
            font-size: 0.95rem;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .user-message {
            background: var(--primary-color);
            color: white;
            align-self: flex-end;
            border-bottom-right-radius: 4px;
            margin-left: 20%;
        }
        
        .ai-message {
            background: #f1f3f5;
            color: var(--dark-color);
            align-self: flex-start;
            border-bottom-left-radius: 4px;
            margin-right: 20%;
        }
        
        .timestamp {
            font-size: 0.75rem;
            color: #adb5bd;
            margin: 2px 0 8px;
            text-align: right;
        }
        
        .user-message + .timestamp {
            text-align: right;
        }
        
        .ai-message + .timestamp {
            text-align: left;
        }
        
        .input-area {
            display: flex;
            gap: 10px;
            background: white;
            padding: 15px;
            border-radius: var(--border-radius);
            box-shadow: var(--box-shadow);
        }
        
        #messageInput {
            flex: 1;
            padding: 12px 15px;
            border: 2px solid #e9ecef;
            border-radius: 8px;
            font-size: 1rem;
            transition: var(--transition);
        }
        
        #messageInput:focus {
            outline: none;
            border-color: var(--accent-color);
            box-shadow: 0 0 0 3px rgba(72, 149, 239, 0.2);
        }
        
        button {
            padding: 12px 20px;
            background: var(--primary-color);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 1rem;
            font-weight: 500;
            cursor: pointer;
            transition: var(--transition);
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        button:hover {
            background: var(--secondary-color);
            transform: translateY(-1px);
        }
        
        button:active {
            transform: translateY(0);
        }
        
        button:disabled {
            background: #adb5bd;
            cursor: not-allowed;
        }
        
        .typing-indicator {
            display: flex;
            padding: 12px 16px;
            background: #f1f3f5;
            border-radius: 18px;
            align-self: flex-start;
            margin-bottom: 8px;
            width: fit-content;
        }
        
        .typing-dot {
            width: 8px;
            height: 8px;
            background: #6c757d;
            border-radius: 50%;
            margin: 0 2px;
            animation: typingAnimation 1.4s infinite ease-in-out;
        }
        
        .typing-dot:nth-child(1) {
            animation-delay: 0s;
        }
        
        .typing-dot:nth-child(2) {
            animation-delay: 0.2s;
        }
        
        .typing-dot:nth-child(3) {
            animation-delay: 0.4s;
        }
        
        @keyframes typingAnimation {
            0%, 60%, 100% { transform: translateY(0); }
            30% { transform: translateY(-5px); }
        }
        
        @media (max-width: 768px) {
            .container {
                padding: 10px;
            }
            
            h1 {
                font-size: 1.8rem;
            }
            
            .message {
                max-width: 90%;
            }
            
            .input-area {
                flex-direction: column;
            }
            
            button {
                width: 100%;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>智能家居AI助手</h1>
            <p class="subtitle">您的智能生活管家</p>
        </header>
        
        <div class="room-selector">
            <label for="roomSelect">当前位置：</label>
            <select id="roomSelect">
                <option value="living_room">客厅</option>
                <option value="master_bedroom">主卧</option>
                <option value="guest_bedroom">次卧</option>
                <option value="kitchen">厨房</option>
                <option value="bathroom">卫生间</option>
            </select>
        </div>
        
        <div id="chat">
            <div class="message-container">
                <div class="ai-message">您好，我是智能家居助手，请问有什么可以帮您？</div>
                <div class="timestamp" style="text-align: left;">系统消息</div>
            </div>
        </div>
        
        <div class="input-area">
            <input type="text" id="messageInput" placeholder="输入您的指令..." autocomplete="off">
            <button id="sendButton" onclick="sendMessage()">发送</button>
        </div>
    </div>

    <script>
        const ws = new WebSocket("ws://localhost:8000/ws");
        const chatDiv = document.getElementById("chat");
        const messageInput = document.getElementById("messageInput");
        const roomSelect = document.getElementById("roomSelect");
        const sendButton = document.getElementById("sendButton");
        const messageContainer = document.querySelector(".message-container");
        
        // 添加打字指示器
        function showTypingIndicator() {
            const typingDiv = document.createElement("div");
            typingDiv.className = "typing-indicator";
            typingDiv.id = "typingIndicator";
            typingDiv.innerHTML = `
                <div class="typing-dot"></div>
                <div class="typing-dot"></div>
                <div class="typing-dot"></div>
            `;
            
            const container = document.createElement("div");
            container.className = "message-container";
            container.appendChild(typingDiv);
            
            chatDiv.appendChild(container);
            chatDiv.scrollTop = chatDiv.scrollHeight;
        }
        
        // 移除打字指示器
        function hideTypingIndicator() {
            const typingIndicator = document.getElementById("typingIndicator");
            if (typingIndicator) {
                typingIndicator.parentElement.remove();
            }
        }
        
        // 添加消息到聊天界面
        function addMessage(sender, text, isUser = false) {
            hideTypingIndicator();
            
            const messageDiv = document.createElement("div");
            messageDiv.className = isUser ? "user-message" : "ai-message";
            messageDiv.textContent = text;
            
            const timestamp = new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
            const timestampDiv = document.createElement("div");
            timestampDiv.className = "timestamp";
            timestampDiv.textContent = `${timestamp} · ${isUser ? "您" : "助手"}`;
            
            const container = document.createElement("div");
            container.className = "message-container";
            container.appendChild(messageDiv);
            container.appendChild(timestampDiv);
            
            chatDiv.appendChild(container);
            chatDiv.scrollTop = chatDiv.scrollHeight;
        }
        
        // 发送消息
        function sendMessage() {
            const message = messageInput.value.trim();
            if (message) {
                addMessage("You", message, true);
                
                const data = {
                    message: message,
                    room: roomSelect.value
                };
                
                ws.send(JSON.stringify(data));
                messageInput.value = "";
                showTypingIndicator();
            }
        }
        
        // WebSocket消息处理
        ws.onmessage = function(event) {
            addMessage("AI", event.data, false);
        };
        
        // 输入框事件监听
        messageInput.addEventListener("keypress", function(event) {
            if (event.key === "Enter") {
                sendMessage();
            }
        });
        
        // 输入框内容变化时启用/禁用发送按钮
        messageInput.addEventListener("input", function() {
            sendButton.disabled = !this.value.trim();
        });
    </script>
</body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(html)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    # 初始化
    thread_id = str(uuid.uuid4())
    session = {
        "thread_id": thread_id,
        "instruction_history": [],
        "user_location": "living_room",
        "messages": [],
    }

    while True:
        try:
            data = await websocket.receive_text()
            
            try:
                data = json.loads(data)
                user_message = data.get("message", "").strip()
                user_location = data.get("room", "living_room")
            except:
                user_message = data.strip()
                user_location = "living_room"

            if not user_message:
                await websocket.send_text("指令不能为空哦～")
                continue

            # 更新指令和用户位置
            initial_state = {
                "instruction": user_message,
                "user_location": user_location,
                "instruction_history": session["instruction_history"],
                "messages": []
            }

            thread = {"configurable": {"thread_id": str(uuid.uuid4())}}

            # 调用graph.invoke
            messages = graph.invoke(initial_state, thread)

            # 保存会话
            session["user_location"] = user_location
            session["instruction_history"] = (
                session["instruction_history"] +
                [f"User: {initial_state['instruction']}"] +
                [f"AI: {messages['clarify_response'].instruction_response}"]
            )

            # 发送AI回复
            await websocket.send_text(messages['clarify_response'].instruction_response)

        except Exception as e:
            # 发送AI回复
            await websocket.send_text("发生错误，请稍后再试。")
            logger.log(f"WebSocket Error: {e}")
            break