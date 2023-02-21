data_type = 'uint8' # input's data type
img_name = './test_pic.jpeg'

batch_size = 1
num_class = 1000
image_dimention = 3
image_shape = (300,300)
data_shape = (batch_size,) + image_shape + (image_dimention,)
out_shape = (batch_size, num_class)



from PIL import Image
import numpy as np

# load image
image_data = Image.open(img_name).resize(image_shape).convert('RGB')
image_data = np.array(image_data).astype('float32')
image_data = np.expand_dims(image_data, axis=0)
np.savez("image",images=image_data)
