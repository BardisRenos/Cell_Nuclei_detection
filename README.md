# Cell_Nuclei_detection

## Into

In this repo will show the ability of image preprocessing to detect and mark cell of human tissue. 

The two below images are an example of image tissue and with which will work with.

<img src="https://github.com/BardisRenos/Cell_Nuclei_detection/blob/main/sample_2.png" width="300"/> <img src="https://github.com/BardisRenos/Cell_Nuclei_detection/blob/main/sample_3.png" width="300"/>


## Image steps to Preprocess 

### Image manipulation

```python

  def image_preprocessing(given_image):
    image_gray_scale = convert_to_gray_scale(given_image)
    _, image_threshold_bw = cv2.threshold(image_gray_scale, 100, 255, cv2.THRESH_OTSU)

    kernel = np.ones((3, 3), np.uint8)
    image_morph = cv2.morphologyEx(image_threshold_bw, cv2.MORPH_CLOSE, kernel, iterations=3)
    image_mask = 255 - image_morph

    background = cv2.dilate(image_mask, kernel, iterations=2)

    dist_transform = cv2.distanceTransform(image_mask, cv2.DIST_L2, 3)
    _, foreground = cv2.threshold(dist_transform, 0.285 * dist_transform.max(), 255, 0)
    the_unknown_image = background - foreground
    foreground = np.uint8(foreground)

```

### Image markers


```python
def markers_creation(foreground, the_unknown_image):
    _, image_markers = cv2.connectedComponents(foreground, connectivity=8)
    image_markers = image_markers + 10
    image_markers[the_unknown_image == 255] = 0

    show_image_with_matplot(image_markers)
    return image_markers

```

### Image watershed

In the study of image processing, a watershed is a transformation defined on a grayscale image. The name refers metaphorically to a geological watershed, or drainage divide, which separates adjacent drainage basins. The watershed transformation treats the image it operates upon like a topographic map, with the brightness of each point representing its height, and finds the lines that run along the tops of ridges. [link](https://en.wikipedia.org/wiki/Watershed_(image_processing))

```python 
def watershed(pure_image, image_markers):
    image_markers = cv2.watershed(pure_image, image_markers)
    pure_image[image_markers == -1] = [0, 255, 0]
    image_label2rgb = color.label2rgb(image_markers, bg_label=0)

    plot_an_image(pure_image)
```


## Plotting the image stages 

<p align="center"> 
<img src="https://github.com/BardisRenos/Cell_Nuclei_detection/blob/main/Screenshot%20from%202021-01-17%2020-07-51.png" width="900" height="650" style=centerme>
</p>



## Ploting the final detection picture
