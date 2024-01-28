import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps2.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]
le_db = data["le_db"]
le_language = data["le_language"]
le_dev = data["le_dev"]
le_tech = data["le_tech"]
le_employment = data["le_employment"]

def show_skill_assessment_page():
    st.title("Software Developer Hiring predictor")

    st.write("""### We need some information to predict the candidate hiring status""")

    countries = (
        "United States",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Netherlands",
        "Australia",
        "Italy",
        "Poland",
        "Spain",
    )

    education = (
        "Master's degree",
        "Bachelor's degree",
        "Less than a Bachelors",
        "Post grad",
    )

    db = (
        "Microsoft SQL Server",
        "MySQL",
        "PostgreSQL",
        "Microsoft SQL Server;MySQL",
        "MongoDB",
        "Microsoft SQL Server;SQLite",
        "MySQL;PostgreSQL",
        "SQLite",
        "MongoDB;MySQL",
        "MySQL;SQLite",
        "Microsoft SQL Server;PostgreSQL",
        "Microsoft SQL Server;MySQL;SQLite",
        "MariaDB;MySQL",     
    )

    language = (
        "C#;HTML/CSS;JavaScript;SQL",
        "C#;HTML/CSS;JavaScript;SQL;TypeScript",
        "HTML/CSS;JavaScript;TypeScript",
        "HTML/CSS;JavaScript;PHP;SQL",
        "Bash/Shell/PowerShell;C#;HTML/CSS;JavaScript;SQL;TypeScript",    
    )

    dev = (
        "Developer, full-stack",
        "Developer, back-end;Developer, front-end;Developer, full-stack",
        "Developer, back-end",
        "Developer, back-end;Developer, full-stack",
        "Developer, back-end;Developer, desktop or enterprise applications;Developer, front-end;Developer, full-stack",
        "Developer, front-end;Developer, full-stack",
        "Developer, front-end",
        "Developer, back-end;Developer, front-end;Developer, full-stack;Developer, mobile",
        "Developer, mobile",
        "Developer, back-end;Developer, desktop or enterprise applications",
        "Developer, back-end;Developer, desktop or enterprise applications;Developer, full-stack",
    )

    tech = (
        "Node.js",
        ".NET;.NET Core",
        ".NET",
        ".NET;.NET Core;Node.js",
        "Node.js;React Native",
        "Pandas",
        "Ansible",
        ".NET;Node.js",
        ".NET Core",
        "Cordova;Node.js",
        "React Native",
        ".NET;.NET Core;Xamarin",
        "Flutter",  
        ".NET Core;Node.js",     
        "Ansible;Node.js",
        "Node.js;Pandas",
    )

    country = st.selectbox("Country", countries)
    educatio = st.selectbox("Education Level", education)
    selected_db = st.selectbox("Database", db)
    selected_language = st.selectbox("Language", language)
    selected_devType = st.selectbox("Dev Type", dev)
    selected_tech = st.selectbox("Technology", tech)

    experience = st.slider("Years of Experience", 0, 50, 3)

    ok = st.button("Assess")
    if ok:
        X = np.array([[country, educatio , experience, selected_db, selected_language, selected_devType, selected_tech]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X[:, 3] = le_db.transform(X[:,3])
        X[:, 4] = le_language.transform(X[:,4])
        X[:, 5] = le_dev.transform(X[:,5])
        X[:, 6] = le_tech.transform(X[:,6])

        X = X.astype(float)
        
        status = regressor.predict(X)
        st.subheader(f"The estimated employee status {status[0]:.2f}")

        threshold = 0.33

        if status[0] < threshold:
            final_prediction = 'Not employed'
        elif status[0] < 2 * threshold:
            final_prediction = 'Intern'
        else:
            final_prediction = 'Employed full-time'

        subheader_color = "#ff0000"

        st.markdown(
            f"""
            <h2 style='color:{subheader_color};'>{final_prediction}</h2>
            """,
            unsafe_allow_html=True,
        )
        #st.subheader(final_prediction)