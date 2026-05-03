"""
High-Performance Distributed Web Scraper
Python, Celery, Redis, PostgreSQL.
Aggregates data from 50+ sites with intelligent proxy rotation.
"""
import time
import random
from typing import Dict, Any

# Mock Celery App
class CeleryMock:
    def task(self, *args, **kwargs):
        def wrapper(func):
            return func
        return wrapper

app = CeleryMock()

class ProxyManager:
    """Intelligent proxy rotation and rate-limiting evasion."""
    def __init__(self):
        self.proxies = [
            "http://proxy1.example.com:8080",
            "http://proxy2.example.com:8080",
            "http://proxy3.example.com:8080",
            "http://proxy4.example.com:8080",
            "http://proxy5.example.com:8080"
        ]
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
        ]
        
    def get_proxy(self):
        return random.choice(self.proxies)
        
    def get_headers(self):
        return {
            "User-Agent": random.choice(self.user_agents),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5"
        }

@app.task(bind=True, max_retries=3)
def scrape_url(self, url: str) -> Dict[str, Any]:
    """Celery task to scrape a single URL."""
    proxy_manager = ProxyManager()
    
    proxy = proxy_manager.get_proxy()
    headers = proxy_manager.get_headers()
    
    print(f"[Worker] Scraping {url} via {proxy}")
    
    # Simulate network latency and anti-bot evasion delays
    time.sleep(random.uniform(0.5, 2.0))
    
    # Simulate a 2% failure rate (matching the 98% success rate metric)
    if random.random() < 0.02:
        print(f"[Worker] 403 Forbidden or CAPTCHA detected on {url}")
        raise Exception("Anti-bot measure triggered")
        
    # Mock extracted data
    data = {
        "url": url,
        "title": f"Extracted Title for {url}",
        "price": round(random.uniform(10, 1000), 2),
        "stock_status": random.choice(["In Stock", "Out of Stock"]),
        "timestamp": time.time()
    }
    
    # In reality, this would save to PostgreSQL here
    print(f"[Worker] Successfully extracted data from {url}")
    return data

def trigger_batch_job():
    """Simulate the master node triggering a daily batch."""
    print("Starting distributed scraping batch job (simulated 1M+ requests)...")
    
    # We'll just simulate a few for the demo
    target_urls = [f"https://target-site-{i}.com/product/{j}" for i in range(1, 5) for j in range(1, 4)]
    
    success_count = 0
    fail_count = 0
    
    for url in target_urls:
        try:
            result = scrape_url(url)
            success_count += 1
        except Exception as e:
            fail_count += 1
            
    total = success_count + fail_count
    success_rate = (success_count / total) * 100
    
    print("\n--- Batch Job Summary ---")
    print(f"Total URLs processed: {total}")
    print(f"Success count: {success_count}")
    print(f"Failure count: {fail_count}")
    print(f"Success Rate: {success_rate:.1f}%")

if __name__ == "__main__":
    trigger_batch_job()
