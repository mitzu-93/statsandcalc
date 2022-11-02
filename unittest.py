import threading
import sys; sys.setswitchinterval(10 ** -10)

class Counter:
    def __init__(self, target):
        self.value = 0
        self.target = target
    def update(self):
        current_value = self.value
        # breakpoint()
        self.value = current_value + 1

    def run(self):
        threads = [threading.Thread(target=self.update) for _ in range(self.target)]
        for t in threads:
            t.start()
            for t in threads:
                t.join()