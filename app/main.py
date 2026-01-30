from agent import agent_decide
from tools.image import generate_image


print("🤖 AI Agent (Pollinations Image Generator)")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    decision = agent_decide(user_input)

    if decision["action"] == "image":
        print()
        image_path = generate_image(decision["prompt"], show_progress)
        print(f"\n🖼️ Image saved as: {image_path}")
    else:
        print("🤖", decision["response"])
