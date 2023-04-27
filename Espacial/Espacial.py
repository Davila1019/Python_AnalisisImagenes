import cv2
from PIL import Image

class Espacial:
    
    def __init__(self,image):
        self.image = image
        
    def segmentarImagen(self,u1,u2):
        image_gray =  cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        thresh, img_seg = cv2.threshold(image_gray, u1, u2, cv2.THRESH_BINARY)
        img = Image.fromarray(img_seg.astype('uint8')).convert('RGBA')
        #cv2.imshow("Segmentación",img_seg)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        
        return img