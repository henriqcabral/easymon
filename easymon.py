from queue import Queue
import threading
import graph
import nmon_parser as nm


def test():
    print("Gosto do GIT so que nao")
  
def main():
    ssh

    threads = []
    ssh_thread = threading.Thread(target=nmon_over_ssh)
    ssh_thread.daemon = True
    ssh_thread.start()
    threads.append(ssh_thread)

    mygraph = graph()
    graph_thread = threading.Thread(target=mygraph.ploty_cpu_graph())
    graph_thread.daemon = True
    graph_thread.start()
    threads.append(graph_thread)

    while True:
        print_function()

main()
