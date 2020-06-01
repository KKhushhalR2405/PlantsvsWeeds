# PlantsvsWeeds
Plants and weed classifier
-------------------------------------------------------------------------------------------------------------------------------------------
### Why is it important to detect weeds while they are still seedlings?

Successful cultivation of maize depends largely on the efficacy of weed control. Weed control during the first six to eight weeks after 
planting is crucial, because weeds compete vigorously with the crop for nutrients and water during this period. Annual yield losses occur 
as a result of weed infestations in cultivated crops. Crop yield losses that are attributable to weeds vary with type of weed, type of 
crop, and the environmental conditions involved. Generally, depending on the level of weed control practiced yield losses can vary from 
10 to 100 %. Rarely does one experience zero yield loss due to weeds... Yield losses occur as a result of weed interference with the 
crop's growth and development....This explains why effective weed control is imperative. In order to do effective control the first 
critical requirement is correct weed identification.

-------------------------------------------------------------------------------------------------------------------------------------------

**Dataset** : Get it [here](https://www.kaggle.com/vbookshelf/v2-plant-seedlings-dataset)

This dataset contains 5,539 images of crop and weed seedlings. The images are grouped into 12 classes as shown in the above pictures. 
These classes represent common plant species in Danish agriculture. Each class contains rgb images that show plants at different growth 
stages. The images are in various sizes and are in png format.

If you want to split the dataset into training, validation, and train set, use **split-folder** module.

```diff
pip install split-folder
```
To know how to use split-folder : https://pypi.org/project/split-folders/

----------------------------------------------------------------------------------------------------------------------------------------

To import the dataset directly into Goggle colab, refer [here](https://medium.com/analytics-vidhya/how-to-fetch-kaggle-datasets-into-google-colab-ea682569851a).

----------------------------------------------------------------------------------------------------------------------------------------

### Further Implementations

Starting a school or university project to create a dataset of crop and weed seedling images in a local farming community and then create a weed detection model based on your dataset and deploying the model as a web app so farmers can use it.

