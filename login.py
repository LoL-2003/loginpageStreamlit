# import streamlit as st
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import auth
# import uuid
# import smtplib                            
# from time import sleep

# def header_footer():
#     st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
#     st.markdown("""
#     <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
#       <div class="container-fluid">
#         <a class="navbar-brand" href="#"><img 
#           src= 
#     "https://assets-global.website-files.com/5fac161927bf86485ba43fd0/6229d40f625c70840c12bcd7_BlogGif_2.gif" 
#           alt="" width="150" 
#           height="45"></a></a>
#         <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#collapsibleNavbar">
#           <span class="navbar-toggler-icon"></span>
#         </button>
#         <div class="collapse navbar-collapse" id="collapsibleNavbar">
#           <ul class="navbar-nav">
#             <li class="nav-item">
#               <a class="nav-link" href="#">Contact Us</a>
#             </li>
#             <li class="nav-item">
#               <a class="nav-link" href="#">GitHub</a>
#             </li>
#             <li class="nav-item">
#               <a class="nav-link" href="#">About Project</a>
#             </li>
#           </ul>
#         </div>
#       </div>
#     </nav>
#     """, unsafe_allow_html=True)
#     hide_st_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             footer:after {content:'Made with ❤️ by ADITYA PURI';visibility: visible;display: block;}
#             .st-emotion-cache-cio0dv {
#             padding-left: 20%;
#             padding-right: 1rem;
#             }
#             header {visibility: hidden;}
#             </style>
#             """
#     st.markdown(hide_st_style, unsafe_allow_html=True)

# st.set_page_config(page_title="EC_HACKATHON-2023")
# # Check if the Firebase Admin SDK is already initialized

# header_footer()

# # Check if the Firebase Admin SDK is already initialized
# if not firebase_admin._apps:
#     # Initialize Firebase Admin SDK
#     cred = credentials.Certificate("ec-hack-2023-c35a12353f9e.json")
#     firebase_admin.initialize_app(cred)

# def sendEmail(to, content, user='User'):
#   try:
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login(st.secrets['from'], st.secrets['pass'])
#     message =f"""
#     Subject: Verify Your Account - AccentLingua
#     Hello {user},

#     Thank you for signing up with AccentLingua! To complete the registration process, please verify your email address.

#     To verify your email address, simply click on the link below:
#       {content}

#     If you are unable to click on the link, you can copy and paste it into your browser's address bar.

#     Verification Link: {content}

#     If you did not sign up for AccentLingua, please ignore this email.

#     Thank you for choosing AccentLingua. We look forward to having you as a valued member of our community.

#     Best regards,
#     Adi
#     AccentLingua

#     P.S. If you encounter any issues or need assistance, please don't hesitate to contact our support team at adi1042003adi@gmail.com.

#     """
#     server.sendmail(st.secrets['from'], to, message)
#     server.close()
#     st.sucess('email sent sucessfully check your email inbox or spam box')
#   except:
#       st.warning('unable to send mail')

# def app():
#     st.title('Welcome to :violet[AccentLingua] :sunglasses:')
    
#     # Initialize session_state with required keys and values
#     if 'username' not in st.session_state:
#         st.session_state.username = ''
#     if 'useremail' not in st.session_state:
#         st.session_state.useremail = ''
#     if 'password' not in st.session_state:
#         st.session_state.password = ''
#     if 'signedout' not in st.session_state:
#         st.session_state.signedout = False
#     if 'signout' not in st.session_state:
#         st.session_state.signout = False

#     def forgot_password():
#         try:
#             flink = auth.generate_password_reset_link(email)
#             sleep(1)
#             sendEmail(email, flink, username)
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
#                     st.session_state.username = user.uid
#                     st.session_state.useremail = user.email
#                     st.session_state.signedout = True
#                     st.session_state.signout = True
#                     if st.button('forgot password'):
#                        forgot_password()
#             else:
#                 link = auth.generate_email_verification_link(email)
#                 sleep(1)
#                 sendEmail(email, link, username)
#                 st.write('Please check your email for verification instructions')
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
    
