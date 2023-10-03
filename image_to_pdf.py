import os
import img2pdf
image_folder = os.getcwd()
folder_name = os.path.basename(os.path.normpath(image_folder))
output_pdf = f"{folder_name}.pdf"
image_files = sorted([f for f in os.listdir(image_folder) if f.endswith(".jpg") or f.endswith(".jpeg")])
image_paths = [os.path.join(image_folder, image_file) for image_file in image_files]
with open(output_pdf, "wb") as f:
    f.write(img2pdf.convert(image_paths))
print(f"PDF '{output_pdf}' created successfully.")
