import cv2
import mediapipe as mp
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Get the default audio endpoint for volume control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Set the volume range (0.0 to 1.0)
MIN_VOLUME = 0.0
MAX_VOLUME = 1.0
VOLUME_STEP = 0.05  # Adjust the step size as needed

# Function to check if the hand is in a closed fist position
def is_closed_fist(landmarks):
    thumb_tip = landmarks[4]
    pinky_tip = landmarks[20]
    distance_threshold = 0.03
    
    distance = ((pinky_tip[0] - thumb_tip[0])**2 + (pinky_tip[1] - thumb_tip[1])**2)**0.5
    
    return distance < distance_threshold

# Function to check if the hand is in an open hand position
def is_open_hand(landmarks):
    thumb_tip = landmarks[4]
    pinky_tip = landmarks[20]
    distance_threshold = 0.1
    
    distance = ((pinky_tip[0] - thumb_tip[0])**2 + (pinky_tip[1] - thumb_tip[1])**2)**0.5
    
    return distance > distance_threshold

# Function to perform a task for an open hand
def perform_task_for_open_hand():
    print("Open Hand Recognized - Perform Task")

# Function to decrease the system volume
def decrease_volume():
    current_volume = volume.GetMasterVolumeLevelScalar()
    if current_volume > MIN_VOLUME:
        new_volume = max(current_volume - VOLUME_STEP, MIN_VOLUME)
        volume.SetMasterVolumeLevelScalar(new_volume, None)
        print("Volume Decreased")

# Function to check if the hand is making a peace sign
def is_peace_sign(landmarks):
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    distance_threshold = 0.1
    
    distance = ((middle_tip[0] - index_tip[0])**2 + (middle_tip[1] - index_tip[1])**2)**0.5
    
    return distance < distance_threshold

# Function to perform a task for a peace sign
def perform_task_for_peace_sign():
    print("Peace Sign Recognized - Perform Task")

# Function to increase the system volume
def increase_volume():
    current_volume = volume.GetMasterVolumeLevelScalar()
    if current_volume < MAX_VOLUME:
        new_volume = min(current_volume + VOLUME_STEP, MAX_VOLUME)
        volume.SetMasterVolumeLevelScalar(new_volume, None)
        print("Volume Increased")

# ... (similar definitions for other functions)

# Function to recognize hand signs and perform corresponding tasks
def recognize_hand_sign(image):
    results = hands.process(image)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Extract landmark positions
            landmarks = [(lm.x, lm.y) for lm in hand_landmarks.landmark]
            
            # Implement hand sign recognition logic
            if is_closed_fist(landmarks):
                decrease_volume()
            elif is_open_hand(landmarks):
                increase_volume()
            elif is_peace_sign(landmarks):
                perform_task_for_peace_sign()
            elif is_thumbs_up(landmarks):
                perform_task_for_thumbs_up()
            else:
                # Add more conditions for other hand signs
                pass

# ... (other functions remain unchanged)

# Function to start the main loop for capturing and processing video frames
def main():
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Flip the frame horizontally for a later selfie-view display
        frame = cv2.flip(frame, 1)

        # Convert the BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame and recognize hand sign
        recognize_hand_sign(rgb_frame)

        # Display the frame
        cv2.imshow("Hand Sign Recognition", cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2BGR))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
