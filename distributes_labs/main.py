import multiprocessing
import sys
import time


def is_odd(input: multiprocessing.Queue, output: dict, name: str):
    try:
        output[name] = 0
        while True:
            item = input.get()
            if item is None:
                break

            # Do some work here
            result = item % 2 == 0  # Example: check for oddness
            output[name] += result
    except KeyboardInterrupt:
        return  # Exit the process


def is_even(input: multiprocessing.Queue, output: dict, name: str):
    try:
        output[name] = 0
        while True:
            item = input.get()
            if item is None:
                break

            # Do some work here
            result = item % 2 == 1  # Example: check for evenness
            output[name] += result
    except KeyboardInterrupt:
        return  # Exit the process


def count_all(input: multiprocessing.Queue, output: dict, name: str):
    try:
        output[name] = 0
        while True:
            item = input.get()
            if item is None:
                break

            # Do some work here
            output[name] += 1    # Example: sum all numbers
    except KeyboardInterrupt:
        return  # Exit the process


def sum_all(input: multiprocessing.Queue, output: dict, name: str):
    try:
        output[name] = 0
        while True:
            item = input.get()
            if item is None:
                break

            # Do some work here
            output[name] += item    # Example: sum all numbers
    except KeyboardInterrupt:
        return  # Exit the process


def manager(output_dict):
    def log(output_dict):
        print('------------------')
        for key, value in output_dict.items():
            print(f'{key}: {value}')
        print('------------------')

    try:
        while True:
            time.sleep(5)
            log(output_dict)
    except KeyboardInterrupt:
        log(output_dict)
        return  # Exit the process


if __name__ == '__main__':
    input_queue = multiprocessing.Queue()
    output_dict = multiprocessing.Manager().dict()

    workers = [(is_odd, 'odd'), (is_even, 'even'), (count_all, 'count'), (sum_all, 'sum')]
    processes = []

    for (w, name) in workers:
        p = multiprocessing.Process(target=w, args=(input_queue, output_dict, name))
        p.start()
        processes.append(p)

    p = multiprocessing.Process(target=manager, args=(output_dict,))
    p.start()
    processes.append(p)

    try:
        while True:
            data = sys.stdin.buffer.read(2)
            number = int.from_bytes(data, 'big')
            for _ in range(len(workers)):
                input_queue.put(number)
    except KeyboardInterrupt:
        print("Interrupted by user, stopping workers...")
        for _ in range(len(workers)):
            input_queue.put(None)
        for p in processes:
            p.join()
        print("All workers stopped.")
