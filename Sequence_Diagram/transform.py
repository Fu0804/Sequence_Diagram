import xml.etree.ElementTree as ET
import base64

# 解析XML文件
tree = ET.parse('Sequence_Diagram.xml')
root = tree.getroot()

# 从XML提取Base64编码的图像数据
encoded_data = root.find('data').text

# 解码Base64字符串
image_data = base64.b64decode(encoded_data)

# 将解码后的图像数据保存为PNG文件
with open('output.png', 'wb') as file:
    file.write(image_data)

