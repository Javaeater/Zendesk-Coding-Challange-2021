#File used to decode authentication info
import base64

#Decode email from base64
base64_message = "Y2Vzc2VyamFja3NvbkBnbWFpbC5jb20="
base64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
emailA = message_bytes.decode('ascii')

#Decode token from base64
base64_message = "RzRueU5GQnNTR29ORmZlVjNpTFU2QXVUaktuNWhOSzJmNHVWYXRreQ=="
base64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
tok = message_bytes.decode('ascii')

#decode password from base64
base64_message = "emNjamF2YWVhdGVy"
base64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
passWd = message_bytes.decode('ascii')