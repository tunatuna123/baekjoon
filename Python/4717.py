while True:
    num = float(input())
    if num < 0:
        break
    print(f"Objects weighing {num:.2f} on Earth will weigh {num*0.167:.2f} on the moon.")