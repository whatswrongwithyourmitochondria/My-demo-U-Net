"""importing modules"""
import os
import cv2 as cv
from demo import demo


base_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(os.path.abspath("../tests"))

img_path = os.path.join(root_dir, os.path.normpath("./img/portrait_result.png"))
img_path_original = os.path.join(root_dir, os.path.normpath("./img/portrait.png"))
print(img_path)


def test_image_regression():
    """visual regression test checks that we'll always get the same result"""
    standard_sample = cv.imread(img_path)
    gray_std_sample = cv.cvtColor(standard_sample, cv.COLOR_BGR2GRAY)
    duplicate_sample = demo.demo_main(img_path_original, show=False)

    assert gray_std_sample.shape == duplicate_sample.shape

    difference = cv.subtract(gray_std_sample, duplicate_sample)

    assert cv.countNonZero(difference) == 0


test_image_regression()


def test_no_error_big_small():
    """We should be sure that our algorithm works without
    any errors with the images of different sizes"""
    demo.demo_main(
        os.path.join(root_dir, os.path.normpath("./img/anastasia_big.png")), show=True
    )
    demo.demo_main(
        os.path.join(root_dir, os.path.normpath("./img/anastasia_big.png")), show=True
    )
