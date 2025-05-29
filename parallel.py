from time import perf_counter 
from threading import Thread
from random import randint


def task(id):
    lst = [randint(-10, 10) for i in range(100)] 
    with open(f'file{id}.txt', 'w') as f:
        f.writelines(str(lst))


start_time = perf_counter()

# создаем и запускаем 10 потоков
threads = []
for n in range(1, 11):
    t = Thread(target=task, args=(n,))
    threads.append(t)
    t.start()

# ждем, когда потоки выполнятся
for t in threads:
    t.join()

end_time = perf_counter()

print(f'Выполнение заняло {end_time- start_time: 0.2f} секунд.')
#[1]https://codechick.io/tutorials/python/python-threading
#[2]https://ru.stackoverflow.com/questions/565846/%D0%9A%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D1%81%D0%BF%D0%B8%D1%81%D0%BE%D0%BA-%D0%B8%D0%B7-%D1%81%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D1%8B%D1%85-%D1%86%D0%B5%D0%BB%D1%8B%D1%85-%D1%87%D0%B8%D1%81%D0%B5%D0%BB-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D1%83%D1%8F-%D1%81%D0%BF%D0%B8%D1%81%D0%BA%D0%BE%D0%B2%D0%BE%D0%B5-%D0%B2%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D0%B5