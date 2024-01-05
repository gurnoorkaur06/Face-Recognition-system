import streamlit as st
import union
import os
import pandas as pd
import time
def write_to_folder(uploaded_file, folder_name="download"):
    file_path = os.path.join(folder_name, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    progress=st.empty()
    progress.write(f"Processing...")
    return progress
def login(username, password):
    login_details=pd.read_csv("login_details.csv")
    user_row = login_details[(login_details['Username'] == username) & (login_details['Password'] == password)]
    if not user_row.empty:
        user_type = user_row['Type'].values[0]
        return user_type
    else:
        return "invalid"
def main():
    global type_cookie
    global run_var
    user_type=None
    if type_cookie is None :
        st.sidebar.title("Facial Attendance System")
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type='password')
        if st.sidebar.button("Login"):
            user_type = login(username, password)
            type_cookie=user_type
    if type_cookie=='teacher'  or user_type == 'teacher' :
        courses = ['ML-4CS5-8','AI-3C0E-8-12','AI-3C0E-26-30']
        uploaded_videos = []
        file_var={}
        if run_var==False:
            st.title("Teacher Dashboard")
            st.header("Upload Videos")
            for course in courses:
                st.subheader(course)
                file_var[course]=st.file_uploader(f"Upload video for {course}", type=["mp4", "avi","mov"])
                if file_var[course] is not None:
                    print(f'{course} is not none')
                    uploaded_videos.append(file_var[course])
            if st.button("Submit"):
                if not os.path.exists("download"):
                    os.makedirs("download")
                for file in uploaded_videos:
                    if file is not None:
                        progress=write_to_folder(file)
                        file_name=file.name
                        print(f'file name is {file_name}')
                        union.attendance(file_name)
                        progress.write("done")
                    if st.button("Display attendance"):
                        pass
                run_var=True
            
        else:
            df=pd.read_csv("attendance.csv")
            columns = ["Roll Number", "Name", "Attendance"]
            data = df[columns]
            edited_df = st.data_editor(df)
            if st.button("save"):
                edited_df.to_csv("attendance.csv",index=False)

    elif type_cookie=='student' or user_type == 'student' :
        st.title("Student Dashboard")

# Check if 'attendance.csv' is present in the parent folder
        file_path = "../attendance.csv"
        progress=st.empty()
        while True:
            if os.path.isfile(file_path):
                df=pd.read_csv(file_path)
                columns = ["Roll Number", "Name", "Attendance"]
                data = df[columns]
                progress.table(data)
            time.sleep(2)
    elif user_type=="invalid":
        st.sidebar.error("Invalid Username or Password")
try:
    with open('type_cookie.txt', 'r') as file:
        type_cookie = file.read().strip()
        if type_cookie=="" or type_cookie=="None" or type_cookie=="invalid":
            type_cookie=None
except FileNotFoundError:
    type_cookie=None
try:
    with open('run.txt', 'r') as file:
        run_var = file.read().strip()
        if run_var=="" or run_var=="None" or run_var=="False":
            run_var=False
except FileNotFoundError:
    run_var=False
if __name__=="__main__":
    main()
with open('type_cookie.txt', 'w') as file:
    file.write(str(type_cookie))
with open('run.txt', 'w') as file:
    file.write(str(run_var))