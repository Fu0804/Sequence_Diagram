import base64

with open("Sequence_Diagram.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

with open("encoded_image.txt", "w") as text_file:
    text_file.write(encoded_string)
