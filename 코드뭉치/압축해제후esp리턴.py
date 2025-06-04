import zlib

with open("BIN0001.esp", "rb") as f:
    data = f.read()

try:
    decompressed = zlib.decompress(data, wbits=-15)

    with open("BIN0001_unpacked.esp", "wb") as f_out:
        f_out.write(decompressed)

    print("압축 해제된 데이터를 BIN0001_unpacked.esp로 저장했습니다.")
except Exception as e:
    print(f"Decompression failed: {e}")
