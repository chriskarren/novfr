import logging
import json
import os
import tempfile
import azure.functions as func
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import FormRecognizerClient


def main(req: func.HttpRequest) -> func.HttpResponse:
    # Set up logging
    logging.info('Python HTTP trigger function processed a request.')

    # Initialize Form Recognizer client
    subscription_key = "c9b00785b0154b6c8f399564fc2dc2d6"
    endpoint = "https://cog-fr-igv2zmlceav2g.cognitiveservices.azure.com/"
    credential = AzureKeyCredential(subscription_key)
    form_recognizer_client = FormRecognizerClient(endpoint, credential)

# Check if the request has a body
    if not req.get_body():
        return func.HttpResponse("No image data found in the request body", status_code=400)

    try:
        # Get the image data from the request body
        image_data = req.get_body()
        length = len(image_data)

        
        logging.info(f'Length of this bytes object is {length}.')


    except Exception as e:
        return func.HttpResponse(f"An error occurred: {str(e)}", status_code=500)
 
    try:
        result = form_recognizer_client.begin_recognize_content(image_data, content_type="image/jpeg").result()

        extracted_text = ""
        for page in result:
            for line in page.lines:
                 extracted_text += line.text + " "

            response_data = {
                'extracted_text': extracted_text.strip()
            }

            return func.HttpResponse(
                json.dumps(response_data),
                mimetype='application/json',
                status_code=200
            )
        else:
            return func.HttpResponse(
                "No files provided.",
                status_code=400
            )
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return func.HttpResponse(
            "An error occurred during processing.",
            status_code=500
        )






    # file_field_name = 'good.jpeg'
    # if file_field_name not in req.get_body():
    #      return func.HttpResponse(
    #           "No files provided.",
    #             status_code=400
    #      )
    # file = req.files[file_field_name]

     # files = req.files
        # if files:
        #     file_field_name = next(iter(files))
        #     image_file = files[file_field_name]

#------------------------------------------------------------------------------------------------------------------------------------






# import json
# import logging
# import azure.functions as func
# from azure.core.credentials import AzureKeyCredential
# from azure.ai.formrecognizer import FormRecognizerClient


# def main(req: func.HttpRequest) -> func.HttpResponse:
#     # Set up logging
#     logging.info('Python HTTP trigger function processed a request.')

#     # Initialize Form Recognizer client
#     subscription_key = "c9b00785b0154b6c8f399564fc2dc2d6"
#     endpoint = "https://cog-fr-igv2zmlceav2g.cognitiveservices.azure.com/"
#     credential = AzureKeyCredential(subscription_key)
#     form_recognizer_client = FormRecognizerClient(endpoint, credential)

#     # Retrieve the image data from the request
#     try:
#         files = req.files
#         if "image" in files:
#             image_file = files["image"]
#             image_data = image_file.read()
#             try: 
#                 result = form_recognizer_client.begin_recognize_content(image_data, content_type="image/jpeg").result()
#                 extracted_text = ""
#                 for page in result:
#                     for line in page.lines:
#                         extracted_text += line.text + " "
#             except Exception as ex:
#                 logging.error(str(ex))
#                 logging.info("An error occurred while recognizing content")
#     except Exception as ex:
#         logging.error(str(ex))
#         logging.info("An error occurred while retrieving image data")

    # name = req.params.get('name')
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #         name = req_body.get('name')
    #     except ValueError:
    #         pass

    # if extracted_text:
    #     # Create a JSON object with extracted text
    #     json_data = {
    #         "extracted_text": extracted_text
    #     }
    #     json_string = json.dumps(json_data)

    #     # Return JSON response with content type header
    #     return func.HttpResponse(
    #         body=json_string,
    #         mimetype="application/json",
    #         status_code=200
    #     )
    # else:
    #     return func.HttpResponse(
    #          "No text was extracted from the provided image.",
    #          status_code=200)


    # if name:
    #     return func.HttpResponse(json)
    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #          status_code=200
    #     )

    # except Exception as ex:
    #     logging.error(str(ex))
    #     return func.HttpResponse(
    #          "An error occurred while recognizing content.",
    #          status_code=500
    #     )

# import json
# import logging
# import azure.functions as func
# from azure.core.credentials import AzureKeyCredential
# from azure.ai.formrecognizer import FormRecognizerClient


# def main(req: func.HttpRequest) -> func.HttpResponse:
#     # Set up logging
#     logging.info('Python HTTP trigger function processed a request.')

