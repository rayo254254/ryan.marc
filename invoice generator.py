import time
import requests
import mailbox
import smtplib
import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_push_notification(message):
    url = "https://www.pushsafer.com/api?k=AYIor8gFjJ5zb1k0Y7Pv&d=17595&m=ryan_test"
    response = requests.get(url)

    if response.status_code == 200:
        return "Notification sent successfully!"
    else:
        return f"Failed to send notification. Status code: {response.status_code}, Response: {response.text}"

def carbone_test():
    # API endpoint
    url = "https://api.carbone.io/render/0df8fbea1ac8fb648746014ae903fcce23ebe934c2933f69fa1a1d51b4192069"

    # Headers
    headers = {
        "Authorization": "test_eyJhbGciOiJFUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIxMDMyNTAyMzM5Mjg3MTIwNzQxIiwiYXVkIjoiY2FyYm9uZSIsImV4cCI6MjM5NDc5OTA3MCwiZGF0YSI6eyJ0eXBlIjoidGVzdCJ9fQ.AeNwsovwdLdyPAqJ16IjPSOjImuv5Yj0y8mdKJDApZlP0j3XD1T90x1wQSL5AkWU42d6iC3dWOLAjdn9zCUBHQWeAMkP46CN_pMj2NT3acUU7TSIGI1U6a5dRcNXeE4t_WLguijWVCm33Nkus1-ap_bp7GL84eMnpvCHXJ8VVUrqt2tS",
        "Content-Type": "application/json"
    }

    # JSON payload
    data = {
       "data": {
        
        "invoiceId": "FR-2023-781",
        "invoiceDate": "2023-01-17",
        "name": "Timmoty Johnson",
        "phone": "+33 (0)2 23 12 33 25",
        "email": "tim+serverpro@carbone.io",
        "partner": {
        "name": "Charles Nonneau",
        "phone": "+33 (0)6 27 89 01 23",
        "email": "contact@cloudtech.io",
        "vat": "FR45899106785",
         "siren": "899106785",
        "address": {
         "street": "12 Doctor Street",
         "postalcode": 34920,
         "city": "Anger",
         "country": "France"
            }
        },
        "note": "Our team is confident that <b>this cutting-edge technology</b> will enhance your operations and take your business to the next level. Should you have any questions or concerns, please don't hesitate to reach out to us.",
         "subscriptionFromDate": "2023-02-02T07:28:05+00:00",
         "subscriptionToDate": "2024-04-18T07:28:05+00:00",
        "products": [
    {
      "name": "<b>Rackmount case</b> (With bays for multiple 3.5-inch drives and room for the motherboard and other components.)",
      "exTaxTotal": 200,
      "unit": 500,
      "vat": 20,
      "qty": 1
    },
    {
      "name": "<b>Motherboard</b> (has the necessary number of SATA ports for your storage needs)",
      "exTaxTotal": 150,
      "unit": 150,
      "vat": 20,
      "qty": 1
    },
    {
      "name": "<b>3.5-inch SATA hard drives</b> (20TO)",
      "exTaxTotal": 1000,
      "unit": 100,
      "vat": 20,
      "qty": 10
    },
    {
      "name": "<b>Processor</b> ( A low-power consumption processor)",
      "exTaxTotal": 100,
      "unit": 100,
      "vat": 20,
      "qty": 1
    },
    {
      "name": "<b>4GB DDR5 RAM</b>",
      "exTaxTotal": 120,
      "unit": 30,
      "vat": 20,
      "qty": 4
    }
     ],
    "exTaxTotal": 1870,
    "taxTotal": 374,
    "inTaxTotal": 2244,
     "amountRemaining": 1044,
    "invoicePaymentList": [
    {
      "paymentDate": "2023-02-03T07:28:05+00:00",
      "typeSelect": "Paiement",
      "amount": 1200
    }
    ],
    "payment": {
    "name": "SEPA Transfer",
    "typeSelect": "SEPAtransfer",
    "condition": "Upon receipt of invoice",
    "bankLabel": "Revolut",
    "bankBIC": "REVOGB2L",
    "bankIBAN": "FR2112739000409352423869N75"
    },
    
        
    },
    "convertTo": "pdf",
    "timezone": "Europe/Paris",
    "lang": "en",
    "complement": {},
    "variableStr": "",
    "reportName": "document",
    "enum": {},
    "translations": {},
    "currencySource": "",
    "currencyTarget": "",
    "currencyRates": {},
    "hardRefresh": ""
    }

    # Make the POST requests
    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()

    render_id=response_data['data']['renderId']

    if response.status_code < 400 and response_data.get("success"):
        message='Good'
    else:
        message='Bad'
    return render_id, response.status_code, message 
    

        # Print the response
    print("Status Code:", response.status_code)

