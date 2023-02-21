cd $1
python3 converter.py
echo "Start Compiling..."
python3 -m tvm.driver.tvmc compile --target="ethos-n -variant=n78 -tops=4 -ple_ratio=4, llvm -device=arm_cpu -mtriple=aarch64-linux-gnu -mcpu=cortex-a55 -mattr=+neon"  --output ./$1.tar ./$1.tflite 
cd ..
