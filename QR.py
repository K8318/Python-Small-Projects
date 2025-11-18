import qrcode

# Taking UPI ID as Input
upi_id = input("Please enter your UPI ID: ")

# (Optional) You can take amount and message also
amount = input("Enter amount (or press Enter to skip): ")
message = "Payment"

# Creating payment URLs
phonepe_url = f"upi://pay?pa={upi_id}&pn=Recipient&am={amount}&cu=INR&tn={message}"
paytm_url = f"upi://pay?pa={upi_id}&pn=Recipient&am={amount}&cu=INR&tn={message}"
google_pay_url = f"upi://pay?pa={upi_id}&pn=Recipient&am={amount}&cu=INR&tn={message}"

# Create QR codes
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# Save QR codes
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_pay_qr.png")

# Display QR codes
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()
