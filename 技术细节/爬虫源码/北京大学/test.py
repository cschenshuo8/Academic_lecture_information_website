import os
from PIL import Image
import
from paddleocr import PaddleOCR, draw_ocr

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

def get_words(img, index):
    # Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
    # 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
    img_path = img
    result = ocr.ocr(img_path, cls=True)
    result = result[0]

    # 显示结果
    image = Image.open(img_path).convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    print(txts)
    dataframe = pd.DataFrame({'box': boxes, 'txt': txts, 'score': scores})
    dataframe.to_csv("Images/" + str(index) + ".csv")

get_words("Images/110.jpg", 110)