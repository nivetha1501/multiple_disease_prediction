import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
#kidney_model = pickle.load(open('kidney_model.sav', 'rb'))
#liver_model = pickle.load(open('liver_model.sav', 'rb'))
#parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Home','Kidney Prediction',
                            'Liver Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['Home','activity', 'heart', 'person'],
                           default_index=0)
    

# Set the background image
def set_bg_image(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Example usage
set_bg_image("https://media.istockphoto.com/id/1168895929/photo/doctor-in-empty-blue-background-with-copy-space.jpg?s=612x612&w=0&k=20&c=rJvdY5TzKAFlG5a4nq-aNo6Sydk30h5gnVl30xHc4U8=")



if selected == "Home":
    with st.expander('Kidney'):
        st.image(r"C:\Users\nivet\OneDrive\Documents\kidney.download.jpeg")   
        st.title("Symptoms of kidney disease")
        st.subheader("1. Tiredness: Feeling tired or weak", divider=True)
        st.subheader("2. Blood in the urine: Blood in the urine", divider=True)
        st.subheader("3. Itchy skin: Dry, itchy skin", divider=True)
        st.subheader("4. Nausea and vomiting: Feeling sick or being sick", divider=True)
        st.subheader("5. Difficulty sleeping: Having trouble sleeping", divider=True)

    with st.expander('Liver'):
        st.image(r"C:\Users\nivet\OneDrive\Documents\liver.jpeg")
        st.title('Symptoms of Liver disease')
        st.subheader("1. Bleeding and bruising more easily", divider=True)
        st.subheader("2. Weakness and muscle wasting", divider=True)
        st.subheader("3. Swelling in the legs, ankles, and feet (edema)", divider=True)
        st.subheader("4. High temperature and shivering", divider=True)

    with st.expander('Parkinsons'):
        st.image(r"C:\Users\nivet\OneDrive\Documents\parkinsons.jpeg")
        st.title('Symptoms of Parkinsons disease')
        st.subheader("1. Posture instability: This can include stooping or hunching over.", divider=True)
        st.subheader("2. Loss of smell: You may fully or partially lose your sense of smell.", divider=True)
        st.subheader("3. Tremors: Shaking in the hands, arms, legs, jaw, or head.", divider=True)
        st.subheader("4. Impaired balance: This can lead to falls.", divider=True)



if selected == "Kidney Prediction":
    st.title('Kidney Prediction')
    
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
       age = st.text_input('age')

    with col2:
       bp = st.text_input('bp')

    with col3:
       al = st.text_input('al')

    with col4:
       su = st.text_input('su')

    with col5:
       rbc = st.text_input('rbc')

    with col1:
       pc = st.text_input('pc')

    with col2:
       pcc = st.text_input('pcc')

    with col3:
       ba = st.text_input('ba')

    with col4:
        bgr = st.text_input('bgr')

    with col5:
       bu = st.text_input('bu')

    with col1:
        sc = st.text_input('sc')
        
    with col2:
       pot = st.text_input('pot')  

    with col3:
       wc = st.text_input('wc')

    with col4:
       htn = st.text_input('htn')

    with col5:
       dm = st.text_input('dm')
 
    with col1:
        cad = st.text_input('cad')

    with col2:
       pe = st.text_input('pe')

    with col3:
       ane = st.text_input('ane')

    kidney_diagnosis = ''


    if st.button("kidney Test Result"):
        user_input = [age, bp, al, su, rbc,
                        pc, pcc, ba,bgr, bu, sc, pot,
                        wc, htn, dm, cad, pe, ane]
        
        user_input = [float(x) for x in user_input]

        Kidney_Prediction = kidney_model.predict([user_input])

        if Kidney_Prediction[0] == 1:
                kidney_diagnosis = "The person has kidney disease"
        else:
                kidney_diagnosis = "The person does not have kidney disease"

        st.success(kidney_diagnosis)

if selected == "Liver Prediction":
    st.title('Liver Prediction')

    col1,col2,col3 = st.columns(3)

    with col1:
        age = st.text_input('age')

    with col2:
        Total_Bilirubin = st.text_input('Total_Bilirubin')

    with col3:
        Direct_Bilirubin = st.text_input('Direct_Bilirubin')

    with col1:
        Alkaline_Phosphotase = st.text_input('Alkaline_Phosphotase')

    with col2:
        Alamine_Aminotransferase = st.text_input('Alamine_Aminotransferase')

    with col3:
        Aspartate_Aminotransferase = st.text_input('Aspartate_Aminotransferase')

    with col1:
        Total_Protiens = st.text_input('Total_Protiens')

    with col2:
        Albumin = st.text_input('Albumin')

    with col3:
        Albumin_and_Globulin_Ratio = st.text_input('Albumin_and_Globulin_Ratio')

    with col1:
        Gender_Male = st.text_input('Gender_Male')

    liver_diagnosis = ''

    if st.button("Liver Test Result"):
       user_input = [age, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase,
                      Aspartate_Aminotransferase,Total_Protiens, Albumin,Albumin_and_Globulin_Ratio,Gender_Male]
       
       user_input = [float(x) for x in user_input]

       liver_Prediction = liver_model.predict([user_input])

       if liver_Prediction[0] == 1:
            liver_diagnosis = "The person has liver disease"
       else:
            liver_diagnosis = "The person does not have liver disease"

       st.success(liver_diagnosis)



    

    # Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Prediction ")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

        

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)