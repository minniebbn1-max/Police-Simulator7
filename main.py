import http.server
import socketserver
import webbrowser
import threading
import time

PORT = 9000

def start_server():
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Police System Server รันที่พอร์ต {PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    # เริ่ม Server ใน Background
    threading.Thread(target=start_server, daemon=True).start()
    
    # รอ 1 วินาทีให้ Server พร้อม
    time.sleep(1)
    
    # เปิดหน้าเว็บล๊อคอิน
    url = f"http://localhost:{PORT}/index.html"
    print(f"--- กำลังเปิดระบบตำรวจ ---")
    print(f"Link: {url}")
    webbrowser.open(url)
    
    # รักษาการทำงานของโปรแกรม
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nปิดระบบ...")
