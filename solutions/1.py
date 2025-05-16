# llm_service.py

import torch
import torch.nn as nn
import torch.nn.functional as F
from flask import Flask, request, jsonify
import time
import hashlib

app = Flask(__name__)

# -----------------------------
# 模拟轻量级的语言模型（llmLite）
# -----------------------------
class SimpleLLMLite(nn.Module):
    def __init__(self, input_dim=10, hidden_dim=20, output_dim=3):
        super(SimpleLLMLite, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        return self.fc2(x)

# 实例化模型并加载预训练参数（此处为模拟）
model = SimpleLLMLite()
model.eval()

# -----------------------------
# 模拟的 Token 验证机制
# -----------------------------
VALID_TOKENS = {}  # 保存已授权的 Token

def generate_token(user_id):
    """生成短期有效的 Token（模拟：哈希 + 时间戳）"""
    timestamp = str(int(time.time()))
    raw = f"{user_id}-{timestamp}"
    token = hashlib.sha256(raw.encode()).hexdigest()
    VALID_TOKENS[token] = time.time()
    return token

def validate_token(token):
    """验证 Token 是否有效（有效期：300秒）"""
    created_time = VALID_TOKENS.get(token)
    if not created_time:
        return False
    if time.time() - created_time > 300:
        del VALID_TOKENS[token]
        return False
    return True

# -----------------------------
# 推理 API 接口
# -----------------------------
@app.route('/request_token', methods=['POST'])
def request_token():
    """客户端请求 Token"""
    data = request.get_json()
    user_id = data.get("user_id", "anonymous")
    token = generate_token(user_id)
    return jsonify({"token": token})

@app.route('/generate_advice', methods=['POST'])
def generate_advice():
    """生成消费建议接口"""
    token = request.headers.get("Authorization")
    if not validate_token(token):
        return jsonify({"error": "Invalid or expired token"}), 403

    data = request.get_json()
    input_features = data.get("features", [0.5] * 10)  # 模拟消费行为特征

    # 转换为张量并送入模型
    x = torch.tensor(input_features).float().unsqueeze(0)
    output = model(x)

    # 模拟建议生成（输出标签）
    suggestions = ["节省开支", "维持当前预算", "可适度增加娱乐开支"]
    predicted_index = torch.argmax(output, dim=1).item()
    advice = suggestions[predicted_index]

    # 返回结构化建议
    return jsonify({
        "advice": advice,
        "confidence": torch.softmax(output, dim=1).tolist()[0]
    })

# -----------------------------
# 启动服务（Docker 内运行）
# -----------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