#     if choice == 'Sign up':
#         username = st.text_input("Enter your unique username")
        
#         if st.button('Create my account'):
#             try:
#                 uid = str(uuid.uuid4())  # Generate a unique UID
#                 user = auth.create_user(email=email, password=password, uid=uid)
#                 link = auth.generate_email_verification_link(email)
#                 sleep(1)
#                 sendEmail(email, link, username)
#                 st.write('Please check your email for verification instructions or click on the link above')
#                 st.success('Account created successfully! Please check your email for verification.')
#                 st.markdown('Please Login using your email and password')
#                 st.balloons()
#             except auth.EmailAlreadyExistsError:
#                 st.warning('The email address is already in use.')
#             except Exception as e:
#                 st.warning('Account creation failed. Error: ' + str(e))

#     else:
#         if st.button('Login', on_click=f):
#             pass
            
#     if st.session_state.signout:
#         st.text('Name ' + st.session_state.username)
#         st.text('Email id: ' + st.session_state.useremail)
#         st.success('You are logged in!')
#         st.button('Sign out', on_click=t)

# if __name__ == '__main__':
#     app()




import streamlit as st
from audio_recorder_streamlit import audio_recorder
import requests
import os
from time import sleep
import glob
from gtts import gTTS
from googletrans import Translator
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import uuid
import smtplib

def header_footer():
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
    st.markdown("""
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
      <div class="container-fluid">
        <a class="navbar-brand" href="#"><img 
          src= 
    "https://assets-global.website-files.com/5fac161927bf86485ba43fd0/6229d40f625c70840c12bcd7_BlogGif_2.gif" 
          alt="" width="150" 
          height="45"></a></a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#collapsibleNavbar">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="collapsibleNavbar">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link" href="#">Contact Us</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">GitHub</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">About Project</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    """, unsafe_allow_html=True)
    hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {content:'Made with ❤️ by ADITYA PURI';visibility: visible;display: block;}
            .st-emotion-cache-cio0dv {
            padding-left: 20%;
            padding-right: 1rem;
            }
            header {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)

st.set_page_config(page_title="EC_HACKATHON-2023")
# Check if the Firebase Admin SDK is already initialized

header_footer()
if not firebase_admin._apps:
    # Initialize Firebase Admin SDK
    cred = credentials.Certificate("ec-hack-2023-c35a12353f9e.json")
    firebase_admin.initialize_app(cred)

def sendEmail(to, content, user='User'):
  try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(st.secrets['from'], st.secrets['pass'])
    message =f"""
    Subject: Verify Your Account - AccentLingua
    Hello {user},

    Thank you for signing up with AccentLingua! To complete the registration process, please verify your email address.

    To verify your email address, simply click on the link below:
      {content}

    If you are unable to click on the link, you can copy and paste it into your browser's address bar.

    Verification Link: {content}

    If you did not sign up for AccentLingua, please ignore this email.

    Thank you for choosing AccentLingua. We look forward to having you as a valued member of our community.

    Best regards,
    Adi
    AccentLingua

    P.S. If you encounter any issues or need assistance, please don't hesitate to contact our support team at adi1042003adi@gmail.com.

    """
    server.sendmail(st.secrets['from'], to, message)
    server.close()
    st.sucess('email sent sucessfully check your email inbox or spam box')
  except:
      pass

