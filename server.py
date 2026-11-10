#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Local Portfolio Visual Editor Server (/api/save)
Tự động phục vụ trang web và ghi đè file sạch trực tiếp vào thư mục Git khi bấm [💾 Lưu file sạch (Final)].
"""

import json
import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ALLOWED_FILES = {
    "index.html",
    "index_portfolio_v4.html",
    "index_portfolio_clean.html",
    "index_capability_v5.html",
}


class PortfolioEditorHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE_DIR), **kwargs)

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()

    def do_POST(self):
        if self.path != "/api/save":
            self.send_response(404)
            self.end_headers()
            return

        try:
            content_length = int(self.headers.get("Content-Length", 0))
            raw_body = self.rfile.read(content_length).decode("utf-8")
            data = json.loads(raw_body)

            html_content = data.get("html") or data.get("content") or ""
            filename = os.path.basename(data.get("filename") or data.get("file") or "index.html")
            targets = data.get("targets") or [filename]

            saved_files = []
            for target in targets:
                safe_name = os.path.basename(target)
                if safe_name in ALLOWED_FILES and html_content:
                    out_path = BASE_DIR / safe_name
                    out_path.write_text(html_content, encoding="utf-8")
                    saved_files.append(str(out_path))

            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(
                json.dumps({"status": "ok", "saved": saved_files}, ensure_ascii=False).encode("utf-8")
            )
        except Exception as exc:
            self.send_response(500)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(
                json.dumps({"status": "error", "message": str(exc)}, ensure_ascii=False).encode("utf-8")
            )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    server = HTTPServer(("127.0.0.1", port), PortfolioEditorHandler)
    print(f"Portfolio Editor Server running at http://127.0.0.1:{port}")
    server.serve_forever()
