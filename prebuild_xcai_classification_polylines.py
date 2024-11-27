import numpy as np
import cv2

img = cv2.imread('split_layers_out_parted/Mengmei_parted.jpg')

bbox = {
    "x": 483,
    "y": 263,
    "w": 52,
    "h": 66,
    "contour_index": 6,
    "area": 2351.0,
    "img": "part_6.png",
}

del bbox["img"]
del bbox["area"]
del bbox["contour_index"]

x, y, w, h = bbox["x"], bbox["y"], bbox["w"], bbox["h"]
green = (0, 255, 0)

pts = np.int32([[x, y], [x, y + h - 1], [x + w - 1, y + h - 1], [x + w - 1, y]]).reshape(-1, 1, 2)
cv2.polylines(img, [pts], isClosed=True, color=green, thickness=2)

cv2.imwrite('split_layers_out_parted/Mengmei_parted_polylines.jpg', img)