from flask import Flask, request
import africastalking
import os

app = Flask(__name__)
username = "ubongoo"
api_key = "387e195a1a6f397491e7f65333c3146c8ff158b5b0e0e554d7a3df339fd5c49a"
africastalking.initialize(username, api_key)
sms = africastalking.SMS

@app.route('/', methods=['POST', 'GET'])

def ussd_callback():
    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")
    sms_phone_number = []
    sms_phone_number.append(phone_number)

    #ussd logic
    if text == "":
        #main menu
        response = "CON Hello and welcome to Ubongo mental health portal...?\n"
        response += "1. Mental health info\n"
        response += "2. Visit a hospital\n"
        response += "3. Talk to a specialist\n"
        response += "4. Access materials(wait for SMS with link)"
    elif text == "1":
        #sub menu 1
        response = "END According to the World Health Organization, 1 in 8 people are living with a mental disorder. This includes conditions such as anxiety and depression, which saw a sharp increase in 2020 because of the Covid-19 pandemic. Now, more than ever, it is important we reduce the stigma around mental illness so that people can find and get the care they need."
    elif text == "2":
        #sub menu 2
        response = "END We recommend you visit the following facilities for help\n"
        response += "Kenyatta National Hospital +254709854000\n"
        response += "Mathari mental hospital +254704383969"

    elif text == "3":
        #sub menu 1
        response = "CON You can reach out to the following specialists for personalised and professional help\n"
        response += "Dr Margaret Kagwe +254712345678\n"
        response += "Dr William Opodo +254700000000\n"
        response += "Dr Nzau Naliaka +254711111111"
    elif text == "4":
        response = "CON please check your phone for SMS with link to resources."
        try:
            #sending the sms
            sms_response = sms.send("Thank you for visiting Ubongo. Follow this link to get more mental health info. https://www.mentalhealth.gov/ We still highly recommend that you see a certified practitioner for proper diagnosis.", sms_phone_number)
            print(sms_response)
        except Exception as e:
            #show error.
            print(f"Error in code!!: {e}")
    
    else:

        response = "END Invalid input. Try again."

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT"))
