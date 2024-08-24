import time
import httpx

from typing import Tuple

Urls = Tuple[str]

urls = ("https://www.google.com",) * 50


def send_request(count: int, url: str, client: httpx.Client):
    print(f"Sending request #{count}")
    response = client.get(url)
    print(f"got response for request {count}, status code: {response.status_code}")


def main_sync(in_urls: Urls = urls):
    with httpx.Client() as client:
        for num, url in enumerate(in_urls):
            send_request(num, url, client)


if __name__ == "__main__":
    start = time.perf_counter()
    main_sync(urls)
    sync_duration = time.perf_counter() - start
    print(f"Synchronization took {sync_duration} seconds")

