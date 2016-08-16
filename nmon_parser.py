from paramiko import SSHClient
from paramiko import AutoAddPolicy
from queue import Queue
import threading

# Fila onde ficara a stdout continua da Conexão SSH
ssh_queue_stdout = Queue()

# Definição da Função nmon_over_ssh que direciona a stdout para uma fila
def nmon_over_ssh():

    # Instanciando SSHClient
    ssh = SSHClient()

    # Carregando o known_hosts e adicionando entrada se necessário
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(AutoAddPolicy())

    # Estabelecendo a Conexão SSH
    ssh.connect('127.0.0.1', username='xpsroot', password='t1i5t1o0s')

    # Sequencia de comandos SSH para coleta do output do nmon
    ssh.exec_command("mkfifo /tmp/file.fifo")
    ssh.exec_command("nmon -f -t -s2 -F /tmp/file.fifo &")
    (stdin, stdout, stderr) = ssh.exec_command("cat /tmp/file.fifo")

    # Loop para adição de novas linhas na fila
    for line in iter(lambda: stdout.readline(2048), ""):
        ssh_queue_stdout.put(line.replace("\n",""))

# Função basica de manipulação da saida
def print_function():
        print("#########################################")
        print(ssh_queue_stdout.get().replace(",",";"))

def main():
    threads = []
    ssh_thread = threading.Thread(target=nmon_over_ssh)
    ssh_thread.daemon = True
    ssh_thread.start()
    threads.append(ssh_thread)

    while True:
        print_function()

main()
