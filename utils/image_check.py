import cv2
import numpy as np
import requests
from PIL import Image
from skimage.metrics import structural_similarity as ssim
from io import BytesIO

def download_image(url):
    response = requests.get(url)
    return cv2.cvtColor(np.array(Image.open(BytesIO(response.content))), cv2.COLOR_RGB2BGR)

def compare_images(img1_url, img2_url):
    try:
        img1 = download_image(img1_url)
        img2 = download_image(img2_url)
        grayA = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        score, _ = ssim(grayA, grayB, full=True)
        return score
    except:
        return 0.0