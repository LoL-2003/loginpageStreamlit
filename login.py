# import streamlit as st
# import firebase_admin
# from firebase_admin import firestore
# from firebase_admin import credentials
# from firebase_admin import auth


# cred = credentials.Certificate("ec-hack-2023-c35a12353f9e.json")
# #firebase_admin.initialize_app(cred)
# def app():
# # Usernm = []
#     st.title('Welcome to :violet[Pondering] :sunglasses:')

#     if 'username' not in st.session_state:
#         st.session_state.username = ''
#     if 'useremail' not in st.session_state:
#         st.session_state.useremail = ''



#     def f(): 
#         try:
#             user = auth.get_user_by_email(email)
#             print(user.uid)
#             st.session_state.username = user.uid
#             st.session_state.useremail = user.email
            
#             global Usernm
#             Usernm=(user.uid)
            
#             st.session_state.signedout = True
#             st.session_state.signout = True    
  
            
#         except: 
#             st.warning('Login Failed')

#     def t():
#         st.session_state.signout = False
#         st.session_state.signedout = False   
#         st.session_state.username = ''


        
    
        
#     if "signedout"  not in st.session_state:
#         st.session_state["signedout"] = False
#     if 'signout' not in st.session_state:
#         st.session_state['signout'] = False    
        

        
    
#     if  not st.session_state["signedout"]: # only show if the state is False, hence the button has never been clicked
#         choice = st.selectbox('Login/Signup',['Login','Sign up'])
#         email = st.text_input('Email Address')
#         password = st.text_input('Password',type='password')
        

        
#         if choice == 'Sign up':
#             username = st.text_input("Enter  your unique username")
            
#             if st.button('Create my account'):
#                 user = auth.create_user(email = email, password = password,uid=username)
                
#                 st.success('Account created successfully!')
#                 st.markdown('Please Login using your email and password')
#                 st.balloons()
#         else:
#             # st.button('Login', on_click=f)          
#             st.button('Login', on_click=f)
            
            
#     if st.session_state.signout:
#                 st.text('Name '+st.session_state.username)
#                 st.text('Email id: '+st.session_state.useremail)
#                 st.button('Sign out', on_click=t) 
            
                
    

                            
#     def ap():
#         st.write('Posts')

# app()

import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

# Check if the Firebase Admin SDK is already initialized
if not firebase_admin._apps:
    # Initialize Firebase Admin SDK
    cred = credentials.Certificate("ec-hack-2023-c35a12353f9e.json")
    firebase_admin.initialize_app(cred)

def app():
    st.title('Welcome to :violet[Pondering] :sunglasses:')
    
    # Rest of your code...

    def f():
        try:
            user = auth.get_user_by_email(email)
            if user.email_verified:
                st.session_state.username = user.uid
                st.session_state.useremail = user.email
                st.session_state.signedout = True
                st.session_state.signout = True
            else:
                st.warning('Email not verified. Please check your email for verification instructions.')
        except:
            st.warning('Login Failed')

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
                user = auth.create_user(email=email, password=password, uid=username)

                # Set email_verified to False (user's email is not verified)
                auth.update_user(user.uid, email_verified=False)

                st.success('Account created successfully! Please check your email for verification.')
                st.markdown('Please Login using your email and password')
                st.balloons()
            except auth.EmailAlreadyExistsError:
                st.warning('Email address is already in use')
    else:
        st.button('Login', on_click=f)

    if st.session_state.signout:
        st.text('Name ' + st.session_state.username)
        st.text('Email id: ' + st.session_state.useremail)
        st.button('Sign out', on_click=t)

if __name__ == '__main__':
    app()
