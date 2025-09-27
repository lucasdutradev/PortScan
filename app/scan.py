import socket
import sys
import threading
from time import perf_counter
from queue import Queue
import signal
from .cli import parse_args

lock = threading.Lock()

host = "127.0.0.1"
portRange = range(1, 1025)
timeout = 0.5
stop_evt = threading.Event()

def on_sigint(signum, frame):
  stop_evt.set()

def crawl(host, timeout):
  while True:
    currentPort = port_queue.get(timeout=0.1)
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

def start_scan(host, portRange, timeout, qtThre):
  global qtThread, port_queue, open_ports
  port_queue = Queue()
  open_ports = []
  threads = []
  threads.clear()
  start_time = perf_counter()
  qtThread = qtThre

  signal.signal(signal.SIGINT, on_sigint)


  for port in range(portRange[0], portRange[1]):
    port_queue.put(port)

  for _ in range(qtThread):
    port_queue.put(None)

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


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    try:
      start_scan(args.host, args.ports, args.timeout, args.threads)
    except(KeyboardInterrupt):
      print("close program...")
      sys.exit()