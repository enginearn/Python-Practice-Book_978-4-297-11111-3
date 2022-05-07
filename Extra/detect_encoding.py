from chardet import detect
import codecs

file_name = "la_belle_fille_gono_kimyona_kokai.txt"

with open(file_name, "rb") as fn:
    bf = fn.read()
    enc_fn = detect(bf)
    print(f"エンコード: {enc_fn['encoding']}")

    # for line in bf.decode(encoding="utf-8"):
    #     print(line)


# with open("result.txt", "w", encoding="utf-8") as res:
#     sf = bf.decode(encoding="utf-8")
#     for line in sf:
#         res.write(line)

with codecs.open("result.txt", encoding="utf-8", errors="ignore") as res:
    # sf = bf.decode(encoding="utf-8")
    for line in bf:
        res.write(line)