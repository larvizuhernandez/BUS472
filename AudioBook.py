#Creating Audio Book out of PDF without GUI
#We are creating an Audio Book that reads a PDF file from our computer

#pip install gtts
#pip install pypdf2
#you don’t need to install anything for import os. The os module is a built-in Python library,
# meaning it comes pre-installed with Python. You can use it directly without any additional installation.

from gtts import gTTS  # Import gTTS (Google Text-to-Speech) to convert text to speech
from PyPDF2 import PdfReader  # Import PdfReader to read PDF files
import os  # Import os module to interact with the operating system

# Open the PDF file in binary read mode
book = open('file1.pdf', 'rb') #mislead is the name of the PDF file that I have in my pythonProject2 folder in Computer

# Create a PdfReader object to read the PDF
pdfReader = PdfReader(book)

# Get the total number of pages in the PDF
pages = len(pdfReader.pages)

# Initialize an empty string to store the text of the entire PDF
full_text = ""

# Loop through all pages of the PDF and extract text
for num in range(pages):  # Iterate through each page
   page = pdfReader.pages[num]  # Get the current page
   text = page.extract_text()  # Extract text from the page
   if text:  # Check if text extraction was successful
       full_text += text  # Append extracted text to the full text string (i.e., full_text = text +1)

# Close the PDF file after reading
book.close()

# Convert the full extracted text to speech using gTTS
tts = gTTS(text=full_text, lang='en')  # Convert text to speech in English
#also, if you want to slow the speed of the voice, change the code above to:
#tts = gTTS(text=full_text, lang='en', slow=False) # Set slow=True for slower speech, False for normal

# for British accent, change the line of the code above to:
#tts = gTTS(text=full_text, lang='en', tld='co.uk')  or to co.au for Australian or co.in for indian

# Save the speech as a single MP3 file
tts.save("mislead_audiobook.mp3")  # Save the generated speech to an MP3 file

# Play the saved MP3 file using the default system media player
print("Playing the audiobook...")  # Inform the user that playback is starting
os.startfile("mislead_audiobook.mp3")

#***************************************************************************************


#Creating Audio Book out of PDF without GUI
#We are creating an Audio Book that reads a PDF file from our computer

#pip install gtts
#pip install pypdf2
#you don’t need to install anything for import os. The os module is a built-in Python library,
# meaning it comes pre-installed with Python. You can use it directly without any additional installation.

from gtts import gTTS  # Import gTTS (Google Text-to-Speech) to convert text to speech
from PyPDF2 import PdfReader  # Import PdfReader to read PDF files
import os  # Import os module to interact with the operating system

# Open the PDF file in binary read mode
book = open('file1.pdf', 'rb') #mislead is the name of the PDF file that I have in my pythonProject2 folder in Computer

# Create a PdfReader object to read the PDF
pdfReader = PdfReader(book)

# Get the total number of pages in the PDF
pages = len(pdfReader.pages)

# Initialize an empty string to store the text of the entire PDF
full_text = ""

# Loop through all pages of the PDF and extract text
for num in range(pages):  # Iterate through each page
   page = pdfReader.pages[num]  # Get the current page
   text = page.extract_text()  # Extract text from the page
   if text:  # Check if text extraction was successful
       full_text += text  # Append extracted text to the full text string (i.e., full_text = text +1)

# Close the PDF file after reading
book.close()

# Convert the full extracted text to speech using gTTS
tts = gTTS(text=full_text, lang='en')  # Convert text to speech in English
#also, if you want to slow the speed of the voice, change the code above to:
#tts = gTTS(text=full_text, lang='en', slow=False) # Set slow=True for slower speech, False for normal

# for British accent, change the line of the code above to:
#tts = gTTS(text=full_text, lang='en', tld='co.uk')  or to co.au for Australian or co.in for indian

# Save the speech as a single MP3 file
tts.save("mislead_audiobook.mp3")  # Save the generated speech to an MP3 file

# Play the saved MP3 file using the default system media player
print("Playing the audiobook...")  # Inform the user that playback is starting
os.startfile("mislead_audiobook.mp3")

#***************************************************************************************

#Creating audio book out of PDF
#We are creating an audio book that reads PDF but allows choosing the PDF using GUI

import tkinter as tk
from tkinter import filedialog, messagebox  # Tkinter modules for GUI and file selection
from gtts import gTTS  # Import gTTS (Google Text-to-Speech) to convert text to speech
from PyPDF2 import PdfReader  # Import PdfReader to read PDF files
import os  # Import os module to interact with the operating system

# Create the main Tkinter window
root = tk.Tk()
root.title("PDF to Audiobook Converter")
root.geometry("400x200")  # Set the size of the window

# Function to select PDF and convert it to audiobook
def convert_to_audiobook():
   # Open a new file dialog window that allows user to select a PDF file from computer
   pdf_path = filedialog.askopenfilename(title="Select a PDF file", filetypes=[("PDF Files", "*.pdf")])

   if not pdf_path:  # Check if the user did not select a file
       messagebox.showwarning("No file selected", "Please select a PDF file to convert.")
       return

   try:
       # Open the selected PDF file in binary read mode
       with open(pdf_path, 'rb') as book:
           # Create a PdfReader object to read the PDF
           pdfReader = PdfReader(book)

           # Get the total number of pages in the PDF
           pages = len(pdfReader.pages)

           # Initialize an empty string to store the text of the entire PDF
           full_text = ""

           # Loop through all pages of the PDF and extract text
           for num in range(pages):  # Iterate through each page
               page = pdfReader.pages[num]  # Get the current page
               text = page.extract_text()  # Extract text from the page
               if text:  # Check if text extraction was successful
                   full_text += text  # Append extracted text to the full text string

       # Convert the full extracted text to speech using gTTS
       tts = gTTS(text=full_text, lang='en')  # Convert text to speech in English

       # Save the speech as a single MP3 file
       output_mp3 = pdf_path.rsplit('.', 1)[0] + "_audiobook.mp3"  # Create an output filename
       tts.save(output_mp3)  # Save the generated speech to an MP3 file

       # Inform the user the audiobook has been created
       messagebox.showinfo("Success", f"Audiobook has been created and saved as {output_mp3}")

       # Optionally, play the saved MP3 file using the default system media player
       os.startfile(output_mp3)  # Play the saved MP3 file

   except Exception as e:
       messagebox.showerror("Error", f"An error occurred: {e}")  # Show an error if something goes wrong


# Create and place a button to trigger the PDF to audiobook conversion
convert_button = tk.Button(root, text="Convert PDF to Audiobook", command=convert_to_audiobook, padx=20, pady=10)
convert_button.pack(expand=True)  # Center the button on the window

# Start the Tkinter event loop to display the window
root.mainloop()


#**********************************************************************
