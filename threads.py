import random
from collections import Counter
from threading import Thread, Lock


def set_mode():
    if random.random() < 0.25:
        return 1
    else:
        return 0

class Node(Thread):
    def __init__(self, i):
        super().__init__()
        self.one_vote = []
        self.votes = []
        self.lock = Lock()
        self.stop_flag = False
        self.number = i
        self.name = "Node_" + str(self.number + 1)
        self.value = random.randint(0, 1)
        self.mode = set_mode()
        self.decisionList = []
        self.finalDescision = -1

    def run(self):
        print(self.name + " -> chose: " + str(self.value) + " is he broken? " + ("false", "true") [self.mode > 0] + "\n")

    def send(self, data, name):
        self.lock.acquire()
        if name != self.name:
            print(name + " -> " + str(self.name) + " Data: " + str(data))
        self.one_vote.append(data)
        self.lock.release()

    def send_vector(self, one_vote, name):
        self.lock.acquire()
        if name != self.name:
            print(name + " -> " + str(self.name) + " Data: " + str(one_vote))
        self.votes.append(one_vote)
        self.lock.release()

    def stop(self):
        self.stop_flag = True

    def get_info(self):
        self.lock.acquire()

        print(self.name + "\nDecision array: ")
        for i in self.votes:
            print(str(i))

        # przygotowanie danych
        preparedData = []
        for column in zip(*self.votes):
            modified_column = [value for value in column]
            preparedData.append(modified_column)

        # ustalanie konsensusu z otrzymanych informacji
        for list in preparedData:
            #  myczek do znalezienia najszęstszego głosu
            # TODO co robic w przypadku remisu w głosowaniu
            count = Counter(list)
            mostCommonElement = max(count, key=count.get)
            self.decisionList.append(mostCommonElement)

        print("Readed votes from decision array: " + str(self.decisionList))
        count = Counter(self.decisionList)
        mostCommonElement = max(count, key=count.get)
        self.finalDescision = mostCommonElement
        print("Final decision: " + str(self.finalDescision))
        self.lock.release()

    def set_val(self, x):
        self.value = x
