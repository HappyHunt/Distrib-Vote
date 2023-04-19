import random

from tr_general import General


def mian():
    print("Witaj w symulatorze!")
    print("Podaj liczbę wątków:")
    n = int(input())
    threads = []

    for i in range(n):
        threads.append(General(i))

    # threads.append(General(1))
    # threads[0].set_val(3)
    # threads.append(General(2))
    # threads[1].set_val(4)
    # threads.append(General(3))
    # threads[2].set_val(2)
    # threads.append(General(4))
    # threads[3].set_val(5)

    for t in threads:
        t.start()

    for t in threads:
        for tr in threads:
            if t.mode == 0:
                tr.send(t.value)
            else:
                tr.send(random.randint(0, 1))

    for t in threads:
        for tr in threads:
            if t != tr:
                tr.send_vector(t.one_vote)

    for t in threads:
        t.get_info()

    for t in threads:
        t.stop()

    for t in threads:
        t.join()


if __name__ == "__main__":
    mian()