#     # Initialize Form Recognizer client
#     subscription_key = "c9b00785b0154b6c8f399564fc2dc2d6"
#     endpoint = "https://cog-fr-igv2zmlceav2g.cognitiveservices.azure.com/"
#     credential = AzureKeyCredential(subscription_key)
#     form_recognizer_client = FormRecognizerClient(endpoint, credential)

#     # Retrieve the image data from the request
#     try:
#         files = req.files
#         if "image" in files:
#             image_file = files["image"]
#             image_data = image_file.read()
#             try: 
#                 result = form_recognizer_client.begin_recognize_content(image_data, content_type="image/jpeg").result()
#                 extracted_text = ""
#                 for page in result:
#                     for line in page.lines:
#                         extracted_text += line.text + " "
#             except Exception as ex:
#                 logging.error(str(ex))
#                 logging.info("An error occurred while recognizing content")
#     except Exception as ex:
#         logging.error(str(ex))
#         logging.info("An error occurred while retrieving image data")

#     name = req.params.get('name')
#     if not name:
#         try:
#             req_body = req.get_json()
#             name = req_body.get('name')
#         except ValueError:
#             pass

#     if extracted_text:
#         # Create a JSON object with extracted text
#         json_data = {
#             "extracted_text": extracted_text
#         }
#         json_string = json.dumps(json_data)

#         # Return JSON response with content type header
#         return func.HttpResponse(
#             body=json_string,
#             mimetype="application/json",
#             status_code=200
#         )
#     else:
#         return func.HttpResponse(
#              "No text was extracted from the provided image.",
#              status_code=200)


    # if name:
    #     return func.HttpResponse(json)
    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #          status_code=200
    #     )


# import logging


# import azure.functions as func
# from azure.core.credentials import AzureKeyCredential
# from azure.ai.formrecognizer import FormRecognizerClient


# def main(req: func.HttpRequest) -> func.HttpResponse:
#     logger = logging.getLogger()
#     logger.setLevel(logging.DEBUG)
#     logging.info('Python HTTP trigger function processed a request.')

#     logging.info("here1")
#     subscription_key = "c9b00785b0154b6c8f399564fc2dc2d6"
#     endpoint = "https://cog-fr-igv2zmlceav2g.cognitiveservices.azure.com/"

#     credential = AzureKeyCredential(subscription_key)
#     form_recognizer_client = FormRecognizerClient(endpoint, credential)
#     logging.info("here2")

#     # Retrieve the image data from the request
#     try:
#         files = req.files
#         if "image" in files:
#             image_file = files["image"]
#             image_data = image_file.read()
#             try: 
#                 result = form_recognizer_client.begin_recognize_content(image_data, content_type="image/jpeg").result()
#             except Exception as ex:
#                 logging.error(str(ex))
#                 logging.info("here4")
#     except Exception as ex:
#         logging.error(ex)
#         logging.info("here3")

#         logging.debug('at get form recognizer')


        
#         logging.debug('at extracted text')
    
#     try:
#         image_file = files["image"]
#         image_data = image_file.read()
#         result = form_recognizer_client.begin_recognize_content(image_data, content_type="image/jpeg").result()
#         extracted_text = ""
#         for page in result:
#             for line in page.lines:
#                 extracted_text += line.text + " "
#     except Exception as ex:
#         logging.error(str(ex))

#     name = req.params.get('name')
#     if not name:
#         try:
#             req_body = req.get_json()
#         except ValueError:
#             pass
#         else:
#             name = req_body.get('name')

#     if name:
#         return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
#     else:
#         return func.HttpResponse(
#              "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
#              status_code=200
#         )

#F!!!!F!!F!!!!!!!!!!!!

# def main(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function processed a request.')



#     # Call the Form Recognizer API
#     logging.debug('at get form recognizer')
#     try: 
#         result = form_recognizer_client.begin_recognize_content(image_data).result()
#     except Exception as ex:
#         logging.error(ex)
    
#     # Process the result and extract relevant information
#     logging.debug('at extracted text')
#     extracted_text = ""
#     for page in result:
#         for line in page.lines:
#             extracted_text += line.text + " "

#     # Return the extracted text as the HTTP response
#     return func.HttpResponse(extracted_text)

    # image_data = req.get_body()
        # logging.debug(image_data)






  ######## # try: 
    #     result = form_recognizer_client.begin_recognize_content(image_data, content_type="image/jpeg").result()
    # except Exception as ex:
    #     logging.error(str(ex))
    #     logging.info("here4")