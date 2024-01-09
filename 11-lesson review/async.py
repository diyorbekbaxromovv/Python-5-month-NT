import asyncio

async def index():
    print("salom")

async def index2():
    await asyncio.sleep(5)
    print("salom2")
    
async def index3():
    print('salom3')
    

async def main():
    task1 = asyncio.create_task(index())
    task2 = asyncio.create_task(index2())
    task3 = asyncio.create_task(index3())
    
    await asyncio.gather(task1, task2, task3)

asyncio.run(main())
