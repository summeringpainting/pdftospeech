import os

# concat_str = ""
# for i in range(2, 345):
#     # print(f"{i}fun.wav", end=" ")
#     concat_str += f"{i}fun.wav "
# os.system(cmd)
proc = os.popen('ls -1v *fun.wav').read()

# print(proc)
procy = " ".join(proc.split())
# print(procy)

cmd = f"sox {procy} ../longy.wav"
os.system(cmd)
