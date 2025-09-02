import socket
import sys
import threading
from time import perf_counter
from queue import Queue
import signal

lock = threading.Lock()

host = "127.0.0.1"
portRange = range(1, 1025)
timeout = 0.5
port_queue = Queue()
stop_evt = threading.Event()

open_ports = []

def on_sigint(signum, frame):
  stop_evt.set()
  for _ in range(qtThread):
    port_queue.put(None)

def crawl(host, timeout):
  while True:
    currentPort = port_queue.get()
    if currentPort is None:
      port_queue.task_done()
      break
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
      rc = sock.connect_ex((host, currentPort))
      if rc == 0:
        with lock:
          open_ports.append(currentPort)
    finally:
        sock.close()
        port_queue.task_done()

def main(args):
  threads = []
  threads.clear()
  start_time = perf_counter()
  host = args[0]
  portRange = range(int(args[1]), int(args[2]))
  timeout = float(args[3])
  global qtThread
  qtThread = int(args[4])

  signal.signal(signal.SIGINT, on_sigint)

  for port in portRange:
    port_queue.put(port)

  for _ in range(qtThread):
    t = threading.Thread(target=crawl, args=(host, timeout))
    t.start()
    threads.append(t)

  for t in threads:
    t.join()


  print("---------------------")
  open_ports.sort()
  for openPort in open_ports:
    print(f"Porta {openPort}")

  print(f"--- {(perf_counter() - start_time)*1000:.2f} ms ---")


try:
  main([sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]])
except(KeyboardInterrupt):
  print("Finalizando programa...")
  sys.exit()
