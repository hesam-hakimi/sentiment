from concurrent.futures import ProcessPoolExecutor
import concurrent


def adds2(a):
    return a+2


if __name__ == '__main__':
    with ProcessPoolExecutor() as executer:

        result = [executer.submit(adds2, i) for i in range(1, 200)]

    for item in concurrent.futures.as_completed(result):
        print(item.result())
