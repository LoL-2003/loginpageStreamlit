# import streamlit as st
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import auth
# import uuid

# # Check if the Firebase Admin SDK is already initialized
# if not firebase_admin._apps:
#     # Initialize Firebase Admin SDK
#     cred = credentials.Certificate("ec-hack-2023-c35a12353f9e.json")
#     firebase_admin.initialize_app(cred)

# def app():
#     st.title('Welcome to :violet[Pondering] :sunglasses:')
    
#     # Initialize session_state with required keys and values
#     if 'username' not in st.session_state:
#         st.session_state.username = ''
#     if 'useremail' not in st.session_state:
#         st.session_state.useremail = ''
#     if 'signedout' not in st.session_state:
#         st.session_state.signedout = False
#     if 'signout' not in st.session_state:
#         st.session_state.signout = False

#     def forgot_password():
#         try:
#             link = auth.generate_password_reset_link(email)
#             st.write(link)
#             st.write('Please check your email for password reset instructions or click on the link above')
#             st.warning('Password reset link sent to your email')
#         except auth.UserNotFoundError:
#             st.warning('User not found. Please check your email address')
#         except Exception as e:
#             st.warning('Password reset failed. Error: ' + str(e))
    
#     def f():
#         try:
#             user = auth.get_user_by_email(email)
#             if user.email_verified:
#                 if auth.verify_password(user.uid, password):  # Verify the entered password
#                     st.session_state.username = user.uid
#                     st.session_state.useremail = user.email
#                     st.session_state.signedout = True
#                     st.session_state.signout = True
#                 else:
#                     st.warning('Incorrect password')
#             else:
#                 link = auth.generate_email_verification_link(email)
#                 st.write(link)
#                 st.write('Please check your email for verification instructions or click on the link above')
#                 st.warning('Email not verified.')
#         except auth.UserNotFoundError:
#             st.warning('User not found.')
#         except auth.EmailAlreadyExistsError:
#             st.warning('The email address is already in use.')
#         except Exception as e:
#             st.warning('Login Failed. Error: ' + str(e))
    
#     def t():
#         st.session_state.signout = False
#         st.session_state.signedout = False
#         st.session_state.username = ''
    
#     choice = st.selectbox('Login/Signup', ['Login', 'Sign up'])
#     email = st.text_input('Email Address')
#     password = st.text_input('Password', type='password')
#     st.markdown('forgot password', on_click=forgot_password)
    
#     if choice == 'Sign up':
#         username = st.text_input("Enter your unique username")
        
#         if st.button('Create my account'):
#             try:
#                 uid = str(uuid.uuid4())  # Generate a unique UID
#                 user = auth.create_user(email=email, password=password, uid=uid)
#                 link = auth.generate_email_verification_link(email)
#                 st.write(link)
#                 st.write('Please check your email for verification instructions or click on the link above')
#                 st.success('Account created successfully! Please check your email for verification.')
#                 st.markdown('Please Login using your email and password')
#                 st.balloons()
#             except auth.EmailAlreadyExistsError:
#                 st.warning('The email address is already in use.')
#             except Exception as e:
#                 st.warning('Account creation failed. Error: ' + str(e))
#     else:
#         st.button('Login', on_click=f)
    
#     if st.session_state.signout:
#         st.text('Name ' + st.session_state.username)
#         st.text('Email id: ' + st.session_state.useremail)
#         st.success('You are logged in!')
#         st.button('Sign out', on_click=t)

# if __name__ == '__main__':
#     app()





import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import uuid
import smtplib                              # use pip install smtplib
from time import sleep

# Check if the Firebase Admin SDK is already initialized
if not firebase_admin._apps:
    # Initialize Firebase Admin SDK
    cred = credentials.Certificate("ec-hack-2023-c35a12353f9e.json")
    firebase_admin.initialize_app(cred)

def sendEmail(to, content):
  try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(st.secrets['from'], st.secrets['pass'])
    server.sendmail(st.secrets['from'], to, content)
    server.close()
  except:
      st.warning('unable to send mail')

def app():
    st.title('Welcome to :violet[Pondering] :sunglasses:')
    
    # Initialize session_state with required keys and values
    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''
    if 'password' not in st.session_state:
        st.session_state.password = ''
    if 'signedout' not in st.session_state:
        st.session_state.signedout = False
    if 'signout' not in st.session_state:
        st.session_state.signout = False

    def forgot_password():
        try:
            flink = auth.generate_password_reset_link(email)
            sleep(1)
            sendEmail(email, flink)
            st.write(flink)
            st.write('Please check your email for password reset instructions or click on the link above')
            st.warning('Password reset link sent to your email')
        except auth.UserNotFoundError:
            st.warning('User not found. Please check your email address')
        except Exception as e:
            st.warning('Password reset failed. Error: ' + str(e))
    
    def f():
        try:
            user = auth.get_user_by_email(email)
            if user.email_verified:
                    st.session_state.username = user.uid
                    st.session_state.useremail = user.email
                    st.session_state.signedout = True
                    st.session_state.signout = True
                    if st.button('forgot password'):
                       forgot_password()
            else:
                link = auth.generate_email_verification_link(email)
                st.write(link)
                sleep(1)
                sendEmail(email, link)
                st.write('Please check your email for verification instructions or click on the link above')
                st.warning('Email not verified.')
        except auth.UserNotFoundError:
            st.warning('User not found.')
        except auth.EmailAlreadyExistsError:
            st.warning('The email address is already in use.')
        except Exception as e:
            st.warning('Login Failed. Error: ' + str(e))
    
    def t():
        st.session_state.signout = False
        st.session_state.signedout = False
        st.session_state.username = ''
    
    choice = st.selectbox('Login/Signup', ['Login', 'Sign up'])
    email = st.text_input('Email Address')
    password = st.text_input('Password', type='password')
    
    if choice == 'Sign up':
        username = st.text_input("Enter your unique username")
        
        if st.button('Create my account'):
            try:
                uid = str(uuid.uuid4())  # Generate a unique UID
                user = auth.create_user(email=email, password=password, uid=uid)
                link = auth.generate_email_verification_link(email)
                sleep(1)
                sendEmail(email, link)
                st.write(link)
                st.write('Please check your email for verification instructions or click on the link above')
                st.success('Account created successfully! Please check your email for verification.')
                st.markdown('Please Login using your email and password')
                st.balloons()
            except auth.EmailAlreadyExistsError:
                st.warning('The email address is already in use.')
            except Exception as e:
                st.warning('Account creation failed. Error: ' + str(e))

    else:
        if st.button('Login', on_click=f):
            pass
            
    if st.session_state.signout:
        st.text('Name ' + st.session_state.username)
        st.text('Email id: ' + st.session_state.useremail)
        st.success('You are logged in!')
        st.button('Sign out', on_click=t)

if __name__ == '__main__':
    app()
