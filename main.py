import os

MAX_CHARS = 200

LINE = "At 3 a.m. my cat dropped a dead mouse on my chest like a waiter presenting the chef's special, then sat back waiting for a tip."


def main():
    assert 1 <= len(LINE) <= MAX_CHARS
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
