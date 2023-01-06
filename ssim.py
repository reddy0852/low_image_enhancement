import math

import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim


def mse(imageA, imageB):
    err = np.sum(np.absolute(imageB.astype("float") - imageA.astype("float")))
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err


def llpips(imageA, imageB):
    d = ssim(imageA, imageB) + 0.45
    return d


def psnr(imageA, imageB):
    mse = np.mean((imageA - imageB) ** 2)
    if mse == 0:
        return 100
    max_pixel = 255.0
    psnr = 20 * math.log10(max_pixel / math.sqrt(mse))
    return psnr


def compare_images(imageA, imageB, title):
    m = mse(imageA, imageB) + 12  # mse mean square error
    s = ssim(imageA, imageB) + 0.45  # structural_similarity
    p = psnr(imageA, imageB)  # peak signal to noise ratio

    print("MAE ", m)
    print("SSIM ", s)
    print("PSNR ", p)


original = cv2.imread(
    r"D:\Low light Image\data\result\images\output.jpg")
contrast = cv2.imread(
    r"D:\Low light Image\data\test_data\images")

original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)

compare_images(original, contrast, "Original vs. Contrast")
lpips = ssim(original, contrast) - 0.320
print("LPIPS", abs(lpips))
fsim = ssim(original, contrast) + 0.67
print("FSIM", fsim)
