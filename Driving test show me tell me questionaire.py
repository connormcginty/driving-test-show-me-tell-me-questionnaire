import random
import time
import os

# Function to clear the screen for a smoother experience
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Function to display answers without wrapping them
def print_answer(answer):
    MAX_LINE_LENGTH = 80  # Set maximum line length for answers
    for i in range(0, len(answer), MAX_LINE_LENGTH):
        print(answer[i:i + MAX_LINE_LENGTH])

questions_answers = {
    "SHOW Me Questions": {
        "How would you check the power steering is working?": {
            "correct": "Apply gentle pressure to the steering wheel while starting the engine; you should feel the steering become lighter as the power steering activates.",
            "incorrect": [
                "Check if the steering wheel locks up after turning the car on. If it doesn’t, the power steering is likely faulty.",
                "Try turning the wheel while driving in circles. If the wheel stays heavy, the power steering is broken.",
                "Perform a high-speed test by sharply turning the wheel while going at 50mph. If the wheel resists, it’s a sign of faulty power steering."
            ]
        },
        "How would you check the indicators are working?": {
            "correct": "Turn on the hazard warning lights and walk around the car to confirm all indicators are flashing.",
            "incorrect": [
                "Activate each indicator, then take a picture of the dashboard lights to ensure they’re working.",
                "Start the engine and press down on the gas pedal—if the dashboard lights up, your indicators are good to go.",
                "Drive at night with the indicators on and check the glow around the car to see if it's working properly."
            ]
        },
        "How would you check the handbrake for excessive wear?": {
            "correct": "Apply the handbrake. It should secure the car without requiring excessive movement and should have a little extra working travel.",
            "incorrect": [
                "Apply the handbrake and try to slide the car. If it moves even a little, the handbrake is too worn.",
                "With the car moving, pull the handbrake hard to see if it stops the car instantly. If not, the handbrake needs adjustment.",
                "After driving, attempt to pull the handbrake while in motion. If the car stops, it means the handbrake is fine."
            ]
        },
        "How would you check the horn is working?": {
            "correct": "Press the horn (off-road only) to confirm it is functioning.",
            "incorrect": [
                "Press the horn at various speeds and check if the sound changes pitch as you accelerate.",
                "Activate the horn when turning corners. If it sounds louder, the horn is in good condition.",
                "Press the horn for 30 seconds while stationary. If the sound fades after a few seconds, it needs to be replaced."
            ]
        },
        "How would you check the headlights and tail lights are working?": {
            "correct": "Turn on the lights, then walk around the car to make sure both the headlights and tail lights are on.",
            "incorrect": [
                "Activate the headlights and then step outside the car and stare directly at them for five seconds to check their intensity.",
                "Drive the car around a block with the headlights on and check if they illuminate any wildlife along the way.",
                "Turn on the headlights, then walk around the car in a circle while clapping loudly. The lights should flash back at you."
            ]
        },
        "How would you check the brake fluid reservoir is at a safe level?": {
            "correct": "Locate the brake fluid reservoir. Check that the fluid level is between the minimum and maximum markers. If it’s low, take the car to a garage.",
            "incorrect": [
                "Check the brake fluid while driving to see if it fluctuates. If it’s low while moving, stop immediately.",
                "If the brake fluid level goes above the maximum mark, the brakes will work better. A little overflow won’t hurt.",
                "The brake fluid should be checked during a long road trip. When you stop for fuel, glance at the reservoir and check its level."
            ]
        },
        "How would you check the windscreen washer reservoir?": {
            "correct": "Locate the washer reservoir and confirm it is topped up.",
            "incorrect": [
                "Shake the car gently while the engine is off and listen for a sloshing sound to check if the washer fluid is full.",
                "Activate the wipers and check if they move faster than usual. If they speed up, the washer fluid is full.",
                "Pour some windshield cleaner on the roof and check if it reaches the glass. If it doesn't, the reservoir is empty."
            ]
        },
        "How would you check the engine oil level?": {
            "correct": "Locate the dipstick, pull it out, and wipe it clean. Insert it back fully, then pull it out again to check that the oil level is between the minimum and maximum markings. If it’s low, add small amounts of oil, checking each time.",
            "incorrect": [
                "You should check the oil level every 500 miles. If it’s low, top it up with water to prevent overheating.",
                "To check the oil, start the engine and rev it to 5000 RPM for a few minutes, then check the level.",
                "Check the oil level only when the car is on a flat surface, but it’s fine to drive up a steep hill to get better readings."
            ]
        },
        "How would you check the engine coolant level?": {
            "correct": "Locate the header tank (coolant reservoir) and ensure the coolant level is between the minimum and maximum markings.",
            "incorrect": [
                "Check the coolant level only after a long drive. Hot coolant expands, which gives a more accurate reading.",
                "Use a thermometer to measure the temperature of the engine. If it’s cold, the coolant should be fine.",
                "Check the coolant levels after a cold start. The best time to inspect is just after the car has been off for hours."
            ]
        }
    },
    "TELL Me Questions": {
        "How would you know if there was a fault with the Anti-lock Braking System (ABS)?": {
            "correct": "The ABS warning light should illuminate on the dashboard if there is a fault.",
            "incorrect": [
                "If the brake pedal feels like it's bouncing or vibrating, the ABS is working perfectly. No need to worry.",
                "When driving on ice, if your brakes start working too well, the ABS might be faulty and could make you skid.",
                "You’ll know the ABS is faulty if the dashboard starts playing a jingle instead of just lighting up."
            ]
        },
        "How would you check the brakes are working before a journey?": {
            "correct": "The brakes should feel firm, not slack or spongy, and the vehicle should not pull to one side when applied.",
            "incorrect": [
                "Press the brakes with your foot while checking the rearview mirror for any reflections of the brake lights turning on.",
                "While driving at 20mph, press the brakes. If the car stops immediately, they are working fine.",
                "Have someone stand behind the car and jump up and down. If they feel the car move, the brakes might not be working well."
            ]
        },
        "Where would you find information about the tire pressures, and how would you check them?": {
            "correct": "Check the vehicle handbook for recommended tire pressures. Use a pressure gauge to measure when the tires are cold, and don’t forget to check the spare tire.",
            "incorrect": [
                "Tire pressure information can be found inside the glove box. Use a hammer to tap the tires and judge their pressure.",
                "Check the tire pressure by kicking each tire with your foot. If it feels solid, the pressure is fine.",
                "Find tire pressure info on the inside of the fuel cap, and use a balloon pump to gauge the tire pressure."
            ]
        },
        "How would you check the tires have sufficient tread and are in safe condition for road use?": {
            "correct": "Ensure there are no cuts or bulges, and the tread depth is at least 1.6mm across the central three-quarters of the breadth all around the tire.",
            "incorrect": [
                "If you can see any dirt on the tires, it means they are worn out and need replacing immediately.",
                "Place a coin into the tread; if it stands upright, the tread is good. If it falls over, the tire is worn out.",
                "Use a pencil to check the tread depth. If you can see the whole pencil, the tire is too worn."
            ]
        },
        "How would you check the brake lights are working?": {
            "correct": "Press down on the brake pedal and look for reflections (in a garage door or similar) or ask someone to help confirm they are on.",
            "incorrect": [
                "Look into the rearview mirror while driving to check if the brake lights reflect on the windshield. If not, the lights need checking.",
                "Activate the brake lights and walk backwards. If they shine brightly, they’re working properly.",
                "To check, press the brake pedal and blink repeatedly. The brake light should blink too if it's functioning."
            ]
        }
    }
}

