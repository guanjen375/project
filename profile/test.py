import numpy as np
import tflite_runtime.interpreter as tflite
import sys
import time

# Load TFLite model and allocate tensors.
# (if you are using the complete tensorflow package you can find load_delegate in tf.experimental.load_delegate)
armnn_delegate = tflite.load_delegate( library="/home/sunplus/armnn/build-tool/scripts/build/armnn/aarch64_build/delegate/libarmnnDelegate.so",
                                       options={"backends": "EthosNAcc,CpuAcc", "logging-severity":"info"})


# Delegates/Executes all operations supported by Arm NN to/with Arm NN
model_path = "/home/sunplus/profile/"+str(sys.argv[1])+"/"+str(sys.argv[1])+".tflite"
interpreter = tflite.Interpreter(model_path=model_path,experimental_delegates=[armnn_delegate])

interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Test model on random input data.
input_shape = input_details[0]['shape']
input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], input_data)
#time.sleep(30)
print("Start")
start = time.time()
interpreter.invoke()
print("End")
end = time.time()
print(end-start)
    

# Print out result
#output_data = interpreter.get_tensor(output_details[0]['index'])
#print(output_data)
