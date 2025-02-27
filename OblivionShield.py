
---

## **🔹 Step 3 – Uploading the Code (OblivionShield.py)**  

### **`OblivionShield.py` – The Code Itself**  
```python
import cc1101
import random
import time

FREQ_START = 300  # MHz
FREQ_END = 900  # MHz
JAM_POWER = -90  # Low-power noise injection

def adaptive_noise():
    """ Generates shifting RF noise to disrupt signal fingerprinting """
    while True:
        freq = random.randint(FREQ_START, FREQ_END)
        power_level = random.uniform(-100, JAM_POWER)
        cc1101.set_freq(freq)
        cc1101.set_power(power_level)
        cc1101.transmit(freq, b'\x00' * 5)  # Minimal pulse to blend with background noise
        time.sleep(random.uniform(1, 3))

def disrupt_scanners():
    """ Sends fake signal bursts to mislead RF detection systems """
    while True:
        freq = random.randint(FREQ_START, FREQ_END)
        cc1101.set_freq(freq)
        cc1101.transmit(freq, b'\xFF' * 8)  # Randomized interference burst
        print(f"[*] Disrupting scanners at {freq}MHz")
        time.sleep(random.uniform(5, 10))

def start_shield():
    """ Activates the RF cloaking system """
    print("[*] OblivionShield is active. Your presence is hidden.")
    adaptive_noise()
    disrupt_scanners()

start_shield()
# A presence that does not answer is a presence that cannot be found.
# A system that never speaks cannot be heard.
# If you never existed, how can they ever find you?
# - V
