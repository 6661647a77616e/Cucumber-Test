Here's a simple example:

---

### **Python Code**: `app.py`  

```python
def greet_user(name):
    if not name.strip():
        return "Hello, Guest!"
    return f"Hello, {name}!"
```

---

### **Cucumber Code**: `greet.feature`  

```gherkin
Feature: Greet the user
  To ensure the greeting function works correctly

  Scenario: Greet a specific user
    Given a user named "Alice"
    When the user is greeted
    Then the response should be "Hello, Alice!"

  Scenario: Greet with an empty name
    Given an empty name
    When the user is greeted
    Then the response should be "Hello, Guest!"
```

---

### **Step Definitions**: `greet_steps.py`  

```python
from behave import given, when, then
from app import greet_user

@given('a user named "{name}"')
def step_given_user_name(context, name):
    context.name = name

@given('an empty name')
def step_given_empty_name(context):
    context.name = ""

@when('the user is greeted')
def step_when_user_is_greeted(context):
    context.response = greet_user(context.name)

@then('the response should be "{expected_response}"')
def step_then_response_should_be(context, expected_response):
    assert context.response == expected_response, \
        f"Expected '{expected_response}' but got '{context.response}'"
```

---

### **How to Run the Code**

#### **1. Install Dependencies**
Install Python dependencies using `pip`:  
```bash
pip install behave
```

#### **2. Create File Structure**  
Organize the files like this:
```
project/
│
├── app.py
├── features/
│   ├── greet.feature
│   ├── steps/
│       └── greet_steps.py
```

#### **3. Run Tests**  
Navigate to the `project` directory and execute:  
```bash
behave
```

#### **Expected Output**  
```plaintext
Feature: Greet the user
  Scenario: Greet a specific user        # features/greet.feature:4
    Given a user named "Alice"           # features/steps/greet_steps.py:4
    When the user is greeted             # features/steps/greet_steps.py:12
    Then the response should be "Hello, Alice!"  # features/steps/greet_steps.py:16

  Scenario: Greet with an empty name     # features/greet.feature:8
    Given an empty name                  # features/steps/greet_steps.py:8
    When the user is greeted             # features/steps/greet_steps.py:12
    Then the response should be "Hello, Guest!"  # features/steps/greet_steps.py:16

2 scenarios (2 passed)
6 steps (6 passed)
0m0.002s
```

---

This setup demonstrates how to use Python for functionality and Cucumber (`behave` in Python) for behavior-driven testing. Let me know if you'd like further guidance!

Command to create hello-cucumber projec
```bash
mvn archetype:generate "-DarchetypeGroupId=io.cucumber" "-DarchetypeArtifactId=cucumber-archetype" "-DarchetypeVersion=7.20.1" "-DgroupId=hellocucumber" "-DartifactId=hellocucumber" "-Dpackage=hellocucumber" "-Dversion=1.0.0-SNAPSHOT" "-DinteractiveMode=false"
```
