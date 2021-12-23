#!/usr/bin/python3
## Code by 2016152012 김세현

import docker
import os
import multiprocessing as mp

client = docker.from_env()
container_list = client.containers.list()
name_list = []

for c in container_list:
        name_list.append(c.name)
output = mp.Queue()

def stats(name):
        flag = False
        try:
                os.system('docker update --cpus=0.5 {}'.format(name))
                while True:
                        container = client.containers.get(name)
                        status = container.stats(decode=None, stream=False)
                        percent = calculate_percent(status)

                        if (flag == False) and (percent > 50.0):
                                os.system('docker update --cpus=1 {}'.format(name))
                                flag = True
                        if (flag == True) and (percent < 50.0):
                                os.system('docker update --cpus=0.5 {}'.format(name))
                                flag = False
        except KeyboardInterrupt:
                print('stopped')


def calculate_percent(status):
        cpu_count = len(status['cpu_stats']['cpu_usage']['percpu_usage'])
        cpu_percent = 0.0
        cpu_delta = float(status['cpu_stats']['cpu_usage']['total_usage']) - \
                float(status['precpu_stats']['cpu_usage']['total_usage'])

        system_delta = float(status['cpu_stats']['system_cpu_usage']) - \
                float(status['precpu_stats']['system_cpu_usage'])
        if system_delta > 0.0:
                cpu_percent = cpu_delta / system_delta * 100.0 * cpu_count
        print(cpu_percent)
        return cpu_percent


processes = [mp.Process(target=stats, args=(server,)) for server in name_list]

if __name__ == '__main__':
for p in processes:
                p.start()
        for p in processes:
                p.join()