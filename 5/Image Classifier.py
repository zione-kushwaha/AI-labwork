import streamlit as st
import torch
import torchvision.transforms as transforms
from PIL import Image
from torch import nn
import io
import matplotlib.pyplot as plt 

# Define your class dictionary
class_names = {'Donuts': 0, 'French Fries': 1, 'Fried Rice': 2, 'Samosa': 3}
class_names_rev = {v: k for k, v in class_names.items()}  # Reverse the dictionary for easy lookup

# Load your trained model
from model import CustomCNN  # Import your model architecture
model = CustomCNN(num_classes=4)
model.load_state_dict(torch.load("models/modelv1.pth", map_location=torch.device('cpu'), weights_only=True))
model.eval()  # Set model to evaluation mode

# Define image transformations (same as during training)
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))  # Adjust for grayscale if needed
])

# Streamlit UI
st.title("Custom CNN Image Classifier")
st.write("Upload an image to get a prediction")

# Row 1: File uploader
with st.container():
    st.header("Step 1: Upload your Image")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

# Row 2: Display the image (if uploaded)
if uploaded_file is not None:
    with st.container():
        st.header("Step 2: Displaying the Image")
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

# Row 3: Prediction button and display prediction
if uploaded_file is not None:
    with st.container():
        if st.button("Predict"):
            # Transform the image
            image_tensor = transform(image).unsqueeze(0)  # Add batch dimension

            # Get the prediction
            with torch.no_grad():
                output = model(image_tensor)
                _, predicted_class = torch.max(output, 1)

            # Get the class name from the dictionary
            predicted_class_name = class_names_rev[predicted_class.item()]

            # Make the prediction visually appealing
            st.markdown(f"<h3 style='color: #4CAF50;'>Predicted class: {predicted_class_name}</h3>", unsafe_allow_html=True)
            

            # Add a confidence bar or probability chart
            probabilities = torch.nn.functional.softmax(output, dim=1).squeeze()
            fig, ax = plt.subplots()
            ax.bar(class_names_rev.values(), probabilities.tolist())
            ax.set_xlabel('Classes')
            ax.set_ylabel('Probabilities')
            st.pyplot(fig)
