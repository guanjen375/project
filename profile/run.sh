echo "Start Running..."
python3 -m tvm.driver.tvmc run --print-time --profile --repeat 10 --inputs ./$1/image.npz --output prediction.npz ./$1/$1.tar 
