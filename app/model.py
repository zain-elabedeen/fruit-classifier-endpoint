import wandb
import os
import torch
from torch import nn
from torchvision import transforms
from torchvision.models import resnet18, ResNet

#todo: remember to delete the use of the 
# loadotenv and os.getenv entries 
# when we use the Docker image later
from loadotenv import load_env

load_env(file_loc='/workspaces/fruit-classifier-endpoint/app/.env')

MODELS_DIR = 'models'
MODEL_FILE_NAME = 'model.pth'

CATEGORIES = ["freshapples", "freshbanana", "freshoranges", 
              "rottenapples", "rottenbanana", "rottenoranges"]

#todo: delete 
#print(os.getenv('WANDB_API_KEY'))

def download_artifact():
    assert 'WANDB_API_KEY' in os.environ, 'Please enter WANDB_API_KEY as an environmental variable.'

    wandb.login() # here we get access to the artifact registry
    # go to your artifact registry to find this full path
    # antonios-org/banana_apple_orange/resnet18:v1
    wandb_org = os.environ.get('WANDB_ORG')
    wandb_project = os.environ.get('WANDB_PROJECT')
    wandb_model_name = os.environ.get('WANDB_MODEL_NAME')
    wandb_model_version = os.environ.get('WANDB_MODEL_VERSION')

    #here we reconstruct the artifact path
    artifact_path = f'{wandb_org}/{wandb_project}/{wandb_model_name}:{wandb_model_version}'
    artifact = wandb.Api().artifact(artifact_path, type='model')
    artifact.download(root=MODELS_DIR)


download_artifact()