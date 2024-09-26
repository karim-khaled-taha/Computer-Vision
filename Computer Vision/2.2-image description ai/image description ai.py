import cv2
import google.generativeai as genai
from PIL import Image
import os

API_KEY = "AIzaSyDcINe2istQgMnX3B8Rp-XkzDp-_w086K8"

# Setup the LLM API
genai.configure(api_key=API_KEY)
llm_model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")

# Initialize the answer variable
answer = ""
response_text = ""

# Define the directory to save images
save_dir = "image_save"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

image_counter = 0  # To count and name images

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (1280, 720))
    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Check if the 'z' key is pressed
    key = cv2.waitKey(1)
    if key == ord('z'):
        # Convert frame to PIL image
        pil_image = Image.fromarray(framergb)

        # Save the image
        image_path = os.path.join(save_dir, f"image_{image_counter}.png")
        pil_image.save(image_path)
        print(f"Image saved at: {image_path}")

        # Generate content based on the image
        response = llm_model.generate_content(["Describe the image for blind people.", pil_image])
        
        # Print the description generated
        print("\nresponse:\n" + response.text)

        # Save the description to a text file
        description_path = os.path.join(save_dir, f"description_{image_counter}.txt")
        with open(description_path, 'w') as desc_file:
            desc_file.write(response.text)
        
        print(f"Description saved at: {description_path}")

        image_counter += 1  # Increment image counter for naming subsequent images

    # Display the frame
    cv2.imshow("Frame", frame)

    # Exit when 'ESC' key is pressed
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