def app():
    st.title('Welcome to :violet[AccentLingua] :sunglasses:')
    
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
            sendEmail(email, flink,'User')
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
            else:
                link = auth.generate_email_verification_link(email)
                sleep(1)
                sendEmail(email, link, username)
                st.write('Please check your email for verification instructions')
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
                sendEmail(email, link, username)
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
        username = st.session_state.useremail
        # Add your custom content here after the user logs in
        st.header(f'Welcome :yellow[{username}] to :violet[AccentLingua]')
        
        LANGUAGES = {
            'default(hindi)': 'hi',
            'afrikaans': 'af',
            'albanian': 'sq',
            'amharic': 'am',
            'arabic': 'ar',
            'armenian': 'hy',
            'azerbaijani': 'az',
            'basque': 'eu',
            'belarusian': 'be',
            'bengali': 'bn',
            'bosnian': 'bs',
            'bulgarian': 'bg',
            'catalan': 'ca',
            'cebuano': 'ceb',
            'chichewa': 'ny',
            'chinese (simplified)': 'zh-cn',
            'chinese (traditional)': 'zh-tw',
            'corsican': 'co',
            'croatian': 'hr',
            'czech': 'cs',
            'danish': 'da',
            'dutch': 'nl',
            'english': 'en',
            'esperanto': 'eo',
            'estonian': 'et',
            'filipino': 'tl',
            'finnish': 'fi',
            'french': 'fr',
            'frisian': 'fy',
            'galician': 'gl',
            'georgian': 'ka',
            'german': 'de',
            'greek': 'el',
            'gujarati': 'gu',
            'haitian creole': 'ht',
            'hausa': 'ha',
            'hawaiian': 'haw',
            'hebrew': 'iw',
            'hebrew': 'he',
            'hindi': 'hi',
            'hmong': 'hmn',
            'hungarian': 'hu',
            'icelandic': 'is',
            'igbo': 'ig',
            'indonesian': 'id',
            'irish': 'ga',
            'italian': 'it',
            'japanese': 'ja',
            'javanese': 'jw',
            'kannada': 'kn',
            'kazakh': 'kk',
            'khmer': 'km',
            'korean': 'ko',
            'kurdish (kurmanji)': 'ku',
            'kyrgyz': 'ky',
            'lao': 'lo',
            'latin': 'la',
            'latvian': 'lv',
            'lithuanian': 'lt',
            'luxembourgish': 'lb',
            'macedonian': 'mk',
            'malagasy': 'mg',
            'malay': 'ms',
            'malayalam': 'ml',
            'maltese': 'mt',
            'maori': 'mi',
            'marathi': 'mr',
            'mongolian': 'mn',
            'myanmar (burmese)': 'my',
            'nepali': 'ne',
            'norwegian': 'no',
            'odia': 'or',
            'pashto': 'ps',
            'persian': 'fa',
            'polish': 'pl',
            'portuguese': 'pt',
            'punjabi': 'pa',
            'romanian': 'ro',
            'russian': 'ru',
            'samoan': 'sm',
            'scots gaelic': 'gd',
            'serbian': 'sr',
            'sesotho': 'st',
            'shona': 'sn',
            'sindhi': 'sd',
            'sinhala': 'si',
            'slovak': 'sk',
            'slovenian': 'sl',
            'somali': 'so',
            'spanish': 'es',
            'sundanese': 'su',
            'swahili': 'sw',
            'swedish': 'sv',
            'tajik': 'tg',
            'tamil': 'ta',
            'telugu': 'te',
            'thai': 'th',
            'turkish': 'tr',
            'ukrainian': 'uk',
            'urdu': 'ur',
            'uyghur': 'ug',
            'uzbek': 'uz',
            'vietnamese': 'vi',
            'welsh': 'cy',
            'xhosa': 'xh',
            'yiddish': 'yi',
            'yoruba': 'yo',
            'zulu': 'zu',
        }
        
        translator = Translator()
        
        def text_Tmodel(transcribe_Text):
            text = transcribe_Text
        
            language_names = list(LANGUAGES.keys())
        
            input_language = 'en'  # Default to English 
        
            out_lang = st.selectbox(
                "Select your output language",
                language_names
            )
        
            output_language = LANGUAGES.get(out_lang, "hi")  # Default to English if not found
            english_accent = st.selectbox(
                "Select your english accent",
                (
                    "Default",
                    "India",
                    "United Kingdom",
                    "United States",
                    "Canada",
                    "Australia",
                    "Ireland",
                    "South Africa",
                ),
            )
            if english_accent == "Default":
                tld = "co.in"
            elif english_accent == "India":
                tld = "co.in"
            elif english_accent == "United Kingdom":
                tld = "co.uk"
            elif english_accent == "United States":
                tld = "com"
            elif english_accent == "Canada":
                tld = "ca"
            elif english_accent == "Australia":
                tld = "com.au"
            elif english_accent == "Ireland":
                tld = "ie"
            elif english_accent == "South Africa":
                tld = "co.za"
                
            if not os.path.exists("temp"):
                os.makedirs("temp")
            translation = translator.translate(text, src=input_language, dest=output_language)
            trans_text = translation.text
            tts= gTTS(trans_text, lang=output_language, tld=tld, slow=False)
            try:
                my_file_name = text[0:20]
            except:
                my_file_name = "audio"
            tts.save(f"temp/{my_file_name}.mp3")
            
            # Here, we play the generated audio using the st.audio() function
            audio_file = open(f"temp/{my_file_name}.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3", start_time=0,)
            display_output_text = st.checkbox("Display transcription")
            if display_output_text:
                st.markdown(f"## transcription text:")
                st.write(f" {trans_text}")
        

            
        header_footer()
        st.title('EC HACKATHON 2023')
        st.write("Select an option:")
        option = st.radio(
            'How would you like to use the bot?',
            ('Transcribe Pre-recorded Audio', 'Record & Transcribe')
        )
        
        if option == 'Transcribe Pre-recorded Audio':
            st.write("Audio Transcription from Pre-recorded Files")
            st.caption("Upload an audio file, and the bot will transcribe it for you.")
            uploaded_file = st.file_uploader("Upload an audio file (MP3, WAV, etc.)")
            API_URL = st.secrets['huggingfacemodel']
        
            if uploaded_file is not None:
                st.audio(uploaded_file, format="audio/mp3", start_time=0)
                st.write("Transcription:")
                transcript_container = st.empty()
        
                audio_file_path = "temp_audio" + os.path.splitext(uploaded_file.name)[-1]
                with open(audio_file_path, "wb") as f:
                    f.write(uploaded_file.read())
        
                with open(audio_file_path, "rb") as f:
                    audio_data = f.read()
        
                headers = {"Authorization": st.secrets['hugging_face']}
        
                with st.spinner("Transcribing..."):
                    response = requests.post(API_URL, headers=headers, data=audio_data)
                    output = response.json().get('text', "")
        
                    transcript = "**Bot🤖:** "
                    for char in output:
                        transcript += char
                        transcript_container.markdown(transcript)
                        sleep(0.05)
                    text_Tmodel(output)
                st.success("Transcription completed")
                st.balloons()
        
            st.subheader("Voice Recorder and Transcription Bot")
            st.write("Record and play back your voice")
        else:
            st.write("Click the 'Record' button to start recording:")
            recorded_audio_bytes = audio_recorder()
            if recorded_audio_bytes:
                st.audio(recorded_audio_bytes, format="audio/wav", start_time=0)
        
            if st.button("Play Recorded Audio") and recorded_audio_bytes:
                st.write("Playing recorded audio:")
                st.audio(recorded_audio_bytes, format="audio/wav", start_time=0)
        
            if st.button("Transcribe Recorded Audio") and recorded_audio_bytes:
             st.write("Transcribing recorded audio:")
             transcript_container = st.empty()
             headers = {"Authorization": "Bearer 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"}
        
             with st.spinner("Transcribing..."):
                API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v2"
                response = requests.post(API_URL, headers=headers, data=recorded_audio_bytes)
                output = response.json().get('text', "")
        
                transcript = "**Bot🤖:** "
                for char in output:
                    transcript += char
                    transcript_container.markdown(transcript)
                    sleep(0.05)
                #text_Tmodel(output)
             st.success("Transcription completed")
             st.balloons()
        
        


if __name__ == '__main__':
    app()

