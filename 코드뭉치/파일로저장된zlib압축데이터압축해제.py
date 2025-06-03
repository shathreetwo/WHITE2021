import zlib

# 압축된 바이너리 파일 읽기
with open("compressed_data.bin", "rb") as f:
    compressed_data = f.read()

# zlib 압축 해제
try:
    decompressed_data = zlib.decompress(compressed_data)
except zlib.error as e:
    print("압축 해제 중 오류 발생:", e)
    exit()

# 압축 해제된 데이터 파일로 저장
with open("decompressed_output.bin", "wb") as f:
    f.write(decompressed_data)

print("압축 해제 완료, decompressed_output.bin 파일 생성됨")
