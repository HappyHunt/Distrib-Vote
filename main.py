import random

from threads import Node


def mian():
    print("Symulation started!")
    print("Number of nodes: ")
    n = int(input())
    threads = []

    for i in range(n):
        threads.append(Node(i))

    for t in threads:
        t.start()

    for t in threads:
        for tr in threads:
            if t.mode == 0:
                tr.send(t.value, t.name)
            else:
                tr.send(random.randint(0, 1), t.name)

    for t in threads:
        for tr in threads:
            if t != tr:
                tr.send_vector(t.one_vote, t.name)

    for t in threads:
        t.get_info()

    for t in threads:
        t.stop()

    for t in threads:
        t.join()


if __name__ == "__main__":
    mian()
