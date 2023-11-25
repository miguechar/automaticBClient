import firebase_admin
from firebase_admin import credentials, auth, db
import pyautogui
import time

# Initialize Firebase Admin SDK
# cred = credentials.Certificate("./fbproj.json")
cred = credentials.Certificate(
    {
    "type": "service_account",
    "project_id": "nestbar-6833d",
    "private_key_id": "c6a851eb2076c29556a3ee5384fca349f6c888c4",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC25kBN/xuF8Api\nUCUSI6b9foBzxua6dl+/8zoe9a9Q0DTcjIEfh3XbudHNOz5UbWKxSdwQHxPRsxrS\nzoMfi5bACG7JN1NGQ4YF0mxxGC3mL5/Bl00AfiHlRjiEty1nuXnWBn5iF5vd1idV\nI23AqlQk94iuQ8PtsLGF3nyYA7lnK3WZZPFr2PLHnOSfG2R7oZUZVqYYApp3LyQE\nVIHi7pIk4CdVzLBQ2s9aR7X3ntDcDdzRkODNOcncW7Ffw9ItkRfVkCHqS5H6Ai69\nPWArVr7HDbQBc28GjtEtq7uGwGpPpBHygeb6izQ9+1OzdyWOA9HCTem+Gs2wL0nd\nzt+br6JXAgMBAAECggEAL/JvhCLu969EQZ6qATXYdpbdnLxVSydyFXNxVqFomsJi\nQTkSNo4/3uC5N9iij+Z3G2v15UIIY45U51Oc+z2QQPpU9Knsyjw0W71ckU9Z5QCy\nHEGKPalTQHQmp+APZqQwZOOh6RwwT7ju6bpWcM4WLfS4X5rDN8H838/CEOXVCk7f\nsLi0Pz8FW/ZIr9ToegW6wQ3lG/iE+z9dw9FI95XueFdiUGWQcK3dDRjJyhnI4Ka5\nBY3HlQXepfl14IURj7zFaB9N/KaTpaOf2faK4X2o7uX9LpBLf7SeYF8lNjTfAUkO\nFH1k9pjbi4UfGDF9Y6yDv29Z0Bq7N54IJT5csNR6gQKBgQDxIY+A6/qwRX4UwLuN\nWGy4NBTkzOZxxhugeeAj1UVpTGoS1yqs1JoMcD1qMTPbDe4rgrZmFDQtRBMI9Ha9\nX2cVpPoEstXfbTCSkDwcqrpweJLvvcIjCBH8dP2PYJOQjWsZAC8AuUm0zHcHK8TP\nPVTpl/StZEk6DMtn4fEin/q51wKBgQDCLXV63v1e5tLzY9Z3jv6VUPLmCGm1vKgB\ndpOOvjg8Atkk/EbTBHoxPxSWKRxlop6111TERm3xeJiWRT7o2fXegSDllfsZJSD6\nc1/qKk48OUrDXLYG4KmL5RGnuNzxY4Nq/N3L1CvO0Dj9UjeR3O/K9Bn2y6LnN9Gk\n6sKZBIpLgQKBgB220QRGECJgreTIy1PjraIVaO25AjzK+OSRoDlKMr+DFx8zPKMH\nn+QggLDxVz6LPOpHtUpm+vcJCH92AJvdgcp9BgJGN2zM+8tT0tSFhWwOr6yzaZT/\njZfaotRkRkrt4mC2URR5wMdy2sgbcKlJGYmfnBsx3IQ2x2oJwblOlYsJAoGAJTm5\nz/h38n2l62s0bm9HdzCxoE/0lBa6zq0A1Ni6xyZ0opaKrWGqW06Qj8kJ3KI0cv/5\nDDfEVAqelhBoYxOGA0YWHG2IWeW4UMtVk/rQTNNe9d0MOH1Rg7RCkjjqgoxlYVlg\n2/as/1UD1+yvIpOMlQf/AkU/0bvtwQQQkm1AZgECgYA+gyyD0kf8v9wBe61oeHS8\nYGS3z5s9i7/uEnsDBAY/+0qlbmVfZOsTe/4KaqqEIdMaCmeMj0iBswhFkBHf7UHS\nNNds1KPa1M2bqJSx4qxC/lHnqWong4CNlbdyH/lVzr07E+Pgv97uj+tTxgSYuAON\nj/nK4l0u38hmEbNszU+mlg==\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-2vity@nestbar-6833d.iam.gserviceaccount.com",
    "client_id": "117795161251773260703",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-2vity%40nestbar-6833d.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}

)
firebase_admin.initialize_app(cred, {'databaseURL': 'https://nestbar-6833d-default-rtdb.firebaseio.com'})

def login_with_email_and_password(email, password):
    try:
        user = auth.get_user_by_email(email)
        # Check if the provided password is correct (this is a simplified example)
        # In a real-world scenario, you would likely use a different authentication method.
        # For example, you might use Firebase Authentication custom claims or Firebase Auth Emulator.
        print("Successfully logged in!")
        print(f"User ID: {user.uid}")
        print_keys_in_nests()
    except auth.AuthError as e:
        print(f"Authentication failed: {e}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def print_keys_in_nests():
    try:
        ref = db.reference("/nests")
        nests_data = ref.get()

        if nests_data:
            keys = list(nests_data.keys())
            print("Keys in /nests:")
            for i, key in enumerate(keys):
                nestNameRef = db.reference(f"/nests/{key}/")
                nestData = nestNameRef.get()
                print(f"({i + 1}) UID: {key}, Nest Name: {nestData.get('nestName', '')}")

            selection = input("Enter the number of the key you want to select: ")

            try:
                index = int(selection) - 1

                if 0 <= index < len(keys):
                    selected_key = keys[index]
                    print(f"\nSelected key: {selected_key}")
                    print_parts(selected_key)
                    automate_typing(selected_key)
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("No data found in /nests")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def print_parts(selected_key):
    try:
        parts_ref = db.reference(f"/nests/{selected_key}/printablePartsList")
        parts_data = parts_ref.get()
        hull_ref = db.reference(f"/nests/{selected_key}/")
        hull_data = hull_ref.get()

        if parts_data:
            print(f"\nParts under /nests/{selected_key}/printablePartsList:")
            for part in parts_data:
                print(f"name: {part}, hull: {hull_data.get('hull', '')}")
        else:
            print(f"No data found in /nests/{selected_key}/printablePartsList")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def automate_typing(selected_key):
    try:
        parts_ref = db.reference(f"/nests/{selected_key}/printablePartsList")
        parts_data = parts_ref.get()
        hull_ref = db.reference(f"/nests/{selected_key}/")
        hull_data = hull_ref.get()

        if parts_data:
            print("\nAutomating typing...")
            time.sleep(5)  # Adjust the sleep duration if needed
            for part in parts_data:
                hull_value = hull_data.get('hull', '')
                # name_value = part.get('')
                concatenated_string = f"{hull_value}/{part}"

                pyautogui.typewrite(concatenated_string)
                # time.sleep(0.5)  # Adjust the sleep duration if needed
                pyautogui.press('enter')
                time.sleep(0.5)  # Adjust the sleep duration if needed

            # Press Enter at the end
            pyautogui.press('enter')
            print("Automation complete!")
        else:
            print(f"No data found in /nests/{selected_key}/printablePartsList")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # email = input("Enter your email: ")
    # password = input("Enter your password: ")
    email = "jenifer.hodge@us.fincantieri.com"
    password = "123456789"

    login_with_email_and_password(email, password)
