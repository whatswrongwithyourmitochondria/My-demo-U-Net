"""importing modules"""
import os
import cv2 as cv
import demo


base_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(os.path.abspath("../tests"))
img_path = os.path.normpath(root_dir + "/demo/img/portrait_result.png")
img_path_original = os.path.normpath(root_dir + "/demo/img/portrait.png")
print(img_path)


def test_image_regression():
    """visual regression test checks that we'll always get the same result"""
    standard_sample = cv.imread(img_path)
    gray_std_sample = cv.cvtColor(standard_sample, cv.COLOR_BGR2GRAY)
    duplicate_sample = demo.demo_main(img_path_original, show=False)

    assert gray_std_sample.shape == duplicate_sample.shape

    difference = cv.subtract(gray_std_sample, duplicate_sample)

    assert cv.countNonZero(difference) == 0


def test_no_error_big_small():
    """We should be sure that our algorithm works without
    any errors with the images of different sizes"""
    demo.demo_main(
        os.path.normpath(root_dir + "/demo/img/anastasia_big.png"), show=True
    )
    demo.demo_main(
        os.path.normpath(root_dir + "/demo/img/anastasia_big.png"), show=True
    )
