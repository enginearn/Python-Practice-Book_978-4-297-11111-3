import b64
from b64 import encoder, decoder
from b64 import str_to_base64, base64_to_str

print(f"{type(b64.encoder)}")

print(f"{dir(b64.encoder)}")

input_word = "Python"
print(f"{encoder.str_to_base64(input_word)}")

print(f"{type(b64)}")
print(f"{dir(b64)}")
print(f"{b64.__path__}")

enc = encoder.str_to_base64(input_word)
print(f"文字列({input_word})からbytes型: {enc}")

dec = decoder.base64_to_str(enc)
print(f"bytes型({enc})から文字列: {dec}")

print(dir(b64))