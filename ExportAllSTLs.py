import adsk.core, adsk.fusion, traceback, os

def run(context):
    # Initialize UI object
    ui = None
    try:
        # Get the Fusion 360 application and user interface
        app = adsk.core.Application.get()
        ui = app.userInterface

        # Get the active design (must be a 3D design workspace)
        design = adsk.fusion.Design.cast(app.activeProduct)

        # Get the root component (top-level assembly)
        rootComp = design.rootComponent

        # Get the export manager to handle file output
        exportMgr = design.exportManager

        # 💡 Folder path where STL files will be saved
        # Change this to any folder path on your system
        folderPath = r"C:\STL_Export_Output"
        os.makedirs(folderPath, exist_ok=True)  # Create folder if it doesn't exist

        # Collect all components: root + all components from occurrences
        components = [rootComp] + [occ.component for occ in rootComp.allOccurrences]

        # Export each component to an STL file
        for comp in components:
            # Generate output file name (e.g., "wheel.stl")
            filename = os.path.join(folderPath, f"{comp.name}.stl")

            # Create export options for STL
            stlOptions = exportMgr.createSTLExportOptions(comp)
            stlOptions.meshRefinement = adsk.fusion.MeshRefinementSettings.MeshRefinementMedium  # Medium quality
            stlOptions.filename = filename

            # Execute the export
            exportMgr.execute(stlOptions)

            # Log output (optional for debugging)
            print(f"Exported: {filename}")

        # Show confirmation dialog after all exports are completed
        ui.messageBox("STL export completed for all components.")

    except:
        # If an error occurs, show error message
        if ui:
            ui.messageBox('Error:\n{}'.format(traceback.format_exc()))
