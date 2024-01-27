from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

class DialogueManager(object):
    def __init__(self):
        self.chatbot = ChatBot("New_Bot")
        conversation = [
            "You can upload your products in several ways. The application allows importing from PDF files, CSV files, and even extracting data directly from images. Simply choose the option that suits you best in the product upload menu.",
            "Currently, the application supports PDF files, CSV files, and it can also extract product information from images.",
            "Yes, the application allows importing products from PDF files. You just need to select the PDF file containing your product information, and the application will extract the relevant data.",
            "Yes, you can perform bulk product upload using CSV files. Just upload the file, and the application will process the information.",
            "Yes, the application has an automatic extraction feature that analyzes PDF files and retrieves key information about your products to facilitate bulk publishing.",
            "Data extraction from images is done using optical character recognition (OCR) technologies. Simply upload the image containing product information, and the application will automatically convert the information into usable data.",
            "Yes, you can review and edit your product information before bulk publishing. The application provides editing tools to ensure that each publication meets your requirements."

        ]
        trainer = ListTrainer(self.chatbot)
        trainer.train(conversation)

    def generate_answer(self, question):
        return self.chatbot.get_response(question)



