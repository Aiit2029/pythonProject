import asyncio


async def func():
    print('start')
    await asyncio.sleep(1)
    print('finish')

loop = asyncio.get_event_loop()


loop.run_until_complete(func())