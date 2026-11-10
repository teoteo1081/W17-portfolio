#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Local Portfolio Visual Editor & Development Server (/api/save)
Chạy lệnh: python dev_server.py
Sau đó mở: http://localhost:8000
"""

from server import PortfolioEditorHandler, HTTPServer
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    server = HTTPServer(("127.0.0.1", port), PortfolioEditorHandler)
    print(f"W17 Portfolio V3 Dev Server running at http://localhost:{port}")
    server.serve_forever()
