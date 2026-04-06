def make_logger(level):
    level = level.upper()
    def log(msg):
        print(f"[{level}] {msg}")
    return log

# logger = make_logger("info")
# logger("Hello, world!")