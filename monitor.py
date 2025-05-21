# monitor.py
import psutil

def get_system_stats():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    return {"cpu": cpu, "memory": memory}

if __name__ == "__main__":
    stats = get_system_stats()
    print(f"CPU használat: {stats['cpu']}%")
    print(f"Memória használat: {stats['memory']}%")
