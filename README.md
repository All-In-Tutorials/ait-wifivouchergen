📌 **Introduction**
AIT WiFi Voucher Generator is an open-source Python tool designed to generate potential username and password combinations for security testing and password auditing.
It uses itertools to automate the generation of brute-force combinations based on predefined patterns.

⚠️ **Disclaimer:** This tool is intended for educational and security research purposes only.
Unauthorized use against systems you do not own is illegal. Please proceed responsibly.

---

🛠️ **Requirements**

### 1️⃣ Python

Install the latest **stable version** of Python:  

- 📥 [Download Python](https://www.python.org/downloads/)

To verify the installation:
```sh
python --version
```
or
```sh
python3 --version
```

### 2️⃣ Dependencies
This tool uses the built-in Python modules:
- `itertools`
- `string`

There’s no need for external libraries beyond Python.

---

🚀 **Installation & Setup**

### 1️⃣ Clone the Repository
Clone the repository to your local machine:
```sh
git clone https://github.com/yourusername/ait-wifivouchgen.git
```
Navigate into the project directory:
```sh
cd ait-wifivouchgen
```

### 2️⃣ Generate Combinations
The `generator.py` script generates username and password combinations based on your selection. You can run the script with one of the following options (1-14), or select option 15 to generate all combinations.

**Running the Generator:**
```sh
python generator.py
```
This will generate combinations based on the selected option.

**Note:** The script also creates a `prefix.txt` file in the `Dictionary` directory, which is required for testing. This file will contain a hardcoded value for the exact username prefix after execution.

---

🔢 **Option Breakdown**
The following options define different username and password combination formats. Select the option that matches your needs:

### **Available Options:**
- **Option 1:** Uppercase letters (AAAA)
- **Option 2:** Number + Uppercase letters (1AAA)
- **Option 3:** Uppercase + Number + Uppercase + Uppercase (A1AA)
- **Option 4:** Uppercase + Uppercase + Number + Uppercase (AA1A)
- **Option 5:** Uppercase + Uppercase + Uppercase + Number (AAA1)
- **Option 6:** Number + Number + Uppercase + Uppercase (11AA)
- **Option 7:** Number + Number + Number + Uppercase (111A)
- **Option 8:** Number + Number + Number + Number (1111)
- **Option 9:** Uppercase + Uppercase + Number + Number (AA11)
- **Option 10:** Uppercase + Number + Number + Number (A111)
- **Option 11:** Uppercase + Number + Uppercase + Number (A1A1)
- **Option 12:** Uppercase + Number + Number + Uppercase (A11A)
- **Option 13:** Number + Uppercase + Number + Uppercase (1A1A)
- **Option 14:** Number + Uppercase + Uppercase + Number (1AA1)
- **Option 15:** Generate all combinations (1-14)

### **Running the Generator with Option 15:**
To generate all dictionaries for all combinations:
```sh
python generator.py --option 15
```

---

📂 **Generated Files**
The generated combinations will be saved in the `Dictionary` folder inside the project directory. Each combination type will have its own subfolder with `username.txt` and `password.txt` files containing the generated values.

**Example directory structure:**
```plaintext
Dictionary/
├── UC-UC-UC-UC/
│   ├── username.txt
│   └── password.txt
├── Num-UC-UC-UC/
│   ├── username.txt
│   └── password.txt
...
└── All Combinations/
    ├── username.txt
    └── password.txt
```
Each file will contain the generated combinations that match the chosen pattern.

---

🔧 **Troubleshooting**

❌ **Invalid Option Error**
If you see an error like:
```
Invalid option. Please enter a number between 1 and 15.
```
Ensure that you’ve selected a valid option. The script only supports options between 1 and 15.

❌ **Permission Errors**
If you encounter permission issues, make sure you have the necessary permissions to create files and directories in the location where you are running the script.

---

📜 **License**
This project is open-source and licensed under the MIT License.
