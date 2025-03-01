# 🚀 Git Assignment - Hero Vired

![Project Screenshot](screenshots/Q1_Img_01.png)

## 📌 **About This Project**

**This repository contains the Git assignment for the Hero Vired DevOps Cloud Engineering Certification program. It demonstrates best practices in version control, branching strategies, feature implementation, and collaborative development using Git.**

## 📸 Screenshots

_Showcasing key aspects of the project:_

### Q1 - Implementing Square Root Feature
![Calculator Setup](screenshots/Q1_Img_02.png)
![Branching and Development](screenshots/Q1_Img_03.png)
![Feature Implementation](screenshots/Q1_Img_04.png)
![Final Testing](screenshots/Q1_Img_05.png)

### Q2 - Handling Large Files with Git LFS


### Q3 - Geometry Calculator Using Git Stash
![Circle Area Feature](screenshots/Q3_Img_1.png)
![Rectangle Area Feature](screenshots/Q3_Img_2.png)

## 🛠️ Assignment Questions and Workflow

### Q.1: Implementing Square Root Feature in CalculatorPlus

#### Task:
- Implement a new feature for calculating the square root of a number.

#### Steps:
1. Create a repository named `git_assignment_HeroVired`.
2. Create a `dev` branch and add the following code:

```python
import math

class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b

    # TODO: Implement square root function
    def square_root(self, x):
        return math.sqrt(x)
```

3. Merge `dev` into `main` and release `v1` of CalculatorPlus.
4. Add a collaborator.
5. Create a `feature/sqrt` branch to add the `sqrt` function.
6. Address a critical bug in the `divide` function:

```python
def divide(self, a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
```

7. Merge changes, request a review, and release `v2`.

### Q.2: Handling Large Files with Git LFS

#### Task:
- Integrate Git LFS to handle large binary files efficiently.

#### Steps:
1. Create a `lfs` branch in `git_assignment_HeroVired`.
2. Install Git LFS and track large files:

```sh
git lfs install
git lfs track "*.bin"
```

3. Upload and push a file over 200MB.
4. Clone on another machine to verify.

### Q.3: Geometry Calculator Using Git Stash

#### Task:
- Implement a Python program for calculating area of a circle and a rectangle.

#### Steps:
1. Create a `geometry-calculator` branch.
2. Work on `circle-area` feature in a new branch:

```python
class GeometryCalculator:
    def calculate_circle_area(self, radius):
        return math.pi * radius ** 2
```

3. Stash changes and switch to `rectangle-area` branch.
4. Implement rectangle area function:

```python
def calculate_rectangle_area(self, length, width):
    return length * width
```

5. Retrieve stashed changes and finalize both features.
6. Push, create pull requests, review, and merge into `main`.

## 🤝 Contribution Guidelines

We welcome contributions! To get started:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add a new feature'`).
4. Push to your forked repository (`git push origin feature-branch`).
5. Submit a pull request for review.

## 💡 Support

If you encounter any issues or need help, feel free to open an issue in the repository or reach out to me directly.

## 🏆 Credits

This project is developed and maintained by [Your Name]. Special thanks to all contributors and reviewers who helped enhance this project.

## 🔗 Forking This Project

If you’d like to fork this project, follow these steps:
1. Click the **Fork** button at the top right of this repository.
2. Clone your forked repository: `git clone https://github.com/your-username/repository-name.git`
3. Make your changes and push them to your forked repository.
4. Open a pull request to contribute your changes back.

---

🌟 **If you find this project helpful, consider giving it a star! Your support is much appreciated.** 🌟
