#Library imports
import numpy as np
from fastapi import FastAPI, File, UploadFile, Response
from fastapi.responses import StreamingResponse, FileResponse
import numpy as np
import io
from PIL import Image
import cv2
from keras.models import load_model
import warnings
warnings.filterwarnings("ignore")


#Loading the Model
model = load_model('plant_disease.h5')

#Name of Classes
CLASS_NAMES = ['Corn-Common_rust', 'Potato-Early_blight', 'Tomato-Bacterial_spot']

app = FastAPI()

@app.get('/')
def home():
    return {'Title': 'Plant Disease Detection API with Keras'}

@app.post("/enhance")
async def root(file: UploadFile = File(...)):
    """
    The root function returns the prediction of an image using a pretrained model.

    Parameters:
        file (UploadFile): The image to be predicted. 
    Returns:
        result (str): The prediction of the image as a string.  

    Args:
        file:UploadFile=File(...): Specify that the file is uploaded as a multipart/form-data request

    Returns:
        The prediction of the model in json format
    """

    contents = io.BytesIO(await file.read())
    file_bytes = np.asarray(bytearray(contents.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    img = cv2.resize(img, (256,256))
    img.shape = (1,256,256,3)
    image = model.predict(img)
    result = CLASS_NAMES[np.argmax(image)]
    return (str("This is "+result.split('-')[0]+ " leaf with " + result.split('-')[1]))
