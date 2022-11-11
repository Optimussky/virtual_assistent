#pip install tqdm
import time

from tqdm import tqdm
for i in tqdm(range(1000),desc="Esta es mi progressbar y describe... nada"):
    time.sleep(0.01)