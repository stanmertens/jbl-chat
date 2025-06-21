# Jobylon Chat

Let's set the stage, you are the founder of this exciting new messaging startup, you are tasked with building the first version of a product that is aimed to evolve with feedback from the team and users.

You're building the backend using Django, and your initial task is to expose a starting API while also leveraging HTMX for interactive front-end experiences. With this first release, we want to deliver the following user stories:

1. As a user, I want to see all other users on the platform.
2. As a user, I want to view my conversation with another user.
3. As a user, I want to be able to send messages to another user on the platform.

Given that this is your startup, you have the freedom to set up and utilize the practices that align with your goals. You can use any Python libraries or external tools that you prefer.

We have provided a Django skeleton project along with Docker setup for your convenience. Feel free to utilize Docker for development or Python virtual environments for your local setup. Since managing user registration isn’t required for this assessment, you can create dummy users directly using the shell and implement session authentication for the API.

Incorporating HTMX will allow you to create dynamic, interactive elements on the front end without needing to reload the page. We encourage you to think about how HTMX can enhance user interactions effectively.

Please submit your solution as a pull request to our public repository. Happy coding!

## How to run

1. Set up your virtual environment:
   ```bash
   python3.9 -m venv .venv
   source .venv/bin/activate
   make requirements
   ```

2. Set up and start Django:
   ```bash
   cd jbl_chat
   python -m manage migrate
   python -m manage collectstatic --no-input
   python -m manage seed_users
   python -m manage runserver
   ```

3. Login using the credentials from the seeder.