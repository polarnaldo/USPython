# USP Agent Manager

A Python-based utility for streamlined management of User Services Platform (USP) agents within Docker environments.

## Features

* **Dependency Installation:** Automates the installation of Docker and Docker Compose, ensuring a seamless setup experience.
* **Agent Acquisition:** Fetches USP agents directly from the official Broadband Forum repository.
* **Agent Creation:** Provides guided configuration for generating new USP agents with tailored settings.
* **Agent Modification:**  Enables straightforward editing of existing USP agent configurations.
* **Agent Overview:** Displays a comprehensive list of currently installed USP agents. 
* **Agent Removal:** Simplifies the deletion of USP agents when necessary.

## Prerequisites

* Python

## Installation**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/polarnaldo/USPython.git
   ```

2. **Change into the project directory:**
   ```bash
   cd USPython
   ```

3. **Execute the script:**
   ```bash
   sudo python3 USPython.py
   ```

## Usage

1. **Run the script.**  You'll be presented with an interactive, menu-driven interface.
2. **Follow the prompts** to install dependencies, download agents, create new agents, edit configurations, view your agent list, or delete agents.
3. **Note:** Root privileges (using `sudo`) might be required for certain operations.

## Contributing

We enthusiastically welcome contributions!  To share your ideas or code improvements:

1. **Raise an Issue:** File an issue to describe bugs or suggest new features.
2. **Fork & Submit a Pull Request:**  Follow standard GitHub workflows to propose your changes.

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for full details.
