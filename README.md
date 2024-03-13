# Digital Transformation LABNL: API and storage services

Web Application backend for registry process at labnl. Deveopling a service of data ingestion, applying a digital transformation methodology for virtualizing the application via hosting application service in docker container in cloud from Digital Ocean. 

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)
<!-- - [License](#license)
- [Badges](#badges)-->

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/enriquegv001/Trans_Dig_LABNL.git
   cd 3rd_app
   ```
<!--

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
-->


## Usage

1. Create a database in Digital Ocean
2. Change in ```db.py``` the dictionary keys from ```db_params``` with the corresponding from main 
3. Run the web application:
   ```
   uvicorn main:app --reload
   ```
4. Add any other CRUD opperation to the ```main.py```
   
   
## Credits

- **Contact:** enriquegv001@gmail.com

## License

This project is licensed under the [License Name] License - see the [LICENSE](LICENSE) file for details.


## Badges

[![License](https://img.shields.io/badge/License-[License Code]-blue.svg)](LICENSE)

