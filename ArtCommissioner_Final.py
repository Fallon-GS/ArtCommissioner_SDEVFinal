"""
Author: Fallon Skeens
Date: 5/9/25
Program: Art Commissioner
Version: 2.0
Description: This program allows a user to get the price estimate for a commissioned piece of art, based on specified aspects of their request.
"""
import tkinter as tk
from tkinter import ttk, messagebox

class ArtCommissioner(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Artist Commissioner")
        
        # Main window
        bgColor = "#FFECA1"
        self.configure(bg=bgColor)
        labelTitle = tk.Label(self, text="Artist Commissioner", font="Helvetica 22 bold",
                               fg="#5D158C",
                               bg=bgColor, borderwidth=0, highlightthickness=0)
        labelTitle.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Image of paint palette
        origImage = tk.PhotoImage(file="paintpallet.gif")
        self.image = origImage.subsample(2, 2)
        labelImage = tk.Label(self, image=self.image, bg=bgColor, borderwidth=0, highlightthickness=0)
        labelImage.place(x=0, y=0)

        # Image of paint brush
        paintBrush = tk.PhotoImage(file="paintbrush.gif")
        self.smallBrush = paintBrush.subsample(6, 6)
        brushLabel = tk.Label(self, image=self.smallBrush, bg="#FFECA1", borderwidth=0, highlightthickness=0)
        brushLabel.place(relx=0.0, rely=1.0, x=10, y=-10, anchor="sw")
        
        # Art Medium
        labelArtMedium = tk.Label(self, text="Art Medium:", font="Arial 12 bold",
                                  fg="#E95D95",
                                  bg=bgColor, borderwidth=0, highlightthickness=0)
        labelArtMedium.grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.artMediumChoiceVar = tk.StringVar()
        self.artMediumChoice = ttk.Combobox(self, textvariable=self.artMediumChoiceVar,
                                            values=["Painting", "Digital Art Print", "Sketch"],
                                            state="readonly", width=25)
        self.artMediumChoice.grid(row=1, column=1, padx=5, pady=5)
        
        # Size
        labelSize = tk.Label(self, text="Size:", font="Arial 12 bold",
                             fg="#E95D95",
                             bg=bgColor, borderwidth=0, highlightthickness=0)
        labelArtMedium.grid(row=1, column=0, sticky="e", padx=5, pady=5)
        labelSize.grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.sizeChoiceVar = tk.StringVar()
        self.sizeChoice = ttk.Combobox(self, textvariable=self.sizeChoiceVar,
                                       values=["Small", "Medium", "Large"],
                                       state="readonly", width=25)
        self.sizeChoice.grid(row=2, column=1, padx=5, pady=5)
        
        # Subject
        labelSubject = tk.Label(self, text="Subject:", font="Arial 12 bold",
                                fg="#E95D95",
                                bg=bgColor, borderwidth=0, highlightthickness=0)
        labelSubject.grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.subjectChoiceVar = tk.StringVar()
        self.subjectChoice = ttk.Combobox(self, textvariable=self.subjectChoiceVar,
                                          values=["Landscape", "Still Life", "Portrait", "Pet Portrait"],
                                          state="readonly", width=25)
        self.subjectChoice.grid(row=3, column=1, padx=5, pady=5)
        self.subjectChoice.bind("<<ComboboxSelected>>", self.onSubjectChange)
        
        # Detailed Background
        self.backgroundVar = tk.IntVar()
        self.backgroundCheck = tk.Checkbutton(self, text="Include Detailed Background", font="Arial 12 bold",
                                              fg="#E95D95",
                                              bg=bgColor, borderwidth=0, highlightthickness=0,
                                              variable=self.backgroundVar)
        self.backgroundCheck.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        
        # Extra People/Pets
        labelExtra = tk.Label(self, text="Extra People/Pets (number):", font="Arial 12 bold",
                              fg="#E95D95",
                              bg=bgColor, borderwidth=0, highlightthickness=0)
        labelExtra.grid(row=5, column=0, sticky="e", padx=5, pady=5)
        self.extraField = tk.Entry(self, width=27)
        self.extraField.grid(row=5, column=1, padx=5, pady=5)

        # Additional Details
        labelDetails = tk.Label(self, text="Additional Details (Must be reviewed by the artist):", font="Arial 10 bold",
                                fg="#E95D95",
                                bg=bgColor, borderwidth=0, highlightthickness=0)
        labelDetails.grid(row=6, column=0, sticky="ne", padx=5, pady=5)
        self.detailsArea = tk.Text(self, width=40, height=5)
        self.detailsArea.grid(row=6, column=1, padx=5, pady=5)
        
        # Price estimate button
        btnEstimate = tk.Button(self, text="Get Price Estimate", 
                                bg="#5DE2E7", 
                                fg="#FFFFFF", 
                                command=self.computeEstimate)
        btnEstimate.grid(row=7, column=0, columnspan=2, padx=5, pady=10)
        
        # Exit button
        btnExit = tk.Button(self, text="Exit", 
                            bg="#E95D95",
                            fg="#FFFFFF",
                            command=self.exitProgram)
        btnExit.grid(row=8, column=0, columnspan=2, padx=5, pady=5)
    
    def onSubjectChange(self, event):
        """Disable the background checkbox when subject is 'Landscape'."""
        subject = self.subjectChoice.get()
        if subject == "Landscape":
            self.backgroundCheck.config(state="disabled")
            self.backgroundVar.set(0)
        else:
            self.backgroundCheck.config(state="normal")
    
    def computeEstimate(self):
        """Compute the price, and display the result."""
        artMedium = self.artMediumChoice.get()
        size = self.sizeChoice.get()
        subject = self.subjectChoice.get()
        detailedBackground = self.backgroundVar.get()
        extraText = self.extraField.get()
        additionalDetails = self.detailsArea.get("1.0", tk.END).strip()
        
        # Validate input
        try:
            extraCount = int(extraText) if extraText != "" else 0
        except ValueError:
            messagebox.showerror("Input Error", 
                "Please enter a valid whole number for extra people/pets (Ex. 2 or 4).")
            return
        
        # Price based on art medium
        if artMedium == "Painting":
            basePrice = 100
        elif artMedium == "Digital Art Print":
            basePrice = 80
        elif artMedium == "Sketch":
            basePrice = 70
        else:
            basePrice = 100
        
        # Price based on size
        if size == "Small (8x10)":
            sizeCost = 0
        elif size == "Medium (16x20)":
            sizeCost = 40
        elif size == "Large (24x30)":
            sizeCost = 80
        else:
            sizeCost = 0
        
        # Price based on subject
        if subject == "Landscape":
            subjectCost = 30
        elif subject == "Still Life":
            subjectCost = 20
        elif subject == "Portrait":
            subjectCost = 50
        elif subject == "Pet Portrait":
            subjectCost = 40
        else:
            subjectCost = 10
        
        # Additional background cost
        backgroundCost = 50 if subject != "Landscape" and detailedBackground else 0
        
        # Additional cost for extra people/pets
        extraCost = extraCount * 30
        
        # Compute the total price
        total = basePrice + sizeCost + subjectCost + backgroundCost + extraCost
        
        # Display the result
        ResultFrame(total, additionalDetails)
    
    def exitProgram(self):
        """Exit the application."""
        self.destroy()

class ResultFrame(tk.Toplevel):
    def __init__(self, total, additionalDetails):
        super().__init__()
        self.configure(bg="#FFECA1")
        self.title("Commission Estimate")
        self.geometry("350x250")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Display the estimated price
        labelTotal = tk.Label(self, text=f"Estimated Price: ${total}", font="Helvetica 16 bold",
                              fg="#5D158C",
                              bg="#FFECA1", borderwidth=0, highlightthickness=0,
                              anchor="center")
        labelTotal.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        # If additional details were provided, display them as well
        if additionalDetails:
            labelInfo = tk.Label(self, text="Additional Information:",
                                 font="Arial 12 bold",
                                 fg="#E95D95",
                                 bg="#FFECA1", borderwidth=0, highlightthickness=0,
                                 anchor="center")
            labelInfo.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
            textDetails = tk.Text(self, width=30, height=5)
            textDetails.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
            textDetails.insert(tk.END, additionalDetails)
            textDetails.config(state="disabled")
        
        # Close button
        btnClose = tk.Button(self, text="Close",
                             bg="#E95D95",
                             fg="#FFFFFF",
                             anchor="center",
                             command=self.destroy)
        btnClose.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

def main():
    app = ArtCommissioner()
    app.mainloop()

if __name__ == '__main__':
    main()
