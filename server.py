import torch
import torchvision
from PIL import *
import torchvision.transforms as transforms
import pickle
import torch.nn as nn
import torch.nn.functional as F
from PIL import *
import numpy as np
from flask import *
import requests
from io import BytesIO


class Net(nn.Module):
    
    def __init__(self):
        super(Net, self).__init__()
        
        self.conv1 = nn.Conv2d(3, 32, 3, stride=2, padding=1)
        self.conv2 = nn.Conv2d(32, 64, 3, stride=2, padding=1)
        self.conv3 = nn.Conv2d(64, 128, 3, padding=1)

        # pool
        self.pool = nn.MaxPool2d(2, 2)
        
        # fully-connected
        self.fc1 = nn.Linear(7*7*128, 500)
        self.fc2 = nn.Linear(500, num_classes) 
        
        # drop-out
        self.dropout = nn.Dropout(0.3)
    
    def forward(self, x):
        ## Define forward behavior
        x = F.relu(self.conv1(x))
        x = self.pool(x)
        x = F.relu(self.conv2(x))
        x = self.pool(x)
        x = F.relu(self.conv3(x))
        x = self.pool(x)
        
        # flatten
        x = x.view(-1, 7*7*128)
        
        x = self.dropout(x)
        x = F.relu(self.fc1(x))
        
        x = self.dropout(x)
        x = self.fc2(x)
        return x

model = pickle.load(open(r"saved_model\model_arc.pkl","rb"))
checkpoint = torch.load(r"D:\Projects\PlantsvsWeeds\saved_model\model_scratch.pt",map_location=torch.device('cpu'))
model.load_state_dict(checkpoint)



def type(image_path):
    class_names = [
         'Black-grass',
         'Charlock',
         'Cleavers',
         'Common Chickweed',
         'Common wheat',
         'Fat Hen',
         'Loose Silky-bent',
         'Maize',
         'Scentless Mayweed',
         'ShepherdтАЩs Purse',
         'Small-flowered Cranesbill',
         'Sugar beet']

    standard_normalization = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                                  std=[0.229, 0.224, 0.225])
    def load_input_image(img):
        image = img.convert('RGB')
        prediction_transform = transforms.Compose([transforms.Resize(size=(224, 224)),
                                         transforms.ToTensor(),
                                         standard_normalization])


        image = prediction_transform(image)[:3,:,:].unsqueeze(0)
        return image


    def predict_image(model, class_names, img):
        # load the image and return the predicted breed
        img = load_input_image(img)
        model = model.cpu()
        model.eval()
        idx = torch.argmax(model(img))
        return class_names[idx]

    def run_app(img):
        # img = Image.open(img)
        prediction = predict_image(model, class_names, img)
        return prediction
    p = run_app(image_path)

    return p

# print(type(image_path))

# --------------------------------------------- #
# ----------- Flask App Starts Here ----------- #
# --------------------------------------------- #

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def main():
    data = request.get_json()
    img_url=data["data"]
    response=requests.get(img_url)
    img_org=Image.open(BytesIO(response.content))
    output = type(img_org)
    return jsonify(output)



if __name__=="__main__":
    app.run(debug=True)