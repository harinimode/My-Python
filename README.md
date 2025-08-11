Quality Inspection Image Classifier
This project automates image-based quality inspection by processing product images, identifying defects, and generating a color-coded Excel report showing which items are approved and which are rejected.

📌 Features
Preprocesses images (resize, grayscale, normalization)

Reads dataset organized by train and test folders

Classifies test images:

approved ✅ if in good folder

rejected ❌ otherwise

Saves results in an Excel file with:

Green for approved

Red for rejected

Works with multiple categories and defect types



📂 Project Structure

Quality-Inspection-Image-Classifier/
├── quality_check.py              # Main script


├── requirements.txt              # Dependencies


├── README.md                     # Project documentation


├── LICENSE                       # License file


├── .gitignore                    # Ignore venv/cache/temp


│
├── data/                         # Dataset root

│   ├── Category1/

│   │   ├── train/

│   │   │   └── good/             # Approved training samples


│   │   └── test/

│   │       ├── good/             # Defect-free test samples

│   │       └── defect_type1/     # Defective test samples

│   ├── Category2/


│   │   └── ...                   # Additional categories
│


├── outputs/                      # Generated outputs


│   └── e3_final_one.xlsx         # Excel with inspection results


│
└── docs/                         # Documentation & usage examples


    └── usage_examples.md

⚙️ Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/Quality-Inspection-Image-Classifier.git
cd Quality-Inspection-Image-Classifier
Install dependencies:

bash
Copy code
pip install -r requirements.txt
📸 Dataset Format
Your dataset should be structured as follows:

bash
Copy code
data/
└── CategoryName/
    ├── train/
    │   └── good/             # Approved training images
    └── test/
        ├── good/             # Approved test images
        ├── defect_type1/     # Defective items
        └── defect_type2/     # Other defect categories

        
🚀 Usage
Run the script by specifying your dataset path inside the code:

base_path = r"C:\path\to\data"
Then execute:


python quality_check.py


📊 Output


The script creates e3_final_one.xlsx inside the outputs/ folder.

Excel contains:

Green cells → Approved items

Red cells → Rejected items

Example:

| category | defect\_type | file\_name   | status   |
| -------- | ------------ | ------------ | -------- |
| bolts    | good         | img\_001.jpg | approved |
| bolts    | crack        | img\_002.jpg | rejected |
