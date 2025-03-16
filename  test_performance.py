# test_performance.py
import concurrent.futures
import time

import requests


def make_request(url):
    start = time.time()
    response = requests.get(url)
    end = time.time()
    return end - start


def test_concurrent_requests(url, num_requests):
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_requests) as executor:
        futures = [executor.submit(make_request, url) for _ in range(num_requests)]
        results = [
            future.result() for future in concurrent.futures.as_completed(futures)
        ]

    total_time = sum(results)
    avg_time = total_time / num_requests
    print(f"Total time: {total_time:.2f}s, Average time: {avg_time:.2f}s")
    return total_time, avg_time


if __name__ == "__main__":
    print("Testing WSGI (Gunicorn):")
    test_concurrent_requests("http://localhost:8000/sync/?sleep=1", 1000)

    print("Testing ASGI (Uvicorn):")
    test_concurrent_requests("http://localhost:8001/async/?sleep=1", 1000)
