import json, time, hashlib
print("🧬 [COVER FORGE THỨC TỈNH] Lò Bào Chế XOR sẵn sàng phóng thích 4 biến dị.")
# Thực nghiệm bất biến đại số XOR
a = 0b10101010
b = 0b11001100
reverted = (a ^ b) ^ b
assert reverted == a, "Lỗi đối xứng đại số XOR!"
print("✨ Thuật toán XOR tự nghịch đảo A ^ B ^ B == A bảo toàn 100%!")