def getcarbonefile(render_id):
    download_url = f"https://api.carbone.io/render/{render_id}"
    # Headers
    headers = {
        "Authorization": "test_eyJhbGciOiJFUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIxMDMyNTAyMzM5Mjg3MTIwNzQxIiwiYXVkIjoiY2FyYm9uZSIsImV4cCI6MjM5NDc5OTA3MCwiZGF0YSI6eyJ0eXBlIjoidGVzdCJ9fQ.AeNwsovwdLdyPAqJ16IjPSOjImuv5Yj0y8mdKJDApZlP0j3XD1T90x1wQSL5AkWU42d6iC3dWOLAjdn9zCUBHQWeAMkP46CN_pMj2NT3acUU7TSIGI1U6a5dRcNXeE4t_WLguijWVCm33Nkus1-ap_bp7GL84eMnpvCHXJ8VVUrqt2tS",
        "Content-Type": "application/pdf"
    }
    
    print("Download URL:", download_url)

    # Download the generated PDF
    
    pdf_response = requests.get(download_url, headers=headers)
    status = pdf_response.status_code   
    if pdf_response.status_code < 400:
            # Save the PDF to a file
            with open("invoice.pdf", "wb") as pdf_file:
                pdf_file.write(pdf_response.content)
            print("Invoice downloaded successfully.")
            return status, pdf_response.content
    else:
            print(f"Failed to download the invoice: {pdf_response.status_code} - {pdf_response.text}")


    return None




def send_email_with_attachment(to_email, from_email, password, attachment_path):
    """
    Send an email with an attachment using Gmail's SMTP server.

    :param to_email: The recipient's email address.
    :param from_email: The sender's email address.
    :param password: The sender's Gmail app password.
    :param attachment_path: The file path to the attachment.
    """
    # Create a multipart message
    message = MIMEMultipart()

    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = "Invoice"

    # Attach the file
    with open(attachment_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {os.path.basename(attachment_path)}",
        )
        message.attach(part)

    # Send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        text = message.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
        

def send_email_with_attachment1(to_email, from_email, password, content):
    """
    Send an email with an attachment using Gmail's SMTP server.

    :param to_email: The recipient's email address.
    :param from_email: The sender's email address.
    :param password: The sender's Gmail app password.
    :param attachment_path: The file path to the attachment.
    """
    # Create a multipart message
    message = MIMEMultipart()

    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = "Invoice"

    # Attach the file
    with open(content, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= invoice.pdf",
        )
        message.attach(part)

    # Send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        text = message.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
        

# Define the email parameters
to_email = "marc.dekrock@wiseworks.be" 
from_email = "ryanomondi27@gmail.com"  
password = "vftp vslx exli sjjl"  
attachment_path = "C:/Users/ryano/invoice.pdf"  


# Example long-running workflow
print("Flow started.")
carbone_test()
renderid,status,message = carbone_test()
print('Render ID:', renderid)
print('Status:', status)
print('Message:', message)
time.sleep(2)  # Simulate step 1
print("Step 1 complete.")
status_code,content = getcarbonefile(renderid)
time.sleep(2)  # Simulate step 2
send_email_with_attachment(to_email, from_email, password, attachment_path)
send_email_with_attachment1(to_email, from_email, password,content)
print("Step 2 complete.")
time.sleep(2)  # Simulate final step
print("Flow complete.")


    