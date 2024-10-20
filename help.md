TSS Removal Calculator Help Document

        --------------------------------------

        Overview:

        This program calculates the Total Suspended Solids (TSS) removal percentage from a site using multiple Low Impact Development (LID) methods. The user inputs project details, site information, and selects various LID methods. The program calculates how much TSS is removed from runoff as it passes through each LID method.

        Variables:

        1. **Project Number**: Unique identifier for the project.

        2. **Project Name**: Descriptive name for the project.

        3. **Consultant Company Name**: Name of the consulting firm responsible for the project.

        4. **User Name**: The name of the person using the program.

        5. **Site Area**: The total area of the site in square meters (m²) or hectares (ha).

        6. **Impervious Percentage**: The percentage of the site covered by impervious surfaces like concrete, roads, or roofs.

        7. **LID Methods**: The Low Impact Development methods used to treat the runoff. Each method has an associated average TSS removal efficiency (expressed in %).

        8. **TSS Removal Efficiency**: The percentage of TSS that each LID method removes from the runoff.

        How to Use the Program:

        1. **Input Project Information**:

           - Fill in the Project Number, Project Name, Consultant Company Name, and User Name at the top of the interface.

        2. **Input Site Information**:

           - Enter the total site area and choose the appropriate units (m² or ha).

           - Enter the percentage of the site covered by impervious surfaces.

        3. **Select LID Methods**:

           - From the dropdown, select one or more LID methods that will be used on the site.

           - The average TSS removal efficiency for each method will be automatically filled in.

           - Click "Add LID Method" to add the selected method to the list.

        4. **Calculate TSS Removal**:

           - After adding all the LID methods, click "Calculate TSS Removal" to view the total TSS removal percentage and the remaining TSS.

           - The table will display the breakdown of each LID method and its effect on the TSS levels.

        5. **Saving and Opening Projects**:

           - Use the "Save" option from the "File" menu to save the current project to a file.

           - Use the "Open" option from the "File" menu to open an existing project file.

        6. **Printing**:

           - The "Print" option from the "File" menu allows you to save the project details as a text file and send it to a printer.

        Description of LID Methods:

        1. **Bioretention**: Removes 85% of T
 
        1. **Bioretention**: Removes 85% of TSS from the runoff. This method uses soil and plant-based filtration to remove pollutants.

        2. **Permeable Pavement**: Removes 75% of TSS. Pavement allows water to pass through into a substrate layer, filtering out suspended solids.

        3. **Green Roof**: Removes 65% of TSS. Vegetation and soil layers on a roof absorb rainwater, reducing runoff and filtering TSS.

        4. **Vegetated Swale**: Removes 70% of TSS. Shallow, vegetated channels slow down runoff and filter out suspended solids.

        5. **Wet Pond**: Removes 80% of TSS. A permanent pool of water allows sediment to settle and pollutants to be absorbed.

        6. **Sand Filter**: Removes 90% of TSS. Water passes through a sand layer, which traps suspended solids.

        7. **Rain Garden**: Removes 80% of TSS. A shallow, landscaped depression captures and filters runoff using plants and soil.

        8. **Infiltration Basin**: Removes 90% of TSS. Water is directed into a basin where it infiltrates the ground, filtering pollutants.

        Troubleshooting:

        - Ensure that all required fields are filled before adding LID methods or calculating TSS removal.

        - If a method is incorrectly entered, use the "New" option to start over, or manually clear fields.

        - For advanced issues, consult your system's Python environment settings to ensure compatibility with Tkinter and file handling.

        Frequently Asked Questions:

        1. **What is TSS?**

           - Total Suspended Solids (TSS) refer to the particles that are suspended in stormwater runoff. These can include soil, organic matter, and pollutants.

        2. **What are LID methods?**

           - Low Impact Development (LID) methods are sustainable approaches to managing stormwater that aim to mimic natural processes like infiltration and filtration.

        3. **How is TSS removal calculated?**

           - TSS removal is calculated based on the combined efficiencies of the selected LID methods. The more LID methods you use, the greater the cumulative reduction of TSS in the runoff.

        4. **Can I save and reopen projects later?**

           - Yes! Use the "Save" option to store your project as a JSON file and the "Open" option to reload it.

        Contact and Support:

        - If you encounter any problems with the program, feel free to reach out to your support team for assistance.

        --------------------------------------

        End of Help Document
