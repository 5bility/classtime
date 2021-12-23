#!/usr/bin/python3
## Code by 2016152012 김세현

import docker
import os
import multiprocessing as mp
import time

client = docker.from_env()
container_list = client.containers.list()
name_list = []

for c in container_list:
        name_list.append(c.name)
output = mp.Queue()

def restart(name):
        try:
                while True:
                        container = client.containers.get(name)
                        print(name)
                        if (container.status == "exited"):
                                print("exited")
                                print("restarting container...")
                                os.system("docker start {}".format(name))
                        else:
                                print("running")
                        time.sleep(5)
        except KeyboardInterrupt:
                print('stopped')

processes = [mp.Process(target=restart, args=(server,)) for server in name_list]

if __name__ == '__main__':
        for p in processes:
                p.start()
        for p in processes:
                p.join()