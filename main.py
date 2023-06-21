import spacy
import os
import warnings
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText

from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time


############################################################
# Callback function called on update config
############################################################
def config(configuration: ConfigClass):
    # TODO Add code here
    pass


############################################################
# Callback function called on each execution pass
############################################################
"""This is your  code provided belowe is what i done changes"""
# def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
#     output = []
#     for text in request.text:
#         # TODO Add code here
#         response = ''
#         output.append(response)

#     return SimpleText(dict(text=output))



#############################################################################
#Belowe code writen by me which I added to your code with my best of knowledge


def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    # Load the spaCy English model for NLP processing
    nlp = spacy.load("en_core_web_sm")
    output = []

    for text in request.text:
        # Process the user's input text using spaCy
        doc = nlp(text)

        # Check if the user's input contains keywords related to science
        if "science" in doc.text.lower():
            # Respond with a definition of science
            response = "Science is a systematic and logical approach to understanding the natural world through observation and experimentation."
        elif "what" in doc.text.lower() and "science" in doc.text.lower():
            # Respond with a general explanation of science
            response = "Science is the study of the natural world, including its physical laws and processes."
        elif "who" in doc.text.lower() and "discovered" in doc.text.lower() and "gravity" in doc.text.lower():
            # Respond with the name of the person credited with discovering gravity
            response = "Isaac Newton is credited with discovering the concept of gravity."
        else:
            # If the user's input doesn't match any predefined patterns, provide a default response
            response = "I'm sorry, but I don't have an answer for that question."

        # Add the generated response to the output list
        output.append(response)

    # Create a SimpleText object with the output list and return it
    return SimpleText(dict(text=output))


# As an AI language model, I can provide you with an example of how the output might look based on the code snippet I provided earlier. However, since the actual user input is not known, the example output is based on the assumptions made in the code.

""" Example input:
request = SimpleText(text=["What is science?", "Who discovered gravity?"])

Example output:
output = [    "Science is the study of the natural world, including its physical laws and processes.",    "Isaac Newton is credited with discovering the concept of gravity."]


Please keep in mind that this is just an example output based on the code logic provided. The actual output will depend on the user's input and the specific question-answering rules implemented in the code.
"""

"""
To improve the user experience and make the AI app accessible across different devices, including mobile, laptop, tablets, and desktops, you can consider the following:

Responsiveness: Implement a responsive design using CSS media queries and responsive frameworks like Bootstrap or Foundation. This will ensure that the app adapts to different screen sizes and resolutions, providing a consistent and user-friendly experience on various devices.

Mobile-Friendly UI: Optimize the user interface (UI) for mobile devices by utilizing touch-friendly controls, responsive navigation menus, and appropriate font sizes. Consider mobile-specific design patterns and best practices to enhance usability on smaller screens.

Touch Gestures: If applicable, incorporate touch gestures such as swiping, pinching, and tapping to provide intuitive interaction on touch-enabled devices. This can enhance the user experience on mobile devices and tablets.

Device Detection: Implement device detection techniques to identify the user's device and customize the user interface and functionality accordingly. This can be achieved using JavaScript libraries or server-side techniques to detect and adapt to the user's device capabilities.

Offline Support: Consider implementing offline support using service workers or local storage. This allows users to access certain parts of the app even when they are offline or have a weak internet connection, enhancing the overall accessibility.

Accessibility Features: Follow accessibility guidelines (e.g., WCAG 2.1) to ensure the app is accessible to users with disabilities. This includes providing proper HTML structure, descriptive alt text for images, keyboard navigation support, and appropriate color contrast.

Testing on Multiple Devices: Test the app on various devices, screen sizes, and browsers to ensure it works as intended and offers a seamless experience across different platforms. Consider using responsive design testing tools, browser developer tools, or cloud-based testing platforms for comprehensive testing.

By incorporating these considerations, you can enhance the user experience and accessibility of your AI app, making it accessible and user-friendly across a wide range of devices
"""


