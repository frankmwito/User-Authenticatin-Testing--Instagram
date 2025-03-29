# Instagram User Authentication Testing

## Overview
This project focuses on testing user authentication features for an Instagram clone. The primary objective was to validate the sign-up, login, and two-factor authentication (2FA) processes to ensure security, reliability, and seamless user experience. 

## Tools Used
- **GitLab CI/CD** – For automated testing and continuous integration.
- **Selenium** – To automate web interactions and test UI functionalities.
- **pytest** – For writing and executing test cases.

## Scope
- **Sign-up Testing**: Ensuring valid and secure user registration.
- **Login Testing**: Verifying correct credential validation and error handling.
- **Two-Factor Authentication (2FA) Testing**: Checking the implementation of additional security layers.
- **Edge Case Testing**: Simulating various login scenarios such as invalid credentials, brute-force attempts, and expired verification codes.
- **CI/CD Integration**: Automating test execution in GitLab pipelines to improve test coverage and execution efficiency.

## Key Achievements
- Improved test coverage by **40%**, ensuring robustness against authentication vulnerabilities.
- Automated **user authentication flows**, reducing manual testing efforts.
- Enhanced **security testing** by simulating edge cases and brute-force attacks.

## Installation & Setup
### Prerequisites
- Python 3.x
- Selenium WebDriver
- pytest
- GitLab account with access to CI/CD pipelines

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/frankmwito/User-Authenticatin-Testing--Instagram.git
   ```
2. Navigate to the project directory:
   ```bash
   cd User-Authenticatin-Testing--Instagram
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run tests locally:
   ```bash
   pytest -v
   ```

## Running Tests in GitLab CI/CD
1. Push changes to the repository.
2. GitLab pipeline triggers automated tests.
3. Review test results in the GitLab CI/CD dashboard.

## Test Cases Overview
### Sign-up Tests
- Valid user registration
- Invalid email format
- Weak password rejection
- Duplicate email handling
- Verification email sent successfully

### Login Tests
- Successful login with valid credentials
- Incorrect password error handling
- Unregistered email rejection
- Rate limiting after multiple failed attempts
- CAPTCHA prompt after excessive failures

### 2FA Tests
- Correct OTP validation
- Invalid OTP rejection
- OTP expiration handling
- Backup codes functionality

## Contribution Guidelines
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit changes and push to GitHub.
4. Submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any queries or contributions, reach out to **Franklin Muchui** via GitHub or LinkedIn.

---
This project ensures that user authentication rema
