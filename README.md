# distributed-web-scraper

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Celery](https://img.shields.io/badge/Celery-distributed-37814A.svg)](https://docs.celeryq.dev/)

Built this to handle massive data extraction tasks without getting blocked. Pushing the core worker logic here.

It's a distributed web scraping cluster using Python, Celery, and Redis. I needed to pull structured data from about 50 different target sites every day, which meant processing over 1 million requests daily.

The tricky part was avoiding IP bans and CAPTCHAs. I built a proxy manager that rotates through a pool of proxies, spoofs User-Agents, and adds jitter to the request timing. It maintains about a 98% success rate against standard anti-bot measures.

Data gets dumped into a PostgreSQL database. I had to use GIN and B-tree indexes and partition the tables by month because the dataset quickly blew past 500 million rows and queries were crawling.

The scraper.py file contains the core Celery task logic and proxy rotation mechanism. You can run it directly to see a simulation of the worker execution and success rate metrics.

```bash
python scraper.py
```
