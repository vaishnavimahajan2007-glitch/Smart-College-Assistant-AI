print("Welcome to College Helpdesk Chatbot")
print("Type your question (admission, placement, hostel, hostel fees, college fees)")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("Bot: Thank you! Visit again.")
        break
    elif "hello" in user_input or "hi" in user_input:
        print("Bot: Hello! How can I assist you with college information?")

    elif "admission" in user_input:
        print("Bot: Admissions are open from June to August. You can apply online. Required documents: Marksheet, ID proof, passport photo.")

    elif "placement" in user_input:
        print("Bot: Placement training starts in final year. Top companies visit campus. Mock interviews are provided.")

    elif "hostel" in user_input and "fees" not in user_input:
        print("Bot: Hostel is available for both boys and girls with WiFi, laundry and security facilities.")

    elif "hostel fees" in user_input:
        print("Bot: Hostel fees depend on room type. Approx range is ₹40,000 - ₹80,000 per year.")

    elif "college fees" in user_input or "fees" in user_input:
        print("Bot: College fees vary by course. Approx range is ₹50,000 - ₹1,50,000 per year.")

    elif "courses" in user_input:
        print("Bot: We offer courses in Engineering, Science, Commerce, Arts and Management.")

    elif "contact" in user_input:
        print("Bot: You can contact us at xxxxx12345 or email us at 1234@gmail.com.")  

    else:
        print("Bot: Sorry, I don't understand your question. Try admission, placement, hostel or fees.")
