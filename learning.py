{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNeN/G1PMm57d659D+oKMme",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ChandraSekhar463/MachineLearning/blob/main/learning.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import io\n",
        "\n",
        "# Create sample data as a CSV string\n",
        "csv_data = \"\"\"\n",
        "Age,Height,Weight\n",
        "15,165,55\n",
        "16,170,60\n",
        "17,175,65\n",
        "18,180,70\n",
        "19,185,75\n",
        "\"\"\"\n",
        "\n",
        "# Create a file-like object from the CSV string\n",
        "students_csv = io.StringIO(csv_data)\n",
        "\n",
        "# Step 1: Load the CSV file from the in-memory object\n",
        "data = pd.read_csv(students_csv)\n",
        "\n",
        "# Step 2: Extract columns\n",
        "heights = data['Height']\n",
        "weights = data['Weight']\n",
        "ages = data['Age']\n",
        "\n",
        "# Step 3: Create Visualizations\n",
        "\n",
        "# 1. Scatter Plot: Height vs. Weight\n",
        "plt.figure(figsize=(8, 5))\n",
        "plt.scatter(heights, weights, color='blue', label='Height vs Weight')\n",
        "plt.title(\"Height vs Weight\")\n",
        "plt.xlabel(\"Height (cm)\")\n",
        "plt.ylabel(\"Weight (kg)\")\n",
        "plt.legend()\n",
        "plt.grid()\n",
        "plt.show()\n",
        "\n",
        "# 2. Line Plot: Age vs Height\n",
        "plt.figure(figsize=(8, 5))\n",
        "plt.plot(ages, heights, marker='o', color='green', label='Age vs Height')\n",
        "plt.title(\"Age vs Height\")\n",
        "plt.xlabel(\"Age (years)\")\n",
        "plt.ylabel(\"Height (cm)\")\n",
        "plt.legend()\n",
        "plt.grid()\n",
        "plt.show()\n",
        "\n",
        "# 3. Bar Plot: Age vs Weight\n",
        "plt.figure(figsize=(8, 5))\n",
        "plt.bar(ages, weights, color='orange', label='Age vs Weight')\n",
        "plt.title(\"Age vs Weight\")\n",
        "plt.xlabel(\"Age (years)\")\n",
        "plt.ylabel(\"Weight (kg)\")\n",
        "plt.legend()\n",
        "plt.grid(axis='y')\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "NEXUycXNv3GN"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}