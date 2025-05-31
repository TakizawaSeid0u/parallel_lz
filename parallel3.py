import asyncio as a
import random as r

async def Reading(f):
    rand = r.uniform(0.1, 5) 
    await a.sleep(rand) 
    print(f"Файл {f} был прочитан за {rand}")

async def skwabzi():
    files = 10  
    tusk = [Reading(f"file{i}") for i in range(1, 11)]
    await a.gather(*tusk)

a.run(skwabzi())