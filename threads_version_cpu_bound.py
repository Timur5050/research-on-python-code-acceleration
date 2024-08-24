import time
import threading
from typing import Sequence, Tuple

SequenceInt = Sequence[int]
TupleIntDivisors = Tuple[int]

numbers = (
    1_111_111,
    2_222_222,
    3_333_333,
    4_444_444,
    5_555_555,
    6_666_666,
    7_777_777,
    8_888_888,
    9_999_999,
    6_123_123,
    9_123_434,
    1_432_543,
    1_000_000,
    2_000_000,
    3_000_000,
    4_000_000,
    5_000_000,
    6_000_000,
    7_000_000,
    8_000_000,
    9_000_000,
    7_433_123,
    7_343_123,
    2_423_435,
    5_000_999,
    6_432_523,
    3_414_341,
    7_985_345,
    7_098_145,
    7_901_123
)


def factorize_single(number: int) -> TupleIntDivisors:
    return tuple([x for x in range(1, number + 1) if number % x == 0])


def factorize_single_print(index: int, number: int) -> None:
    print(f"start task: {index}")
    divisors = factorize_single(number)
    print(f"result of task {index}: number - {number}, divisors - {divisors}")
    print("-" * 100)


def main_threads(in_numbers: SequenceInt = numbers) -> None:
    tasks = []
    for index, number in enumerate(in_numbers):
        tasks.append(
            threading.Thread(
                target=factorize_single_print,
                args=(index, number)
            )
        )
        tasks[-1].start()

    for task in tasks:
        task.join()


if __name__ == "__main__":
    start = time.perf_counter()
    main_threads(numbers)
    sync_duration = time.perf_counter() - start
    print(sync_duration)
