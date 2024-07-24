import time
import asyncio

async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования")
    for i in range(5):
        print(f'Силач {name} поднял {i+1} шар')
        await asyncio.sleep(1/power)
    print(f"Силач {name} закончил соревнования")
    return 0

async def start_tournament():
    strongman1 = asyncio.create_task(start_strongman('Pasha', 3))
    strongman2 = asyncio.create_task(start_strongman('Denis', 4))
    strongman3 = asyncio.create_task(start_strongman('Apollon', 5))
    await strongman1
    await strongman2
    await strongman3
    return 0

asyncio.run(start_tournament())