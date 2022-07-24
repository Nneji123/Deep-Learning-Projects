#Library imports
import numpy as np
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import PlainTextResponse
import numpy as np
import io
from PIL import Image
import cv2
from keras.models import load_model
import warnings
warnings.filterwarnings("ignore")


#Loading the Model
model = load_model("./model/nike-adidas-classifier.h5")

#Name of Classes
CLASS_NAMES = ['Adidas', 'Nike']

app = FastAPI(
    title="Nike/Adidas Shoe Classifier API",
    description="""An API that utilises a Deep Learning model built with Keras(Tensorflow) to classify a sports shoe whether it's adidas or nike.""",
    version="0.0.1",
    debug=True,
)

@app.get("/", response_class=PlainTextResponse)
async def running():
    note = """
Nike/Adidas Shoe Classifier API 🙌🏻
Note: add "/docs" to the URL to get the Swagger UI Docs or "/redoc"
  """
    return note


favicon_path = "favicon.png"


@app.post("/predict")
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
    img = cv2.resize(img, (224,224))
    img.shape = (1,224,224,3)
    image = model.predict(img)
    result = CLASS_NAMES[np.argmax(image)]
    return f"This is a {result} shoe"
