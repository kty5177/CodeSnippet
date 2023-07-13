import cv2

video_path = 'input.mp4'
save_video_path = 'output.mp4'
with open(video_path, 'rb') as wfile:
    ori_video = wfile.read()

with open(save_video_path, 'wb') as writefile :
    writefile.write(ori_video)

input_img_path = 'input.png'
save_img_path = 'output.jpg'

with open(input_img_path, 'rb') as wfile:
    img_byte = wfile.read()

img = cv2.imread(input_img_path)
_, img_byte2 = cv2.imencode('.jpg', img)

with open(save_img_path, 'wb') as writefile :
    writefile.write(img_byte2)

print(type(img_byte), type(img_byte2))

print(img_byte2)