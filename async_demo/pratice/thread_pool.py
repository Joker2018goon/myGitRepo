import requests
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

# urls = [
#     "http://baidu.com", "http://qq.com", "http://360.com", "http://baidu.com",
#     "http://qq.com", "http://360.com", "http://baidu.com", "http://qq.com",
#     "http://360.com"
# ]

urls = [
    "http://baidu.com", "http://qq.com", "http://360.com"
]

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)-10s: %(message)s')

def download(url):
    result = requests.get(url)
    return url, result.status_code


def main():
    with ThreadPoolExecutor(4,thread_name_prefix='Joker') as executor:
        # futures=[executor.submit(download,url) for url in urls]
        # for future in as_completed(futures):
        #     try:
        #         print(future.result())
        #     except Exception as e:
        #         print(e)
        futures_results=executor.map(download,urls,timeout=30)
        for future in futures_results:
            try:
                print(future)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    main()