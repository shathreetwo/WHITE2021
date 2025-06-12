import base64
import zlib
import io

# 이중 인코딩된 Base64 문자열
compressed_b64 = (
    'BcG9CsIwEADgV5Hg0IJekASHbqK4WYcOXW5Jm6uN5I/0NPj2fl/TUz0+pzfNvBt+G1OAnhhGmq7eUeQWbqlGn4y9O0+NWJlz'
    'J6XScNZw0gqUlsYGFyGvWRzEnuK3u+RsDRvEh5tL2tLCiGMqFnFgU/iTEZcUObwKVO9F+wc='
)

# 디코딩
compressed_data = base64.b64decode(compressed_b64)

# zlib 압축 해제 (Deflate stream)
decompressed_data = zlib.decompress(compressed_data, -zlib.MAX_WBITS)  # raw deflate stream

# 결과 문자열로 디코딩
decompressed_text = decompressed_data.decode('ascii', errors='ignore')
decompressed_text[:1000]  # 미리보기 출력
