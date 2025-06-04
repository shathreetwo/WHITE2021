import zlib

def brute_force_deflate_stream(file_path):
    with open(file_path, "rb") as f:
        data = f.read()

    for i in range(len(data)):
        try:
            decompressed = zlib.decompress(data[i:], wbits=-15)
            print(f"[+] Success at offset {i}")
            # 저장하거나 확인
            with open("decompressed_output.txt", "wb") as out:
                out.write(decompressed)
            return
        except:
            continue

    print("[-] No valid deflate stream found.")

brute_force_deflate_stream("BIN0001.esp")

#파일 바이트를 0부터 끝까지 1바이트 단위로 이동하면서
#zlib.raw decompress 시도하는 코드
#실제 악성 EPS/PDF는 stream부터가 아니라
#몇 바이트 전에서 시작되는 경우가 많습니다.
