import os

for i in range(10):
    cmd = 'python main.py --model VGG19 --bs 64 --lr 0.01 --fold %d' %(i+1)
    os.system(cmd)
print("Train VGG19 ok!")

