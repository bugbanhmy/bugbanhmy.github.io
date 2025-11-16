from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def home():
    # Lấy thời gian hiện tại ở Việt Nam
    vn_timezone = pytz.timezone('Asia/Ho_Chi_Minh')
    thoi_gian = datetime.now(vn_timezone).strftime("%H:%M:%S - %d/%m/%Y")
    
    # Trả về nội dung HTML (Web động)
    return f"""
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <title>Web Python Flask</title>
        <style>
            body {{ font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; background-color: #f4f4f9; }}
            .card {{ background: white; padding: 40px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); text-align: center; }}
            h1 {{ color: #306998; }} /* Màu xanh của Python */
            p {{ font-size: 1.2em; color: #555; }}
            .time {{ color: #e74c3c; font-weight: bold; font-size: 1.5em; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Xin chào từ Python! 🐍</h1>
            <p>Trang web này đang chạy bằng Flask trên Render.</p>
            <p>Thời gian hiện tại:</p>
            <div class="time">{thoi_gian}</div>
            <p><small>Hãy F5 để thấy thời gian thay đổi</small></p>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
