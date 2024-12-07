import streamlit as st
import os
import torch
from inference_and_annotate import annotate_video  # Import the annotate_video function
from video_resnet import ViolenceClassifier  # Import the ViolenceClassifier
import shutil
from run_inference import ViolenceClassifierInference, get_clips, stitch_clips_with_annotations
import configparser

config = configparser.ConfigParser()
config.read("config.conf")

# Streamlit UI setup
st.set_page_config(page_title="Violence Detection", page_icon=":movie_camera:")

# Set constants
TEMP_VIDEO_PATH = "temp_video.mp4"
ANNOTATED_VIDEO_PATH = "annotated_video.mp4"
MODEL_PATH = "model_resnet.pt"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

inference_engine = ViolenceClassifierInference()

# Streamlit UI
st.title("Violent vs Non-Violent Video Classification with Annotation")

uploaded_video = st.file_uploader("Upload a video (mp4 format)", type=["mp4"])

if uploaded_video is not None:
    with open(TEMP_VIDEO_PATH, "wb") as f:
        f.write(uploaded_video.read())

    st.write("Processing the uploaded video...")

    # Perform annotation and classification
    try:
        clips = get_clips(TEMP_VIDEO_PATH)
        video_name = os.path.basename(TEMP_VIDEO_PATH)
        output = inference_engine.infer(clips)

        output_folder = config["Inference"]["output_dir"]

        stitch_clips_with_annotations(clips, output, ANNOTATED_VIDEO_PATH, fps=30)

        st.success("The video has been processed and annotated successfully!")

        # Display annotated video
        st.video(ANNOTATED_VIDEO_PATH)

    except Exception as e:
        st.error(f"Error during video processing: {e}")
