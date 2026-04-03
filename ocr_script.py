import os
import sys
from paddleocr import PaddleOCR

def run_ocr(image_path, output_file=None):
    # Init OCR (CPU friendly)
    ocr = PaddleOCR(use_angle_cls=True, lang='en', show_log=False)

    # Run OCR
    result = ocr.ocr(image_path)

    extracted_texts = []

    if result and result[0]:
        for line in result[0]:
            text = line[1][0]
            extracted_texts.append(text)

    # Print result
    print(f"\n📄 OCR Result for: {image_path}")
    for t in extracted_texts:
        print(t)

    # Save to file (optional)
    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(extracted_texts))

    return extracted_texts


def process_path(path):
    if os.path.isfile(path):
        run_ocr(path)

    elif os.path.isdir(path):
        print(f"\n📂 Processing folder: {path}")
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)

            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                run_ocr(file_path)
    else:
        print("❌ Invalid path")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ocr_script.py <image_or_folder_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    process_path(input_path)
