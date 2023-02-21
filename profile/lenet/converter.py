data_type = 'uint8' # input's data type
img_name = './test_pic.jpeg'

batch_size = 1
num_class = 1000
image_dimention = 3
image_shape = (227,227)
data_shape = (batch_size,) + image_shape + (image_dimention,)
out_shape = (batch_size, num_class)



from PIL import Image
import numpy as np

# load image
image = Image.open('./test_img.jpg').resize((28,28))
x = np.array(image).astype('uint8')
data = np.reshape(x, (1,28,28,1))
np.savez("image",input_1=data)
