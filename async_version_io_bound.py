import time
import httpx
import asyncio

from typing import Tuple

Urls = Tuple[str]

urls = ("https://www.google.com",) * 50


async def async_send_request(count: int, url: str, client: httpx.AsyncClient) -> None:
    print(f"Sending request #{count}")
    response = await client.get(url)
    print(f"got response for request {count}, status code: {response.status_code}")


async def main_asyncio(in_urls: Urls = urls):
    async with httpx.AsyncClient() as client:
        async with asyncio.TaskGroup() as tg:
            [tg.create_task(async_send_request(count, url, client)) for count, url in enumerate(in_urls)]


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main_asyncio(urls))
    sync_duration = time.perf_counter() - start
    print(f"Synchronization took {sync_duration} seconds")
