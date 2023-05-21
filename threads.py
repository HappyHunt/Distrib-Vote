import random
from collections import Counter
from threading import Thread, Lock


def set_mode():
    if random.random() < 0.3:
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
        self.decision_list = []
        self.final_decision = -1

    def run(self):
        print(self.name + " -> chose: " + str(self.value) + " is he broken? " + ("false", "true")[self.mode > 0] + "\n")

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
        prepared_data = []
        for column in zip(*self.votes):
            modified_column = [value for value in column]
            prepared_data.append(modified_column)

        # ustalanie konsensusu z otrzymanych informacji
        for list_of_vote in prepared_data:
            #  myczek do znalezienia najszęstszego głosu
            count = Counter(list_of_vote)
            most_common_element = max(count, key=count.get)
            self.decision_list.append(most_common_element)

        print("Readed votes from decision array: " + str(self.decision_list))
        count = Counter(self.decision_list)
        most_common_element = max(count, key=count.get)
        self.final_decision = most_common_element
        print("Final decision: " + str(self.final_decision))
        self.lock.release()

    def set_val(self, x):
        self.value = x
