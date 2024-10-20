import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for i in range(1, 6):
        await asyncio.sleep(1 / power)  # Задержка обратно пропорционально силе
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    # Создаем три задачи для разных силачей
    tasks = [
        asyncio.create_task(start_strongman('Pasha', 3)),
        asyncio.create_task(start_strongman('Denis', 4)),
        asyncio.create_task(start_strongman('Apollon', 5)),
    ]

    # Ожидаем завершения всех задач
    await asyncio.gather(*tasks)

# Запуск асинхронной функции
if __name__ == "__main__":
    asyncio.run(start_tournament())