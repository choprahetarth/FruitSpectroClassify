import time
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from datetime import datetime


ENDPOINT = "https://fruit360.cognitiveservices.azure.com/"

# Replace with a valid key
project_id="239a1ed5-b4c0-4c57-b92c-03b0097aaa8e"
training_key = "72a9a9f87ee7484faa9343a727ac11de"
prediction_key = "90b75d8296474fe184e2c4d51c3a4adb"
prediction_resource_id = "/subscriptions/e85fff3e-6fea-46db-8ca2-4c3419470103/resourceGroups/cloud-shell-storage-centralindia/providers/Microsoft.CognitiveServices/accounts/Fruit360-Prediction"
publish_iteration_name = "classifyModel"
# Vision API Setup
trainer = CustomVisionTrainingClient(training_key, endpoint=ENDPOINT)
predictor = CustomVisionPredictionClient(prediction_key,endpoint = ENDPOINT)
project = trainer.get_project(project_id)

# define the retrain function
def retrainerFunction():
    # Now the code to start the training
    print("Training...")
    iteration = trainer.train_project(project.id)
    while (iteration.status != "Completed"):
            iteration = trainer.get_iteration(project_id, iteration.id)
            print("Trianing Status :" + iteration.status)
            time.sleep(1)
    # Now to Publish the trained Iteration
    trainer.publish_iteration(project.id, iteration.id, publish_iteration_name, prediction_resource_id)
    print ("Done!")

# define the predict function
def predictionFunction(filePath):
    # use the open object to open the image as binary 'rb' to the object image_contents
    with open(filePath, "rb") as image_contents:
        results = predictor.classify_image(
            project.id, publish_iteration_name, image_contents.read())
        # Display the results.
        for prediction in results.predictions:
            print("\t" + prediction.tag_name +
                  ": {0:.2f}%".format(prediction.probability * 100))

#def communicateToGUI():
#    imageSaved = 

def captureAndProcess():
    #now = datetime.now()
    #date_time = now.strftime("%m%d%Y%H%M%S")
    #tempVariable = '/picture'+date_time+'.jpg'
    #from picamera import PiCamera
    #from time import sleep
    #camera = PiCamera()
    #camera.start_preview()
    #sleep(5)
    #camera.capture(tempVariable)
    #camera.stop_preview()
    predictionFunction(tempVariable)
    #communicateToGUI()

# main function
if __name__ == "__main__":
    print("this is invoked automatically")
    captureAndProcess()
    #predictionFunction('/Users/hetarth/Desktop/example_code/aha.jpg')
    #anotherFunction()
