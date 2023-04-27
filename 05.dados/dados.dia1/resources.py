from subprocess import check_output
from time import sleep


def cpu_read():
    cpu_information = check_output("lscpu").decode("UTF-8").split("\n")

    desired_info = [
        "model name",
        "cpu(s)",
        "cpu mhz",
        "l1d",
        "l1i",
        "l2",
        "l3",
    ]

    for info in cpu_information:
        for desired in desired_info:
            if info.lower().startswith(desired):
                print(info)

    print("=" * 35)


def memory_read():
    memory_info = [
        information
        for information in check_output("free")
        .decode("UTF-8")
        .split("\n")[1]
        .split(" ")
        if information != ""
    ]

    total_memory = int(memory_info[1]) / 1000
    used_memory = int(memory_info[2]) / 1000

    return total_memory, used_memory


def main():
    print("=" * 35)
    counter = 0
    while True:
        total_memory, used_memory = memory_read()
        sleep(1)
        print(f"total = {total_memory}MB")
        print(f"em uso = {used_memory}MB")
        print("=" * 35)
        counter += 1
        if counter == 5:
            break


if __name__ == "__main__":
    main()
