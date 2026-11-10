#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fetch_ga4_bigquery.py
Truy vấn dữ liệu thực tế Google Analytics 4 từ Google BigQuery (Project: airy-web-503408-c6)
và xuất kết quả ra file ga4_metrics_live.json phục vụ cập nhật Portfolio W17.
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

PROJECT_ID = "airy-web-503408-c6"
DATE_START = "20261104"
DATE_END = "20261110"
OUTPUT_JSON = Path(__file__).resolve().parent / "ga4_metrics_live.json"

# Dữ liệu đối chiếu từ báo cáo GA4 7 ngày (2026-11-04 -> 2026-11-10)
GA4_REPORT_BASELINE = {
    "project_id": PROJECT_ID,
    "property_name": "TJ Sai Gon Project / TJ WordLoop Hub",
    "date_range": {"start": "2026-11-04", "end": "2026-11-10"},
    "total_events": "5,000+",
    "active_users_by_country": [
        {"country": "Vietnam", "active_users": 23},
        {"country": "Israel", "active_users": 3},
        {"country": "United States", "active_users": 2},
        {"country": "China", "active_users": 1},
        {"country": "Germany", "active_users": 1},
        {"country": "Sweden", "active_users": 1},
    ],
    "pageviews_by_page_title": [
        {"page_title": "TJ WordLoop Game", "page_views": 125},
        {"page_title": "TJ WordLoop Hub — Courses & Academy", "page_views": 68},
        {"page_title": "Operation 0 — 1,000 Chunks Engine", "page_views": 44},
        {"page_title": "WRP Tax Services — US Tax 1040 Funnel", "page_views": 32},
    ],
    "users_by_source_medium": [
        {"source_medium": "(direct) / (none)", "active_users": 27},
        {"source_medium": "facebook / social", "active_users": 4},
        {"source_medium": "zalo / referral", "active_users": 3},
        {"source_medium": "instagram / social", "active_users": 2},
        {"source_medium": "wechat / social", "active_users": 1},
    ],
}


def find_analytics_dataset(client: "bigquery.Client") -> str:
    """Tự động quét tìm dataset analytics_<PROPERTY_ID> trong project."""
    datasets = list(client.list_datasets(project=PROJECT_ID))
    for ds in datasets:
        if ds.dataset_id.startswith("analytics_"):
            return ds.dataset_id
    raise RuntimeError(
        f"Không tìm thấy dataset 'analytics_*' nào trong project '{PROJECT_ID}'. "
        f"Danh sách dataset hiện có: {[d.dataset_id for d in datasets]}"
    )


def build_queries(dataset_id: str, start_suffix: str, end_suffix: str) -> dict:
    table_ref = f"`{PROJECT_ID}.{dataset_id}.events_*`"
    return {
        "active_users_by_country": f"""
SELECT
  geo.country AS country,
  COUNT(DISTINCT user_pseudo_id) AS active_users
FROM {table_ref}
WHERE _TABLE_SUFFIX BETWEEN '{start_suffix}' AND '{end_suffix}'
GROUP BY 1
ORDER BY active_users DESC
""",
        "pageviews_by_page_title": f"""
SELECT
  (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'page_title') AS page_title,
  COUNT(1) AS page_views
FROM {table_ref}
WHERE event_name = 'page_view'
  AND _TABLE_SUFFIX BETWEEN '{start_suffix}' AND '{end_suffix}'
GROUP BY 1
ORDER BY page_views DESC
""",
        "users_by_source_medium": f"""
SELECT
  CONCAT(
    IFNULL(traffic_source.source, '(direct)'), ' / ',
    IFNULL(traffic_source.medium, '(none)')
  ) AS source_medium,
  COUNT(DISTINCT user_pseudo_id) AS active_users
FROM {table_ref}
WHERE _TABLE_SUFFIX BETWEEN '{start_suffix}' AND '{end_suffix}'
GROUP BY 1
ORDER BY active_users DESC
""",
    }


def run_bigquery() -> dict:
    from google.cloud import bigquery

    client = bigquery.Client(project=PROJECT_ID)
    dataset_id = find_analytics_dataset(client)
    print(f"[OK] Đã tìm thấy GA4 Dataset: {PROJECT_ID}.{dataset_id}")

    queries = build_queries(dataset_id, DATE_START, DATE_END)
    results = {
        "source": "google_bigquery_live",
        "fetched_at": datetime.now().isoformat(),
        "project_id": PROJECT_ID,
        "dataset_id": dataset_id,
        "date_range": {"start": "2026-11-04", "end": "2026-11-10"},
    }

    for key, sql in queries.items():
        print(f"[QUERY] Đang thực thi: {key} ...")
        job = client.query(sql)
        rows = [dict(row.items()) for row in job.result()]
        results[key] = rows
        print(f"  -> Thu được {len(rows)} dòng.")

    return results


def main():
    try:
        data = run_bigquery()
    except Exception as exc:
        print(f"[WARN] Không thể truy vấn trực tiếp BigQuery ({type(exc).__name__}: {exc})")
        print("[INFO] Sử dụng bộ số liệu GA4 7 ngày đã xác thực (Validated Snapshot) để xuất ga4_metrics_live.json.")
        data = {
            "source": "ga4_validated_report_snapshot",
            "fetched_at": datetime.now().isoformat(),
            "bigquery_status": f"{type(exc).__name__}: {exc}",
            **GA4_REPORT_BASELINE,
        }

    OUTPUT_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[DONE] Đã lưu dữ liệu GA4 tại: {OUTPUT_JSON}")
    print(json.dumps(data, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
