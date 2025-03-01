# 🚀 Git Assignment - Hero Vired

This repository contains the Git assignment for the **Hero Vired DevOps Cloud Engineering Certification** program. It demonstrates best practices in **version control, branching strategies, feature implementation,** and **collaborative development** using Git.

## ✨ Why This Project?

This project showcases various **Git features and workflows**, helping developers understand best practices for:

- 📌 **Branching strategies** and version control.  
- 📂 **Handling large files** using Git LFS.  
- 🛠️ Efficiently using **Git stash** for managing multiple feature implementations.  

---

## Table of Contents

1. [Implementing Solution](#-implementing-solution)   
2. [Installation](#-installation) 
3. [Assignment Workflow](#-assignment-workflow) 
4. [Contribution Guidelines](#-contribution-guidelines)  
5. [Support](#-support)  
6. [Credits](#-credits)  
7. [License](#-license)  
8. [Forking This Project](#-forking-this-project)  
9. [Screenshots](#-screenshots)  
  
---
## 🚀 Implementing Solution


This section outlines the key steps to implement the required features in the repository.

### 📌 Q1: Implementing Square Root Feature in "CalculatorPlus"

1. **Create Repository & Branch**
   - Create a GitHub repository named `git_assignment_HeroVired`.
   - Create a new branch `dev` and add the provided calculator code.

2. **Implement Square Root Feature**
   - Uncomment and implement the `square_root()` function.
   - Test the function by uncommenting the test code.

3. **Merge and Release Version 1**
   - Merge `dev` into `main`.
   - Create a release tagged as `v1.0`.

4. **Add Collaborators**
   - Invite a classmate as a collaborator on the repository.

5. **Feature Branch for Square Root**
   - Create a new branch `feature/sqrt`.
   - Add the square root functionality in this branch.

6. **Fix Critical Bug**
   - Switch to `dev` branch.
   - Fix the divide-by-zero bug in the `divide()` function.
   - Merge the bug fix while keeping `feature/sqrt` up to date.

7. **Pull Request and Code Review**
   - Create a pull request to merge `feature/sqrt` into `main`.
   - Request a code review and apply suggested improvements.

8. **Final Merge and Release Version 2**
   - Merge `feature/sqrt` into `dev` and then into `main`.
   - Release `v2.0` with all features and fixes.

---

### 📌 Q2: Implementing Git LFS for Large Files

1. **Create LFS Branch**
   - Create a new branch `lfs` in `git_assignment_HeroVired`.

2. **Install & Initialize Git LFS**
   - Run:  
     ```sh
     git lfs install
     ```
   - Track large files (e.g., `.zip`, `.mp4`):
     ```sh
     git lfs track "*.zip"
     ```
   - Commit `.gitattributes` file.

3. **Upload Large File**
   - Add and commit a file >200MB.
   - Push changes to `lfs` branch.

4. **Verify by Cloning on Another Machine**
   - Clone the repository on a different system.
   - Ensure large files download correctly.

---

### 📌 Q3: Implementing Geometry Calculator with Git Stash

1. **Create `geometry-calculator` Branch**
   - Create a new branch `geometry-calculator`.

2. **Work on Circle Area Feature**
   - Create a `feature/circle-area` branch.
   - Implement `calculate_circle_area()`.
   - Use `git stash` to save progress.

3. **Work on Rectangle Area Feature**
   - Switch to `feature/rectangle-area` branch.
   - Implement `calculate_rectangle_area()`.
   - Use `git stash` to save progress.

4. **Restore Stashed Changes & Complete Features**
   - Switch back to `feature/circle-area`, apply stash, finalize code.
   - Commit and push changes.
   - Repeat for `feature/rectangle-area`.

5. **Create Pull Requests & Merge**
   - Create pull requests for both features.
   - Review, merge into `dev`, then into `main`.

---
---

## 📌 Installation

Follow these steps to set up and run the project.

### 1️⃣ Clone the repository:
```bash
git clone https://github.com/yourusername/git-assignment.git
cd git-assignment
```
### 2️⃣ Install dependencies (if any):
```bash
Copy
Edit
pip install -r requirements.txt
```
### 3️⃣ Set up Git LFS (if required):
```bash
git lfs install
git lfs pull
```

## 🛠️ Assignment Workflow

### Q1 - Implementing Square Root Feature
- Created repository `git_assignment_HeroVired`.
- Developed square root function and merged into `main`.
- Addressed a critical bug in `divide` function.
- Released `v1` and `v2` with reviewed changes.

---

### Q2 - Handling Large Files with Git LFS
- Created a branch `lfs`.
- Integrated Git LFS to track and push large files.
- Verified file handling by cloning on another machine.

---

### Q3 - Geometry Calculator Using Git Stash
- Implemented area calculation for circle and rectangle.
- Used `git stash` to switch between features.
- Completed and merged both features after review.

---

## 🤝 Contribution Guidelines

We welcome contributions! To get started:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add a new feature'`).
4. Push to your forked repository (`git push origin feature-branch`).
5. Submit a pull request for review.

---

## 💡 Support

If you encounter any issues or need help, feel free to open an issue in the repository or reach out to me directly.

---

## 🏆 Credits

This project is developed and maintained by [Your Name]. Special thanks to all contributors and reviewers who helped enhance this project.

---

## 📚 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

---

## 🔗 Forking This Project

If you’d like to fork this project, follow these steps:
1. Click the **Fork** button at the top right of this repository.
2. Clone your forked repository: `git clone https://github.com/your-username/repository-name.git`
3. Make your changes and push them to your forked repository.
4. Open a pull request to contribute your changes back.

---
## 📸 Screenshots

_Showcasing key aspects of the project:_

### Q1 - Implementing Square Root Feature:

- Implemented a function to calculate square roots accurately.
- Debugged issues related to floating-point precision.
- Verified output with multiple test cases.

<div align="center">
  <img src="https://github.com/user-attachments/assets/772eaa05-82e5-4025-b019-937f6422f3c8" width="45%">
  <img src="https://github.com/user-attachments/assets/78a6330b-6895-4b4e-b6bd-e7d7879a7236" width="45%">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/008d624a-39ed-4d1b-97a7-c302fc253156" width="45%">
  <img src="https://github.com/user-attachments/assets/b65d6203-5fea-42db-9167-a1942ed74f7a" width="45%">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/c78d1345-16df-424f-8640-640bedf642d4" width="45%">
  <img src="https://github.com/user-attachments/assets/3de3bd08-5946-40b3-83b1-080de78db35e" width="45%">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/6eef8bb6-4404-42a8-b6e3-cba65a582015" width="45%">
  <img src="https://github.com/user-attachments/assets/49f5c8cf-51d9-4030-b5ba-78bc8f0b8359" width="45%">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/4e9b9251-5eb6-459f-8dd5-dd9f15e754ed" width="45%">
  <img src="https://github.com/user-attachments/assets/d4f34fc7-3c08-4355-95ad-1043987556ff" width="45%">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/e4673c88-fc33-4967-917c-36ee7f4baea1" width="45%">
  <img src="https://github.com/user-attachments/assets/bc7e2660-7a6b-475f-8285-8bb582ff33c5" width="45%">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/41e8f09d-f062-4bb3-bb41-899523e8952a" width="45%">
  <img src="https://github.com/user-attachments/assets/e7fd9def-f3a4-44e4-8370-b7f47f62e9d7" width="45%">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/6cd930ab-3039-4a5a-b896-4d816ccfcdb4" width="45%">
  <img src="https://github.com/user-attachments/assets/27a95f9d-e1fa-46f3-9341-1480477a7d62" width="45%">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/038c97a6-049d-47f7-b6cd-b0db186705fa" width="45%">
  <img src="https://github.com/user-attachments/assets/93785afc-68d3-42d6-bab7-053ea407d6b2" width="45%">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/40707d26-7bd4-45f7-9637-b2c27b6054c1" width="45%">
  <img src="https://github.com/user-attachments/assets/8f8a7a91-b2a5-4080-b733-cc2f81cb7cbb" width="45%">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/d9ae61cf-c092-469c-8b68-7efa8e7d142b" width="45%">
  <img src="https://github.com/user-attachments/assets/676a9a15-56f8-45bc-b4b2-8ea3ddba457e" width="45%">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/e883f721-105c-4776-befb-5ebea212e3c1" width="45%">
  <img src="https://github.com/user-attachments/assets/4ab59d2e-021b-4efa-8adf-64c3e3cf1152" width="45%">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/3d0b6f1f-87b7-4159-bd7f-ba9cc72f515a" width="45%">
  <img src="https://github.com/user-attachments/assets/9c82b0c0-38af-44b3-9b28-e6fcca94c163" width="45%">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/0371f074-4d24-4a27-abfc-ea7295a9a86e" width="45%">
  <img src="https://github.com/user-attachments/assets/52be84c5-eefd-4291-8c3e-fb23e8e73a03" width="45%">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/98b2e9c9-13a9-48da-82ab-511cb5417eb1" width="45%">
  <img src="https://github.com/user-attachments/assets/a351ab01-8157-4112-9ffb-ba90262ad6d1" width="45%">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/8ef8f1d8-7b87-4c0b-b54f-86b6e579290c" width="45%">
</div>

---

### Q2 - Handling Large Files with Git LFS:

### 1. Initializing Git LFS and Creating the `lfs` Branch
<div style="display: flex; justify-content: center;">
    <img src="https://github.com/user-attachments/assets/cd5bfe89-4891-4c77-8fd5-a914606db938" width="45%">
    <img src="https://github.com/user-attachments/assets/1628eb64-5929-43dc-bdde-4952b8362165" width="45%">
</div>

### 2. Tracking Large Files and Adding Them to Git LFS
<div style="display: flex; justify-content: center;">
    <img src="https://github.com/user-attachments/assets/f7b43e29-ee6b-41ef-a7ff-dd80e5959633" width="45%">
    <img src="https://github.com/user-attachments/assets/9a02e3f3-6709-4c5b-8d69-1d7f647a2862" width="45%">
</div>

### 3. Committing and Pushing the Large File to the Repository
<div style="display: flex; justify-content: center;">
    <img src="https://github.com/user-attachments/assets/e02fc45c-4b91-48e3-ac0b-078e80c288ac" width="45%">
    <img src="https://github.com/user-attachments/assets/e3232a49-6f8b-455d-916e-b3d2d4156bfd" width="45%">
</div>

### 4. Cloning the Repository and Verifying Git LFS Functionality
<div style="display: flex; justify-content: center;">
    <img src="https://github.com/user-attachments/assets/f0e28fb4-35fb-441f-91b1-f53505040409" width="45%">
    <img src="https://github.com/user-attachments/assets/f93b0ad3-a70d-4744-b783-6eba99cdd07e" width="45%">
</div>

---

### Q3 - Geometry Calculator Using Git Stash:

- Developed a Geometry Calculator supporting multiple shape computations.
- Used Git stash to manage multiple development tasks efficiently.

<div align="center">
  <img src="https://github.com/user-attachments/assets/fbd9bb22-0d33-4293-9792-90beb01f19d6" width="45%">
  <img src="https://github.com/user-attachments/assets/75a1ee2a-4174-4ac8-892a-a5703b0179ae" width="45%">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/2ad07b2b-1138-4e2b-9e7b-0bafd4dab69f" width="45%">
  <img src="https://github.com/user-attachments/assets/453b38c7-6fd8-4b9c-a859-a7adc5e02d8e" width="45%">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/35e0f1ba-dfb3-4185-99e3-4684382f762a" width="45%">
  <img src="https://github.com/user-attachments/assets/b746ca34-474f-48c4-a035-72e1a52c37c7" width="45%">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/d53d9db6-d23d-4f1b-bab1-a3b71bc382e8" width="45%">
  <img src="https://github.com/user-attachments/assets/e492de74-9c40-4cfc-a098-5e2c6e5559b5" width="45%">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/8af90492-e083-4c55-ad1f-4e812f419643" width="45%">
  <img src="https://github.com/user-attachments/assets/04534c66-f793-4563-97c2-1b87256392d4" width="45%">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/85976a11-9f0a-4503-af92-2f52110a43ff" width="45%">
  <img src="https://github.com/user-attachments/assets/983f5f4c-906c-49db-9124-7808added7cc" width="45%">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/c8f2feb5-905d-4837-a5d8-ebf4226eba62" width="45%">
  <img src="https://github.com/user-attachments/assets/20aa5fdd-e591-4102-bf56-a5bd1505d47f" width="45%">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/6ad27a64-b5a7-4ed5-841f-0b5a3b99c33b" width="45%">
  <img src="https://github.com/user-attachments/assets/f9f73554-e510-4b1a-8d99-eeccabc62653" width="45%">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/5b2af346-9fef-40e0-bc0d-a1845ae56763" width="45%">
  <img src="https://github.com/user-attachments/assets/cbd7ca5b-2667-47a0-b771-d750ccb69730" width="45%">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/a3ca9010-46c6-4fc0-a1d3-dc6fa64da845" width="45%">
  <img src="https://github.com/user-attachments/assets/40896b7b-1b02-47a3-a03f-b1dd609e77d9" width="45%">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/70f4caaa-f997-423e-b963-a6db65eec4b7" width="45%">
  <img src="https://github.com/user-attachments/assets/b15ccc28-8b42-4586-8425-0f1d2beddfa6" width="45%">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/bac2ad31-dd9c-4d2e-b920-0bd4e3e9bd34" width="45%">
  <img src="https://github.com/user-attachments/assets/3e86364f-45d1-4de7-a549-2fd1a2690418" width="45%">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/092673ee-0735-4d10-a2d2-073916aa8815" width="45%">
  <img src="https://github.com/user-attachments/assets/4b22050a-12f4-4e30-9dcc-3790fa3e89b9" width="45%">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/1024e8cf-703a-4343-a24b-680a9ebfc2e5" width="45%">
  <img src="https://github.com/user-attachments/assets/0e1e5d80-895f-475e-b069-c51c08cd241e" width="45%">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/0f87a33f-2961-4235-99c6-795e3bf4336a" width="45%">
  <img src="https://github.com/user-attachments/assets/73276859-d1d7-434d-ba52-ff828255fca8" width="45%">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/98c0742f-be5e-4121-854d-e61d7903aaf6" width="45%">
</div>



---


🌟 **If you find this project helpful, consider giving it a star! Your support is much appreciated.** 🌟
