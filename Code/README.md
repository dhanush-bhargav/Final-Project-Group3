# **DATS 6303: Deep Learning Final Project**
## Real Life Violence detection from video

### Dataset
Real Life Violence Situations Dataset: https://www.kaggle.com/datasets/mohamedmustafa/real-life-violence-situations-dataset

### Pre-trained weights
Weights of the trained classifier with ResNet3D backbone is available [here](https://drive.google.com/file/d/1BWmsp_PVSEqfKwnlmHfZ_AW4ssw3Amu1/view?usp=sharing). Please request access to avail the weights.
Once downloaded, update the location in the config file at line:
```
[Inference]
...
model_path=[path to the downloaded weights]
```

### Running the Streamlit App
Modify the 'Streamlit' section in the config.conf file as follows:
```
[Streamlit]
temp_folder=[folder to store the uploaded videos and annotated results]
model_path=[path to downloaded weights]
device=[cuda if GPU is present, else cpu]
```

```shell
streamlit run frontend.py
```

### Obtaining the training data
Due to copyright and size restrictions, the dataset can not be uploaded in this repository.
Download the dataset from [here](https://www.kaggle.com/datasets/mohamedmustafa/real-life-violence-situations-dataset) and unzip it.
Update the following lines in config.conf file:
````
dataset_path=[root directory of dataset]
violence_directory=[directory name inside dataset_path where violent videos are stored]
non_violence_directory=[directory name inside dataset_path where non-violent videos are stored]
````

### Training the ResNet 3D model
To train the ResNet3D model, update the following part of config.conf:
```
[Training]
epochs=[Number of epochs you wish to train the model for]
model_save_path=[path to save model, example: model_resnet.pt]
device=[cuda if GPU is present, else cpu]
```
After making the above changes, run the following command in terminal
```shell
python video_resnet.py
```
This will automatically read the data, partition into it into `train` and `test`, train the model and provide the test results.
It will save the model weights at the specified path.

