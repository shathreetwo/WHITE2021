import zlib

with open("BIN0001.esp", "rb") as f:
    data = f.read()

try:
    decompressed = zlib.decompress(data, wbits=-15)
    print(decompressed.decode("latin1"))  # or 'utf-8', try both
except Exception as e:
    print(f"Decompression failed: {e}")
