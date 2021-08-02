#File used to decode authentication info
import base64

#Decode email from base64
base64_email = "Y2Vzc2VyamFja3NvbkBnbWFpbC5jb20="
base64_bytes = base64_email.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
emailA = message_bytes.decode('ascii')

#Decode token from base64
base64_token = "RzRueU5GQnNTR29ORmZlVjNpTFU2QXVUaktuNWhOSzJmNHVWYXRreQ=="
base64_bytes = base64_token.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
tok = message_bytes.decode('ascii')

#decode password from base64
base64_subD = "emNjamF2YWVhdGVy"
base64_bytes = base64_subD.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
domain = message_bytes.decode('ascii')