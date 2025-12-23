import asyncio

async def work_data():
    await asyncio.sleep(2)
    return {'data': 'value'}
