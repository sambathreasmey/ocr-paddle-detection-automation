import os
import sys
from paddleocr import PaddleOCR

def run_ocr(image_path, output_file=None):
    # ✅ Removed show_log (causes crash in some versions)
    ocr = PaddleOCR(use_angle_cls=True, lang='en')

    result = ocr.ocr(image_path)

    extracted_texts = []

    if result and result[0]:
        for line in result[0]:
            text = line[1][0]
            score = line[1][1]

            # Optional: filter low confidence
            if score > 0.5:
                extracted_texts.append(text)

    print(f"\n📄 OCR Result for: {image_path}")
    for t in extracted_texts:
        print(t)

    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(extracted_texts))

    return extracted_texts


def process_path(path):
    if os.path.isfile(path):
        run_ocr(path, "output.txt")

    elif os.path.isdir(path):
        print(f"\n📂 Processing folder: {path}")
        for filename in os.listdir(path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                file_path = os.path.join(path, filename)
                run_ocr(file_path, "output.txt")
    else:
        print("❌ Invalid path")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ocr_script.py <image_or_folder_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    process_path(input_path)
