import os
import google.generativeai as genai
from flask import Flask, jsonify, request
from flask_cors import CORS
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure CORS
CORS(app)


previous_data="""Your name is Gracy your a chatbot designed by Samcharles  to speak about Francos Xavier Engineering College and he's doing final final in ECE department.Francis Xavier Engineering College (FXEC), nestled in the heart of Tirunelveli, Tamil Nadu, stands as a bastion of academic prowess and innovation since its inception in 2000. Renowned for its commitment to excellence, FXEC has emerged as a trailblazer in the field of technical education, offering a diverse array of programs across various disciplines.

Under the aegis of the St. Xavier’s Educational Trust, FXEC has garnered widespread acclaim for its unwavering dedication to fostering a culture of academic excellence and holistic development. The institution's autonomous status, coupled with accreditation from esteemed bodies such as the National Board of Accreditation (NBA) and support from the Department of Science and Technology (DST) under the FIST initiative, underscores its commitment to delivering quality education.

FXEC's academic portfolio spans a wide spectrum, encompassing undergraduate, postgraduate, and doctoral programs tailored to meet the evolving needs of industry and society. From Bachelor of Technology (B.Tech) and Bachelor of Engineering (B.E) to Master of Business Administration (MBA) and Master of Computer Applications (MCA), the college offers a comprehensive range of programs designed to empower students with the knowledge and skills needed to thrive in the competitive global landscape.

Each academic group within FXEC is dedicated to excellence in its respective field. The Department of Electrical and Electronics Engineering (EEE), Department of Electronics and Communication Engineering (ECE), Department of Computer Science and Engineering (CSE), and Department of Information Technology (IT) are instrumental in shaping future technocrats and innovators. Similarly, the Department of Civil Engineering (CE) and Department of Mechanical Engineering (ME) cater to the diverse needs of the infrastructure and manufacturing sectors, respectively.

The institution's commitment to fostering a culture of innovation and entrepreneurship is exemplified by its numerous accolades, including a Platinum Rating in the AICTE-CII Survey of Technical Institutes and a Four Star Status conferred by the Ministry of Education, Government of India. FXEC's exemplary performance in national rankings, such as the "NIRF India Innovation Ranking 2023," further cements its status as a beacon of excellence in higher education.

FXEC's research endeavors are bolstered by substantial funding from esteemed government agencies such as DST, AICTE, MNRE, ISRO, and DRDO. The college's collaboration with industry leaders, including IBM, CDAC, HCL, and Sutherland, facilitates hands-on learning experiences and industry-relevant projects, ensuring that graduates are well-equipped to tackle real-world challenges.

In addition to academic pursuits, FXEC places a strong emphasis on extracurricular activities and community engagement. Student clubs and societies, such as the IEEE Student Branch, ISTE Chapter, and Entrepreneurship Development Cell, provide platforms for students to hone their leadership skills, showcase their talents, and contribute to societal welfare.

Under the dynamic leadership of Chairman Cletus Babu, FXEC continues its journey of academic excellence and innovation, steadfast in its commitment to nurturing the next generation of leaders, innovators, and change-makers. With a focus on academic rigor, industry relevance, and holistic development, FXEC is poised to shape the future of engineering education and make a lasting impact on society."""




# Configure logging
logging.basicConfig(filename='error.log', level=logging.DEBUG)

# Configure the Google API key
os.environ['GOOGLE_API_KEY'] = 'AIzaSyDpp_vnAlO1-1_2TcPsDGm4dhN41F2ZPCU'
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Initialize the generative model and chat
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

chat.send_message(previous_data)



@app.route('/')
def hello_world():
    app.logger.debug('Hello world endpoint was called')
    return "Gracy's Gemini!"

@app.route('/gemini', methods=['POST'])
def gemini_response_chat():
    data = request.json
    app.logger.debug(f'Received data: {data}')
    try:
        query = data.get('query')
        response =  chat.send_message(query)
        app.logger.debug(f'Response from chat: {response.text}')
        return jsonify({'response': response.text})
    except Exception as e:
        app.logger.error(f'Error processing request: {e}')
        return jsonify({'error': str(e)}), 500

# Remove or comment out the app.run() line for PythonAnywhere deployment
if __name__ == "__main__":
    app.run(debug=True)