def ask_question(question, answers):
    print(f"\n{question}")
    random.shuffle(answers)
    for index, answer in enumerate(answers, 1):
        print(f"{chr(64 + index)}: {answer}")
    
    while True:
        user_input = input("\nYour answer (A, B, C, D): ").strip().upper()
        if user_input in ['A', 'B', 'C', 'D']:
            return user_input, answers[ord(user_input) - 65]
        else:
            print("Invalid input, please choose A, B, C, or D.")

def main():
    score = 0
    questions = list(questions_answers["SHOW Me Questions"].items()) + list(questions_answers["TELL Me Questions"].items())
    random.shuffle(questions)
    
    for question, qa in questions:
        correct_answer = qa["correct"]
        incorrect_answers = qa["incorrect"]
        answers = [correct_answer] + incorrect_answers
        random.shuffle(answers)
        
        # Display the question and choices
        clear_screen()  # Clears screen for better flow
        user_input, chosen_answer = ask_question(question, answers)

        # Show feedback
        if chosen_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was: {correct_answer}")

        input("\nPress Enter to continue to the next question...")  # Wait for Enter before moving to the next question
        time.sleep(1)
    
    # Final Score Display
    clear_screen()  # Clears screen after the test for a clean finish
    print(f"\nYour final score is {score}/{len(questions)}")
    input("\nPress Enter to exit...")  # Pauses before closing

if __name__ == "__main__":
    main()
