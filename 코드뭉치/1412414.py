import zlib

# 전체 데이터를 bytes로 변환 (예: data = bytes.fromhex("..."))

# '78 c9' 시작 위치 찾기
start = data.find(b'\x78\xC9')
if start == -1:
    print("zlib header not found")
    exit()

compressed_data = data[start:]

try:
    decompressed = zlib.decompress(compressed_data)
    print("Decompressed successfully")
    # print or save decompressed data
except zlib.error as e:
    print("zlib decompress failed:", e)
    # raw deflate (-15)로 시도
    try:
        decompressed = zlib.decompress(compressed_data, -15)
        print("Decompressed with raw deflate")
    except Exception as e2:
        print("raw deflate decompress failed:", e2)
