Step to run application locally:
Step 1:	Create the copy of the project.
Step 2: Open command prompt and change your current path
to folder where you can find 'app.py' file.
Step 3: Create environment by command given below-
conda create -name <environment name>
Step 4: Activate environment by command as follows-
conda activate <environment name>
Step 5: Install tesseract using windows installer available at: https://github.com/UB-Mannheim/tesseract/wiki
Step 6: Note the tesseract path from the installation. Default installation path at the time of this edit was: C:\ProgramFiles\Tesseract-OCR. It may change so please check the installation path.
Step 7: pytesseract.pytesseract.tesseract_cmd = r'C:\ProgramFiles\Tesseract-OCR\tesseract.exe'
Step 8: Use command below to install required dependencies-
python -m pip install -r requirements.txt
Step 9: Run application by command-
python app.py
You will get url copy it and paste in browser.
Step 10: You have sample_data folder where you can get images to test.
