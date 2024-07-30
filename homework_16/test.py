import time
import subprocess;
def measure_execution_time(script_path, num_runs=100):
    total_execution_time = 0
    for _ in range(num_runs):
        start_time = time.time()

        subprocess.run(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        end_time = time.time()
        execution_time = end_time - start_time
        total_execution_time += execution_time

    average_execution_time = total_execution_time / num_runs
    print(f"Среднее время выполнения скрипта ({num_runs} запусков): {average_execution_time:.6f} секунд")

if __name__ == "__main__":
    script_path = "work_with_list_comprehension.py"  # Путь к вашему скрипту
    measure_execution_time(script_path)
