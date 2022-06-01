#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""importing modules"""
import time

import os
import cv2 as cv  # pylint: disable=import-error
import numpy as np  # pylint: disable=import-error

# import pkg_resources
import tensorflow as tf  # pylint: disable=import-error


root_dir = os.path.dirname(__file__)
model_path = os.path.normpath(root_dir + "/model/model_float16_quant.tflite")
img_path = os.path.normpath(root_dir + "/img/portrait.png")


def run_inference(interpreter, image, input_size=(512, 512)):
    """Pre process:Resize, BGR->RGB, PyTorch standardization, float32 cast"""
    # temp_image = copy.deepcopy(image)

    img_u_mat = image
    resize_image = cv.resize(img_u_mat, dsize=(input_size[0], input_size[1]))
    rgb_img = cv.cvtColor(resize_image, cv.COLOR_BGR2RGB)
    rgb_img = np.array(rgb_img, dtype=np.float32)

    mean = [0.485, 0.456, 0.406]
    std = [0.229, 0.224, 0.225]
    rgb_img = (rgb_img / 255 - mean) / std
    rgb_img = rgb_img.reshape((-1, input_size[0], input_size[1], 3)).astype("float32")

    # Inference
    input_details = interpreter.get_input_details()
    interpreter.set_tensor(input_details[0]["index"], rgb_img)
    interpreter.invoke()

    output_details = interpreter.get_output_details()
    result_map = interpreter.get_tensor(output_details[0]["index"])

    # Post process
    result_map = np.array(result_map).squeeze()
    result_map = 1 - result_map
    min_value = np.min(result_map)
    max_value = np.max(result_map)
    result_map = (result_map - min_value) / (max_value - min_value)
    result_map *= 255
    result_map = result_map.astype("uint8")

    return result_map


def resize_aspect_ratio(image, width=None, height=None, inter=cv.INTER_AREA):
    """resizing image with the aspect ratio"""
    (img_height, img_width) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        ratio = height / float(img_height)
        dim = (int(img_width * ratio), height)
    else:
        ratio = width / float(img_width)
        dim = (width, int(img_height * ratio))

    return cv.resize(image, dim, interpolation=inter)


def demo_main(image_path=img_path, show=True, image_data=None):
    """main function executing"""
    # Load model
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()

    start_time = time.time()

    if image_data is None:
        image_data = cv.imread(image_path)

    result_map = run_inference(interpreter, image_data)

    elapsed_time = time.time() - start_time

    # Inference elapsed time
    elapsed_time_text = "Elapsed time: "
    elapsed_time_text += str(round((elapsed_time * 1000), 1))
    elapsed_time_text += "ms"
    cv.putText(
        result_map,
        elapsed_time_text,
        (10, 30),
        cv.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        1,
        cv.LINE_AA,
    )
    # Map Resize
    resized_image = cv.resize(
        result_map, dsize=(image_data.shape[1], image_data.shape[0])
    )
    image_result = resize_aspect_ratio(resized_image, width=600)
    image_original = resize_aspect_ratio(image_data, width=600)

    if show:
        cv.imshow("U-2-Net Original", image_original)
        cv.imshow("U-2-Net Result", image_result)
        cv.waitKey(0)

    return image_result
