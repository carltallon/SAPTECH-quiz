import random
from flask import Flask, render_template
from string import ascii_lowercase

app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')

# QUESTIONS NESTED DICT
QUESTIONS = {
    "Which menus are visible in every transaction? (2 answers) ": [
        "Help", "Support","System","Go-to"
    ],

    "What is the function of the enqueue work process?" : [
        "To manage the logical lock of the SAP Transactions at application level ", "To perform the update of the business data into the database. ",
        "To check and update the lock table with the current locks being held by the users. ","To manage the logical lock of the SAP transactions at Database level"
    ],

    "Which of the following components can perform load balancing?" : [
        "ICM", "SAP GUI", "ABAP Message Server", "Dialog Work Process"
    ],

    "Which of the following represents customer developments? " : [
        "Creation of new report called ZFINANCE","Creation of a new table called ORDERS","Creation of customer exits","Creation of a new client",
    ],

    "For which of the following can you use Application Link Enabling (ALE)?" : [
        "To sync processes between SAP CRM and ERP systems to provide updates","To send and receive messages from different systems via RFC only",
        "To create and operate a distributed application to ensure the operation of a distributed, yet integrated system landscape. ","To exchange data between SAP systems as long as they have the same release status",
    ],

    "Why does SAP recommend a three system landscape?" : [
        "To enable multiple clients per SAP system ","To accommodate the special data structure in SAP Systems",
        "To enable preparing and testing of upgrades","To sell more licenses",
    ],

    "What can you do with the SAP Quick Sizer?" : [
        "Monitor the load of the system during normal operation","Test virtual loads in the system before its productive start",
        "Perform an initial assessment of the hardware required for an SAP system ","Ensure that instances always have a balanced load",
    ],

    "What is rollback?" : [
        "(I)The name of the temporary tables used to store erroneous update requests","The restart of a dialog work process once it has reached its memory limits",
        "The process of restoring the dataset to its previous state after a transaction has terminated with an error","The release of a dialog work process after executing a dialog step. ",
    ],

    "When does a dialog work process access the lock table directly instead of sending a request to the enqueue work process?" : [
        "When a dialog request is processed in the central instance","When the message server cannot forward the request to the central instance. ",
        "When a dialog request is processed in the central instance ","When the enqueuer work process is not available ",
    ],

    "What is the default maintenance period of an SAP product, including mainstream and extended maintenance? " : [
        "9 years","5 years",
    ],

    "What does the ABAP repository contain?" : [
        "All dictionary objects, all ABAP programs, menus and screens ","All application data added to the system by users",
    ],

    "Which of the following is a characteristic of a client? " : [
        "A client has its own business data environment, its own master and transaction data and its own user data and changes",
        "A client contains both business and technical definitions and descriptions of SAP data and enables all data definitions ",
    ],

    "What are Enhancement Packages? " : [
        "A collection of improvements and new functionalities that can be installed by the customer","A collection of corrections that must be installed by the customer",
    ],

    "Which of the following guarantee the reliable processing of database transactions? " : [
        "Consistency ","Dependability","Isolation","Accessibility",
    ],

    "Which of the following are considered to be Single Points of Failure?" : [
        "Database ","SAP GUI","Enqueue Service ","Dialog Instance",
    ],

    "Which services run only on the SAP AS ABAP central instance? " : [
        "The message server","The dispatcher process","The enqueue work process ","The application server",
    ],


    "Which of the following can you use to access the Application level on an SAP NetWeaver AS ABAP system?" : [
        "SAP GUI for Windows PC","SAP Solution Manager","SAP GUI for Java and HTML","Service Marketplace ",
    ],

    "What are advantages of a three tier configuration over a two tier configuration?" : [
        "Load balancing","Simpler installation and configuration","Better scalability","Easier maintenance ",
    ],


    "Which of the following are characteristics of the ABAP Dictionary? " : [
        "It enables all data definitions used in the SAP system to be described and managed centrally. ","It determines during a dialog step what data needs to be exchanged with the database or the buffer",
        "It is a central component of the ABAP Workbench that contains both business and technical definitions and descriptions. ","It contains all programs, tables and function modules available in the system, ",
    ],

    "What is the SAP GUI" : [
        "Software which enables the user to interact with SAP systems based on AS ABAP","An application layer component of SAP NetWeaver AS ABAP ",
    ],

    "What is SAP NetWeaver? " : [
        "An SAP technology platform ","An SAP component ",
    ],

    "Why is a separate work process required to perform the update processing in SAP AS ABAP systems? " : [
        "Because the update is performed asynchronously to permit the execution of a roll-back in case a transaction is incorrect",
        "Because the update is performed synchronously with the dialog step to ensure the information being updated is correct",
    ],

    "How can you start a function in SAP GUI? " : [
        "Choose an item from the user menu","Hold down the Ctrl key and type the function name ",
        "Enter a transaction code in the command field ","Drag and drop the transaction name to the command line",
    ],

    "To which of the following does work process multiplexing refer: " : [
        "Individual dialog steps of a program can be executed by different dialog work processes during program runtime","Dialog work process can be converted to background work processes for batch processing ","","",
    ],

    "What is the SAP business Suite?" : [
        "bundle of end-to-end enterprise software applications that integrate data, processes and functions for important areas such as finance, sales and HR, as well as industry-focused features.",
        "Other",
    ],

    "SAP NetWeaver is a ______ ______." : [
        "a technology platform","networking software"
    ],


    "What is the SAP GUI?" : [
        "Graphical User Interface","Programming language from SAP for developing application programs."
    ],


    "What are the 3 types of SAP GUIs?" : [
        "SAP GUI for JAVA, HTML","SAP GUI for ABAP","SAP GUI for Windows","SAP GUI for Mac",
    ],

    "What is the ACID principle?" : [
        "atomicity, consistency, isolation, and durability","attention, consistency, isolation, and dependability",
    ],

    "What is the NWDI?" : [
        "NetWeaver Development Infrastructure","Next Window Deployment Index",
    ],

    "What is the Buffer?" : [
        "Area in the main memory of an application server in which data frequently used by applications can be temporarily stored.",
        "Wait time for an SAP system to load",
    ],

    "What is the ABAP dictionary?" : [
        "Central redundancy-free information store in the SAP system for the logical structures of application development objects ",
        "Dictionary for terms used within SAP and their definitions.",
    ],

    "What is the system landscape directory for? (SLD)" : [
        "As the central data storage for SAP system landscape information","Monitor the load of the system during normal operation","Test virtual loads in the system before its productive start",
    ],

    "What is an RFC?" : [
        "an SAP interface protocol based on CPI-C. It simplifies the programming of communication processes between systems.","is a Web protocol for reading and updating data based on open standards such as HTTP",
    ],

    "What is Odata?" : [
        "is a Web protocol for reading and updating data based on open standards such as HTTP","an SAP interface protocol based on CPI-C. It simplifies the programming of communication processes between systems."
    ],

    "What can BAPIs be used for?" : [
        " Request data from an SAP system"," Transfer SAP screen images to third-party applications (such as Microsoft Word)",
        "Pass data to an SAP system","Download of SAP screen images to local device",
    ],

    "Which product is the next generation of SAP CRM?" : [
        "SAP Customer Experience","SAP S/4HANA"
    ],

    "Which work process types are there in an AS ABAP-based SAP system?" : [
        "Update work process","Internet Communication Manager (ICM) ",
    ],

    "At the end of the development project, the tasks and transport requests must be released so that they can be exported. Who releases what here?" : [
        "Developers release their tasks.","The system automatically releases the transport request once all tasks are released. ",
        "The development project lead releases the entire transport request.","The customer releases the developers tasks",
    ],
}

def prepare_questions(questions):
    return random.sample(list(questions.items()), k=len(QUESTIONS))

@app.route("/")
def index():
    #shuffle questions and answers
    questions = prepare_questions(QUESTIONS)
    
    #for loop to display questions and pass to html file
    for num, (question, alternatives) in enumerate(questions, start=1): 
        if len(alternatives) > 2:
            correct_answer = alternatives[0]
            correct_answer2 = alternatives[2]
            correctanswercount = 2
            ordered_alternatives = random.sample(alternatives, k=len(alternatives))
            return render_template('index.html',answercount = correctanswercount, num = num, question = question,alternatives = ordered_alternatives, correct_answer = correct_answer, correct_answer2 = correct_answer2)
        else:
            correct_answer = alternatives[0]
            correctanswercount = 1
            ordered_alternatives = random.sample(alternatives, k=len(alternatives))
            return render_template('index.html',answercount = correctanswercount, num = num, question = question,alternatives = ordered_alternatives, correct_answer = correct_answer)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)