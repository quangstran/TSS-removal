import tkinter as tk
from tkinter import messagebox, ttk, filedialog, Toplevel, Text
from datetime import datetime
import os
import json
import markdown

class TSSCalculatorApp:

    def __init__(self, root):
        self.root = root
        self.root.title("TSS Removal Calculator")

        # Set up the menu bar
        menubar = tk.Menu(root)
        root.config(menu=menubar)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_project)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Print", command=self.print_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)

        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="Help", command=self.show_help)

        # Predefined LID Methods and TSS Removal Efficiencies (in %)

        self.lid_methods_dict = {
            'Bioretention': 85,
            'Permeable Pavement': 75,
            'Green Roof': 65,
            'Vegetated Swale': 70,
            'Wet Pond': 80,
            'Sand Filter': 90,
            'Rain Garden': 80,
            'Infiltration Basin': 90
        }

        # Capture current date and time
        self.current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Labels and inputs for project details
        tk.Label(root, text="Project Number").grid(row=0, column=0, padx=10, pady=5)
        self.project_number_entry = tk.Entry(root)
        self.project_number_entry.grid(row=0, column=1)
        tk.Label(root, text="Project Name").grid(row=1, column=0, padx=10, pady=5)
        self.project_name_entry = tk.Entry(root)
        self.project_name_entry.grid(row=1, column=1)
        tk.Label(root, text="Consultant Company Name").grid(row=2, column=0, padx=10, pady=5)
        self.consultant_company_entry = tk.Entry(root)
        self.consultant_company_entry.grid(row=2, column=1)
        tk.Label(root, text="User Name").grid(row=3, column=0, padx=10, pady=5)
        self.user_name_entry = tk.Entry(root)
        self.user_name_entry.grid(row=3, column=1)

        # Labels and inputs for site area and impervious percentage
        tk.Label(root, text="Site Area").grid(row=4, column=0, padx=10, pady=5)
        self.site_area_entry = tk.Entry(root)
        self.site_area_entry.grid(row=4, column=1)
        tk.Label(root, text="Units (m2 or ha)").grid(row=4, column=2, padx=10, pady=5)
        self.units_entry = tk.Entry(root)
        self.units_entry.grid(row=4, column=3)
        tk.Label(root, text="Impervious Percentage").grid(row=5, column=0, padx=10, pady=5)
        self.impervious_percentage_entry = tk.Entry(root)
        self.impervious_percentage_entry.grid(row=5, column=1)

        # LID Methods Dropdown Menu
        tk.Label(root, text="Select LID Method").grid(row=6, column=0, padx=10, pady=10)
        self.lid_method_combobox = ttk.Combobox(root, values=list(self.lid_methods_dict.keys()), state="readonly")
        self.lid_method_combobox.grid(row=6, column=1)
        self.lid_method_combobox.bind("<<ComboboxSelected>>", self.set_tss_efficiency)
        tk.Label(root, text="TSS Removal Efficiency (%)").grid(row=6, column=2, padx=10, pady=10)
        self.tss_efficiency_entry = tk.Entry(root)
        self.tss_efficiency_entry.grid(row=6, column=3)

        # Add Button
        self.add_button = tk.Button(root, text="Add LID Method", command=self.add_lid_method)
        self.add_button.grid(row=6, column=4, padx=10, pady=10)

        # Treeview Table for displaying the LID methods
        columns = ('Index', 'LID Method', 'TSS Efficiency (%)', 'Remaining TSS (%)')
        self.tree = ttk.Treeview(root, columns=columns, show='headings')
        self.tree.heading('Index', text='Index')
        self.tree.heading('LID Method', text='LID Method')
        self.tree.heading('TSS Efficiency (%)', text='TSS Efficiency (%)')
        self.tree.heading('Remaining TSS (%)', text='Remaining TSS (%)')
        self.tree.grid(row=7, column=0, columnspan=5, padx=10, pady=10)


        # Calculate Button
        self.calculate_button = tk.Button(root, text="Calculate TSS Removal", command=self.calculate_tss_removal)
        self.calculate_button.grid(row=8, column=1, pady=20)

        # Output Summary Label
        self.summary_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.summary_label.grid(row=9, column=0, columnspan=5, padx=10, pady=10)

        # List to store the selected LID methods
        self.lid_methods_list = []

    def show_help(self):
        """Show the help document."""
        help_window = Toplevel(self.root)
        help_window.title("Help - TSS Removal Calculator")
        help_text = Text(help_window, wrap="word", width=100, height=30)
        help_text.pack(expand=True, fill="both")

        # Read and render the Markdown file
        try:
            with open("help.md", "r") as file:
                md_content = file.read()
                html_content = markdown.markdown(md_content)
                help_text.insert(tk.END, html_content)
        except FileNotFoundError:
            help_text.insert(tk.END, "Help file not found.")
        except Exception as e:
            help_text.insert(tk.END, f"An error occurred: {e}")

        help_text.config(state=tk.DISABLED)

    def new_project(self):
        self.project_number_entry.delete(0, tk.END)
        self.project_name_entry.delete(0, tk.END)
        self.consultant_company_entry.delete(0, tk.END)
        self.user_name_entry.delete(0, tk.END)
        self.site_area_entry.delete(0, tk.END)
        self.units_entry.delete(0, tk.END)
        self.impervious_percentage_entry.delete(0, tk.END)
        self.lid_method_combobox.set('')
        self.tss_efficiency_entry.delete(0, tk.END)
        
        for row in self.tree.get_children():
            self.tree.delete(row)

        self.lid_methods_list.clear()
        self.summary_label.config(text="")

    def open_file(self):
        filepath = filedialog.askopenfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")])
        if filepath:
            with open(filepath, 'r') as file:
                data = json.load(file)
                
                # Load project details
                self.project_number_entry.delete(0, tk.END)
                self.project_number_entry.insert(0, data["project_number"])
                self.project_name_entry.delete(0, tk.END)
                self.project_name_entry.insert(0, data["project_name"])
                self.consultant_company_entry.delete(0, tk.END)
                self.consultant_company_entry.insert(0, data["consultant_company"])
                self.user_name_entry.delete(0, tk.END)
                self.user_name_entry.insert(0, data["user_name"])
                self.site_area_entry.delete(0, tk.END)
                self.site_area_entry.insert(0, data["site_area"])
                self.units_entry.delete(0, tk.END)
                self.units_entry.insert(0, data["units"])
                self.impervious_percentage_entry.delete(0, tk.END)
                self.impervious_percentage_entry.insert(0, data["impervious_percentage"])

                # Load LID methods
                for row in self.tree.get_children():
                    self.tree.delete(row)

                self.lid_methods_list.clear()
                for lid in data["lid_methods"]:
                    self.lid_methods_list.append(lid)
                    self.tree.insert('', tk.END, values=(lid[0], f'{lid[1]:.2f}', lid[2]))

                self.summary_label.config(text=data["summary"])

    def save_file(self):
          project_data = {
            "project_number": self.project_number_entry.get(),
            "project_name": self.project_name_entry.get(),
            "consultant_company": self.consultant_company_entry.get(),
            "user_name": self.user_name_entry.get(),
            "site_area": self.site_area_entry.get(),
            "units": self.units_entry.get(),
            "impervious_percentage": self.impervious_percentage_entry.get(),
            "lid_methods": self.lid_methods_list,
            "summary": self.summary_label.cget("text")
          }
          filepath = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")])
          if filepath:
                    with open(filepath, 'w') as file:
                        json.dump(project_data, file, indent=4)

    def print_file(self):
        """Print the project by saving the content to a file and sending it to the printer."""

        # Create a temporary file to save the project data in a printable format
        temp_filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

        if temp_filepath:
            with open(temp_filepath, 'w') as file:
                # Write project details
                file.write(f"Project Number: {self.project_number_entry.get()}\n")
                file.write(f"Project Name: {self.project_name_entry.get()}\n")
                file.write(f"Consultant Company: {self.consultant_company_entry.get()}\n")
                file.write(f"User Name: {self.user_name_entry.get()}\n")
                file.write(f"Date and Time: {self.current_datetime}\n")
                file.write("-" * 40 + "\n")

                # Write site details
                file.write(f"Site Area: {self.site_area_entry.get()} {self.units_entry.get()}\n")
                file.write(f"Impervious Percentage: {self.impervious_percentage_entry.get()}%\n")

                # Write LID methods
                file.write("LID Methods:\n")
                file.write(f"{'LID Method':<25} {'TSS Efficiency (%)':<20} {'Remaining TSS (%)':<20}\n")

                for lid in self.lid_methods_list:
                    file.write(f"{lid[0]:<25} {lid[1]:<20.2f} {lid[2]:<20}\n")

                # Write summary
                file.write("-" * 40 + "\n")
                file.write(f"{self.summary_label.cget('text')}\n")

            # Send the file to the default printer
            try:
                os.startfile(temp_filepath, "print")
            except Exception as e:
                messagebox.showerror("Error", f"Unable to print the file. Error: {e}")

    def set_tss_efficiency(self, event):
        """Set the TSS removal efficiency based on the selected LID method."""
        selected_lid = self.lid_method_combobox.get()
        tss_efficiency = self.lid_methods_dict[selected_lid]
        self.tss_efficiency_entry.delete(0, tk.END)
        self.tss_efficiency_entry.insert(0, str(tss_efficiency))

    def add_lid_method(self):
        """Add an LID method to the list."""
        lid_name = self.lid_method_combobox.get()
        tss_efficiency = self.tss_efficiency_entry.get()
    
        if lid_name and tss_efficiency:
            try:
                tss_efficiency = float(tss_efficiency)
                if 0 <= tss_efficiency <= 100:
                    remaining_tss = 100.0 * (1 - tss_efficiency / 100)
                    self.lid_methods_list.append((lid_name, tss_efficiency, f"{remaining_tss:.2f}"))
                    index = len(self.lid_methods_list)
                    self.tree.insert('', tk.END, values=(index, lid_name, f"{tss_efficiency:.2f}", f"{remaining_tss:.2f}"))
                else:
                    messagebox.showerror("Error", "TSS Efficiency must be between 0 and 100.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number for TSS Efficiency.")
        else:
            messagebox.showerror("Error", "Please select an LID Method and ensure TSS Efficiency is valid.")


    def calculate_tss_removal(self):
        """Calculate the total TSS removal after all LID methods and display the breakdown."""
        try:
            # Clear the treeview for a new calculation
            for row in self.tree.get_children():
                self.tree.delete(row)

            site_area = float(self.site_area_entry.get())
            unit = self.units_entry.get().strip().lower()
            impervious_percentage = float(self.impervious_percentage_entry.get())

            if unit == 'ha':
                site_area = site_area * 10000  # Convert hectares to square meters

            total_runoff = site_area * (impervious_percentage / 100)

            # Initial TSS level before treatment
            initial_tss = 100.0

            # Loop through each LID system and apply TSS removal
            for index, (lid_name, tss_removal_efficiency, _) in enumerate(self.lid_methods_list, start=1):
                remaining_tss = initial_tss * (1 - tss_removal_efficiency / 100)
                self.tree.insert('', tk.END, values=(index, lid_name, f'{tss_removal_efficiency:.2f}', f'{remaining_tss:.2f}'))
                initial_tss = remaining_tss

            # Final TSS removal percentage
            final_tss_removal = 100 - remaining_tss

            # Display the result in the summary label
            self.summary_label.config(text=f"Total Runoff: {total_runoff:.2f} m2\n"
                                           f"Final TSS Removal: {final_tss_removal:.2f}%\n"
                                           f"Remaining TSS after Treatment: {remaining_tss:.2f}%")
            print(f"Total Runoff: {total_runoff:.2f} m2")
            print(f"Final TSS Removal: {final_tss_removal:.2f}%")
            print(f"Remaining TSS after Treatment: {remaining_tss:.2f}%")
        except ValueError as e:
            messagebox.showerror("Error", f"Please enter valid numeric inputs. Error: {e}")



# Create the Tkinter window
root = tk.Tk()
app = TSSCalculatorApp(root)

# Run the Tkinter main loop
root.mainloop()
