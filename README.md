# Projector-Camera-Calibration
Using structured light to perform Projector-Camera Calibration. The code here is forked from the following git https://github.com/kamino410/procam-calibration


Inorder to generate the graycode patterns for projector of resolution M,N
```
python gen_graycode_imgs.py <projector_pixel_height> <projector_pixel_width> [-graycode_step <graycode_step(default=1)>]

#For the images given here use
python gen_graycode_imgs.py 256 256 -graycode_step 1

```

After the graycode pattern has been generated project that into the scene and capture the images and store in the format mentioned in the code.


Calibrate the projector-camera system, using the following command

```
python calibrate.py <projector_pixel_height> <projector_pixel_width> <num_chess_corners_vert> <num_chess_corners_hori> <chess_block_size> <graycode_step> [-black_thr <black_thr(default=40)>] [-white_thr <white_thr(default=5)>]

#For the images given here use
python3 calibrate.py 256 256 3 3 30 1 -black_thr 40 -white_thr 5


```
