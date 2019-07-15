
async def download(url):
    return "bobbu"


async def download_url(url):
    #dosomething
    html = await download(url)

    return html

if __name__ == '__main__':
    coro = download_url("http://www.baidu.com")
    try:
        coro.send(None)
    except StopIteration as e:
        pass
