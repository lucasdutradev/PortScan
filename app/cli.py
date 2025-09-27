import argparse
import ipaddress

def positive_int(val: str | int) -> int:
  if isinstance(val, str) and not val.isnumeric():
        raise argparse.ArgumentTypeError("should be numeric")

  number = int(val)
  if number <= 0:
    raise argparse.ArgumentTypeError("should be > 0")

  return number

def port_int(val: str | int) -> int:
  if isinstance(val, str) and not val.isnumeric():
      raise argparse.ArgumentTypeError("should be numeric")
  port = int(val)
  if not 1 <= port <= 65535:
    raise argparse.ArgumentTypeError("should be between 1... 65535")
  return port

def host_type(val: str) -> str:
  try:
    ipaddress.ip_address(val)
    return val
  except ValueError:
    if val.startswith(["http://", "https://"]):
      return val
    raise argparse.ArgumentTypeError("should be literal ip or hostname")

def build_parser() -> argparse.ArgumentParser:
  parse = argparse.ArgumentParser(
    prog="PortScan",
    description="My mini port scan"
  )

  parse.add_argument("--host", "-H", required=True, type=host_type, help="")
  parse.add_argument("--timeout", "-T", type=float, default=0.5, help="")
  parse.add_argument("--threads", "-TH", type=positive_int, default=10, help="")
  # parse.add_argument("--verbose", "-v", type=positive_int, default=10, help="")

  group = parse.add_mutually_exclusive_group(required=True)
  group.add_argument("--top-ports", type=positive_int, help="scan top N common ports")
  group.add_argument("--ports", "-p", nargs=2, metavar=("START", "END"), type=port_int, help="")

  return parse

def parse_args(argv):
  parser = build_parser()
  args = parser.parse_args(argv)

  if args.ports:
    start, end = args.ports
    if start >= end:
      parser.error("--ports(-p) should be with lass value first")
  return args
