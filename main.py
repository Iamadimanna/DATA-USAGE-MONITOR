import psutil
import time
import tkinter as tk


def get_total_data_usage():
    total_data_sent = psutil.net_io_counters().bytes_sent
    total_data_received = psutil.net_io_counters().bytes_recv
    return total_data_sent + total_data_received


def convert_bytes_to_mb(bytes_value):
    mb_value = bytes_value / (1024 ** 2)
    return round(mb_value, 2)


def update_data_usage_label():
    current_data_usage = get_total_data_usage() - start_data_usage
    mb_data_usage = convert_bytes_to_mb(current_data_usage)
    data_usage_label.config(text=f"Data consumed: {mb_data_usage} MB")
    if not paused:
        logger.after(5000, update_data_usage_label)


def toggle_pause(button):
    global paused
    paused = not paused
    button.config(text="Continue" if paused else "Pause")
    if not paused:
        update_data_usage_label()


def main():
    global start_data_usage, paused, data_usage_label, logger, pause_button

    start_data_usage = get_total_data_usage()
    paused = False

    logger = tk.Tk()
    logger.title("Internet Data Consumption Monitor")

    data_usage_label = tk.Label(logger, text="", font=("Arial", 16))
    data_usage_label.pack(pady=20)

    pause_button = tk.Button(logger, text="Pause", width=10, command=lambda: toggle_pause(pause_button))
    pause_button.pack(pady=10)

    update_data_usage_label()

    logger.mainloop()


if __name__ == "__main__":
    main()
