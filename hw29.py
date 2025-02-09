import asyncio
import aiofiles
# ex 1


async def async_counter(n):
    for i in range(1, n+1):
        print(i)
        await asyncio.sleep(1)

asyncio.run(async_counter(5))

# ex 2


async def download_file_1():
    await asyncio.sleep(3)
    print("File 1 downloaded")


async def download_file_2():
    await asyncio.sleep(2)
    print("File 2 downloaded")


async def download_file_3():
    await asyncio.sleep(1)
    print("File 3 downloaded")


async def async_check():
    await asyncio.gather(download_file_1(), download_file_2(), download_file_3())

asyncio.run(async_check())

# ex 3


async def async_write_file(filename, text):
    async with aiofiles.open(filename, "w") as file:
        await file.write(text)
    print(f"Текст записан у {filename}")


async def async_read_file(filename):
    async with aiofiles.open(filename, "r") as file:
        data = await file.read()
    print(f"Вміст {filename}:\n{data}")


async def async_task():
    await asyncio.gather(
        async_write_file("file1.txt", "Це перший файл."),
        async_write_file("file2.txt", "Це другий файл."),
        async_write_file("file3.txt", "Це третій файл.")
    )

    await asyncio.gather(
        async_read_file("file1.txt"),
        async_read_file("file2.txt"),
        async_read_file("file3.txt")
    )

asyncio.run(async_task())