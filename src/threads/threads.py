import threading


class SumThread(threading.Thread):
    def __init__(self, low, high):
        super().__init__()
        self.low = low
        self.high = high
        self.total = 0

    def run(self):
        print('Start: {}'.format(self.getName()))
        for i in range(self.low, self.high):
            self.total += i
        print('Finished: {}, total: {}'.format(self.getName(), self.total))


threads = []

for i in range(10):
    low = i * 1000000
    high = low + 1000000
    thread = SumThread(low, high)
    threads.append(thread)

for thread in threads:
    thread.start()

print('All threads started\n')

for thread in threads:
    thread.join()

print('All threads finished\n')

result = 0
for thread in threads:
    result += thread.total

print(result)
