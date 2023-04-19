import random
import time
from threading import Thread, Lock, Event


def set_mode():
    if random.random() < 0.3:
        return 1
    else:
        return 0


class General(Thread):
    def __init__(self, i):
        super().__init__()
        self.one_vote = []
        self.votes = []
        self.lock = Lock()
        self.stop_flag = False
        self.number = i
        self.name = "General_" + str(self.number + 1)
        self.value = random.randint(0, 1)
        self.mode = set_mode()

    def run(self):
        print(self.name + " -> Vote: " + str(self.value) + " Mode: " + str(self.mode) + "\n")
        # while not self.stop_flag:
        #     self.lock.acquire()
        #     if self.one_vote:
        #         print(self.name + " Data: " + str(self.one_vote))
        #     self.lock.release()

    def send(self, data):
        self.lock.acquire()
        # print("Send: " + str(data) + " T: " + str(self.name))
        self.one_vote.append(data)
        self.lock.release()

    def send_vector(self, one_vote):
        self.lock.acquire()
        # print("Send: " + str(one_vote) + " T: " + str(self.name))
        self.votes.append(one_vote)
        self.lock.release()

    def stop(self):
        self.stop_flag = True

    def get_info(self):
        self.lock.acquire()

        print(self.name + "\nData: ")
        for i in self.votes:
            print(str(i))
        self.lock.release()

    def set_val(self, x):
        self.value = x
