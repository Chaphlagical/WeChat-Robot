import os
import cv2 as cv
import numpy as np

# Initialize the parameters
confThreshold = 0.5  #Confidence threshold
nmsThreshold = 0.4   #Non-maximum suppression threshold
inpWidth = 416       #Width of network's input image
inpHeight = 416      #Height of network's input image

def Yolo_img(msg):
    print(os.getcwd())
    if 'yolo' not in os.getcwd():
        os.chdir('./analysis/CV/yolo')
    msg.get_file(save_path="data/temp.jpg")
    msg.reply("Begin to detect object\nplease wait...")
    if os.system("./darknet detect cfg/yolov3.cfg yolov3.weights data/temp.jpg")==0:
        msg.reply_image("predictions.jpg")
    os.chdir('../../..')



def Yolo_video(msg):
    if 'yolo' not in os.getcwd():
        os.chdir('./analysis/CV/yolo')
    msg.get_file(save_path="data/temp.mp4")
    msg.reply("Begin to process the video\nplease wait...")
    classesFile = "data/coco.names"
    classes = None
    with open(classesFile, 'rt') as f:
        classes = f.read().rstrip('\n').split('\n')
    
    # Give the configuration and weight files for the model and load the network using them.
    modelConfiguration = "./cfg/yolov3.cfg"
    modelWeights = "yolov3.weights"
    
    net = cv.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
    net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)
    
    outputFile="./predictions.avi"
    cap = cv.VideoCapture("./data/temp.mp4")
    vid_writer = cv.VideoWriter(outputFile, cv.VideoWriter_fourcc('M','J','P','G'), 30, (round(cap.get(cv.CAP_PROP_FRAME_WIDTH)),round(cap.get(cv.CAP_PROP_FRAME_HEIGHT))))

    def getOutputsNames(net):
        # Get the names of all the layers in the network
        layersNames = net.getLayerNames()
        # Get the names of the output layers, i.e. the layers with unconnected outputs
        return [layersNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    def postprocess(frame, outs):
        frameHeight = frame.shape[0]
        frameWidth = frame.shape[1]
        # Scan through all the bounding boxes output from the network and keep only the
        # ones with high confidence scores. Assign the box's class label as the class with the highest score.
        classIds = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                classId = np.argmax(scores)
                confidence = scores[classId]
                if confidence > confThreshold:
                    center_x = int(detection[0] * frameWidth)
                    center_y = int(detection[1] * frameHeight)
                    width = int(detection[2] * frameWidth)
                    height = int(detection[3] * frameHeight)
                    left = int(center_x - width / 2)
                    top = int(center_y - height / 2)
                    classIds.append(classId)
                    confidences.append(float(confidence))
                    boxes.append([left, top, width, height])
        indices = cv.dnn.NMSBoxes(boxes, confidences, confThreshold, nmsThreshold)
        for i in indices:
            i = i[0]
            box = boxes[i]
            left = box[0]
            top = box[1]
            width = box[2]
            height = box[3]
            drawPred(classIds[i], confidences[i], left, top, left + width, top + height)
            
    def drawPred(classId, conf, left, top, right, bottom):
        # Draw a bounding box.
        cv.rectangle(frame, (left, top), (right, bottom), (0, 0, 255),2)
    
        label = '%.2f' % conf
    
        # Get the label for the class name and its confidence
        if classes:
            assert (classId < len(classes))
            label = '%s:%s' % (classes[classId], label)
        cv.putText(frame, label, (left, top), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255),2)
    
    while cv.waitKey(1) < 0:
        try:
            # get frame from the video
            hasFrame, frame = cap.read()
        
            # Create a 4D blob from a frame.
            blob = cv.dnn.blobFromImage(frame, 1 / 255, (inpWidth, inpHeight), [0, 0, 0], 1, crop=False)
        
            # Sets the input to the network
            net.setInput(blob)
        
            # Runs the forward pass to get output of the output layers
            outs = net.forward(getOutputsNames(net))
        
            # Remove the bounding boxes with low confidence
            postprocess(frame, outs)
        
            # Put efficiency information. The function getPerfProfile returns the
            # overall time for inference(t) and the timings for each of the layers(in layersTimes)
            t, _ = net.getPerfProfile()
    
            # Write the frame with the detection boxes
            vid_writer.write(frame.astype(np.uint8))
        except:
            break

    msg.reply_video("predictions.avi")
    os.chdir('../../..')

