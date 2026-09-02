#!/usr/bin/env python3
import time
import traceback

def main():
    # Put your main logic here. Example:
    i = 0
    while True:
        i += 1
        print("Iteration", i)
        # simulate work
        time.sleep(5)
        # raise RuntimeError("boom")   # uncomment to test crash

if __name__ == "__main__":
    backoff = 1.0
    while True:
        try:
            main()
            # If main() returns normally and you want to exit, break here:
            # break
        except Exception:
            # log the exception and restart after a short backoff
            traceback.print_exc()
            print(f"Restarting in {backoff:.1f}s...")
            time.sleep(backoff)
            # exponential backoff up to a cap
            backoff = min(backoff * 2, 60.0)
        else:
            # If you want to restart even on clean exit, reset backoff and continue
            backoff = 1.0

